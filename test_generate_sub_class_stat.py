from unittest import TestCase
from game import generate_sub_class_stat as sub_class_stat


class Test(TestCase):
    def test_generate_sub_class_stat_boost_attack(self):
        test_character = {
            'Name': 'Test',
            'Class': 'Archer',
            'HP': 450,
            'Attack': 90
        }
        sub_class_stat(test_character, '1')
        expected_attack = 110
        self.assertEqual(expected_attack, test_character['Attack'])

    def test_generate_sub_class_stat_boost_HP(self):
        test_character = {
            'Name': 'Test',
            'Class': 'Archer',
            'HP': 450,
            'Attack': 90
        }
        sub_class_stat(test_character, '2')
        expected_hp = 500
        self.assertEqual(expected_hp, test_character['HP'])

    def test_generate_sub_class_stat_boost_both_HP_and_Attack(self):
        test_character = {
            'Name': 'Test',
            'Class': 'Archer',
            'HP': 450,
            'Attack': 90
        }
        sub_class_stat(test_character, '3')
        expected_hp = 475
        expected_attack = 100
        self.assertEqual(expected_hp, test_character['HP'])
        self.assertEqual(expected_attack, test_character['Attack'])

    def test_generate_sub_class_stat_normal(self):
        test_character = {
            'Name': 'Test',
            'Class': 'Archer',
            'HP': 450,
            'Attack': 90
        }
        sub_class_stat(test_character, '4')
        expected_hp = 465
        expected_attack = 95
        self.assertEqual(expected_hp, test_character['HP'])
        self.assertEqual(expected_attack, test_character['Attack'])
