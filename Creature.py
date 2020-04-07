from WorldObj import WorldObj

class Creature(WorldObj):

    def __init__(self, xPos, yPos, pChar, pCol, description):
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description)

    def MoveTowards(self, target):
        if (self.localX == target.localX and self.localY == target.localY):
            return

        if (self.localX > target.localX):
            self.localX -= 1
        elif (self.localX < target.localX):
            self.localX += 1

        if (self.localY > target.localY):
            self.localY -= 1
        elif (self.localY < target.localY):
            self.localY += 1
