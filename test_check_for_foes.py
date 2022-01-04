from unittest import TestCase
from game import check_for_foes as check_for_foes
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', return_value=3)
    def test_check_for_foes_true(self, _):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = check_for_foes(test_character)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_check_for_foes_no_check_in_boss_location(self, _):
        test_character = {'X-coordinate': 22, 'Y-coordinate': 22}
        actual = check_for_foes(test_character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_false_scenario_1(self, _):
        test_character = {'X-coordinate': 10, 'Y-coordinate': 0}
        actual = check_for_foes(test_character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_false_scenario_2(self, _):
        test_character = {'X-coordinate': 4, 'Y-coordinate': 5}
        actual = check_for_foes(test_character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_check_for_foes_false_scenario_3(self, _):
        test_character = {'X-coordinate': 6, 'Y-coordinate': 5}
        actual = check_for_foes(test_character)
        expected = False
        self.assertEqual(actual, expected)
