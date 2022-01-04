from unittest import TestCase
from game import generate_game_board as generate


class Test(TestCase):
    def test_generate_game_board_total_rooms(self):
        board = generate()
        expected_total_rooms = 25 * 25
        self.assertEqual(expected_total_rooms, len(board))

    def test_generate_game_board_outside_castle(self):
        board = generate()
        description_check = True

        for x in range(0, 10):
            for y in range(20, 25):
                if board[(x, y)] != "You are outside of the Castle.":
                    description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_castle_door(self):
        board = generate()
        description_check = True

        for x in range(0, 10):
            if board[(x, 19)] != "You step inside the Castle. It's huge.":
                description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_inside_castle(self):
        board = generate()
        description_check = True

        castle_descriptions = ['You see a golden vase. It must be expensive.',
                               'You see a huge drawing. It looks historic.',
                               'You see many swords hung on the wall. They must belong to the royalty.',
                               'You see a magic circle under the floor. Is it some kind of protection?',
                               'Class Training', 'Battle Training']

        for x in range(0, 10):
            for y in range(10, 19):
                if board[(x, y)] not in castle_descriptions:
                    description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_forest(self):
        board = generate()
        description_check = True

        forest_descriptions = ['You catch something moving from the corner of your eyes.',
                               'You feel like someone is observing you.',
                               'A gentle wind stirs your hair. You feel calm.',
                               'You hear giggles from afar. You wonder where that come from.',
                               'Portal']

        for x in range(0, 25):
            for y in range(0, 9):
                if board[(x, y)] not in forest_descriptions:
                    description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_wasteland(self):
        board = generate()
        description_check = True

        wasteland_descriptions = ['You sense an an ominous presence.',
                                  'You hear a roar. What could make that sound in this desert?',
                                  'Nothing happens, which is unusual.',
                                  'You nearly step into a lava pool.',
                                  'An ogre passes by, looking pissed off. Better not bother them.',
                                  'Boss', 'Heal', 'Blessing', 'Portal']

        for x in range(11, 25):
            for y in range(10, 25):
                if board[(x, y)] not in wasteland_descriptions:
                    description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_walls(self):
        board = generate()
        description_check = True

        for x in range(3, 25):
            if board[(x, 9)] != 'Wall':
                description_check = False

        for y in range(9, 25):
            if board[(10, y)] != 'Wall':
                description_check = False

        self.assertEqual(description_check, True)

    def test_generate_game_board_gates(self):
        board = generate()
        description_check = True

        for x in range(3):
            if board[(x, 9)] != 'Gate':
                description_check = False

        self.assertEqual(description_check, True)
