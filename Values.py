# Values.py by Andrew Sosa

class Values:
    #Board Values
    EMPTY = 0
    START = 1
    ENEMY = 2
    GOAL = 3
    DEATH = 4
    HEALTH = 5

    NORTH = 10
    EAST = 11
    SOUTH = 12
    WEST = 13

    # Navigation Messages
    MOVE = "You traveled {}."
    WALL = "You can not travel any further {}."
    DEATH_MESSAGE = "You were blown up by a Creeper."
    HEALTH_MESSAGE = "You founds some Bread in a chest."
    ENEMY_MESSAGE = "You encountered a Zombie!"
    GOAL_MESSAGE = "You found the Diamonds!"
    EMPTY_MESSAGE = "This section of the cave is empty."
    NO_GO = "You can not flee from this fight!"

    # Controller .
    INTRO = """
Welcome to Textcraft! A text based Minecraft clone.
Your goal is to find the diamonds! Beware of Creepers
and Zombies. You may also find bread. Good luck! \n\n"""
    #PROMPT = "What would you like to do? "
    PROMPT = "> "
    CHECK_HEALTH = "{} has {} health points left."
