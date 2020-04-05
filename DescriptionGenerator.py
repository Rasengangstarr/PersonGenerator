import random

maleFirstnames = ["David", "William", "Matthew", "Mark", "Luke", "John"]
femaleFirstnames = ["Charlotte", "Mary", "Alison", "Caroline", "Chloe", "Scarlet"]

adjectives = ["Big", "Small", "Red", "Blue", "Grey", "Stoic", "Strong", "Weak"]
nouns = ["fox", "shield", "wall", "brick", "spear", "bear"]

heights = ["short", "very short", "average height", "tall", "very tall"]
builds = ["skeletally thin", "thin", "muscular", "very muscular", "chubby", "fat", "obese"]
hairstyles = ["buzzcut", "wavy", "afro", "bowlcut", "braided"]
haircolours = ["brown", "white", "red", "auburn", "blonde"]
beardTypes = ["scruffy", "braided", "short", "whispy"]
noseTypes = ["long", "flat", "straight", "curved"]
eyeTypes = ["squinty", "wide", "deep", "blank"]
eyeColors = ["blue", "green", "brown", "yellow", "bluey-green"]
chinTypes = ["strong", "receding", "protruding", "bum", "small"]
teethTypes = ["crooked", "mangled", "gone", "shining white", "white", "yellow"]
skinColors = ["pale white", "fair", "tanned", "dark", "yellow", "reddish", "brown", "pitch black"]
complexions = ["dry", "greasy", "healthy"]

outgoingAdjs = ["shy", "outgoing"]
hardworkingAdjs = ["lazy", "hardworking"]
intelligentAdjs = ["stupid", "intelligent"]
quickAdjs = ["sluggish", "quick"]
strongAdjs = ["physically weak", "physically strong"]
attactiveAdjs = ["ugly", "beautiful"]
spiritualAdjs = ["irreligious", "pious"]
  

class Person:
    def __init__(self):
        self.gender = random.randint(0,1)
        if (self.gender == 0):
            self.firstname = random.choice(maleFirstnames)
        else:
            self.firstname = random.choice(femaleFirstnames)
        self.surname = random.choice(adjectives) + random.choice(nouns)
        self.height = random.choice(heights)
        self.build = random.choice(builds)
        self.hairstyle = random.choice(hairstyles)
        self.haircolour = random.choice(haircolours)
        if (self.gender == 0):
            self.beardType = random.choice(beardTypes)
        else:
            self.beardType = None
        self.noseType = random.choice(noseTypes)
        self.eyeType = random.choice(eyeTypes)
        self.eyeColor = random.choice(eyeColors)
        self.chinType = random.choice(chinTypes)
        self.teethType = random.choice(teethTypes)
        self.skinColor = random.choice(skinColors)
        self.complexion = random.choice(complexions)

        self.outgoing = random.randint(0,10)
        self.hardworking = random.randint(0,10)
        self.intelligent = random.randint(0,10)
        self.quick = random.randint(0,10)
        self.strong = random.randint(0,10)
        self.attractive = random.randint(0,10)
        self.spiritual = random.randint(0,10)

        self.description = self.GenerateDescription()

   

    def GenerateDescription(self):
        if (self.gender == 0):
            pronoun = "He"
            posessivePronoun = "His"
        else:
            pronoun = "She"
            posessivePronoun = "Her"
        clauses = []
        clauses.append(pronoun + " is " + self.height + " and has a " + self.build + " build. ")
        clauses.append(pronoun + " has " + self.haircolour + " " + self.hairstyle + " hair. ")
        if (self.beardType is not None):
            clauses.append(pronoun + " has a " + self.beardType + " beard. ")  

        clauses.append(posessivePronoun + " nose is " + self.noseType + ". ")
        clauses.append(posessivePronoun + " " + self.eyeColor + " eyes are " + self.eyeType + ". ")
        clauses.append(posessivePronoun + " teeth are " + self.teethType + " and " + pronoun.lower() + " has a " + self.chinType + " chin. ")
        clauses.append(posessivePronoun + " " + self.complexion + " skin is " + self.skinColor + ". ")
       
        clauses.append(GenerateTraitDescription(outgoingAdjs, self.outgoing, pronoun))
        clauses.append(GenerateTraitDescription(hardworkingAdjs, self.hardworking, pronoun))
        clauses.append(GenerateTraitDescription(intelligentAdjs, self.intelligent, pronoun))
        clauses.append(GenerateTraitDescription(quickAdjs, self.quick, pronoun))
        clauses.append(GenerateTraitDescription(strongAdjs, self.strong, pronoun))
        clauses.append(GenerateTraitDescription(attactiveAdjs, self.attractive, pronoun))
        clauses.append(GenerateTraitDescription(spiritualAdjs, self.spiritual, pronoun))

        random.shuffle(clauses)

        description = self.firstname + " " + self.surname + "\n"

        for i in clauses:
            description += i
        
        return description

def NumToWord(quantity):
    if (quantity < 1 or quantity > 9):
        return "extremely"
    elif(quantity < 2 or quantity > 8 ):
        return "very"
    elif(quantity < 3 or quantity > 7 ):
        return "notably"
    else:
        return ""

def GenerateTraitDescription(adjList, trait, pronoun):
    if (NumToWord(trait) != ""):
        if (trait <= 5):
            descriptor = adjList[0]
        else:
            descriptor = adjList[1]
        return pronoun + " is " + NumToWord(trait) + " " + descriptor + ". "
    else:
        return ""


p1 = Person()
print(p1.description)
