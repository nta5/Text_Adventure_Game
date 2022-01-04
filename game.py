"""
Name: Melanie Ta
Text-based Adventure Game

All of my code is in this file.
"""
import time
import random
import itertools


# Constant variables
VISUALIZATION = {
    'Wall': ' ' + chr(2011),
    'Gate': ' /',
    'Class Training': ' CT',
    'Battle Training': ' BT',
    'Portal': ' ' + chr(1421),
    'Heal': '!!!',
    'Blessing': ' ' + chr(1421),
    'Boss': '???'
}

CLASS_SYSTEM = {
    'Warrior': ['Berserker', 'Fencer', 'Samurai', 'Normal'],
    'Knight': ['Cyborg', 'Paladin', 'Guardian', 'Normal'],
    'Magician': ['Sorcerer', 'Shaman', 'Rune Fencer', 'Normal'],
    'Archer': ['Hunter', 'Ranger', 'Gunner', 'Normal']
}

CLASS_DESCRIPTIONS = ('WARRIORS\n'
                      'With their trust-worthy swords, or just fists, they fight with all their might.\n'
                      'A warrior loves fighting and fighting with worthy enemies.\n'
                      'Overall, they are well-rounded.\n',

                      'KNIGHTS\n'
                      'The skilled combatants who fight in the name of honour and chivalry.\n'
                      'A knight is protected by the power of the God of Yggdra so'
                      'they last longer on the battlefield.\n'
                      'Yet, their attack may not on par to that of warriors and magicians.\n',

                      'MAGICIANS\n'
                      'They are loved by the nature.\n'
                      'Hence, they are the strongest combatant with high Attack stat.\n'
                      'The cost of this power is their low HP.\n',

                      'ARCHERS\n'
                      'They are the favourite child of air.\n'
                      'An archer uses their bow, or gun, to solve every problem.\n'
                      'Being good friend with the wind, they are durable and flexible in combat.\n')

SUB_CLASS_DESCRIPTIONS = {
    'Normal': 'No sub-class chosen.',

    'Berserker': 'Bold and direct. Berserkers are stronger in attack compared to other Warrior sub-classes.',
    'Fencer': 'Disciplined and calm. Fencers are all about tactics so they last longer on the battlefield.',
    'Samurai': 'Honoured and skilled. Samurais are balance in both combat and defense.',

    'Cyborg': 'Half-human, half-machine. Part of their body is optimized,\n'
              '\tso cyborgs are stronger in attack compared to other Knight sub-classes.',
    'Paladin': 'Loyal and dedicated. Paladins are the main branch of Knights, \n'
               '\tand they are proud to be closely watched and protected by Gods.',
    'Guardian': 'Well-rounded. Guardians carry an important mission to protect, \n'
                '\tso they are balance in both combat and defense.',

    'Sorcerer': 'A natural enthusiast. Sorcerers carve magical circles into their body \n'
                '\tto truly become one with nature, so they are the strongest combatant.',
    'Shaman': 'A believer. Shamans connect to the nature and, above all, to the Gods, \n'
              "\tso that they can use Gods' protection power in the battlefield.",
    'Rune Fencer': 'A natural lover. Rune Fencers combine their swordsmanship and \n'
                   '\tmagic knowledge to create new combat tactics. Hence, they are well-rounded.',

    'Hunter': 'Reckless. Hunters pursues the thrill of finding the perfect prey.\n'
              '\tHunters are stronger in attack compared to other Archer sub-classes.',
    'Ranger': 'Serene but firm. Rangers want to protect the green forest with all their might\n'
              '\tso you will be surprised by their toughness on the battlefield.',
    'Gunner': 'Adventurous. Gunners are the new branch of Archers. With guns in their hands, \n'
              '\tgunners become balance in both combat and defense.'
}

LEVEL_UP_BASE = 1.5


# Create map
def generate_game_board() -> dict:
    """
    Generate a 25 x 25 game board.

    This function creates a game board where each key is a tuple for a set of coordinates
    and each value is a string description. Each room in the board will be randomly assigned
    a description, except for special coordinates.

    :postcondition: creates a dictionary where each key is a tuple for a set of coordinates
                    and each value is a random string description
    :return: a dictionary which represents a 25 x 25 game board
    """
    # Holy Capital
    castle_descriptions = ['You see a golden vase. It must be expensive.',
                           'You see a huge drawing. It looks historic.',
                           'You see many swords hung on the wall. They must belong to the royalty.',
                           'You see a magic circle under the floor. Is it some kind of protection?']

    game_board = {(column, row): "You are outside of the Castle." for column in range(0, 10) for row in range(20, 25)}
    game_board.update({(column, 19): "You step inside the Castle. It's huge." for column in range(0, 10)})
    game_board.update({(column, row): castle_descriptions[random.randint(0, 3)]
                       for column in range(0, 10) for row in range(10, 19)})

    # Soul Island
    forest_descriptions = ['You catch something moving from the corner of your eyes.',
                           'You feel like someone is observing you.',
                           'A gentle wind stirs your hair. You feel calm.',
                           'You hear giggles from afar. You wonder where that come from.']
    game_board.update({(column, row): forest_descriptions[random.randint(0, 3)]
                       for column in range(0, 25) for row in range(0, 9)})

    # Nine Territories of Fire
    wasteland_descriptions = ['You sense an an ominous presence.',
                              'You hear a roar. What could make that sound in this desert?',
                              'Nothing happens, which is unusual.',
                              'You nearly step into a lava pool.',
                              'An ogre passes by, looking pissed off. Better not bother them.']
    game_board.update({(column, row): wasteland_descriptions[random.randint(0, 4)]
                       for column in range(10, 25) for row in range(10, 25)})

    # Doors and walls
    game_board.update({(column, 9): 'Gate' for column in range(0, 3)})
    game_board.update({(column, 9): 'Wall' for column in range(3, 25)})
    game_board.update({(10, row): 'Wall' for row in range(9, 25)})

    # Special coordinate
    game_board.update({
        (5, 17): 'Class Training',
        (5, 12): 'Battle Training',
        (12, 4): 'Portal',
        (17, 10): 'Portal',
        (17, 16): 'Blessing',
        (13, 22): 'Heal',
        (22, 11): 'Heal',
        (22, 22): "Boss",
    })

    return game_board


