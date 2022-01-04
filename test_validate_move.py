from unittest import TestCase
from game import validate_move as validate_move


class Test(TestCase):
    def test_validate_move_south_valid(self):
        test_board = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="South")
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_north_valid(self):
        test_board = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        actual = validate_move(test_board, test_character, move="North")
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_east_valid(self):
        test_board = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="East")
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_west_valid(self):
        test_board = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="West")
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_south_invalid(self):
        test_board = {(0, 0): 'Random', (1, 0): 'Random', (0, 1): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 1}
        actual = validate_move(test_board, test_character, move="South")
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_north_invalid(self):
        test_board = {(0, 0): 'Random', (1, 0): 'Random', (0, 1): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="North")
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_east_invalid(self):
        test_board = {(0, 0): 'Random', (1, 0): 'Random', (0, 1): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="East")
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_west_invalid(self):
        test_board = {(0, 0): 'Random', (1, 0): 'Random', (0, 1): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="West")
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_walk_into_wall(self):
        test_board = {(0, 0): 'Random', (1, 0): 'Random', (0, 1): 'Wall', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = validate_move(test_board, test_character, move="South")
        expected = False
        self.assertEqual(actual, expected)
