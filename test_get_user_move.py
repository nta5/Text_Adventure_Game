import io
from unittest import TestCase
from game import get_user_move as get_user_move
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=["N"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_short_form(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "North"
        self.assertEqual(actual_direction, expected)

    @patch('builtins.input', side_effect=["e"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_not_capitalized_short_form(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "East"
        self.assertEqual(actual_direction, expected)

    @patch('builtins.input', side_effect=["Quit"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_full_form(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "Quit"
        self.assertEqual(actual_direction, expected)

    @patch('builtins.input', side_effect=["west"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_not_capitalized_full_form(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "West"
        self.assertEqual(actual_direction, expected)

    @patch('builtins.input', side_effect=["NoRtH"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_mixed_format_form(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "North"
        self.assertEqual(actual_direction, expected)

    @patch('builtins.input', side_effect=["above", "3", "le", "e"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_choice_run_until_correct(self, mock_output, _):
        actual_direction = get_user_move()
        mock_output.getvalue()
        expected = "East"
        self.assertEqual(actual_direction, expected)
