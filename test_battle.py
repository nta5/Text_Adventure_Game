import io
import itertools
from unittest import TestCase
from game import battle as battle
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['r'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_lose(self, mock_output, __, _):
        test_character = {
            'HP': 1,
            'Attack': 1,
            'Status': 'Alive'
        }
        test_opponent = {
            'Name': 'Helios the Ogre',
            'HP': 256,
            'Attack': 35
        }
        battle(test_character, test_opponent)
        mock_output.getvalue()
        self.assertTrue(test_character['Status'] == 'Dead')

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=itertools.cycle(['L', 'N', 'R']))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_battle_win(self, mock_output, __, _):
        test_character = {
            'HP': 600,
            'Attack': 144,
            'Status': 'Alive'
        }
        test_opponent = {
            'Name': 'Helios the Ogre',
            'HP': 504,
            'Attack': 50
        }
        battle(test_character, test_opponent)
        actual = mock_output.getvalue()
        expected = "You won!"
        self.assertIn(expected, actual)
