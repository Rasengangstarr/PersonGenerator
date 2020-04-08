import random
from WorldObj import WorldObj

leafTypes = ["very broad", "broad", "narrow", "needle like"]
leafColors = ["red", "green", "purple", "yellow", "blue"]
heights = ["short", "medium height", "tall", "gigantic"]
types = ["bush", "grass", "flower", "tree"]

class Plant(WorldObj):

    def __init__(self, xPos, yPos):
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description)
