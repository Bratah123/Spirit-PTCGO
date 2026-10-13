import asyncio
from collections import deque
import struct
import json
import zlib
import sys
import os

from spirit import config
from spirit.server import metrics

# Ensure path is loaded
protobuf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'protobuf', 'compiled'))
if protobuf_path not in sys.path:
    sys.path.insert(0, protobuf_path)
    
from dwd.Protobuf.wrapper_pb2 import ProtoMessage

def _encode_varint(value):
    res = bytearray()
    while value >= 0x80:
        res.append(0x80 | (value & 0x7f))
        value >>= 7
    res.append(value)
    return bytes(res)

class WargFlags:
    CLEAR = 0
    COMPRESSED = 1
    PROTOBUF = 2
    PING_PONG = 4
    CONNECTION_ERROR = 16
    ACKNOWLEDGE_REQUEST = 32
    RECONNECT_SESSION = 64
    GRANTED_SESSION = 128

class WargProtocol:
    HEADER_SIZE = 12

    @staticmethod
    def zigzag_encode(n):
        """Encodes a signed integer using ZigZag encoding (sint32/sint64)."""
        return (n << 1) ^ (n >> 31)

    @staticmethod
    def zigzag_decode(n):
        """Decodes a ZigZag encoded integer back to a signed integer."""
        return (n >> 1) ^ -(n & 1)

    @staticmethod
    def decode_header(data):
        # Big-Endian: Length(4), RequestID(4), Flags(4)
        
        # Check for TLS Client Hello (0x16 0x03 0x01 ... )
        # If the first byte is 22 (Handshake), it's highly likely to be SSL/TLS
        if len(data) >= 3 and data[0] == 0x16 and data[1] == 0x03:
            raise ConnectionError("TLS/SSL Client Hello detected! The client is expecting a secure connection, but the server is running raw TCP.")
            
        length, request_id, flags = struct.unpack(">III", data)
        body_length = length - 8
        
        if body_length < 0 or body_length > 10000000: # 10MB sanity check
             raise ConnectionError(f"Invalid body length decoded: {body_length}")
             
        return body_length, request_id, flags

    @staticmethod
    def encode_header(body_length, request_id, flags):
        length = body_length + 8
        return struct.pack(">III", length, request_id, flags)

    @staticmethod
    def decode_body(body, flags):
        if flags & WargFlags.COMPRESSED:
            # Skip first 2 bytes if compressed (Zlib header). Bound the OUTPUT size:
            # deflate reaches ~1000:1, so an unbounded decompress of a 10 MB body can
            # allocate ~10 GB from a single unauthenticated packet. Cap the expansion
            # and reject anything larger — the read loop tears the connection down.
            limit = config.MAX_DECOMPRESSED_BYTES
            decompressor = zlib.decompressobj(-zlib.MAX_WBITS)  # Raw deflate
            body = decompressor.decompress(body[2:], limit)
            if decompressor.unconsumed_tail:
                raise ConnectionError(
                    f"Decompressed body exceeds {limit}-byte cap (possible zlib bomb)")

        if flags & WargFlags.PROTOBUF:
            # The structure for Protobuf in PTCGO is generally just the binary payload.
            # However, because there are multiple possible root messages, Warg Server
            # sometimes relies on context (the request ID or state) to know what to deserialize.
            # In our case, the router processes raw `bytes` for protobuf, or we can parse it in the handler.
            return body
        else:
            try:
                return json.loads(body)
            except (UnicodeDecodeError, json.JSONDecodeError):
                return body

    @staticmethod
    def encode_body(data, flags):
        if flags & WargFlags.PROTOBUF:
            
            # The PTCGO client expects a ProtoMessage wrapper
            # 1. messageName (string, tag 1)
            # 2. messageTag (int32, tag 2)
            # 3. The actual payload is appended as an extension field using the messageTag
            
            wrapper = ProtoMessage()
            # Use the fully qualified name (e.g. dwd.Protobuf.Progression.AllScenarios)
            # as the client uses Assembly.GetType(messageName)
            msg_name = data.DESCRIPTOR.full_name 
            wrapper.messageName = msg_name
            wrapper.messageTag = 100 # Use a tag that doesn't collide with 1 (messageName) or 2 (messageTag)

            wrapper_bytes = wrapper.SerializeToString()

            # Manual extension field at messageTag
            payload_bytes = data.SerializeToString()

            # Wire type 2 (Length-delimited) for nested messages
            extension_header = _encode_varint((wrapper.messageTag << 3) | 2)
            extension_length = _encode_varint(len(payload_bytes))
            
            return wrapper_bytes + extension_header + extension_length + payload_bytes

        if isinstance(data, dict):
            # PTCGO's JsonFx requires polymorphic objects to be wrapped in {"name": ClassName, "value": {payload}}
            if "messageName" in data:
                # We need to make a copy so we don't modify the original dict passed by the handler
                payload = dict(data) 
                msg_name = payload.pop("messageName")
                
                # If the ONLY thing in the packet was the messageName (e.g. an empty request),
                # we send value as {} to match C# expectations for empty classes.
                if len(payload) == 0:
                     wrapped_data = {"name": msg_name, "value": {}}
                else:
                     wrapped_data = {"name": msg_name, "value": payload}
            else:
                wrapped_data = data
                
            body = json.dumps(wrapped_data).encode('utf-8')
        elif isinstance(data, list):
            body = json.dumps(data).encode('utf-8')
        else:
            body = data # Assume bytes
        
        return body


