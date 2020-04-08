from WorldObj import WorldObj
from State import WorldSize
from State import World
import math

class Creature(WorldObj):

    def __init__(self, xPos, yPos, pChar, pCol, description, sightRange, shortDesc, holdable):
        self.knownObjects = []
        self.sightRange = sightRange
        self.perception = 8
        self.seeking = None
        self.target = None
        self.intent = None
        self.goal = None
        WorldObj.__init__(self, xPos, yPos, pChar, pCol, description, shortDesc, holdable)

    def Act(self):
        if self.hasActed:
            return
        if (self.target is not None):
            self.MoveTowards(self.target)
        WorldObj.Act(self)
        
    def MoveTowards(self, target):
        xdir = 0
        ydir = 0
        if (self.xPos == target.xPos and self.yPos == target.yPos):
            return
        if (self.xPos > target.xPos):
            xdir-=1
        elif (self.xPos < target.xPos):
            xdir+=1
        if (self.yPos > target.yPos):
            ydir-=1
        elif (self.yPos < target.yPos):
            ydir+=1

        World[self.xPos][self.yPos].remove(self)
        self.xPos += xdir
        self.yPos += ydir
        World[self.xPos][self.yPos].append(self)

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
    
    def FindObjectOfType(self, soughtType):
        nearestKnownDist = 1000000
        nearestKnown = None
        for o in self.knownObjects:
            if isinstance(o,soughtType):
                dist = (((self.xPos - o.xPos)**2) + ((self.yPos - o.yPos)**2)) ** 0.5
                if dist < nearestKnownDist:
                    nearestKnown = o
                    nearestKnownDist = dist

        return nearestKnown

    def ExaminationText(self):
        ex = ["this creature knows about:"]
        #ex.append(self.knownObjects)
        for k in self.knownObjects:
            ex.append(k.shortDesc)
        return ex                    

