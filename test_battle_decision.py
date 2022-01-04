import io
from unittest import TestCase
from game import battle_decision as battle_decision
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_decision_decide_to_battle(self, mock_output, _):
        test_character = {'HP': 1}
        actual = battle_decision(test_character)
        mock_output.getvalue()
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=['Y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_decision_decide_to_flee(self, mock_output, _):
        test_character = {'HP': 1}
        actual = battle_decision(test_character)
        mock_output.getvalue()
        self.assertFalse(actual)

    @patch('builtins.input', side_effect=['Y'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_decision_decide_to_flee_no_damage_taken(self, mock_output, __, _):
        test_character = {'HP': 1}
        actual = battle_decision(test_character)
        mock_output.getvalue()
        self.assertFalse(actual)
        self.assertTrue(test_character['HP'] == 1)

    @patch('builtins.input', side_effect=['Y'])
    @patch('random.randint', side_effect=[3, 45])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_decision_decide_to_flee_damage_taken(self, mock_output, __, _):
        test_character = {'HP': 100}
        battle_decision(test_character)
        actual = mock_output.getvalue()
        expected = "You lose 45 HP."
        self.assertIn(expected, actual)

