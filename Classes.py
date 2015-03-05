# Character.py by Andrew Sosa

from Grid import Point
from random import randint
from Values import Values

class Character():
    def __init__(self, hp, strength, defense, name):
        #self.max_health = hp
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.name = name

    def update_health(self, val):
        self.health = self.health + val

    def calc_damage(self, opponent):
        damage = randint(0, 6) + self.strength - opponent.defense
        if damage <= 0:
            print "{0} evades {1}'s attack.".format(opponent.name, self.name)
        else:
            opponent.hp = opponent.hp - damage
            print "{0} attacks {1} for {2} points of damage!".format(
                            self.name, opponent.name, str(damage))

class Zombie(Character):
    def __init__(self):
        Character.__init__(self, 15, 9, 7, "Zombie")
    def attack(self, player):
        print "You were attacked by the Zombie."
        self.calc_damage(player)



def north(player):
    if player.pos.y > 0:
        player.pos.y = player.pos.y - 1
        print Values.MOVE.format("North")
    else:
        print Values.WALL.format("North")
    return player.pos

def east(player):
    if player.pos.x < 4:
        player.pos.x = player.pos.x + 1
        print Values.MOVE.format("East")
    else:
        print Values.WALL.format("East")
    return player.pos


def south(player):
    if player.pos.y < 4:
        player.pos.y = player.pos.y + 1
        print Values.MOVE.format("South")
    else:
        print Values.WALL.format("South")
    return player.pos


def west(player):
    if player.pos.x > 0:
        player.pos.x = player.pos.x - 1
        print Values.MOVE.format("West")
    else:
        print Values.WALL.format("West")
    return player.pos

class Player(Character):

    def __init__(self, hp, strength, defense, pos, name):
        Character.__init__(self, hp, strength, defense, name)
        self.pos = pos
        self.engaged = False

    def help():
        print "\tgo [N, S, E, or W] \n\tquit \n\tattack \n\thealth \n\thelp "

    def health(self):
        print "{} has {} health.".format(self.name, self.health)

    def go(self, direction, board):
        if self.engaged:
            print Values.NO_GO
            return

        print "Traveling {}.".format(direction)

        # Handle movement
        directions = {'N', 'E', 'S', 'W'}
        options = { 'N' : north,
                    'E' : east,
                    'S' : south,
                    'W' : west
        }
        if direction not in directions:
            print "Not a valid direction."
            return
        move = options[direction](self)

        # Check for encounters
        encounter = board.check_tile(self.pos)
        print encounter
        if encounter == Values.ENEMY_MESSAGE:
            self.engaged = True
        else:
            self.engaged = False


    def attack(self, board):
        if board.has_enemy(self.pos):
            print "You swing at the Zombie!"
            self.calc_damage(board.enemy_list[0])
            if board.enemy_list[0].hp < 1:
                print "You killed the Zombie."
                board.enemy_list.pop(0)
                board.board[self.pos.x][self.pos.y] = Values.EMPTY
                self.engaged = False
        else:
            print "No enemy to attack."

    def quit():
        print "Quit stub."

class Alex(Player):
    def __init__(self, board):
        Player.__init__(self, 30, 10, 8, board.start_pos, "Alex")


class Steve(Player):
    def __init__(self, board):
        Player.__init__(self, 30, 8, 10, board.start_pos, "Steve")
