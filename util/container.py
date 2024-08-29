WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Container(Generic[T]):
    def __init__(self):
        self._table = {}

    def __getitem__(self, key: Any | tuple[Any, ...]) -> T:
        """
        Return the container item, with its location denoted by a tuple key.

        Multiple dimensions are available by providing comma-separated values.
        """
        return self._table[key]

    def __str__(self) -> str:
        """
        Return a string of the locations and items in the container.
        """
        return str(self._table)

    def all(self) -> bool:
        """
        Return True if bool(x) is True for all values x in the container.

        If the container is empty, return True.
        """
        for key in self._table.keys():
            if not self[key]:
                return False

        return True

    def any(self) -> bool:
        """
        Return True if bool(x) is True for any x in the container.

        If the container is empty, return False.
        """
        for key in self._table.keys():
            if self[key]:
                return True

        return False

    def max(self):
        """
        Return the largest item in the container.

        If the container is empty, raise an exception.
        """
        result = self[[*self._table][0]]

        for key in [*self._table][1:]:
            if self[key] > result:
                result = self[key]

        return result

    def min(self):
        """
        Return the smallest item in the container.

        If the container is empty, raise an exception.
        """
        result = self[[*self._table][0]]

        for key in [*self._table][1:]:
            if self[key] < result:
                result = self[key]

        return result

    def sum(self):
        """
        Return the sum of all values in the container.

        When the container is empty, return 0.

        This function is intended specifically for use with
        numeric values and may reject non-numeric types.
        """
        result = 0

        for key in self._table.keys():
            result += self[key]

        return result