# Create visual map
def print_map(board: dict, character: dict) -> None:
    """
    Get character's location and draw a 5 x 7 visual map.

    This function gets character's X-coordinate and Y-coordinate. From character's
    location, this function draws a 5 x 7 map which represents the area surrounding
    the character.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary used to represent a 25 x 25 map
                   where each key is a tuple for a set of coordinates, and each value is a short string description
    :precondition: character must be a dictionary which contains two keys with two positive-integer
                   values: 'X-coordinate' and 'Y-coordinate'
    :postcondition: prints a 5 x 7 visual map based on character's location
    """
    x_standing = character['X-coordinate']
    y_standing = character['Y-coordinate']

    for y_value in range(y_standing - 2, y_standing + 3):
        for x_value in range(x_standing - 3, x_standing + 4):
            coordinate = (x_value, y_value)

            if coordinate == (x_standing, y_standing):
                print('[#]', end='\t')
            elif coordinate in board.keys():
                if board[coordinate] in VISUALIZATION:
                    print(VISUALIZATION[board[coordinate]], end='\t')
                else:
                    print(' .', end='\t')
            else:
                print(VISUALIZATION['Wall'], end='\t')
        print()


# Auto generator
def print_separation_line() -> None:
    """
    Print a separation line.
    """
    line = ''.join(itertools.repeat('*', 40))
    print(f"\n{line}\n")


def place_holder() -> None:
    """
    Generate a Y/N question.

    This function generates a Y/N question and wait for user's input. This function is
    mostly invoked in-between large paragraphs to keep users engaged and prevent wall of text.

    :postcondition: prints a Y/N question and waits for input
    :postcondition: keeps asking until user types Y or y
    """
    user_choice = input("Y/N\n").upper()

    while user_choice != 'Y':
        time.sleep(2)
        print("Are you ready now?")
        user_choice = input().upper()


# Storyline
def introduction() -> None:
    """
    Generate the introduction scene.
    """
    print_separation_line()
    print("The sudden light makes you squint.\n")

    time.sleep(1)
    print("You hear some murmurs: 'It must be him, the hero in the prophecy...'")
    print("You open your eyes.\n"
          "A girl in royal outfit is looking at you.\n")

    time.sleep(3)
    print("'Welcome to the continent of Yggdra', she says, 'I am Juliana, the Queen of the Holy Capital.'\n"
          "Juliana asks: 'May I ask for your name, adventurer?'\n")


def ask_for_player_information() -> dict:
    """
    Ask for character's name and generate basic character information.

    :postcondition: creates a dictionary with user's input name and basic information
    :return: a dictionary where the key 'Name' is user's input, 'Level' is 1, 'Experience' is 0,
             'X-coordinate' is 5, 'Y-coordinate' is 23, and 'Status' is 'Alive'
    """
    print("A voice whispers in the distance: 'You only have one chance to tell us your name.'")
    name = input("My name... ").title()

    print(f"\nJuliana says: '{name}, my pleasure to meet you.\n"
          "\tNow then, let us go to the castle. Everyone is waiting.'")

    time.sleep(3)
    print_separation_line()

    character = {
        'Name': name,
        'Level': 1,
        'Experience': 0,
        'X-coordinate': 5,
        'Y-coordinate': 23,
        'Status': 'Alive',
    }

    return character


# Class decision
def class_decision(character: dict) -> None:
    """
    Ask and update character's class.

    This function prints an interaction scene and receives user's class choice.
    Based on user's choice, this function adds a 'Class' key to the character dictionary.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'Name'
    :postcondition: adds a 'Class' key to character
    :postcondition: the value of 'Class' can be 'Warrior', 'Knight', 'Magician', or 'Archer' based on user's choice
    """
    print("You arrive at a huge white castle.\n"
          f"Juliana says: '{character['Name']}, you must still be unfamiliar with this new world.\n"
          "\tTell me your class and I will promptly organize a training session for you.'\n")

    help_choice = input("Do you want to learn about the class system first?\n"
                        "Type Y to proceed. Type any other letter to skip.\n").upper()

    if help_choice == 'Y':
        help_classes()

    print(f"\nJuliana says: '{character['Name']}, are you ready to tell me your class?'")

    classes = list(CLASS_SYSTEM.keys())
    for index, value in enumerate(classes, 1):
        print("\t{0}: {1}".format(index, value))

    chosen_class = input("Your choice: ").title()
    while chosen_class not in map(str, range(1, 5)):
        chosen_class = input("Invalid. Please try again. \nYour choice: ")

    character['Class'] = classes[int(chosen_class) - 1]

    time.sleep(1)
    print(f"\nJuliana says: 'So you are a {character['Class']}.\n"
          "\tA training session has been arranged for you. Please follow me.'")


