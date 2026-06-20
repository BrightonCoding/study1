"""
collect.py — metadata collection.

Primary backend: yt-dlp (no API quota). A YouTube Data API backend is provided behind
the SAME Collector interface, selectable via config (collection.backend).

IMPORTANT design constraints baked in here:
  * SNAPSHOT semantics. yt-dlp/API return *current accumulated* stats, not a time series.
    Every video record therefore carries scrape_date + upload_date so age can be controlled
    for downstream. (The true longitudinal dataset is built later by rescrape.py, which
    appends a fresh snapshot of the SAME ids on each run.)
  * Everything cached to disk keyed by id, so re-runs never re-hit the network.
  * Polite: rate-limited, retried with exponential backoff.
  * Shorts are FLAGGED (is_short), never silently dropped.
  * Missing like/comment counts (disabled) are kept as null and flagged, never crash.

Public surface:
  make_collector(cfg, logger) -> Collector
  Collector.get_channel_metadata(ref) -> dict
  Collector.list_channel_videos(ref, cap) -> list[dict]   # light: ids + basic
  Collector.get_video_metadata(video_id) -> dict          # full stats (cached)
  Collector.download_thumbnail(video_id, raw) -> (url, local_path|None)
  discover_channels_by_search(cfg, logger, keywords, n)   # search-based expansion
"""
from __future__ import annotations

import datetime as _dt
import json
import time
from pathlib import Path
from typing import Any, Iterable

from .config import Cfg
from .logging_setup import get_logger


# --------------------------------------------------------------------------- #
# Caching helpers
# --------------------------------------------------------------------------- #
def _cache_path(cfg: Cfg, kind: str, key: str) -> Path:
    d = cfg.path("raw_dir") / kind
    d.mkdir(parents=True, exist_ok=True)
    safe = "".join(c if c.isalnum() or c in "-_@." else "_" for c in key)
    return d / f"{safe}.json"


