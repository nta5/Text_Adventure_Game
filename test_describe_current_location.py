import io
from unittest import TestCase
from game import describe_current_location as describe_location
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_starting_point(self, mock_output):
        test_board = {(0, 0): "You are outside of the Castle.", (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}

        describe_location(test_board, test_character)
        actual = mock_output.getvalue()
        expected = "Coordinate (0, 0). You are outside of the Castle."

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_edge_point(self, mock_output):
        test_board = {(0, 0): 'Random', (0, 1): 'Random',
                      (0, 2): 'Random', (0, 3): "You step inside the Castle. It's huge.",
                      (1, 0): 'Random', (1, 1): 'Random',
                      (1, 2): 'Random', (1, 3): 'Random'}
        test_character = {'X-coordinate': 0, 'Y-coordinate': 3}

        describe_location(test_board, test_character)
        actual = mock_output.getvalue()
        expected = "Coordinate (0, 3). You step inside the Castle. It's huge."

        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_middle_point(self, mock_output):
        test_board = {(0, 0): 'Random', (0, 1): 'Random',
                      (1, 0): 'You feel like someone is observing you.', (1, 1): 'Random',
                      (2, 0): 'Random', (2, 1): 'Random'}
        test_character = {'X-coordinate': 1, 'Y-coordinate': 0}

        describe_location(test_board, test_character)
        actual = mock_output.getvalue()
        expected = "Coordinate (1, 0). You feel like someone is observing you."

        self.assertIn(expected, actual)
        