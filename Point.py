# Point.py by Andrew Sosa

# Class containing x and y coordinate for coordinates on the grid.
class Point():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "[" + str(self.x) +", " + str(self.y) + "]"
