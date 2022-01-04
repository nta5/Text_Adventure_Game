import io
from unittest import TestCase
from game import update_character_level as update_character_level
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_character_level_level_up_notification(self, mock_output, _):
        test_character = {'Level': 1, 'Experience': 1030, 'Attack': 120, 'HP': 300, 'Max HP': 320}
        update_character_level(test_character)
        actual = mock_output.getvalue()
        expected = "You reached level 2! You became stronger."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_character_level_level_2_stat_change(self, mock_output, _):
        test_character = {'Level': 1, 'Experience': 1030, 'Attack': 120, 'HP': 300, 'Max HP': 320}
        update_character_level(test_character)
        mock_output.getvalue()
        expected = {'Attack': 180, 'Experience': 1030, 'HP': 460, 'Level': 2, 'Max HP': 480}
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_character_level_level_3_stat_change(self, mock_output, _):
        test_character = {'Level': 2, 'Experience': 2152, 'Attack': 180, 'HP': 460, 'Max HP': 480}
        update_character_level(test_character)
        mock_output.getvalue()
        expected = {'Attack': 270, 'Experience': 2152, 'HP': 700, 'Level': 3, 'Max HP': 720}
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_character_level_level_4_stat_change(self, mock_output, _):
        test_character = {'Level': 3, 'Experience': 3752, 'Attack': 270, 'HP': 675, 'Max HP': 720}
        update_character_level(test_character)
        mock_output.getvalue()
        expected = {'Attack': 405, 'Experience': 3752, 'HP': 1035, 'Level': 4, 'Max HP': 1080}
        self.assertEqual(expected, test_character)
