import time

from spirit import config

# CAS tickets issued by the HTTP server and consumed by the TCP server.
# Format: { "ST-TICKET-12345": (username, issued_at_monotonic) }
PENDING_TICKETS = {}
TICKET_TTL_SECONDS = 600

def sweep_expired_tickets():
    """Drops tickets whose CAS handshake never completed."""
    now = time.monotonic()
    # Snapshot: inserted from HTTP threads while swept on the event loop
    expired = [t for t, (_, issued_at) in list(PENDING_TICKETS.items())
               if now - issued_at > TICKET_TTL_SECONDS]
    for ticket in expired:
        PENDING_TICKETS.pop(ticket, None)

# The active server host (captured from HTTP config request)
SERVER_HOST = f"{config.PUBLIC_HOST}:{config.HTTP_PORT}"
