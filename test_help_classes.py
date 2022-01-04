import io
from unittest import TestCase
from game import help_classes as help_classes
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['1', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_classes_warrior(self, mock_output, __, _):
        help_classes()
        actual = mock_output.getvalue()
        expected = "WARRIORS\nWith their trust-worthy swords, or just fists, they fight with all their might.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['2', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_classes_knight(self, mock_output, __, _):
        help_classes()
        actual = mock_output.getvalue()
        expected = 'KNIGHTS\nThe skilled combatants who fight in the name of honour and chivalry.\n'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['3', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_classes_magician(self, mock_output, __, _):
        help_classes()
        actual = mock_output.getvalue()
        expected = 'MAGICIANS\nThey are loved by the nature.\n'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['4', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_classes_archer(self, mock_output, __, _):
        help_classes()
        actual = mock_output.getvalue()
        expected = 'ARCHERS\nThey are the favourite child of air.\n'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['4', 'Y', '3', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_classes_multiple_classes(self, mock_output, __, _):
        help_classes()
        actual = mock_output.getvalue()
        first_expected_prints = 'ARCHERS\nThey are the favourite child of air.\n'
        second_expected_prints = 'MAGICIANS\nThey are loved by the nature.\n'
        self.assertTrue(first_expected_prints in actual and second_expected_prints in actual)
