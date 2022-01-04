import io
from unittest import TestCase
from game import generate_game_board as generate_game_board
from game import print_map as print_map
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_starting_point(self, mock_output):
        test_board = generate_game_board()
        test_character = {
            'X-coordinate': 5,
            'Y-coordinate': 23,
        }

        print_map(test_board, test_character)

        actual = mock_output.getvalue()
        expected = " .\t .\t .\t .\t .\t .\t .\t\n" \
                   " .\t .\t .\t .\t .\t .\t .\t\n" \
                   " .\t .\t .\t[#]\t .\t .\t .\t\n" \
                   " .\t .\t .\t .\t .\t .\t .\t\n"

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_class_training(self, mock_output):
        test_board = generate_game_board()
        test_character = {
            'X-coordinate': 5,
            'Y-coordinate': 19,
        }

        print_map(test_board, test_character)

        actual = mock_output.getvalue()

        expected = " .\t .\t .\t CT\t .\t .\t .\t\n"

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_battle_training(self, mock_output):
        test_board = generate_game_board()
        test_character = {
            'X-coordinate': 5,
            'Y-coordinate': 14,
        }

        print_map(test_board, test_character)

        actual = mock_output.getvalue()

        expected = " .\t .\t .\t BT\t .\t .\t .\t\n"

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_gate(self, mock_output):
        test_board = generate_game_board()
        test_character = {
            'X-coordinate': 3,
            'Y-coordinate': 11,
        }

        print_map(test_board, test_character)

        actual = mock_output.getvalue()

        expected = ' /\t /\t /\t'

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_boss(self, mock_output):
        test_board = generate_game_board()
        test_character = {
            'X-coordinate': 21,
            'Y-coordinate': 21,
        }

        print_map(test_board, test_character)

        actual = mock_output.getvalue()

        expected = " .\t .\t .\t .\t???\t .\t .\t\n"

        self.assertIn(expected, actual)
