# Textcraft.py by Andrew Sosa

from Grid import Grid
from Classes import Alex
from Classes import Steve
from Values import Values
import sys


# Get name and Class
#name = raw_input("Please name your character: ")
sys.stdout.write("Please name your character: ")
name = sys.stdin.readline().rstrip()
sys.stdout.write("Oh, I remember now! Your name is " + name + "!\n")
#class_type = raw_input("Would you like to use the Alex or Steve skin model? ").lower()
sys.stdout.write("Would you like to use the Alex or Steve skin model? ")
class_type = sys.stdin.readline().rstrip().lower()
#sys.stdout.write(class_type)

# Choose difficulty
#difficulty = raw_input("Choose your difficulty (Easy, Normal, Hard): ").lower()
sys.stdout.write("Choose your difficulty (Easy, Normal, Hard): ")
difficulty = sys.stdin.readline().rstrip().lower()

if difficulty not in {"easy", "normal", "hard"}:
    difficulty = "normal"

# Initilization
message = Values.INTRO
board = Grid(difficulty)

# Create character
if class_type == "alex":
    player = Alex(board, name)
elif class_type == "steve":
    player = Steve(board, name)
else:
    print "Since you didn't choose one of our class options, we're going to make you Alex."
    player = Alex(board, name)



# Gameplay Loop
while (message != Values.DEATH_MESSAGE) and (message != Values.GOAL_MESSAGE):
    print message
    #command = raw_input(Values.PROMPT)
    sys.stdout.write(Values.PROMPT)
    command = sys.stdin.readline().rstrip()
    command = command.split(" ")

    options = {'go', 'quit', 'attack', 'health', 'help'}
    if command[0] in options:
        if (command[0] == 'go') and (command[1] != None):
            message = player.go(command[1], board)
        elif command[0] == 'quit':
            message = Values.DEATH_MESSAGE
            continue
        elif command[0] == 'attack':
            message = player.attack(board)
        elif command[0] == 'health':
            #message = Values.CHECK_HEALTH.format(player.name, player.hp)
            message = player.health()
            continue
        elif command[0] == 'help':
            #message = Values.HELP_MESSAGE
            message = player.help()
            continue
        else:
            message = "How'd you even get to this else clause?? Seriously??"
    else:
        message = "That's not a valid command."
        continue

    if player.engaged:
        print board.enemy_list[0].attack(player)

    player.check_engage(board, message)

print message
