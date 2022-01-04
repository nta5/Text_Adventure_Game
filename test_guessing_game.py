import io
from unittest import TestCase
from game import guessing_game as guessing_game
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['L'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_is_not_boss(self, mock_output, _):
        guessing_game(False)
        actual = mock_output.getvalue()
        expected = "\t[L]eft\t[R]ight\t[N]ot guessing"

        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['L'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_is_boss(self, mock_output, _):
        guessing_game(True)
        actual = mock_output.getvalue()
        not_expected = "\t[L]eft\t[R]ight\t[N]ot guessing"
        expected = "\t[L]eft\t[R]ight"
        self.assertFalse(not_expected in actual)
        self.assertTrue(expected in actual)

    @patch('builtins.input', side_effect=['L'])
    @patch('random.choice', return_value='L')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_correct_guess(self, mock_output, __, _):
        actual = guessing_game(False)
        mock_output.getvalue()
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=['L'])
    @patch('random.choice', return_value='R')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_incorrect_guess(self, mock_output, __, _):
        actual = guessing_game(True)
        mock_output.getvalue()
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=['N'])
    @patch('random.choice', return_value='R')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_no_guess(self, mock_output, __, _):
        actual = guessing_game(False)
        mock_output.getvalue()
        self.assertTrue(actual is None)
