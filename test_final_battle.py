import io
import itertools
from unittest import TestCase
from game import final_battle as final_battle
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['r'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_battle_lose(self, mock_output, __, _):
        test_character = {
            'HP': 1,
            'Attack': 1,
            'Status': 'Alive'
        }
        final_battle(test_character)
        mock_output.getvalue()
        self.assertTrue(test_character['Status'] == 'Dead')

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=itertools.cycle(['L', 'R']))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_battle_win(self, mock_output, __, _):
        test_character = {
            'HP': 1200,
            'Attack': 200,
            'Status': 'Alive'
        }
        final_battle(test_character)
        mock_output.getvalue()
        self.assertTrue(test_character['Status'] == 'Win')
