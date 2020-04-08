from WorldObj import WorldObj
from State import WorldSize
from State import World
import math

class Creature(WorldObj):

    def __init__(self, xPos, yPos, pChar, pCol, description, sightRange):
        self.knownObjects = []
        self.sightRange = sightRange
        self.perception = 8
        self.seeking = None
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


    def Look(self):
        minX = self.localX - math.floor(sightRange/2)
        maxX = self.localX + math.floor(sightRange/2)
        minY = self.localY - math.floor(sightRange/2)
        maxY = self.localY + math.floor(sightRange/2)
        for x in range (minX, maxX):
            for y in range (minY, minY):
                if x >= 0 and y >=0 and x <= WorldSize and y <= WorldSize:
                    dist = (((self.localX - x)**2) + ((self.localY - y)**2)) ** 0.5
                    if dist < self.sightRange:
                        for o in World[x][y]:
                            #TODO Perception logic could go here
                            if (o in self.knownObjects):
                                self.knownObjects.remove(o)
                            self.knownObjects.append(o)
                            

