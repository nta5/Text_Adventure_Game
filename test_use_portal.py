import io
from unittest import TestCase
from game import use_portal as use_portal
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_portal_to_forest(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 17,
            'Y-coordinate': 10,
            'Compass': True
        }
        use_portal(test_character)
        mock_output.getvalue()
        expected = {
            'X-coordinate': 12,
            'Y-coordinate': 5,
            'Compass': True
        }
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_portal_to_wasteland(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 12,
            'Y-coordinate': 4,
            'Compass': True
        }
        use_portal(test_character)
        mock_output.getvalue()
        expected = {
            'X-coordinate': 17,
            'Y-coordinate': 10,
            'Compass': True
        }
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_portal_not_using_portal(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 17,
            'Y-coordinate': 10,
            'Compass': True
        }
        use_portal(test_character)
        mock_output.getvalue()
        expected = {
            'X-coordinate': 17,
            'Y-coordinate': 10,
            'Compass': True
        }
        self.assertEqual(expected, test_character)
