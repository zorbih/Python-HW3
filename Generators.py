from Grid import Point
from Classes import Zombie

# This function generates a list of all coordinate pairs for the board.
def generate_point_list():
    list = []
    for x in range(5):
        for y in range(5):
            list.append(Point(x, y))
    return list

def generate_enemy_list():
    list = []
    for x in range(4):
        list.append(Zombie())
    return list
