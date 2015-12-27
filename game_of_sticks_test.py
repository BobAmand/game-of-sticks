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
        self.assertTrue(better_starting_stick_parameters(start_stick, low, high))


#
#
#
#     def test_easy_words(self):
#         self.assertEqual(easy_words(word_list), ["bird", "calf", "river", "stream", "brain"])
#
#
#     def test_medium_words(self):
#         self.assertEqual(medium_words(word_list), ["stream", "kneecap", "cookbook", "language", "sneaker"])
#
#
#     def test_hard_words(self):
#         self.assertEqual(hard_words(word_list), ["cookbook", "language", "algorithm", "integration"])
#
#
#     def test_random_word(self):
#         """This test is not very good. Testing things that are random is hard,
#         in that there's not a predictable choice. The best we can do is make
#         sure we have valid output."""
#         word = random_word(word_list)
#         self.assertTrue(word in word_list)
#
#
#     def test_display_word(self):
#         word = "integration"
#         self.assertEqual(display_word(word, []), "_ _ _ _ _ _ _ _ _ _ _")
#         self.assertEqual(display_word(word, ["z"]), "_ _ _ _ _ _ _ _ _ _ _")
#         self.assertEqual(display_word(word, ["g"]), "_ _ _ _ G _ _ _ _ _ _")
#         self.assertEqual(display_word(word, ["i"]), "I _ _ _ _ _ _ _ I _ _")
#         self.assertEqual(display_word(word, ["i", "g"]), "I _ _ _ G _ _ _ I _ _")
#         self.assertEqual(display_word(word, ["i", "n", "z"]), "I N _ _ _ _ _ _ I _ N")
#
#
#     def test_is_word_complete(self):
#         word = "river"
#         self.assertFalse(is_word_complete(word, []))
#         self.assertFalse(is_word_complete(word, ["r"]))
#         self.assertFalse(is_word_complete(word, ["r", "e"]))
#         self.assertFalse(is_word_complete(word, ["r", "e", "z"]))
#         self.assertTrue(is_word_complete(word, ["r", "e", "v", "i"]))

if __name__ == '__main__':
    unittest.main()
