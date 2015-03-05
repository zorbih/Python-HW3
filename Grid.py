# Grid.py by Andrew Sosa

from Values import Values
from random import randint
from random import shuffle
from Point import Point
from Classes import Zombie
from Generators import generate_enemy_list
from Generators import generate_point_list

class Grid():

    def assign_tile(self, value):
        p = self.point_set.pop()
        self.board[p.x][p.y] = value
        return p

    def __init__(self):
        # Initialize board to empties
        self.board = [[Values.EMPTY for x in range(5)] for x in range(5)]

        # List of my things
        self.enemy_list = generate_enemy_list()
        self.point_set = generate_point_list()
        shuffle(self.point_set)

        # Randomly assign entities to the board
        self.assign_tile(Values.GOAL)
        self.assign_tile(Values.DEATH)
        self.start_pos = self.assign_tile(Values.START)

        # Spawn 4 monsters
        for x in range(4):
            self.assign_tile(Values.ENEMY)

        # Spawn 1 Health
        self.assign_tile(Values.HEALTH)

    def has_enemy(self, pos):
        return self.board[pos.x][pos.y] == Values.ENEMY

    def has_death(self, pos):
        return self.board[pos.x][pos.y] == Values.DEATH

    def has_health(self, pos):
        return self.board[pos.x][pos.y] == Values.HEALTH

    def has_goal(self, pos):
        return self.board[pos.x][pos.y] == Values.GOAL

    def check_tile(self, pos):
        if self.has_death(pos):
            return Values.DEATH_MESSAGE
        elif self.has_goal(pos):
            return Values.GOAL_MESSAGE
        elif self.has_enemy(pos):
            return Values.ENEMY_MESSAGE
        elif self.has_health(pos):
            return Values.HEALTH_MESSAGE
        else:
            return Values.EMPTY_MESSAGE