def help_classes() -> None:
    """
    Offer information about class system.

    This function is invoked in class_decision() to provide information about the class system.
    When executed, this function prints an introducing paragraph. It then prompts user for input
    and prints a class description accordingly.

    :postcondition: prints an introduction and waits for input
    :postcondition: prints class descriptions based on user's choice
    """
    print("\nIn this world, there is four main classes: Warrior, Knight, Magician, and Archer.\n"
          "Each class has their own strengths and weaknesses.\n"
          "Which class are you interested in learning?")

    for index, value in enumerate(CLASS_SYSTEM.keys(), 1):
        print("\t{0}: {1}".format(index, value))

    choice = input()
    while choice not in map(str, range(1, 5)):
        print("Invalid. Try again.")
        choice = input()

    print(CLASS_DESCRIPTIONS[int(choice) - 1])

    learn_more = input("Do you want to learn about another class?\n"
                       "Type Y to proceed. Type any other letter to skip.\n").upper()
    if learn_more == 'Y':
        help_classes()


def generate_class_stat(character: dict) -> None:
    """
    Create 'HP' and 'Attack' attribute for a character based on their 'Class'.

    :param character: a dictionary
    :precondition: character must be a dictionary with a 'Class' key
    :postcondition: character's 'Class' key must be 'Warrior', 'Knight', 'Magician', or 'Archer'
    :postcondition: adds 'HP' and 'Attack' key with positive integer values to character
    """
    class_name = character['Class']

    if class_name == "Warrior":
        character['HP'] = 400
        character['Attack'] = 100
    elif class_name == "Knight":
        character['HP'] = 500
        character['Attack'] = 80
    elif class_name == "Magician":
        character['HP'] = 300
        character['Attack'] = 120
    elif class_name == "Archer":
        character['HP'] = 450
        character['Attack'] = 90


# Storyline
def gameplay_training(character: dict) -> None:
    """
    Print an interactive training scene.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'Name'
    :postcondition: prints a training scene
    """
    time.sleep(5)
    print_separation_line()

    print("Juliana says: 'Let's familiarize yourself with the movement system.\n"
          "\tWhen you are prompted to move, a list of directions will be displayed.\n"
          "\tTo move to a direction, type the initials or the whole direction name.\n"
          "\tPractice makes perfect. Be ready to make your first move.'\n")

    print("Are you ready? It will be easy.", end=" ")

    place_holder()

    time.sleep(1)
    print(f"Juliana says: '{character['Name']}, try moving to the East.'")
    practice_choice = get_user_move()

    while practice_choice != 'East':
        print(f"\nJuliana says: 'That is not correct, {character['Name']}. Try again.'\n")
        practice_choice = get_user_move()

    print(f"\nJuliana smiles: 'Great job, {character['Name']}! You nailed it.\n"
          "\tYou seem to be a fast learner, which is great.'\n")

    time.sleep(3)
    print("Juliana says: 'Now, I fear that we must part ways here.\n"
          "\tPlease go North to the castle to receive more battle trainings.\n"
          "\tAfter you feel confident enough, I will return to assist you.\n"
          "\tGood luck with your training. We will meet again.'\n")
    time.sleep(7)


# Sub-class decision
def class_training(character: dict) -> None:
    """
    Introduce sub-class system and ask for character's sub-class.

    This function prints an interaction scene and receives user's sub-class choice.
    Then, this function calls the helper function, generate_sub_class_stat, to change
    character's stat accordingly.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Name', 'Class', 'HP', and 'Attack'
    :postcondition: get character's sub-class and pass it to the helper function generate_sub_class_stat
    :postcondition: character's 'HP' and 'Attack' will be updated based on sub-class choice
    """
    print(f"Louise says: 'Hi there. You must be {character['Name']}.\n"
          "\tMy name is Louise. I am an assistant of Queen Juliana.\n"
          "\tTell me when you are ready and I will walk you through the basics of your class.'", end=' ')

    place_holder()

    print("Louise observes you: 'It's time for you to know about sub-class.\n"
          "\tChoosing sub-class will create some changes to your HP and Attack stats.\n"
          f"\tNow then, {character['Name']}, what sub-class will pique your interest?'\n")

    time.sleep(8)

    for shortcut, sub_class in enumerate(CLASS_SYSTEM[character['Class']], 1):
        print(f"{shortcut} - {sub_class}:\n"
              f"\t{SUB_CLASS_DESCRIPTIONS[sub_class]}")

    chosen_sub_class = input("Your choice: ").title()
    while chosen_sub_class not in map(str, range(1, 5)):
        chosen_sub_class = input("Invalid. Please try again. \nYour choice: ")

    generate_sub_class_stat(character, chosen_sub_class)

    print(f"\nLouise hums: 'I see. So this is your choice, {character['Name']}.'")
    time.sleep(3)

    print("\nLouise says: 'Your training with me is finished. Please continue to go North.\n"
          "\tKain, the Leader of the Volunteer Army, will show you how to battle.'\n")


