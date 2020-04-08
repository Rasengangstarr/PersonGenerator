import State

class WorldObj:
    
    def __init__(self, xPos, yPos, pChar, pCol, description, shortDesc, holdable):
        self.xPos = xPos
        self.yPos = yPos
        self.pChar = pChar
        self.pCol = pCol
        self.description = description
        self.shortDesc = shortDesc
        self.history = []
        self.holdable = holdable
        self.holding = []
        self.hasActed = False

    def Act(self):
        self.hasActed = True

    def ExaminationText(self):
        return ["an unremarkable object"]
