import io
from unittest import TestCase
from game import heal as heal
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_normal_case(self, mock_output):
        test_character = {
            'HP': 342,
            'Max HP': 850,
            'Blessing': True
        }
        heal(test_character)
        mock_output.getvalue()
        expected = {
            'HP': 850,
            'Max HP': 850,
            'Blessing': True
        }
        self.assertEqual(expected, test_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_cannot_heal(self, mock_output):
        test_character = {
            'HP': 1350,
            'Max HP': 850,
            'Blessing': True
        }
        heal(test_character)
        mock_output.getvalue()
        expected = {
            'HP': 1350,
            'Max HP': 850,
            'Blessing': True
        }
        self.assertEqual(expected, test_character)
