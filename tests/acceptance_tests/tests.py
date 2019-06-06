import unittest
from scrabble import scrabble

class AcceptanceTests(unittest.TestCase):

    def create_scrabble(self, input):
        _scrabble = scrabble.Scrabble(input)
        return _scrabble.score

    def test_various_inputs_and_outputs(self):
        self.assertEqual(self.create_scrabble(''), 0)
        self.assertEqual(self.create_scrabble(' /t/n'), 0)
        self.assertEqual(self.create_scrabble(None), 0)
        self.assertEqual(self.create_scrabble('a'), 1)
        self.assertEqual(self.create_scrabble('f'), 4)
        self.assertEqual(self.create_scrabble('street'), 6)
        self.assertEqual(self.create_scrabble('quriky'), 22)
        self.assertEqual(self.create_scrabble('OXYPHENBUTAZONE'), 41)