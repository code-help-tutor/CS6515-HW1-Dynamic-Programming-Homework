WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import unittest

from cs6515_cursed_chests import CursedChests

from util.mutablesequence import MutableSequence
from util.sequence import Sequence


class TestCursedChests(unittest.TestCase):
    def test_base_case_1(self):
        gold, chests = CursedChests(Sequence([1, 0, 2]))

        self.assertEqual(gold, 2)
        self.assertEqual(chests, MutableSequence([3]))

    def test_base_case_2(self):
        gold, chests = CursedChests(Sequence([2, 0, 1]))

        self.assertEqual(gold, 2)
        self.assertEqual(chests, MutableSequence([1]))


if __name__ == "__main__":
    unittest.main()
