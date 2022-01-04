import io
from unittest import TestCase
from game import execute_game_scenario as execute_game_scenario
from unittest.mock import patch
import itertools


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_class_training(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Magician',
            'HP': 300,
            'Attack': 120
        }
        execute_game_scenario(test_character, 'Class Training')
        actual = mock_output.getvalue()
        expected = "Louise says: 'Hi there. You must be Test."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_battle_training(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Magician',
            'HP': 300,
            'Attack': 120
        }
        execute_game_scenario(test_character, 'Battle Training')
        actual = mock_output.getvalue()
        expected = "Kain smiles: 'Welcome, Test. Great to see you.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_start_mission(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Experience': 0,
        }
        execute_game_scenario(test_character, 'Gate')
        actual = mock_output.getvalue()
        expected = "Juliana says: 'And we meet again, Test. I hope you are ready."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_use_portal(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'X-coordinate': 17,
            'Y-coordinate': 10,
            'Compass': True
        }
        execute_game_scenario(test_character, 'Portal')
        mock_output.getvalue()
        expected = {
            'Name': 'Test',
            'X-coordinate': 12,
            'Y-coordinate': 5,
            'Compass': True
        }
        self.assertEqual(expected, test_character)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_heal(self, mock_output, _):
        test_character = {
            'Name': 'Test',
            'HP': 342,
            'Max HP': 850,
            'Experience': 0,
        }
        execute_game_scenario(test_character, 'Heal')
        actual = mock_output.getvalue()
        expected = 'You are fully healed.'
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_special_encounter(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'HP': 342,
            'Attack': 220,
            'Max HP': 850,
            'Experience': 0,
        }
        execute_game_scenario(test_character, 'Blessing')
        actual = mock_output.getvalue()
        expected = "Phoena says: 'Test! I know you will come.\n"
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=itertools.cycle(['L', 'R']))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_game_scenario_final_battle(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'HP': 1200,
            'Attack': 200,
            'Status': 'Alive'
        }
        execute_game_scenario(test_character, 'Boss')
        actual = mock_output.getvalue()
        expected = "You meet the Dark King. You get your weapons ready."
        self.assertIn(expected, actual)
