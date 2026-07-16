import logging
import threading
import asyncio
import queue
from typing import Callable, Any
from spirit.database.connection import db_session

class DBWriteJob:
    def __init__(self, action_func: Callable, loop: asyncio.AbstractEventLoop):
        self.action_func = action_func
        self.loop = loop
        self.event = asyncio.Event()
        self.result = None
        self.error = None

class DBQueueManagerCrossThread:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBQueueManagerCrossThread, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return
        self._initialized = True
        self.write_queue: queue.Queue = queue.Queue()
        self.worker_thread: threading.Thread | None = None
        self.running: bool = False

    def start_writer(self):
        if self.running:
            return
        self.running = True
        self.worker_thread = threading.Thread(target=self._writer_loop, daemon=True)
        self.worker_thread.start()
        logging.info("[DB] Background write worker started.")

    def stop_writer(self):
        self.running = False
        # Push a sentinel to wake up the thread
        self.write_queue.put(None)
        if self.worker_thread:
            self.worker_thread.join(timeout=2.0)
        logging.info("[DB] Background write worker stopped.")

    def _writer_loop(self):
        """Runs in a background thread, processes DB write jobs synchronously."""
        while self.running:
            try:
                job = self.write_queue.get(timeout=1.0)
                if job is None:
                    continue # Sentinel to stop
                    
                # Execute the synchronous DB function with a fresh thread-safe session
                try:
                    with db_session() as session:
                        # We pass the session to the action_func
                        job.result = job.action_func(session)
                except Exception as e:
                    job.error = e
                    logging.error(f"[DB] Write Job Error: {e}", exc_info=True)
                finally:
                    # Notify the async task that we are done
                    job.loop.call_soon_threadsafe(job.event.set)
                    self.write_queue.task_done()
            except queue.Empty:
                pass

    async def execute_write(self, action_func: Callable) -> Any:
        """Pushes a write job to the queue and awaits its completion."""
        if not self.running:
            # Fail fast rather than enqueue into a stopped writer (whose Event would
            # never be set, hanging the awaiter forever).
            raise RuntimeError("DB write worker is not running")
        loop = asyncio.get_running_loop()
        job = DBWriteJob(action_func, loop)
        self.write_queue.put(job)

        await job.event.wait()

        if job.error:
            raise job.error
        return job.result

db_manager = DBQueueManagerCrossThread()
