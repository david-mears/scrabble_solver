import unittest
from scrabble import scrabble

class ScrabbleTests(unittest.TestCase):

    def test_can_take_input(self):
        _scrabble = scrabble.Scrabble('input')
        self.assertTrue(_scrabble)

    def test_can_return_score_attr(self):
        _scrabble = scrabble.Scrabble('input')
        self.assertTrue(isinstance(_scrabble.score, int))

    def test_can_sum_letters_from_multielement_string(self):
        _scrabble = scrabble.Scrabble('aaa')
        self.assertEqual(_scrabble.calculate_score(), 3)
        _scrabble = scrabble.Scrabble('zzz')
        self.assertEqual(_scrabble.calculate_score(), 30)
