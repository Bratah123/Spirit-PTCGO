from dwd.Protobuf import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

class AllAvatarArchetypesFound(_message.Message):
    __slots__ = ["archetypes", "checksum"]
    archetypes: _containers.RepeatedCompositeFieldContainer[_base_pb2.Archetype]
    checksum: str
    def __init__(self, archetypes: _Optional[_Iterable[_Union[_base_pb2.Archetype, _Mapping]]] = ..., checksum: _Optional[str] = ...) -> None: ...
