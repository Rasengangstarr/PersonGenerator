import math

class PersonNeed:
    def __init__(self, initialValue, increaseFactor, adjectives, moodMod):
        self.value = initialValue
        self.adjectives = adjectives
        self.increaseFactor = increaseFactor
        self.moodMod = moodMod

    def GetNeedAdjective(self):
        return self.adjectives[math.ceil((len(self.adjectives) * self.value))-1]

    def Increment(self):
        self.value += self.increaseFactor