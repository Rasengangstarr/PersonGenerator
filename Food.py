import random
from WorldObj import WorldObj

class Food(WorldObj):
    def __init__(self, xPos, yPos):
        pChar = 'f'
        pCol = 4
        description = 'some food'
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description)

    def Act(self):
        return