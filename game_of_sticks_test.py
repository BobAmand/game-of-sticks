# This will be the test code.
import unittest
from game_of_sticks import *


class Test_Game_of_Sticks(unittest.TestCase):

    def test_confirm_input(self):
        min = 1
        max = 3
        take = 1
        self.assertTrue(confirm_input(take, min, max))
        take = 4
        self.assertFalse(confirm_input(take, min, max))

    def test_starting_stick_parameters(self):
        low = 10
        high = 100
        start_stick = 99
        self.assertTrue(starting_stick_parameters(start_stick, low, high))
        start_stick = 4
        self.assertFalse(starting_stick_parameters(start_stick, low, high))
        start_stick = 500
        self.assertFalse(starting_stick_parameters(start_stick, low, high))

    def test_better_starting_stick_parameters(self):
        low = 10
        high = 100
        start_stick = 0
        self.assertTrue(better_starting_stick_parameters(start_stick,
                                                         low, high))


if __name__ == '__main__':
    unittest.main()