def generate_sub_class_stat(character: dict, sub_class: str) -> None:
    """
    Update character dictionary based on sub-class choice.

    :param character: a dictionary
    :param sub_class: a string
    :precondition: character must be a dictionary with the keys 'HP' and 'Attack'
    :precondition: the values of 'HP' and 'Attack' keys must be positive integers
    :precondition: sub_class must be '1', '2', '3', or '4'
    :postcondition: updates the character's 'HP' and 'Attack' based on sub_class
    :postcondition: create new key "Max HP" which stores max HP number

    >>> test_character = {'Class': 'Archer', 'HP': 450, 'Attack': 90}
    >>> generate_sub_class_stat(test_character, '1')
    >>> test_character
    {'Class': 'Archer', 'HP': 450, 'Attack': 110, 'Max HP': 450}

    >>> test_character = {'Class': 'Archer', 'HP': 450, 'Attack': 90}
    >>> generate_sub_class_stat(test_character, '3')
    >>> test_character
    {'Class': 'Archer', 'HP': 475, 'Attack': 100, 'Max HP': 475}
    """
    if sub_class == '1':
        character['Attack'] += 20
    elif sub_class == '2':
        character['HP'] += 50
    elif sub_class == '3':
        character['Attack'] += 10
        character['HP'] += 25
    elif sub_class == '4':
        character['Attack'] += 5
        character['HP'] += 15

    character['Max HP'] = character['HP']


# Storyline
def battle_training(character: dict) -> None:
    """
    Generate a battle training scene.

    This function prints an interaction scene to tell user about the battle system.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'Name'
    :postcondition: prints a training scene
    """
    print("\nYou meet Kain.\n\n"
          f"Kain smiles: 'Welcome, {character['Name']}. Great to see you.\n"
          "\tI am Kain, the Leader of the Volunteer Army.\n"
          "\tLet's keep it fast. Are you ready for this battle training?'", end=' ')

    place_holder()

    print("\nKain says: 'The battle system is very simple.\n"
          "\tYou only need to guess your opponent's next movement: Left or Right.\n"
          "\tIf you are correct, you will deal 120% of your Attack stat to them.\n"
          "\tIf you are wrong, your damage will only be 80% of your Attack.\n"
          "\tYou can choose not to guess, and you will deal damage equal to 100% Attack.'\n")

    time.sleep(15)
    print(f"Kain smiles: '{character['Name']}, do your best. That's it from me today.\n"
          "\tQueen Juliana is waiting outside the Castle. Go northwest from here and you can meet her.\n"
          "\tShe will tell you your true mission and what you need to know. Best of luck to you!'\n")


def start_mission(character: dict) -> None:
    """
    Generate the start mission scene.

    This function prints an interaction scene to tell user their mission.
    In the end, this function gives 500 EXP points to the user. After receiving
    the EXP, the user cannot activate this scene anymore.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Name' and 'Experience'
    :postcondition: prints the start mission scene
    :postcondition: increases the 'Experience' key in character dictionary by 500 points
    """
    if character['Experience'] > 0:
        return None

    print(f"Juliana says: 'And we meet again, {character['Name']}. I hope you are ready.\n"
          "\tThe mission I am about to tell you affects the whole fate of this continent.\n"
          "\tAre you prepared for this important mission?'", end=" ")

    place_holder()

    print(f"Juliana says: '{character['Name']}, Yggdra is a small continent, but we have a long history.\n"
          "\tEver since 1,000 years ago, we have been gifted with Chronicle, a tome of God.\n"
          "\tThe Chronicle records the history and bears the future of the world.\n"
          "\tIt has the supreme power, and therefore, the Dark Force wants it to take over the world.'\n")
    time.sleep(15)

    print("Juliana says: 'Recently, we discovered a hidden tunnel where the Dark Army stationed.\n"
          f"\tAnd you, {character['Name']}, is the only person who is strong enough to win against them.'\n")
    time.sleep(5)

    print(f"Juliana says: 'Now, {character['Name']}, ahead of you is the Soul Island.\n"
          "\tFind the Portal at coordinate (12, 4). It is the only way you can go to the Dark Tunnel.\n"
          "\tOletta, the matriarch of Soul Island, is waiting for you there.\n"
          f"\tGoodbye, {character['Name']}. I wish you good luck on your journey.'\n")
    time.sleep(10)

    print("You receive 500 EXP from Juliana.\n")
    character['Experience'] += 500
    time.sleep(3)


def mission_guidance(character: dict) -> None:
    """
    Generate the mission guidance scene.

    This function prints an interaction scene to tell user their next steps before
    meeting the boss. Then, this function creates a 'Compass' key, changes user's
    location, and fully restores the user's HP.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Name', 'X-coordinate', 'Y-coordinate',
                   'HP', and 'Max HP'
    :postcondition: creates a 'Compass' key for character and sets the value to True
    :postcondition: changes the values of 'X-coordinate' key to 17 and 'Y-coordinate' key to 10
    :postcondition: gives 'HP' key the value stored in 'Max HP' key
    """
    print(f"\nOletta welcomes you: '{character['Name']}, my pleasure to meet you.\n"
          "\tThis portal will lead you to Nine Territories of Fire.\n"
          "\tResidents of the Nine Territories of Fire are the toughest warriors in this continent.\n"
          "\tHowever, even they couldn't win against the Dark Force's army.\n"
          "\tIf the source of Darkness is not eliminated as soon as possible, Yggdra will be in great danger.\n"
          "\tPlease find the Dark Tunnel at the southeast of Nine Territories and kill the Dark King.'\n")

    time.sleep(20)
    print("Oletta says: 'Phoena, the Keeper of the Chronicle, is waiting at (17, 16).\n"
          "\tFind her and she will use the power of Chronicle to give you blessing.\n"
          "\tIn some spots, there will be a heal station. Drop by and heal yourself when needed.\n"
          "\tAnd, lastly, I will give you the Sacred Compass.\n"
          "\tEach time you move, the compass will have 25% to activate and show you where Dark King is.\n"
          "\tNow, are you ready to go?'", end=" ")

    place_holder()

    character['Compass'] = True
    character['X-coordinate'] = 17
    character['Y-coordinate'] = 10
    character['HP'] = character['Max HP']


