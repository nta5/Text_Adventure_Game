from unittest import TestCase
from game import move_character as move_character


class Test(TestCase):
    def test_move_character_south(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        move_character(test_character, 'South')
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(expected, test_character)

    def test_move_character_north(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        move_character(test_character, 'North')
        expected = {'X-coordinate': 0, 'Y-coordinate': 0}
        self.assertEqual(expected, test_character)

    def test_move_character_east(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        move_character(test_character, 'East')
        expected = {'X-coordinate': 1, 'Y-coordinate': 1}
        self.assertEqual(expected, test_character)

    def test_move_character_west(self):
        test_character = {'X-coordinate': 1, 'Y-coordinate': 1}
        move_character(test_character, 'West')
        expected = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(expected, test_character)
