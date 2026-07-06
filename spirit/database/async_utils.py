import asyncio

async def run_db(func, *args, **kwargs):
    """Runs a blocking DB function on a worker thread so it never stalls the event loop."""
    return await asyncio.to_thread(func, *args, **kwargs)