# Movement
def get_user_move() -> str:
    """
    Get the next movement of a character.

    :postcondition: displays a list of directions for character to choose from
    :postcondition: keeps asking until getting a valid direction
    :postcondition: gets a valid movement of a character
    :return: a string that contains the direction which a character is heading to
    """
    directions = {
        'N': "North",
        'S': "South",
        'E': "East",
        'W': "West",
        'Q': "Quit"
    }

    print("Available directions:\n \t", end='')
    for key, value in directions.items():
        print("{0}: {1}".format(key, value), end='     ')
    move = input("\nChoose your move: ").title()

    while move not in directions.keys() and move not in directions.values():
        move = input("Invalid choice. Please try again. \nChoose your move: ").title()

    if move in directions.values():
        return move
    else:
        return directions[move]


def validate_move(board: dict, character: dict, move: str) -> bool:
    """
    Check if a move for a character is valid in a board.

    :param board: a dictionary
    :param character: a dictionary
    :param move: a string
    :precondition: board must be a dictionary where each key is a tuple for a set of coordinates
                   and each value is a short string description
    :precondition: character must be a dictionary which has the keys "X-coordinate" key and "Y-coordinate"
    :precondition: move must be a string with the value of "North", "South", "West", or "East"
    :postcondition: checks if the move is valid
    :return: True if character can move in a direction, False if character cannot

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> test_map = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
    >>> validate_move(test_map, test_character, "East")
    True

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> test_map = {(0, 0): 'Random', (0, 1): 'Random', (1, 0): 'Random', (1, 1): 'Random'}
    >>> validate_move(test_map, test_character, "West")
    False
    """
    x_value = character["X-coordinate"]
    y_value = character["Y-coordinate"]

    if move == "North":
        y_value -= 1
    elif move == "South":
        y_value += 1
    elif move == "West":
        x_value -= 1
    elif move == "East":
        x_value += 1

    new_coordinate = (x_value, y_value)
    if new_coordinate in board.keys() and board[new_coordinate] != 'Wall':
        return True
    else:
        return False


def move_character(character: dict, move: str) -> None:
    """
    Move character to a given direction.

    :param character: a dictionary
    :param move: a string
    :precondition: character must be a dictionary which has the keys "X-coordinate" and "Y-coordinate"
    :precondition: move must be a string with the value of "North", "South", "West", or "East"
    :postcondition: moves the character accordingly

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(test_character, 'East')
    >>> test_character
    {'X-coordinate': 1, 'Y-coordinate': 0}

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(test_character, 'South')
    >>> test_character
    {'X-coordinate': 0, 'Y-coordinate': 1}
    """
    if move == "North":
        character["Y-coordinate"] -= 1
    elif move == "South":
        character["Y-coordinate"] += 1
    elif move == "East":
        character["X-coordinate"] += 1
    elif move == "West":
        character["X-coordinate"] -= 1


# Game flow control
def describe_current_location(board: dict, character: dict) -> None:
    """
    Display where a character is standing in a game board.

    This functions prints the description of where a character is standing.
    If the description falls into special cases, invoke the helper function
    execute_game_scenario instead.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary where each key is a tuple for a set of coordinates,
                   and each value is a short string description
    :precondition: character must be a dictionary which has "X-coordinate" key and "Y-coordinate" key
    :precondition: the tuple created from "X-coordinate" and "Y-coordinate" of character must be a key in board
    :postcondition: prints the current coordinates of character with the location description
    """
    special_cases = ['Class Training', 'Battle Training', 'Gate', 'Portal', 'Heal', 'Blessing', 'Boss']

    x_value = character["X-coordinate"]
    y_value = character["Y-coordinate"]
    description = board[(x_value, y_value)]

    if description not in special_cases:
        print("\nCoordinate {0}. {1}".format((x_value, y_value), description))
    else:
        execute_game_scenario(character, description)


# Game flow anchors
def execute_game_scenario(character: dict, description: str) -> None:
    """
    Receive the room description and generate the corresponding game scene.

    :param character: a dictionary
    :param description: a string
    :precondition: character must be a dictionary
    :precondition: description must be 'Class Training', 'Battle Training', 'Gate', 'Portal', 'Heal',
                   'Blessing', or 'Boss'
    """
    if description == 'Class Training':
        class_training(character)
    elif description == 'Battle Training':
        battle_training(character)
    elif description == 'Gate':
        start_mission(character)
    elif description == 'Portal':
        use_portal(character)
    elif description == 'Heal':
        heal(character)
    elif description == 'Blessing':
        special_encounter(character)
    elif description == 'Boss':
        final_battle(character)

    time.sleep(5)


