import struct
import json
import zlib
import sys
import os

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
            # Skip first 2 bytes if compressed (Zlib header)
            body = zlib.decompress(body[2:], -zlib.MAX_WBITS) # Raw deflate
        
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
