"""Lightweight, dependency-free process metrics.
"""
import time
import asyncio
import logging
from typing import Callable

_counters: dict[str, int] = {}
_gauges: dict[str, Callable] = {}

# Event-loop lag ring buffer (ms), filled by sample_loop_lag().
_lag_samples: list[float] = []
_LAG_WINDOW = 300  # ~5 min at 1 Hz


def inc(name: str, amount: int = 1) -> None:
    _counters[name] = _counters.get(name, 0) + amount


def register_gauge(name: str, fn) -> None:
    """Registers a zero-arg callable read at scrape time (controlled cardinality)."""
    _gauges[name] = fn


def _lag_stats() -> dict:
    if not _lag_samples:
        return {"count": 0, "p50_ms": 0.0, "p95_ms": 0.0, "p99_ms": 0.0, "max_ms": 0.0}
    ordered = sorted(_lag_samples)
    n = len(ordered)

    def pct(p):
        return round(ordered[min(n - 1, int(p * n))], 3)

    return {
        "count": n,
        "p50_ms": pct(0.50),
        "p95_ms": pct(0.95),
        "p99_ms": pct(0.99),
        "max_ms": round(ordered[-1], 3),
    }


def snapshot() -> dict:
    """Point-in-time view of all counters, gauges, and loop-lag stats."""
    gauges = {}
    for name, fn in _gauges.items():
        try:
            gauges[name] = fn()
        except Exception:
            gauges[name] = None
    return {
        "ts": time.time(),
        "counters": dict(_counters),
        "gauges": gauges,
        "event_loop_lag": _lag_stats(),
    }


async def sample_loop_lag(interval: float = 1.0):
    """Sleeps `interval` and records how much longer than `interval` it actually
    took — the classic asyncio starvation probe. Never raises out of the loop."""
    while True:
        start = time.perf_counter()
        try:
            await asyncio.sleep(interval)
        except asyncio.CancelledError:
            raise
        except Exception as e:  # defensive: keep the sampler alive
            logging.debug(f"[Metrics] lag sampler hiccup: {e}")
            continue
        lag_ms = max(0.0, (time.perf_counter() - start - interval) * 1000.0)
        _lag_samples.append(lag_ms)
        if len(_lag_samples) > _LAG_WINDOW:
            del _lag_samples[0]
