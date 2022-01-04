from unittest import TestCase
from game import generate_class_stat


class Test(TestCase):
    def test_generate_class_stat_warrior(self):
        test_character = {'Class': 'Warrior'}
        generate_class_stat(test_character)
        expected = {'Attack': 100, 'Class': 'Warrior', 'HP': 400}
        self.assertEqual(expected, test_character)

    def test_generate_class_stat_knight(self):
        test_character = {'Class': 'Knight'}
        generate_class_stat(test_character)
        expected = {'Attack': 80, 'HP': 500, 'Class': 'Knight'}
        self.assertEqual(expected, test_character)

    def test_generate_class_stat_magician(self):
        test_character = {'Class': 'Magician'}
        generate_class_stat(test_character)
        expected = {'Attack': 120, 'HP': 300, 'Class': 'Magician'}
        self.assertEqual(expected, test_character)

    def test_generate_class_stat_archer(self):
        test_character = {'Class': 'Archer'}
        generate_class_stat(test_character)
        expected = { 'Class': 'Archer', 'Attack': 90, 'HP': 450}
        self.assertEqual(expected, test_character)
