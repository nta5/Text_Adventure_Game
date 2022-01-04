import io
from unittest import TestCase
from game import start_mission as start_mission
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_mission_receive_reward(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Experience': 0,
        }
        start_mission(test_character)
        mock_output.getvalue()
        expected = {
            'Name': 'Test',
            'Experience': 500,
        }
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_mission_prevent_return_user(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Experience': 500,
        }
        start_mission(test_character)
        actual = mock_output.getvalue()
        expected = ''
        self.assertEqual(expected, actual)
