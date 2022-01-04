import io
from unittest import TestCase
from game import mission_guidance as mission_guidance
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_guidance_receive_compass(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'HP': 352,
            'Max HP': 500,
            'X-coordinate': 12,
            'Y-coordinate': 4
        }
        mission_guidance(test_character)
        mock_output.getvalue()
        self.assertTrue('Compass' in test_character.keys())

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_guidance_hp_restored(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'HP': 352,
            'Max HP': 500,
            'X-coordinate': 12,
            'Y-coordinate': 4
        }
        mission_guidance(test_character)
        mock_output.getvalue()
        expected = test_character['Max HP']
        self.assertEqual(expected, test_character['HP'])

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_guidance_change_location(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'HP': 352,
            'Max HP': 500,
            'X-coordinate': 12,
            'Y-coordinate': 4
        }
        mission_guidance(test_character)
        mock_output.getvalue()
        actual_location = (test_character['X-coordinate'], test_character['Y-coordinate'])
        expected_location = (17, 10)
        self.assertEqual(expected_location, actual_location)
