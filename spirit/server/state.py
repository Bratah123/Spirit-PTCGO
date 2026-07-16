import time
import threading

from spirit import config

# CAS tickets issued by the HTTP server (worker threads) and consumed by the TCP
# server (event loop). Guarded by a lock since writers and the sweeper race across
# threads. Format: { "ST-TICKET-12345": (username, issued_at_monotonic) }
PENDING_TICKETS = {}
PENDING_TICKETS_LOCK = threading.Lock()
TICKET_TTL_SECONDS = 600

def issue_ticket(ticket, username):
    with PENDING_TICKETS_LOCK:
        PENDING_TICKETS[ticket] = (username, time.monotonic())

def consume_ticket(ticket, username):
    """Atomically validates and removes a ticket; returns True on success."""
    with PENDING_TICKETS_LOCK:
        entry = PENDING_TICKETS.get(ticket)
        if entry is None or entry[0] != username:
            return False
        del PENDING_TICKETS[ticket]
        return True

def sweep_expired_tickets():
    """Drops tickets whose CAS handshake never completed."""
    now = time.monotonic()
    with PENDING_TICKETS_LOCK:
        expired = [t for t, (_, issued_at) in PENDING_TICKETS.items()
                   if now - issued_at > TICKET_TTL_SECONDS]
        for ticket in expired:
            PENDING_TICKETS.pop(ticket, None)

# The active server host (captured from HTTP config request)
SERVER_HOST = f"{config.PUBLIC_HOST}:{config.HTTP_PORT}"