def _read_cache(path: Path) -> Any | None:
    if path.exists():
        try:
            with open(path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return None
    return None


def _write_cache(path: Path, obj: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(obj, f, ensure_ascii=False, default=str)
    tmp.replace(path)  # atomic-ish; protects against crash mid-write


# --------------------------------------------------------------------------- #
# Base interface
# --------------------------------------------------------------------------- #
class Collector:
    def __init__(self, cfg: Cfg, logger):
        self.cfg = cfg
        self.log = logger
        self.scrape_date = cfg.scrape_date()
        self._last_net = 0.0
        self.concurrency = int(cfg.collection.get("concurrency", 1) or 1)
        # crude counters surfaced in the run summary (approximate under threads — fine)
        self.stats = {"net_calls": 0, "cache_hits": 0, "failures": 0}

    # -- politeness --
    def _throttle(self) -> None:
        # When running concurrently, the bounded worker pool is the rate limit, so we don't
        # also serialize every call behind a shared sleep. Only throttle in sequential mode.
        if self.concurrency > 1:
            return
        gap = float(self.cfg.collection.rate_limit_seconds)
        elapsed = time.monotonic() - self._last_net
        if elapsed < gap:
            time.sleep(gap - elapsed)
        self._last_net = time.monotonic()

    # Errors that are PERMANENT for a given id — retrying cannot help, so we fail fast.
    # (members-only, private, removed, geo-blocked, comments/likes-disabled-channel, etc.)
    _PERMANENT_MARKERS = (
        "members-only",
        "members only",
        "this channel's members",
        "join this channel",
        "private video",
        "video unavailable",
        "video is unavailable",
        "has been removed",
        "account associated with this video has been terminated",
        "does not have a videos tab",
        "this live event will begin",
        "premieres in",
        "sign in to confirm your age",
        "is not available",
    )

    def _is_permanent(self, e: Exception) -> bool:
        msg = str(e).lower()
        return any(m in msg for m in self._PERMANENT_MARKERS)

    def _retrying(self, fn, what: str):
        """Run fn() with exponential backoff. Returns None on terminal failure.

        Permanent errors (members-only, private, removed, ...) are NOT retried — at M3
        scale, retrying tens of thousands of dead ids would waste hours. They are logged
        once and skipped (the row is simply absent; downstream tolerates missing ids).
        """
        tries = int(self.cfg.collection.max_retries)
        base = float(self.cfg.collection.retry_backoff_seconds)
        for attempt in range(1, tries + 1):
            try:
                self._throttle()
                self.stats["net_calls"] += 1
                return fn()
            except Exception as e:  # noqa: BLE001 - we genuinely want any transient error
                if self._is_permanent(e):
                    self.stats["failures"] += 1
                    self.log.info(f"skip {what}: permanent ({str(e)[:90]})")
                    return None
                wait = base * (2 ** (attempt - 1))
                if attempt == tries:
                    self.stats["failures"] += 1
                    self.log.warning(f"FAILED {what} after {tries} tries: {e}")
                    return None
                self.log.info(
                    f"retry {attempt}/{tries} for {what} in {wait:.1f}s ({e.__class__.__name__})"
                )
                time.sleep(wait)

    def get_videos_metadata(self, ids: list[str]) -> dict[str, dict]:
        """Fetch many videos -> {video_id: meta}. Default: parallel single-id calls (good for
        yt-dlp). The API backend overrides this to BATCH 50 ids/call so quota stays sane
        (videos.list = 1 unit per call of up to 50 ids, not 1 unit per video)."""
        from concurrent.futures import ThreadPoolExecutor

        out: dict[str, dict] = {}
        workers = max(1, self.concurrency)
        with ThreadPoolExecutor(max_workers=workers) as ex:
            for vid, meta in zip(ids, ex.map(self.get_video_metadata, ids)):
                if meta:
                    out[vid] = meta
        return out

    # subclasses implement:
    def get_channel_metadata(self, ref: str) -> dict | None:  # pragma: no cover
        raise NotImplementedError

    def list_channel_videos(self, ref: str, cap: int) -> list[dict]:  # pragma: no cover
        raise NotImplementedError

    def get_video_metadata(self, video_id: str) -> dict | None:  # pragma: no cover
        raise NotImplementedError

    # shared: derived fields applied to every normalized video record
    def _finalize_video_record(self, rec: dict) -> dict:
        up = rec.get("upload_date")
        rec["scrape_date"] = self.scrape_date.isoformat()
        rec["days_since_upload"] = None
        if up:
            try:
                up_d = _dt.date.fromisoformat(up)
                rec["days_since_upload"] = (self.scrape_date - up_d).days
            except ValueError:
                pass
        short_max = float(self.cfg.collection.short_max_seconds)
        dur = rec.get("duration_seconds")
        rec["is_short"] = bool(
            (dur is not None and dur <= short_max) or rec.get("from_shorts_tab")
        )
        rec["like_count_is_null"] = rec.get("like_count") is None
        rec["comment_count_is_null"] = rec.get("comment_count") is None
        return rec

    # thumbnail download (shared; uses requests, independent of metadata backend)
    def download_thumbnail(self, video_id: str, raw: dict | None = None):
        import requests

        thumbs_dir = self.cfg.path("thumbnails_dir")
        thumbs_dir.mkdir(parents=True, exist_ok=True)
        out = thumbs_dir / f"{video_id}.jpg"
        # build candidate URLs in resolution-preference order
        names = list(self.cfg.collection.thumbnail_pref)
        candidates = [f"https://i.ytimg.com/vi/{video_id}/{n}.jpg" for n in names]
        # fall back to whatever yt-dlp/API surfaced
        if raw:
            for t in sorted(
                raw.get("thumbnails", []) or [],
                key=lambda t: (t.get("width") or 0) * (t.get("height") or 0),
                reverse=True,
            ):
                if t.get("url"):
                    candidates.append(t["url"])
            if raw.get("thumbnail"):
                candidates.append(raw["thumbnail"])

        if out.exists() and out.stat().st_size > 0:
            self.stats["cache_hits"] += 1
            # return the first candidate as the canonical url for the record
            return candidates[0] if candidates else None, str(out)

        for url in candidates:
            try:
                r = requests.get(url, timeout=20)
                # maxresdefault often 404s; skip empties / placeholders
                if r.status_code == 200 and len(r.content) > 1000:
                    out.write_bytes(r.content)
                    return url, str(out)
            except requests.RequestException:
                continue
        self.log.info(f"no usable thumbnail for {video_id}")
        return (candidates[0] if candidates else None), None


# --------------------------------------------------------------------------- #
# yt-dlp backend
# --------------------------------------------------------------------------- #
class _QuietYdlLogger:
    """Adapter so yt-dlp's internal error/warning spam goes to our logfile at DEBUG,
    not the console. We surface the meaningful outcome ourselves via _retrying()."""

    def __init__(self, logger):
        self._log = logger

    def debug(self, msg):  # yt-dlp routes most info here (prefixed '[debug] ')
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        self._log.debug(f"[yt-dlp] {msg}")

    def error(self, msg):
        self._log.debug(f"[yt-dlp] {msg}")


class YtDlpCollector(Collector):
    def __init__(self, cfg: Cfg, logger):
        super().__init__(cfg, logger)
        import yt_dlp  # imported here so API-only users need not install it

        self._yt_dlp = yt_dlp
        # Route yt-dlp's own chatter into our logger at DEBUG so the console isn't spammed
        # with ERROR lines for members-only/private videos that we already handle & log.
        self._ydl_logger = _QuietYdlLogger(logger)

    def _opts(self, **extra) -> dict:
        base = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "logger": self._ydl_logger,
        }
        base.update(extra)
        return base

    @staticmethod
    def _channel_url(ref: str) -> str:
        ref = ref.strip()
        if ref.startswith("http"):
            return ref
        if ref.startswith("@"):
            return f"https://www.youtube.com/{ref}"
        if ref.startswith("UC") and len(ref) == 24:
            return f"https://www.youtube.com/channel/{ref}"
        return f"https://www.youtube.com/@{ref}"

    def _extract(self, url: str, opts: dict, what: str):
        def _run():
            with self._yt_dlp.YoutubeDL(opts) as ydl:
                return ydl.extract_info(url, download=False)

        return self._retrying(_run, what)

    # ---- channel metadata ----
    def get_channel_metadata(self, ref: str) -> dict | None:
        cache = _cache_path(self.cfg, "channels", ref)
        cached = _read_cache(cache)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached

        url = self._channel_url(ref) + "/videos"
        # we only need the channel-level header here
        opts = self._opts(extract_flat="in_playlist", playlistend=1)
        info = self._extract(url, opts, f"channel meta {ref}")
        if info is None:
            return None
        rec = {
            "channel_ref": ref,
            "channel_id": info.get("channel_id") or info.get("uploader_id"),
            "channel_title": info.get("channel") or info.get("uploader") or info.get("title"),
            # yt-dlp exposes follower count at the channel-tab top level
            "subscriber_count": info.get("channel_follower_count"),
            # yt-dlp can't give a reliable lifetime total here (we cap the header listing),
            # so record None rather than a misleading 0. The Data API backend fills the true
            # videoCount. Documented limitation.
            "total_video_count": None,
            # channel created date is NOT reliably available via yt-dlp flat extract.
            "channel_created_at": None,
            "channel_url": info.get("channel_url") or self._channel_url(ref),
            "scrape_date": self.scrape_date.isoformat(),
        }
        _write_cache(cache, rec)
        return rec

    # ---- list videos (light) ----
    def list_channel_videos(self, ref: str, cap: int) -> list[dict]:
        url = self._channel_url(ref) + "/videos"
        opts = self._opts(extract_flat="in_playlist", playlistend=int(cap))
        info = self._extract(url, opts, f"list videos {ref}")
        if info is None:
            return []
        out = []
        for e in info.get("entries", []) or []:
            if not e:
                continue
            out.append(
                {
                    "video_id": e.get("id"),
                    "title": e.get("title"),
                    "duration_seconds": e.get("duration"),
                    "view_count": e.get("view_count"),
                    "url": e.get("url"),
                }
            )
        return out

    # ---- full per-video metadata (cached) ----
    def get_video_metadata(self, video_id: str) -> dict | None:
        cache = _cache_path(self.cfg, "videos", video_id)
        cached = _read_cache(cache)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached

        url = f"https://www.youtube.com/watch?v={video_id}"
        info = self._extract(url, self._opts(), f"video {video_id}")
        if info is None:
            return None

        up = info.get("upload_date")  # 'YYYYMMDD'
        upload_iso = None
        if up and len(str(up)) == 8:
            upload_iso = f"{up[:4]}-{up[4:6]}-{up[6:8]}"

        rec = {
            "video_id": info.get("id"),
            "channel_id": info.get("channel_id"),
            "channel_title": info.get("channel") or info.get("uploader"),
            "title": info.get("title"),
            "description": info.get("description"),
            "upload_date": upload_iso,
            "duration_seconds": info.get("duration"),
            "view_count": info.get("view_count"),
            "like_count": info.get("like_count"),
            "comment_count": info.get("comment_count"),
            "subscriber_count": info.get("channel_follower_count"),
            "tags": info.get("tags") or [],
            "webpage_url": info.get("webpage_url"),
            "availability": info.get("availability"),
            "was_live": info.get("was_live"),
            "from_shorts_tab": False,
            # keep the thumbnails list so download_thumbnail can fall back without a re-fetch
            "thumbnails": info.get("thumbnails") or [],
            "thumbnail": info.get("thumbnail"),
        }
        rec = self._finalize_video_record(rec)
        _write_cache(cache, rec)
        return rec


# --------------------------------------------------------------------------- #
# YouTube Data API backend (alternative; same interface)
# --------------------------------------------------------------------------- #
class YouTubeApiCollector(Collector):
    """
    Quota-aware Data API backend. Built behind the same interface so it is a drop-in
    alternative (collection.backend: youtube_api). Quota accounting:
      search.list = 100 units; videos.list / channels.list ~= 1 unit per call (50 ids/call).
    We log spend against youtube_api.daily_quota_units.
    """

    def __init__(self, cfg: Cfg, logger):
        super().__init__(cfg, logger)
        import os

        from googleapiclient.discovery import build  # type: ignore

        key = os.environ.get(str(cfg.youtube_api.api_key_env))
        if not key:
            raise RuntimeError(
                f"API backend selected but env var {cfg.youtube_api.api_key_env} is unset. "
                f"Set it in .env (see .env.example)."
            )
        self._yt = build("youtube", "v3", developerKey=key, cache_discovery=False)
        self.quota_spent = 0

    def _spend(self, units: int, what: str) -> None:
        self.quota_spent += units
        cap = int(self.cfg.youtube_api.daily_quota_units)
        self.log.info(f"quota +{units} ({what}); total {self.quota_spent}/{cap}")
        if self.quota_spent > cap:
            raise RuntimeError("daily quota exceeded — stopping to avoid silent failures")

    def _resolve_channel_id(self, ref: str) -> str | None:
        ref = ref.strip()
        if ref.startswith("UC") and len(ref) == 24:
            return ref
        handle = ref.lstrip("@") if not ref.startswith("http") else ref.rstrip("/").split("/")[-1].lstrip("@")
        res = self._retrying(
            lambda: self._yt.channels().list(part="id", forHandle=handle).execute(),
            f"resolve {ref}",
        )
        self._spend(1, "channels.list(forHandle)")
        items = (res or {}).get("items", [])
        return items[0]["id"] if items else None

    def get_channel_metadata(self, ref: str) -> dict | None:
        cache = _cache_path(self.cfg, "channels", ref)
        cached = _read_cache(cache)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached
        cid = self._resolve_channel_id(ref)
        if not cid:
            return None
        res = self._retrying(
            lambda: self._yt.channels()
            .list(part="snippet,statistics,contentDetails", id=cid)
            .execute(),
            f"channel {ref}",
        )
        self._spend(1, "channels.list")
        items = (res or {}).get("items", [])
        if not items:
            return None
        it = items[0]
        sn, st = it.get("snippet", {}), it.get("statistics", {})
        rec = {
            "channel_ref": ref,
            "channel_id": cid,
            "channel_title": sn.get("title"),
            "subscriber_count": int(st["subscriberCount"]) if "subscriberCount" in st else None,
            "total_video_count": int(st["videoCount"]) if "videoCount" in st else None,
            "channel_created_at": (sn.get("publishedAt") or "")[:10] or None,
            "channel_url": f"https://www.youtube.com/channel/{cid}",
            "uploads_playlist": it.get("contentDetails", {})
            .get("relatedPlaylists", {})
            .get("uploads"),
            "scrape_date": self.scrape_date.isoformat(),
        }
        _write_cache(cache, rec)
        return rec

    def list_channel_videos(self, ref: str, cap: int) -> list[dict]:
        meta = self.get_channel_metadata(ref)
        if not meta or not meta.get("uploads_playlist"):
            return []
        playlist = meta["uploads_playlist"]
        out: list[dict] = []
        page = None
        while len(out) < cap:
            res = self._retrying(
                lambda: self._yt.playlistItems()
                .list(part="contentDetails", playlistId=playlist, maxResults=50, pageToken=page)
                .execute(),
                f"playlistItems {ref}",
            )
            self._spend(1, "playlistItems.list")
            if not res:
                break
            for it in res.get("items", []):
                out.append({"video_id": it["contentDetails"]["videoId"]})
            page = res.get("nextPageToken")
            if not page:
                break
        return out[:cap]

    def get_video_metadata(self, video_id: str) -> dict | None:
        cache = _cache_path(self.cfg, "videos", video_id)
        cached = _read_cache(cache)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached
        res = self._retrying(
            lambda: self._yt.videos()
            .list(part="snippet,statistics,contentDetails", id=video_id)
            .execute(),
            f"video {video_id}",
        )
        self._spend(1, "videos.list")
        items = (res or {}).get("items", [])
        if not items:
            return None
        rec = self._normalize_api_video(items[0])
        _write_cache(cache, rec)
        return rec

    def _normalize_api_video(self, it: dict) -> dict:
        """Map a Data API videos.list item to our standard video record schema."""
        sn = it.get("snippet", {})
        st = it.get("statistics", {})
        cd = it.get("contentDetails", {})
        vid = it.get("id")
        rec = {
            "video_id": vid,
            "channel_id": sn.get("channelId"),
            "channel_title": sn.get("channelTitle"),
            "title": sn.get("title"),
            "description": sn.get("description"),
            "upload_date": (sn.get("publishedAt") or "")[:10] or None,
            "duration_seconds": _iso8601_duration_to_seconds(cd.get("duration")),
            "view_count": int(st["viewCount"]) if "viewCount" in st else None,
            "like_count": int(st["likeCount"]) if "likeCount" in st else None,
            "comment_count": int(st["commentCount"]) if "commentCount" in st else None,
            "subscriber_count": None,  # filled from channel meta in the collect stage
            "tags": sn.get("tags") or [],
            "webpage_url": f"https://www.youtube.com/watch?v={vid}",
            "availability": None,
            "was_live": None,
            "from_shorts_tab": False,
            "thumbnails": list((sn.get("thumbnails") or {}).values()),
            "thumbnail": (sn.get("thumbnails", {}).get("maxres") or {}).get("url"),
        }
        return self._finalize_video_record(rec)

    def get_videos_metadata(self, ids: list[str]) -> dict[str, dict]:
        """Batched videos.list: up to 50 ids per call = 1 quota unit per call (not per video).
        Cached ids are served from disk; only uncached ids hit the API."""
        out: dict[str, dict] = {}
        uncached: list[str] = []
        for vid in ids:
            cached = _read_cache(_cache_path(self.cfg, "videos", vid))
            if cached is not None:
                self.stats["cache_hits"] += 1
                out[vid] = cached
            else:
                uncached.append(vid)

        for i in range(0, len(uncached), 50):
            chunk = uncached[i:i + 50]
            res = self._retrying(
                lambda c=chunk: self._yt.videos()
                .list(part="snippet,statistics,contentDetails", id=",".join(c), maxResults=50)
                .execute(),
                f"videos.list batch [{i}:{i + len(chunk)}]",
            )
            self._spend(1, f"videos.list x{len(chunk)}")
            if not res:
                continue
            for it in res.get("items", []):
                rec = self._normalize_api_video(it)
                if rec.get("video_id"):
                    _write_cache(_cache_path(self.cfg, "videos", rec["video_id"]), rec)
                    out[rec["video_id"]] = rec
        return out


def _iso8601_duration_to_seconds(dur: str | None) -> int | None:
    """Parse 'PT#H#M#S' (YouTube API duration) to seconds. None-safe."""
    if not dur:
        return None
    import re

    m = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", dur)
    if not m:
        return None
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


# --------------------------------------------------------------------------- #
# Factory + search-based discovery
# --------------------------------------------------------------------------- #
def make_collector(cfg: Cfg, logger=None) -> Collector:
    logger = logger or get_logger("collect", cfg.path("logs_dir"))
    backend = str(cfg.collection.backend)
    if backend == "yt_dlp":
        return YtDlpCollector(cfg, logger)
    if backend == "youtube_api":
        return YouTubeApiCollector(cfg, logger)
    raise ValueError(f"unknown collection.backend: {backend!r}")


def discover_channels_by_search(
    cfg: Cfg, logger, keywords: Iterable[str], n_per_keyword: int = 20
) -> list[dict]:
    """
    Search-based channel discovery (yt-dlp path). Returns unique channels surfaced by
    niche keyword search: [{channel_id, channel_title, channel_url, source_keyword}].
    Used to EXPAND the hand seed; results are written to the versioned seed CSV by the
    caller so the sample stays reproducible.
    """
    import yt_dlp

    found: dict[str, dict] = {}
    for kw in keywords:
        url = f"ytsearch{int(n_per_keyword)}:{kw}"
        opts = {"quiet": True, "no_warnings": True, "skip_download": True, "extract_flat": "in_playlist"}
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
        except Exception as e:  # noqa: BLE001
            logger.warning(f"search failed for {kw!r}: {e}")
            continue
        for e in info.get("entries", []) or []:
            cid = e.get("channel_id") or e.get("uploader_id")
            if cid and cid not in found:
                found[cid] = {
                    "channel_id": cid,
                    "channel_title": e.get("channel") or e.get("uploader"),
                    "channel_url": e.get("channel_url") or e.get("uploader_url"),
                    "source_keyword": kw,
                }
        logger.info(f"search {kw!r}: cumulative unique channels = {len(found)}")
    return list(found.values())
