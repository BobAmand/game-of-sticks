import unittest
from sticks import *


class TestSticks(unittest.TestCase):
    def test_is_game_over(self):
        self.assertTrue(is_game_over(-5))
        self.assertTrue(is_game_over(-1))
        self.assertTrue(is_game_over(0))
        self.assertFalse(is_game_over(1))
        self.assertFalse(is_game_over(2))
        self.assertFalse(is_game_over(3))
        self.assertFalse(is_game_over(50))


if __name__ == '__main__':
    unittest.main()
