# Remote (VPS) deployment

The game server runs fine locally but Python's built-in asset server doesn't hold up
over WAN. This directory fixes that.

## 1. Put a real static edge in front of the asset server

Python's `http.server` writes each ~84 MB set bundle in one `wfile.write()` with
no HTTP Range / resume. Over WAN that truncates. Front it with nginx (recommended)
or Caddy.

```
client ──HTTP :8000──> nginx (cache + range) ──> Python asset server 127.0.0.1:8001
```

Run the Python server on 8001 so nginx can own the public port:

```bash
SPIRIT_HTTP_PORT=8001 SPIRIT_PUBLIC_HOST=YOUR_VPS_IP python -m spirit.main
```

`AssetURL` is built from the client's `Host` header, so it keeps resolving to
`:8000` (nginx) with no server code change.

### nginx (recommended — built-in disk cache + byte-range)

Stand up the edge on the VPS:

```bash
sudo cp deploy/nginx-spirit.conf /etc/nginx/sites-available/spirit
sudo ln -s /etc/nginx/sites-available/spirit /etc/nginx/sites-enabled/
sudo mkdir -p /var/cache/spirit_assets && sudo chown www-data:www-data /var/cache/spirit_assets
sudo nginx -t && sudo systemctl reload nginx
```

Then start the game server on 8001 (command above). Firewall: open `8000` (nginx)
and `39389` (TCP game server); keep `8001` closed — nginx reaches Python over loopback.

### Caddy (simpler; streams robustly, but response caching needs the Souin plugin)

See `Caddyfile`.

### Verify range/resume works

```bash
# should return HTTP/1.1 206 Partial Content and a Content-Range header
curl -s -D- -o /dev/null -r 0-1023 http://YOUR_VPS_IP:8000/en_US/en_US_SWSH8.unity3d
# second hit should show X-Cache-Status: HIT (nginx)
curl -s -D- -o /dev/null http://YOUR_VPS_IP:8000/en_US/en_US_SWSH8.unity3d | grep -i x-cache
```

## 2. (Optional) config.py default host

`spirit/config.py` defaults `PUBLIC_HOST` to a hardcoded IP. On the VPS always
set `SPIRIT_PUBLIC_HOST=YOUR_VPS_IP` (env) rather than relying on the committed
default — it's the address the Warg login handshake redirects clients to for TCP.
