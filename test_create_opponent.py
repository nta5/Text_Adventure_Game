from unittest import TestCase
from game import create_opponent as create_opponent
from unittest.mock import patch


class Test(TestCase):
    @patch('random.choice', side_effect=['Helios', 'Ogre'])
    @patch('random.randint', side_effect=[256, 35])
    def test_create_opponent_check_opponent_profile(self, __, _):
        test_character = {
            'X-coordinate': 3,
            'Y-coordinate': 3,
            'Max HP': 400,
            'Attack': 100
        }
        actual = create_opponent(test_character)
        expected = {
            'Name': 'Helios the Ogre',
            'HP': 256,
            'Attack': 35
        }
        self.assertEqual(expected, actual)

    def test_create_opponent_check_opponent_HP(self):
        test_character = {
            'X-coordinate': 3,
            'Y-coordinate': 3,
            'Max HP': 400,
            'Attack': 100
        }
        test_opponent = create_opponent(test_character)
        opponent_hp_upper_bound = test_character['Attack'] * 3
        opponent_hp_lower_bound = test_character['Attack']
        self.assertTrue(test_opponent['HP'] <= opponent_hp_upper_bound)
        self.assertTrue(test_opponent['HP'] >= opponent_hp_lower_bound)

    def test_create_opponent_check_opponent_Attack(self):
        test_character = {
            'X-coordinate': 3,
            'Y-coordinate': 3,
            'Max HP': 400,
            'Attack': 100
        }
        test_opponent = create_opponent(test_character)
        opponent_hp_upper_bound = test_character['Max HP'] // 15
        opponent_hp_lower_bound = test_character['Max HP'] // 20
        self.assertTrue(test_opponent['Attack'] <= opponent_hp_upper_bound)
        self.assertTrue(test_opponent['Attack'] >= opponent_hp_lower_bound)

    def test_create_opponent_check_opponent_name_forest_location(self):
        test_character = {
            'X-coordinate': 3,
            'Y-coordinate': 3,
            'Max HP': 400,
            'Attack': 100
        }
        test_opponent = create_opponent(test_character)
        name_components = test_opponent['Name'].split()

        opponent_classes = ["Elf", "Ogre", "Sniper", "Assassin", "Thief", "Commander", "Pirate"]
        opponent_names = ["Vienta", "Eshal", "Amatsu", "Helios", "Yuni", "Chidori", "Einslotte", "Arietta"]

        self.assertTrue(name_components[0] in opponent_names)
        self.assertTrue(name_components[2] in opponent_classes)

    def test_create_opponent_check_opponent_name_wasteland_location(self):
        test_character = {
            'X-coordinate': 11,
            'Y-coordinate': 11,
            'Max HP': 400,
            'Attack': 100
        }
        test_opponent = create_opponent(test_character)
        name_components = test_opponent['Name'].split()

        opponent_classes = ["Elf", "Ogre", "Sniper", "Assassin", "Thief", "Commander", "Pirate", 'Dragon', 'Demon',
                            'Archdemon', 'Demon of Destruction', 'Demon of Desecration', 'Killer', 'Prisoner',
                            'Misbeliever']
        opponent_names = ["Vienta", "Eshal", "Amatsu", "Helios", "Yuni", "Chidori", "Einslotte", "Arietta",
                          'Eirneus', 'Razanil', 'Sellen', 'Kataris', "Barcus", "Labezerin", "Suphlatus"]

        self.assertTrue(name_components[0] in opponent_names)
        self.assertTrue(name_components[2] in opponent_classes)
