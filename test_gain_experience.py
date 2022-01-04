import io
from unittest import TestCase
from game import gain_experience as gain_experience
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=456)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_experience_increase_correctly(self, mock_output, __, _):
        test_character = {'Experience': 0}
        gain_experience(test_character)
        mock_output.getvalue()
        expected = {'Experience': 456}
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=456)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_experience_print(self, mock_output, __, _):
        test_character = {'Experience': 0}
        gain_experience(test_character)
        actual = mock_output.getvalue()
        expected = 'You receive 456 EXP.\n'
        self.assertEqual(expected, actual)

