import io
from unittest import TestCase
from game import calculate_attack_point as calculate_attack_point
from unittest.mock import patch


class Test(TestCase):
    def test_calculate_attack_point_None(self):
        test_character = {'Attack': 100}
        actual = calculate_attack_point(test_character, None)
        expected = 100
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_attack_point_True(self, mock_output):
        test_character = {'Attack': 90}
        actual = calculate_attack_point(test_character, True)
        mock_output.getvalue()
        expected = 108
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calculate_attack_point_False(self, mock_output):
        test_character = {'Attack': 120}
        actual = calculate_attack_point(test_character, False)
        mock_output.getvalue()
        expected = 96
        self.assertEqual(expected, actual)
