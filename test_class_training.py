import io
from unittest import TestCase
from game import class_training as class_training
from unittest.mock import patch


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_training_warrior_sub_class_list(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Warrior',
            'HP': 400,
            'Attack': 100
        }
        class_training(test_character)
        actual = mock_output.getvalue()
        expected = "1 - Berserker:\n" \
                   "\tBold and direct. Berserkers are stronger in attack compared to other Warrior sub-classes.\n" \
                   "2 - Fencer:\n" \
                   "\tDisciplined and calm. Fencers are all about tactics so they last longer on the battlefield.\n" \
                   "3 - Samurai:\n" \
                   "\tHonoured and skilled. Samurais are balance in both combat and defense.\n" \
                   "4 - Normal:\n" \
                   "\tNo sub-class chosen."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_training_knight_sub_class_list(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Knight',
            'HP': 500,
            'Attack': 80
        }
        class_training(test_character)
        actual = mock_output.getvalue()
        expected = "1 - Cyborg:\n" \
                   "\tHalf-human, half-machine. Part of their body is optimized,\n" \
                   "\tso cyborgs are stronger in attack compared to other Knight sub-classes.\n" \
                   "2 - Paladin:\n" \
                   "\tLoyal and dedicated. Paladins are the main branch of Knights, \n" \
                   "\tand they are proud to be closely watched and protected by Gods.\n" \
                   "3 - Guardian:\n" \
                   "\tWell-rounded. Guardians carry an important mission to protect, \n" \
                   "\tso they are balance in both combat and defense.\n" \
                   "4 - Normal:\n" \
                   "\tNo sub-class chosen."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_training_magician_sub_class_list(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Magician',
            'HP': 300,
            'Attack': 120
        }
        class_training(test_character)
        actual = mock_output.getvalue()
        expected = "1 - Sorcerer:\n" \
                   "\tA natural enthusiast. Sorcerers carve magical circles into their body \n" \
                   "\tto truly become one with nature, so they are the strongest combatant.\n" \
                   "2 - Shaman:\n" \
                   "\tA believer. Shamans connect to the nature and, above all, to the Gods, \n" \
                   "\tso that they can use Gods' protection power in the battlefield.\n" \
                   "3 - Rune Fencer:\n" \
                   "\tA natural lover. Rune Fencers combine their swordsmanship and \n" \
                   "\tmagic knowledge to create new combat tactics. Hence, they are well-rounded.\n" \
                   "4 - Normal:\n" \
                   "\tNo sub-class chosen."
        self.assertIn(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('builtins.input', side_effect=['y', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_training_archer_sub_class_list(self, mock_output, __, _):
        test_character = {
            'Name': 'Test',
            'Class': 'Archer',
            'HP': 450,
            'Attack': 90
        }
        class_training(test_character)
        actual = mock_output.getvalue()
        expected = "1 - Hunter:\n" \
                   "\tReckless. Hunters pursues the thrill of finding the perfect prey.\n" \
                   "\tHunters are stronger in attack compared to other Archer sub-classes.\n" \
                   "2 - Ranger:\n" \
                   "\tSerene but firm. Rangers want to protect the green forest with all their might\n" \
                   "\tso you will be surprised by their toughness on the battlefield.\n" \
                   "3 - Gunner:\n" \
                   "\tAdventurous. Gunners are the new branch of Archers. With guns in their hands, \n" \
                   "\tgunners become balance in both combat and defense.\n" \
                   "4 - Normal:\n" \
                   "\tNo sub-class chosen."
        self.assertIn(expected, actual)
