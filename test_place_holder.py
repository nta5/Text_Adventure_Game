import io
from unittest import TestCase
from game import place_holder as place_holder
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_place_holder_no_capital_y(self, mock_output, _):
        place_holder()
        actual = mock_output.getvalue()
        expected = ''

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_place_holder_capital_y(self, mock_output, _):
        place_holder()
        actual = mock_output.getvalue()
        expected = ''

        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['n', 'N', 'Y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_place_holder_capital_and_no_capital_n(self, mock_output, __, _):
        place_holder()
        actual = mock_output.getvalue()
        expected = "Are you ready now?\n" \
                   "Are you ready now?"

        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['232321', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_place_holder_junk_input(self, mock_output, __, _):
        place_holder()
        actual = mock_output.getvalue()
        expected = "Are you ready now?"

        self.assertIn(expected, actual)
