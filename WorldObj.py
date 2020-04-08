import State

class WorldObj:
    
    def __init__(self, xPos, yPos, pChar, pCol, description):
        self.xPos = xPos
        self.yPos = yPos
        self.pChar = pChar
        self.pCol = pCol
        self.description = description
        self.history = []

    def Act(self):
        pass
    
    def Move(self, tarXPos, tarYPos):
        State.World[self.xPos][self.yPos].remove(self)
        self.xPos = tarXPos
        self.yPos = tarYPos
        State.World[tarXPos][tarYPos].append(self)

    def ExaminationText(self):
        return ["an unremarkable object"]
