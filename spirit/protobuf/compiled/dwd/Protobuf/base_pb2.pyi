from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

class UUID(_message.Message):
    __slots__ = ["lo", "hi"]
    lo: int
    hi: int
    def __init__(self, lo: _Optional[int] = ..., hi: _Optional[int] = ...) -> None: ...

class KeyObjectPair(_message.Message):
    __slots__ = ["key", "value"]
    key: str
    value: Object
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ["objectType", "arrayValue", "dictionaryValue", "stringValue", "boolValue", "intValue", "floatValue", "guidValue"]
    class Type(int):
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> int: ...
        @classmethod
        def keys(cls) -> _Iterable[str]: ...
        @classmethod
        def values(cls) -> _Iterable[int]: ...
        @classmethod
        def items(cls) -> _Iterable[tuple[str, int]]: ...
        UNKNOWN: _ClassVar[Object.Type]
        ARRAY: _ClassVar[Object.Type]
        DICT: _ClassVar[Object.Type]
        STRING: _ClassVar[Object.Type]
        BOOL: _ClassVar[Object.Type]
        INT: _ClassVar[Object.Type]
        FLOAT: _ClassVar[Object.Type]
        UUID: _ClassVar[Object.Type]
        JSON: _ClassVar[Object.Type]

    UNKNOWN: Object.Type
    ARRAY: Object.Type
    DICT: Object.Type
    STRING: Object.Type
    BOOL: Object.Type
    INT: Object.Type
    FLOAT: Object.Type
    UUID: Object.Type
    JSON: Object.Type
    
    objectType: Object.Type
    arrayValue: _containers.RepeatedCompositeFieldContainer[Object]
    dictionaryValue: _containers.RepeatedCompositeFieldContainer[KeyObjectPair]
    stringValue: str
    boolValue: bool
    intValue: int
    floatValue: float
    guidValue: UUID
    def __init__(self, objectType: _Optional[_Union[Object.Type, str]] = ..., arrayValue: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., dictionaryValue: _Optional[_Iterable[_Union[KeyObjectPair, _Mapping]]] = ..., stringValue: _Optional[str] = ..., boolValue: bool = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., guidValue: _Optional[_Union[UUID, _Mapping]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["name", "value", "originalValue", "modValue"]
    name: int
    value: Object
    originalValue: Object
    modValue: Object
    def __init__(self, name: _Optional[int] = ..., value: _Optional[_Union[Object, _Mapping]] = ..., originalValue: _Optional[_Union[Object, _Mapping]] = ..., modValue: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class Archetype(_message.Message):
    __slots__ = ["guid", "attributes"]
    guid: UUID
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    def __init__(self, guid: _Optional[_Union[UUID, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...