# Special events
def use_portal(character: dict) -> None:
    """
    Teleport the user between two locations.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'X-coordinate' and 'Y-coordinate'
    :postcondition: changes the location of character
    """
    x_value = character['X-coordinate']
    y_value = character['Y-coordinate']
    coordinate = (x_value, y_value)

    if coordinate == (12, 4) and 'Compass' not in character.keys():
        mission_guidance(character)

    elif coordinate == (12, 4) and 'Compass' in character.keys():
        return_choice = input("Return to Nine Territories of Fire?\n"
                              "Type Y to proceed. Type any other letter to skip.\n").title()
        if return_choice == 'Y':
            character['X-coordinate'] = 17
            character['Y-coordinate'] = 10

    elif coordinate == (17, 10):
        return_choice = input("Return to Soul Island?\n"
                              "Type Y to proceed. Type any other letter to skip.\n").title()
        if return_choice == 'Y':
            character['X-coordinate'] = 12
            character['Y-coordinate'] = 5


def heal(character: dict) -> None:
    """
    Restore the value of a character's HP to Max HP.

    This function restores the value of a character's HP to Max HP. If the HP is
    currently higher than Max HP, keep the HP value.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'HP' and 'Max HP'
    :postcondition: updates character's 'HP' value

    >>> test_character = {'HP': 304, 'Max HP': 600}
    >>> heal(test_character)
    <BLANKLINE>
    You are fully healed.
    <BLANKLINE>
    >>> test_character['HP'] == 600
    True
    """
    if 'Blessing' in character.keys() and character['HP'] > character['Max HP']:
        return

    print("\nYou are fully healed.\n")
    character['HP'] = character['Max HP']


def special_encounter(character: dict) -> None:
    """
    Give blessing to a character.

    This function prints an interactive special encounter scene and give a blessing to a character.
    If the character already receive blessing, this function will call the heal function instead.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Name', 'HP', 'Max HP', and 'Attack'
    :postcondition: creates a 'Blessing' key for character and sets the value to True
    :postcondition: over-heals the character and boosts attack point
    """
    if 'Blessing' in character.keys():
        print(f"Phoena says: 'For the peace and happiness of Yggdra.'")
        heal(character)
        return None

    print("You meet Phoena.\n\n"
          f"Phoena says: '{character['Name']}! I know you will come.\n"
          "\tI am Phoena, the Keeper of the Chronicle.\n"
          "\tThe final battle is approaching. But don't be worried.\n"
          "\tThe Chronicle will bless you and give you strength.'\n")

    print("You receive Chronicle's blessing.")

    character['Blessing'] = True
    character['HP'] = character['Max HP'] + 300
    character['Attack'] += 20

    time.sleep(10)
    print("\nPhoena grabs your hand: 'The future of Yggdra lies on your shoulder.\n"
          "\tPlease protect this beautiful continent from the Dark Force.\n"
          "\tThe Dark Tunnel is not far from this spot. You just need to go southeast from here.\n"
          f"\tGoodbye, {character['Name']}. I wish you strength and victory.'")
    time.sleep(5)


def compass(character: dict) -> None:
    """
    Manage the compass function.

    The compass has 25% to activate and prints how far the character is from the boss.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'X-coordinate' and 'Y-coordinate'
    :postcondition: the compass has 25% to activate
    """
    activation = random.randint(1, 4)
    x_value = character['X-coordinate']
    y_value = character['Y-coordinate']

    if 'Compass' in character.keys() and activation == 4 and (x_value, y_value) != (22, 22):
        print("The compass shines and shows something you don't understand:", end=" ")
        if y_value > 22:
            print(f"{y_value - 22}N", end=" ")
        elif y_value < 22:
            print(f"{22 - y_value}S", end=" ")

        if x_value > 22:
            print(f"{x_value - 22}W", end="")
        elif x_value < 22:
            print(f"{22 - x_value}E", end="")

        print("\nWhat could it mean?\n")


def final_battle(character: dict) -> None:
    """
    Fight the final boss.

    This function creates the boss and generates the final battle scene.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'HP', 'Attack', and 'Status'
    :postcondition: if the character loses, change 'Status' to 'Dead';
                    if the character wins, change 'Status' to 'Win'
    """
    boss = {
        'Name': 'Dark King',
        'HP': 1200,
        'Attack': 150,
    }

    print("\nYou meet the Dark King. You get your weapons ready.\n\n"
          f"{boss['Name']} says: 'Insolent human! You dare disobey me.\n"
          "\tYou think you can defeat me? Just with you and that kind of power?\n"
          "\tYou will pay for your foolishness.'")

    while boss['HP'] > 0:
        print(f"\n{boss['Name']}'s HP is {boss['HP']}.\n")

        guess_result = guessing_game(True)
        attack = calculate_attack_point(character, guess_result)

        print(f"You attack {boss['Name']}, deal {attack} damage.")
        boss['HP'] -= attack

        character['HP'] -= boss['Attack']
        if character['HP'] > 0:
            print(f"You lose {boss['Attack']} HP. Your HP is now {character['HP']}.")
        else:
            character['Status'] = 'Dead'
            return None

    character['Status'] = 'Win'


# Battle system
def check_for_foes(character: dict) -> bool:
    """
    Check if there is a foe in the room.

    :postcondition: checks if there is a foe in the room
    :postcondition: the player has a 20% chance of meeting a foe
    """
    if character['X-coordinate'] == 22 and character['Y-coordinate'] == 22:
        return False
    else:
        foe_checking = random.randint(1, 5)
        return foe_checking == 3


