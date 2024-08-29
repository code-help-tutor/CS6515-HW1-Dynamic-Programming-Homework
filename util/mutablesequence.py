WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from __future__ import annotations

import copy
from decimal import Decimal
from typing import Generic, TypeVar

from util.sequence import Sequence

T = TypeVar("T", bool, Decimal, float, int, str)


class MutableSequence(Sequence[T], Generic[T]):
    def __init__(self, items: list[T] = []):
        super().__init__(items)

        self.__next = len(items) + 1

    def __eq__(self, other: MutableSequence[T]) -> bool:
        """
        Return whether two sequences are the same.
        """
        if len(self) != len(other):
            return False

        for i in range(1, len(self) + 1):
            if self[i] != other[i]:
                return False

        return True

    def __setitem__(self, key: int, value: T) -> None:
        """
        Sets the sequence item, with its index denoted by its key.

        Trying to set the value at an unallocated index is an error.
        """
        if not (1 <= key <= len(self)):
            raise IndexError(f"{key} out of bounds from [1, {len(self)}]")

        self._table[key] = copy.deepcopy(value)

    def append(self, item: T) -> None:
        """
        Adds one item to the end of the sequence.
        """
        self._table[self.__next] = copy.deepcopy(item)

        self.__next += 1
