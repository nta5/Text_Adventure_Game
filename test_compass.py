import io
from unittest import TestCase
from game import compass as compass
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_compass_not_being_activated(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 17,
            'Y-coordinate': 10,
        }
        compass(test_character)
        actual = mock_output.getvalue()
        expected = ''
        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_compass_boss_is_to_the_upper_left_of_character(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 24,
            'Y-coordinate': 24,
            'Compass': True
        }
        compass(test_character)
        actual = mock_output.getvalue()
        expected = '2N 2W'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_compass_boss_is_to_the_upper_right_of_character(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 19,
            'Y-coordinate': 23,
            'Compass': True
        }
        compass(test_character)
        actual = mock_output.getvalue()
        expected = '1N 3E'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_compass_boss_is_to_the_lower_left_of_character(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 24,
            'Y-coordinate': 19,
            'Compass': True
        }
        compass(test_character)
        actual = mock_output.getvalue()
        expected = '3S 2W'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_compass_boss_is_to_the_lower_right_of_character(self, mock_output, __, _):
        test_character = {
            'X-coordinate': 16,
            'Y-coordinate': 19,
            'Compass': True
        }
        compass(test_character)
        actual = mock_output.getvalue()
        expected = '3S 6E'
        self.assertIn(expected, actual)
