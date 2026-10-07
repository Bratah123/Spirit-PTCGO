"""Global server addressing config — the single place to set the host players connect to."""
import os

# The address players use to reach this server (IP or domain, no scheme/port).
# For public hosting set this to your public IP/domain, or export SPIRIT_PUBLIC_HOST.
# The client is redirected here mid-login (ConnectionService), so 127.0.0.1 only works
# when the client runs on the same machine as the server.
PUBLIC_HOST = os.environ.get("SPIRIT_PUBLIC_HOST", "127.0.0.1")

HTTP_PORT = int(os.environ.get("SPIRIT_HTTP_PORT", "8000"))
TCP_PORT = int(os.environ.get("SPIRIT_TCP_PORT", "39389"))

# Player database. Leave unset for local SQLite, or set a mysql+pymysql:// or
# mariadb+pymysql:// URL for MariaDB/MySQL
# See example in README in sql/README.md
DATABASE_URL = os.environ.get("SPIRIT_DATABASE_URL")

HTTP_BASE_URL = f"http://{PUBLIC_HOST}:{HTTP_PORT}"
PLACEHOLDER_IMG = f"{HTTP_BASE_URL}/placeholder.png"

# --- Operational tunables (env-overridable; safe defaults chosen to never affect legit play) ---
LOG_LEVEL = os.environ.get("SPIRIT_LOG_LEVEL", "INFO").upper()

# Outbound send: abort a socket whose write buffer never drains within this many
# seconds (a wedged/zero-window peer). Largest payloads are a few-hundred-KB SGS
# snapshots, so a stalled drain past this is a dead peer, not a slow one.
SEND_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_SEND_TIMEOUT", "60"))

# Inbound read idle deadlines. The client pings regularly, so a header that never
# arrives for this long is a half-open/dead socket. Pre-auth is tighter to reap
# port-scanners and stalled handshakes before they allocate a router.
IDLE_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_IDLE_TIMEOUT", "240"))
PREAUTH_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_PREAUTH_TIMEOUT", "60"))

# Max bytes an inbound zlib body may expand to (decompression-bomb guard). Legit
# client-originated compressed payloads are decks/telemetry, well under 1 MB.
MAX_DECOMPRESSED_BYTES = int(os.environ.get("SPIRIT_MAX_DECOMPRESSED", str(16 * 1024 * 1024)))

# Hard cap on simultaneous TCP connections (0 = unlimited). Excess accepts are
# closed immediately, before a router is built.
MAX_CONNECTIONS = int(os.environ.get("SPIRIT_MAX_CONNECTIONS", "0"))

# Per-connection inbound packet-rate token bucket (abuse guard). Generous enough
# that normal offer/reply cadence and reconnect replay never trip it.
INBOUND_RATE_PER_SEC = float(os.environ.get("SPIRIT_INBOUND_RATE", "80"))
INBOUND_RATE_BURST = float(os.environ.get("SPIRIT_INBOUND_BURST", "240"))

# Matchmaking AI fill: seconds a player may sit alone in a queue before the
# server pairs them with the AI bot instead of leaving them searching forever
# on a quiet server (0 disables the fallback; a human joining first wins).
AI_MATCH_TIMEOUT = float(os.environ.get("SPIRIT_AI_MATCH_TIMEOUT", "8"))

# --- Match timers (server-side only; the client just renders what we send) ---
# Your own turn: quiet seconds before the visible countdown starts, then the
# countdown itself. When both run out the server ends YOUR TURN (never the match).
TURN_INACTIVITY_SECONDS = float(os.environ.get("SPIRIT_TURN_INACTIVITY_SECONDS", "15"))
TURN_COUNTDOWN_SECONDS = float(os.environ.get("SPIRIT_TURN_COUNTDOWN_SECONDS", "15"))
# Prompts answered while it is the OPPONENT'S turn (choosing a new Active after
# a KO, prize picks, forced effect responses). The client shows this whole
# window as a countdown, and when it runs out the server auto-picks a legal
# default and play continues -- no forfeit, no skipped turn of yours.
RESPONSE_TIMEOUT_SECONDS = float(os.environ.get("SPIRIT_RESPONSE_TIMEOUT_SECONDS", "90"))