class OutboundQueue:
    def __init__(self, writer, on_error, *, max_bytes=8 * 1024 * 1024,
                 batch_bytes=256 * 1024, timeout=60):
        if max_bytes <= 0 or batch_bytes <= 0 or timeout <= 0:
            raise ValueError("Outbound limits and timeout must be positive")
        self.writer = writer
        self.on_error = on_error
        self.max_bytes = max_bytes
        self.batch_bytes = batch_bytes
        self.timeout = timeout
        self.pending_bytes = 0
        self._frames = deque()
        self._ready = asyncio.Event()
        self._progress = asyncio.Event()
        self._accepted = 0
        self._drained = 0
        self._closed = False
        self._task = None

    def enqueue(self, frames):
        """Accept a complete batch without yielding, or fail the connection."""
        if self._closed:
            return False
        batch = []
        size = 0
        for frame in frames:
            size += len(frame)
            if self.pending_bytes + size > self.max_bytes:
                metrics.inc("outbound_overflows")
                self.fail(BufferError("Outbound byte limit exceeded"))
                return False
            if frame:
                batch.append(frame)
        if not batch:
            return True
        deadline = asyncio.get_running_loop().time() + self.timeout
        self._frames.extend((frame, deadline) for frame in batch)
        self.pending_bytes += size
        self._accepted += size
        self._ready.set()
        if self._task is None:
            self._task = asyncio.create_task(self._run(), name="warg-writer")
        return True

    def _notify_progress(self):
        self._progress.set()
        self._progress = asyncio.Event()

    async def flush(self):
        """Wait for bytes accepted before this call to drain, not for peer acknowledgment."""
        target = self._accepted
        while not self._closed and self._drained < target:
            await self._progress.wait()
        return not self._closed

    def _discard(self):
        self._closed = True
        self._frames.clear()
        self.pending_bytes = 0
        self._ready.set()
        self._notify_progress()

    def fail(self, error):
        if self._closed:
            return
        self._discard()
        try:
            self.writer.transport.abort()
        finally:
            self.on_error(error)

    async def _run(self):
        try:
            while not self._closed:
                await self._ready.wait()
                if self._closed:
                    break
                frames = []
                size = 0
                deadline = self._frames[0][1]
                while self._frames:
                    frame = self._frames[0][0]
                    if frames and size + len(frame) > self.batch_bytes:
                        break
                    self._frames.popleft()
                    frames.append(frame)
                    size += len(frame)
                if not self._frames:
                    self._ready.clear()
                remaining = deadline - asyncio.get_running_loop().time()
                if remaining <= 0:
                    raise TimeoutError("Outbound queue deadline expired")
                self.writer.write(b"".join(frames))
                metrics.inc("bytes_out", size)
                metrics.inc("outbound_batches")
                metrics.inc("outbound_frames", len(frames))
                del frames, frame
                await asyncio.wait_for(self.writer.drain(), timeout=remaining)
                if self._closed:
                    break
                self.pending_bytes -= size
                self._drained += size
                self._notify_progress()
        except asyncio.CancelledError:
            raise
        except Exception as error:
            if isinstance(error, TimeoutError):
                metrics.inc("send_timeouts")
            else:
                metrics.inc("outbound_errors")
            self.fail(error)

    async def close(self):
        """Discard pending output and join the writer task."""
        self._discard()
        if self._task is not None:
            self._task.cancel()
            await asyncio.gather(self._task, return_exceptions=True)
