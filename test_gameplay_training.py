import io
from unittest import TestCase
from game import gameplay_training as gameplay_training
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gameplay_training_no_wrong_input(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        gameplay_training(test_character)
        actual = mock_output.getvalue()
        expected = "Juliana smiles: 'Great job, Test! You nailed it.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['Y', 'w', 'e'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gameplay_training_wrong_answer(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        gameplay_training(test_character)
        actual = mock_output.getvalue()
        expected = "\nJuliana says: 'That is not correct, Test. Try again.'\n"
        self.assertIn(expected, actual)
