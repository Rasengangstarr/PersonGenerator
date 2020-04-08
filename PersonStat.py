import math

class PersonStat:
    def __init__(self, initialValue, adjectives):
        self.value = initialValue
        self.adjectives = adjectives
        self.description =  self.GetStatAdjective()

    def GetStatAdjective(self):
        if self.value == 0:
            return self.adjectives[0]
        return self.adjectives[math.ceil((len(self.adjectives) * self.value))-1]