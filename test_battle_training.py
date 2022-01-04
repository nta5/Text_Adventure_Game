import io
from unittest import TestCase
from game import battle_training as battle_training
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_training_start(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        battle_training(test_character)
        actual = mock_output.getvalue()
        expected = "Kain smiles: 'Welcome, Test. Great to see you.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_training_middle(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        battle_training(test_character)
        actual = mock_output.getvalue()
        expected = "\nKain says: 'The battle system is very simple.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_training_end(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        battle_training(test_character)
        actual = mock_output.getvalue()
        expected = "Kain smiles: 'Test, do your best. That's it from me today.\n"
        self.assertIn(expected, actual)
