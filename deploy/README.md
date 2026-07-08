# Remote (VPS) deployment

The game server runs fine locally but two classes of data don't survive a
`git clone`/`pull` deploy, and Python's built-in asset server doesn't hold up
over WAN. This directory fixes both.

## 1. Get the data onto the VPS

A `git pull` gives you the code, the card PNGs, the bundle template, and (now)
the localization DB. It does **not** give you the built bundles or avatars —
those are gitignored on purpose (too large / regenerable). Ship them with rsync:

```bash
# from the repo root, in Git Bash or WSL
VPS=user@66.179.95.41 REMOTE=/home/user/Spirit-PTCGO ./deploy/sync-assets.sh
```

- **Localization strings** (the raw-key bug): fixed by `git pull` now that
  `LocalizationDB-UTF8.db` is committed. `sync-assets.sh` verifies it matches by
  checksum. A cold VPS was showing ~2,868 strings (just the auto-generated
  custom-card names) instead of the full ~30,418 because the DB wasn't present.
- **Card bundles** (`Bundle-Failed` / slow): shipped prebuilt by the script.
  Shipping them prebuilt avoids the VPS cold-generating ~1 GB from PNGs on first
  boot while players are waiting.

## 2. Put a real static edge in front of the asset server

Python's `http.server` writes each ~84 MB set bundle in one `wfile.write()` with
no HTTP Range / resume. Over WAN that truncates. Front it with nginx (recommended)
or Caddy.

```
client ──HTTP :8000──> nginx (cache + range) ──> Python asset server 127.0.0.1:8001
```

Run the Python server on 8001 so nginx can own the public port:

```bash
SPIRIT_HTTP_PORT=8001 SPIRIT_PUBLIC_HOST=66.179.95.41 python -m spirit.main
```

`AssetURL` is built from the client's `Host` header, so it keeps resolving to
`:8000` (nginx) with no server code change.

- **nginx** (built-in disk cache + byte-range): see `nginx-spirit.conf` — install
  steps are in the file header.
- **Caddy** (simpler, streams robustly; response caching needs the Souin plugin):
  see `Caddyfile`.

### Verify range/resume works

```bash
# should return HTTP/1.1 206 Partial Content and a Content-Range header
curl -s -D- -o /dev/null -r 0-1023 http://66.179.95.41:8000/en_US/en_US_SWSH8.unity3d
# second hit should show X-Cache-Status: HIT (nginx)
curl -s -D- -o /dev/null http://66.179.95.41:8000/en_US/en_US_SWSH8.unity3d | grep -i x-cache
```

## 3. (Optional) config.py default host

`spirit/config.py` defaults `PUBLIC_HOST` to a hardcoded IP. On the VPS always
set `SPIRIT_PUBLIC_HOST=66.179.95.41` (env) rather than relying on the committed
default — it's the address the Warg login handshake redirects clients to for TCP.
