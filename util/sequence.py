WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from __future__ import annotations

import copy
from decimal import Decimal
from typing import Generic, TypeVar

from util.container import Container

T = TypeVar("T", bool, Decimal, float, int, str)


class Sequence(Container[T], Generic[T]):
    def __init__(self, items: list[T]):
        super().__init__()

        for index, item in enumerate(items):
            self._table[index + 1] = copy.deepcopy(item)

    def __len__(self) -> int:
        """
        Returns the number of items in the sequence.
        """
        return len(self._table.keys())

    def copy(self) -> Sequence[T]:
        """
        Returns a copy of all items in the sequence as a new Sequence.
        """
        values = []

        for key in self._table.keys():
            values.append(copy.deepcopy(self[key]))

        return Sequence(values)

    def reverse(self) -> None:
        """
        Reverses the order of items in the sequence in place.
        """
        temp = {}

        for index, key in enumerate(reversed(self._table.keys())):
            temp[index + 1] = self[key]

        self._table = temp
