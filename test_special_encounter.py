import io
from unittest import TestCase
from game import special_encounter as special_encounter
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_encounter_first_time(self, mock_output, _):
        test_character = {
            'Name': 'Test',
            'HP': 300,
            'Max HP': 800,
            'Attack': 200
        }
        special_encounter(test_character)
        mock_output.getvalue()

        expected = {
            'Name': 'Test',
            'HP': 1100,
            'Max HP': 800,
            'Attack': 220,
            'Blessing': True
        }
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_encounter_returning_user(self, mock_output, _):
        test_character = {
            'Name': 'Test',
            'HP': 300,
            'Max HP': 800,
            'Attack': 200,
            'Blessing': True
        }
        special_encounter(test_character)

        actual_printing = mock_output.getvalue()
        expected_printing = "Phoena says: 'For the peace and happiness of Yggdra.'"
        expected_hp = test_character['Max HP']

        self.assertIn(expected_printing, actual_printing)
        self.assertEqual(expected_hp, test_character['HP'])
