WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from typing import Any, Generic, TypeVar

from util.container import Container

T = TypeVar("T")


class Table(Container[T], Generic[T]):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key: Any | tuple[Any, ...], value: T) -> None:
        """
        Sets the table item, with its location denoted by a tuple key.

        Multiple dimensions are available by providing comma-separated values.
        """
        self._table[key] = value
