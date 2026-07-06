from google.protobuf import message as _message
from typing import Optional as _Optional

class ProtoMessage(_message.Message):
    __slots__ = ["messageName", "messageTag"]
    messageName: str
    messageTag: int
    def __init__(self, messageName: _Optional[str] = ..., messageTag: _Optional[int] = ...) -> None: ...
