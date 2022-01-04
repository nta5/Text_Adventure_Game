import io
from unittest import TestCase
from game import class_decision as class_decision
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['N', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_decision_warrior(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        class_decision(test_character)
        mock_output.getvalue()
        expected = {'Name': 'Test', 'Class': 'Warrior'}
        self.assertEqual(test_character, expected)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['N', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_decision_knight(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        class_decision(test_character)
        mock_output.getvalue()
        expected = {'Name': 'Test', 'Class': 'Knight'}
        self.assertEqual(test_character, expected)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['N', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_decision_magician(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        class_decision(test_character)
        mock_output.getvalue()
        expected = {'Name': 'Test', 'Class': 'Magician'}
        self.assertEqual(test_character, expected)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['N', '4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_decision_archer(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        class_decision(test_character)
        mock_output.getvalue()
        expected = {'Name': 'Test', 'Class': 'Archer'}
        self.assertEqual(test_character, expected)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['N', 'War', 'sdadf', '5', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_decision_ignore_wrong_input(self, mock_output, __, _):
        test_character = {'Name': 'Test'}
        class_decision(test_character)
        mock_output.getvalue()
        expected = {'Name': 'Test', 'Class': 'Knight'}
        self.assertEqual(test_character, expected)
