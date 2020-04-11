import random
from Food import Food
from WorldObj import WorldObj

leafTypes = ["very broad", "broad", "narrow", "needle like"]
leafColors = ["red", "green", "purple", "yellow", "blue"]
heights = ["short", "medium height", "tall", "gigantic"]
types = ["bush", "grass", "flower", "tree"]

class Plant(WorldObj):

    def __init__(self, xPos, yPos):
        self.holding = [Food(0,0)]
        pChar = 'P'
        pCol = 5
        description = "an edible"
        shortdesc = "a plant"
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description, shortdesc, True)
