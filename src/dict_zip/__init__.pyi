from __future__ import annotations

from collections.abc import Iterator
from typing import Any, TypeVar, overload

__version__: tuple[int, int, int]

_T_co = TypeVar("_T_co", covariant=True)
_K = TypeVar("_K")
_V1 = TypeVar("_V1")
_V2 = TypeVar("_V2")
_V3 = TypeVar("_V3")
_V4 = TypeVar("_V4")
_V5 = TypeVar("_V5")
_V6 = TypeVar("_V6")

class dict_zip(Iterator[_T_co]):
    @overload
    def __new__(cls) -> dict_zip[Any]: ...
    @overload
    def __new__(cls, dict1: dict[_K, _V1]) -> dict_zip[tuple[_K, _V1]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, _V1],
        dict2: dict[_K, _V2],
    ) -> dict_zip[tuple[_K, _V1, _V2]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, _V1],
        dict2: dict[_K, _V2],
        dict3: dict[_K, _V3],
    ) -> dict_zip[tuple[_K, _V1, _V2, _V3]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, _V1],
        dict2: dict[_K, _V2],
        dict3: dict[_K, _V3],
        dict4: dict[_K, _V4],
    ) -> dict_zip[tuple[_K, _V1, _V2, _V3, _V4]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, _V1],
        dict2: dict[_K, _V2],
        dict3: dict[_K, _V3],
        dict4: dict[_K, _V4],
        dict5: dict[_K, _V5],
    ) -> dict_zip[tuple[_K, _V1, _V2, _V3, _V4, _V5]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, _V1],
        dict2: dict[_K, _V2],
        dict3: dict[_K, _V3],
        dict4: dict[_K, _V4],
        dict5: dict[_K, _V5],
        dict6: dict[_K, _V6],
    ) -> dict_zip[tuple[_K, _V1, _V2, _V3, _V4, _V5, _V6]]: ...
    @overload
    def __new__(
        cls,
        dict1: dict[_K, Any],
        dict2: dict[_K, Any],
        dict3: dict[_K, Any],
        dict4: dict[_K, Any],
        dict5: dict[_K, Any],
        dict6: dict[_K, Any],
        /,
        *dicts: dict[_K, Any],
    ) -> dict_zip[tuple[Any, ...]]: ...
    def __next__(self) -> _T_co: ...
