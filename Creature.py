from WorldObj import WorldObj
from State import WorldSize
from State import World
import math

class Creature(WorldObj):

    def __init__(self, xPos, yPos, pChar, pCol, description, sightRange, shortDesc):
        self.knownObjects = []
        self.sightRange = sightRange
        self.perception = 8
        self.seeking = None
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description, shortDesc)
        
    def MoveTowards(self, target):
        if (self.xPos == target.xPos and self.yPos == target.yPos):
            return

        if (self.xPos > target.xPos):
            self.xPos -= 1
        elif (self.xPos < target.xPos):
            self.xPos += 1

        if (self.yPos > target.yPos):
            self.yPos -= 1
        elif (self.yPos < target.yPos):
            self.yPos += 1


    def Look(self):
        minX = self.xPos - math.floor(self.sightRange)
        maxX = self.xPos + math.floor(self.sightRange)
        minY = self.yPos - math.floor(self.sightRange)
        maxY = self.yPos + math.floor(self.sightRange)
        for x in range (minX, maxX):
            for y in range (minY, maxY):
                if x >= 0 and y >= 0 and x < WorldSize and y < WorldSize:
                    dist = (((self.xPos - x)**2) + ((self.yPos - y)**2)) ** 0.5
                    if dist <= self.sightRange:
                        if World[x][y] is not None:
                            for o in World[x][y]:
                                #TODO Perception logic could go here
                                if (o in self.knownObjects):
                                    self.knownObjects.remove(o)
                                self.knownObjects.append(o)

    def ExaminationText(self):
        ex = ["this creature knows about:"]
        #ex.append(self.knownObjects)
        for k in self.knownObjects:
            ex.append(k.shortDesc)
        return ex                    

