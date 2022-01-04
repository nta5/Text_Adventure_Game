from unittest import TestCase
from game import check_character_level as check_character_level


class Test(TestCase):
    def test_check_character_level_no_level_up(self):
        test_character = {'Level': 1, 'Experience': 999, 'Attack': 120, 'HP': 300, 'Max HP': 320}
        check_character_level(test_character)
        result = check_character_level(test_character)
        self.assertFalse(result)

    def test_check_character_level_experience_equal_to_required(self):
        test_character = {'Level': 1, 'Experience': 1000, 'Attack': 120, 'HP': 300, 'Max HP': 320}
        check_character_level(test_character)
        result = check_character_level(test_character)
        self.assertTrue(result)

    def test_check_character_level_experience_higher_than_required(self):
        test_character = {'Level': 1, 'Experience': 1034, 'Attack': 120, 'HP': 300, 'Max HP': 320}
        check_character_level(test_character)
        result = check_character_level(test_character)
        self.assertTrue(result)
