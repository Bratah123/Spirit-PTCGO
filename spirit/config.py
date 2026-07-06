"""Global server addressing config — the single place to set the host players connect to."""
import os

# The address players use to reach this server (IP or domain, no scheme/port).
# For public hosting set this to your public IP/domain, or export SPIRIT_PUBLIC_HOST.
# The client is redirected here mid-login (ConnectionService), so 127.0.0.1 only works
# when the client runs on the same machine as the server.
PUBLIC_HOST = os.environ.get("SPIRIT_PUBLIC_HOST", "127.0.0.1")

HTTP_PORT = int(os.environ.get("SPIRIT_HTTP_PORT", "8000"))
TCP_PORT = int(os.environ.get("SPIRIT_TCP_PORT", "39389"))

HTTP_BASE_URL = f"http://{PUBLIC_HOST}:{HTTP_PORT}"
PLACEHOLDER_IMG = f"{HTTP_BASE_URL}/placeholder.png"