def battle_decision(character: dict) -> bool:
    """
    Ask if the character want to run away or not.

    This function asks if the user want to run away or not. If user chooses to
    run away, they have 20% chance of taking flee damage.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'HP', the value of which is a positive integer
    :postcondition: user has 20% chance of taking damage if running away
    :return: True if user decides to battle, False if user decides to flee
    """
    print(f"Your HP is now {character['HP']}.", end=" ")
    run_away = input("Run? Y/N ").upper()

    while run_away != 'Y' and run_away != 'N':
        run_away = input("Invalid. Try again.\nY/N ").upper()

    if run_away == 'N':
        return True
    else:
        if random.randint(1, 5) == 3:
            flee_damage = random.randint(30, 100)
            print(f"You lose {flee_damage} HP.")
            character['HP'] -= flee_damage

        return False


def create_opponent(character: dict) -> dict:
    """
    Randomize an opponent profile and stat.

    This function randomizes and creates an opponent profile. When character
    reaches a new region, more random options will be added. Opponent stat
    will be randomized based on character's stat.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'X-coordinate', 'Y-coordinate',
                   'Attack' and 'Max HP'
    :return: a dictionary with the keys 'Name', 'HP', 'Attack' which store random values
    """
    x_value = character['X-coordinate']
    y_value = character['Y-coordinate']

    opponent_classes = ["Elf", "Ogre", "Sniper", "Assassin", "Thief", "Commander", "Pirate"]
    opponent_names = ["Vienta", "Eshal", "Amatsu", "Helios", "Yuni", "Chidori", "Einslotte", "Arietta"]

    if x_value >= 10 and y_value >= 10:
        opponent_classes += ['Dragon', 'Demon', 'Archdemon', 'Demon of Destruction', 'Demon of Desecration',
                             'Killer', 'Prisoner', 'Misbeliever']
        opponent_names += ['Eirneus', 'Razanil', 'Sellen', 'Kataris', "Barcus", "Labezerin", "Suphlatus"]

    opponent = {
        'Name': random.choice(opponent_names) + ' the ' + random.choice(opponent_classes),
        'HP': random.randint(character['Attack'], character['Attack'] * 3),
        'Attack': random.randint(character['Max HP'] // 20, character['Max HP'] // 15),
    }

    return opponent


def battle(character: dict, opponent: dict) -> None:
    """
    Start a battle between character and opponent.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary with the keys 'HP' and 'Attack'
    :precondition: opponent must be a dictionary with the keys 'Name', 'HP' and 'Attack'
    :postcondition: generates a battle scene
    :postcondition: if the character loses, changes 'Status' to 'Dead' and immediately ends battle
    """
    while opponent['HP'] > 0:
        print(f"\n{opponent['Name']}'s HP is {opponent['HP']}.\n")

        guess_result = guessing_game(False)
        attack = calculate_attack_point(character, guess_result)

        opponent['HP'] -= attack
        print(f"\nYou attack {opponent['Name']} with {attack} damage.")

        character['HP'] -= opponent['Attack']
        if character['HP'] > 0:
            print(f"You lose {opponent['Attack']} HP. Your HP is now {character['HP']}.")
        else:
            character['Status'] = 'Dead'
            return None

        if foe_run_away(opponent):
            break

    print("You won!")


# Battle helper functions
def guessing_game(is_boss: bool) -> bool or None:
    """
    Play a guessing game to determine damage dealt.

    This function creates a guessing game to determine damage dealt to an opponent.
    If the opponent is not the final boss, three options are presented.
    If the opponent is the final boss, only two options are presented.

    :param is_boss: a boolean
    :precondition: is_boss must be a boolean
    :postcondition: creates a guessing game and determine the attack damage
    :return: None if user chooses not to guess;
             True if user guesses correctly; False if user guesses wrong
    """
    if not is_boss:
        shortcut = ['L', 'R', 'N']

        print("Where will your opponent move? Enter a letter.\n"
              "\t[L]eft\t[R]ight\t[N]ot guessing")
    else:
        shortcut = ['L', 'R']

        print("Where will your opponent move? Enter a letter.\n"
              "\t[L]eft\t[R]ight")

    guess = input().title()

    if guess not in shortcut:
        print('Invalid guess.')
        guess = input().title()

    if guess == 'N':
        return None
    else:
        opponent_move = random.choice(shortcut)
        return opponent_move == guess


def calculate_attack_point(character: dict, guess_result: bool or None) -> int:
    """
    Calculate the attack damage.

    :param character: a dictionary
    :param guess_result: a boolean or None
    :precondition: character must be a dictionary with the key 'Attack', the value of which is a positive integer
    :precondition: guess_result must be True, False, or None
    :return: the damage dealt based on guess_result

    >>> test_character = {'Attack': 10}
    >>> calculate_attack_point(test_character, None)
    10

    >>> test_character = {'Attack': 10}
    >>> calculate_attack_point(test_character, True)
    You guess correctly!
    12

    >>> test_character = {'Attack': 10}
    >>> calculate_attack_point(test_character, False)
    Your guess is incorrect.
    8
    """
    if guess_result is None:
        return character['Attack']
    elif guess_result:
        print("You guess correctly!")
        return int(character['Attack'] * 1.2)
    else:
        print("Your guess is incorrect.")
        return int(character['Attack'] * 0.8)


def foe_run_away(foe: dict) -> bool:
    """
    Determine if a foe wants to run away from battle.

    :param foe: a dictionary
    :precondition: foe must be a dictionary with the key 'Name'
    :postcondition: foe has 20% chance of running away
    :return: True if foe runs away, False if foe doesn't run away
    """
    chance = random.randint(1, 5)

    if chance == 1:
        print(f"\n{foe['Name']} runs away.")
        return True

    return False


# Leveling system
def gain_experience(character: dict) -> None:
    """
    Increase character's experience point.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'Experience'
    :precondition: the value of 'Status' must be a positive integer
    :postcondition: randomizes a experience point and increases character's experience
    """
    experience_point = random.randint(300, 500)
    character["Experience"] += experience_point

    print(f"You receive {experience_point} EXP.")
    time.sleep(2)


def check_character_level(character: dict) -> bool:
    """
    Check if a character is eligible to level up.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Level' and 'Experience'
    :postcondition: checks character's 'Experience' and decides if character can level up

    >>> test_character = {'Level': 1, 'Experience': 1030}
    >>> check_character_level(test_character)
    True

    >>> test_character = {'Level': 2, 'Experience': 2000}
    >>> check_character_level(test_character)
    True

    >>> test_character = {'Level': 2, 'Experience': 1999}
    >>> check_character_level(test_character)
    False
    """
    experience_each_level = [1000, 1000, 1500]
    total_experience_needed = list(itertools.accumulate(experience_each_level))

    level_up = False

    for level, total_experience in enumerate(total_experience_needed, 1):
        if character['Level'] == level and character['Experience'] >= total_experience:
            level_up = True

    return level_up


def update_character_level(character: dict) -> None:
    """
    Level up a character and update their stat.

    :param character: a dictionary
    :precondition: character must be a dictionary with the keys 'Level', 'Attack', 'HP', and 'Max HP'
    :postcondition: increase 'Level' by one
    :postcondition: increase 'Attack', 'HP', and 'Max HP' based on level up base.

    >>> test_character = {'Level': 1, 'Attack': 120, 'HP': 300, 'Max HP': 320}
    >>> update_character_level(test_character)
    <BLANKLINE>
    You reached level 2! You became stronger.
    Your attack is now 180. Your max HP is now 480.
    >>> test_character
    {'Level': 2, 'Attack': 180, 'HP': 460, 'Max HP': 480}
    """
    character['Level'] += 1

    character['Attack'] = int(character['Attack'] * LEVEL_UP_BASE)

    hp_increase = int(character['Max HP'] * (LEVEL_UP_BASE - 1))
    character['HP'] += hp_increase
    character['Max HP'] = int(character['Max HP'] * LEVEL_UP_BASE)

    print(f"\nYou reached level {character['Level']}! You became stronger.\n"
          f"Your attack is now {character['Attack']}. Your max HP is now {character['Max HP']}.")
    time.sleep(5)


# Ending scene
def ending_scene(character: dict) -> None:
    """
    Generate an ending scene based on character's status.

    :param character: a dictionary
    :precondition: character must be a dictionary with the key 'Status'
    :precondition: the value of 'Status' must be a string
    :postcondition: prints a winning scene if 'Status' is 'Win' and losing scene if 'Status' is 'Dead'
    """
    # Winning scene
    if character["Status"] == 'Win':
        print("\nYou defeated the Dark King.\n")
        time.sleep(2)
        print("Congratulations! You won!\n"
              "The Dark Force withers away. You had saved Yggdra.\n\n"
              "\t████░██░██░░▄███▄░░██▄░██░██░▄██\n"
              "\t░██░░██▄██░██▀░▀██░███▄██░████▀░\n"
              "\t░██░░██▀██░███████░██▀███░████▄░\n"
              "\t░██░░██░██░██░░░██░██░░██░██░▀██\n\n"
              "\t██▄░░▄██░░▄███▄░░██░░██░░\n"
              "\t░▀████▀░░██▀░▀██░██░░██░░\n"
              "\t░░░██░░░░██▄░▄██░██░░██░░\n"
              "\t░░░██░░░░░▀███▀░░▀████▀░░")
    # Losing scene
    elif character["Status"] == "Dead":
        print("\nYour HP falls below 0. You died.\n")
        time.sleep(3)
        print("\t███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀\n"
              "\t██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼\n"
              "\t██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀\n"
              "\t██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼\n"
              "\t███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄\n\n"
              "\t███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼\n"
              "\t██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼\n"
              "\t██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼\n"
              "\t██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼\n"
              "\t███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄")


# Game
def game() -> None:
    """
    Drive the game.
    """
    # Introduction
    introduction()
    player = ask_for_player_information()
    class_decision(player)
    generate_class_stat(player)

    gameplay_training(player)
    board = generate_game_board()

    # Game loop
    while player["Status"] == 'Alive':
        print_map(board, player)
        compass(player)
        movement = get_user_move()

        if movement == "Quit":
            print("You quit the game.")
            break

        valid_move = validate_move(board, player, movement)
        if valid_move:
            move_character(player, movement)
            describe_current_location(board, player)

            there_is_a_challenger = check_for_foes(player)
            if player['Experience'] > 0 and there_is_a_challenger:  # Training ends
                print("You meet a challenger.")
                time.sleep(1)

                fight_foe = battle_decision(player)  # Choose to fight or run
                if fight_foe:
                    challenger = create_opponent(player)
                    battle(player, challenger)

                    if player["Status"] == "Dead":
                        break

                    gain_experience(player)

                    if check_character_level(player):
                        update_character_level(player)

                describe_current_location(board, player)
        else:
            print("\nIt's a dead end. You can't go there.\n")

    ending_scene(player)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
