import io
from unittest import TestCase
from game import ending_scene as ending_scene
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ending_scene_winning(self, mock_output, _):
        test_character = {
            'Status': 'Win'
        }
        ending_scene(test_character)
        actual = mock_output.getvalue()
        expected = "Congratulations! You won!\nThe Dark Force withers away. You had saved Yggdra."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ending_scene_losing(self, mock_output, _):
        test_character = {
            'Status': 'Dead'
        }
        ending_scene(test_character)
        actual = mock_output.getvalue()
        expected = "Your HP falls below 0. You died."
        self.assertIn(expected, actual)
