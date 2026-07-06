from dwd.Protobuf import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

class Scenario(_message.Message):
    __slots__ = ["scenarioID", "attributes", "children", "entryRequirements", "completionRequirements"]
    scenarioID: _base_pb2.UUID
    attributes: _containers.RepeatedCompositeFieldContainer[_base_pb2.Attribute]
    children: _containers.RepeatedCompositeFieldContainer[_base_pb2.UUID]
    entryRequirements: str
    completionRequirements: str
    def __init__(self, scenarioID: _Optional[_Union[_base_pb2.UUID, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[_base_pb2.Attribute, _Mapping]]] = ..., children: _Optional[_Iterable[_Union[_base_pb2.UUID, _Mapping]]] = ..., entryRequirements: _Optional[str] = ..., completionRequirements: _Optional[str] = ...) -> None: ...

class AllScenarios(_message.Message):
    __slots__ = ["completed", "available", "unavailable", "roots"]
    completed: _containers.RepeatedCompositeFieldContainer[Scenario]
    available: _containers.RepeatedCompositeFieldContainer[Scenario]
    unavailable: _containers.RepeatedCompositeFieldContainer[Scenario]
    roots: _containers.RepeatedCompositeFieldContainer[Scenario]
    def __init__(self, completed: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ..., available: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ..., unavailable: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ..., roots: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ...) -> None: ...
