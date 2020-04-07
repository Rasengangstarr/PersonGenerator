import random
from Creature import Creature
from PersonStat import PersonStat
from PersonNeed import PersonNeed
from State import People
from State import Foods

maleFirstnames = ["David", "William", "Matthew", "Mark", "Luke", "John", "Graham", "Wayne", "Ali", "Mo", "Steve"]
femaleFirstnames = ["Charlotte", "Mary", "Alison", "Caroline", "Chloe", "Scarlet", "Elenor", "Amy", "Sarah", "Colette"]

adjectives = ["Big", "Small", "Red", "Blue", "Grey", "Stoic", "Strong", "Weak", "Gay", "Far", "Near", "Stone", "Wood"]
nouns = ["fox", "shield", "wall", "brick", "spear", "bear", "fish", "axe", "pick", "beard", "dick", "son"]

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


class Person(Creature):
    def __init__(self, xPos, yPos):
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

        self.baseStats = {
            "sociability": PersonStat(random.randint(0,10) / 10, ["very shy", "shy", "quite sociable", "very outgoing"]),
            "workethic": PersonStat(random.randint(0,10) / 10, ["very lazy", "lothargic", "quite hardworking", "very industrious"]),
            "speed": PersonStat(random.randint(0,10) / 10, ["sloth-like", "sluggish", "quick", "super speedy"]),
            "strength": PersonStat(random.randint(0,10) / 10, ["weak", "strong"]),
            "trustworthiness": PersonStat(random.randint(0,10) / 10, ["very shady", "shady", "of average trustworthiness", "trustworthy", "truly honourable"]),
            "trustfulness": PersonStat(random.randint(0,10) / 10, ["untrusting to the point of paranoia", "naturally suspicious", "trusting", "overtrusting"])
        }

        self.needs = {
            "hunger": PersonNeed(0, random.randint(0,10) / 100, ["completely full", "sated", "a bit peckish", "ravenous", "starving"], random.randint(0,10) / 10),
            "thirst": PersonNeed(0, random.randint(0,10) / 100, ["not thirsty", "not very thirsty", "kind of thirsty", "parched", "seriously dehydrated"], random.randint(0,10) / 10),
            "sleepiness": PersonNeed(0, random.randint(0,10) / 100, ["wide awake", "awake", "a bit tired", "tired", "knackered"], random.randint(0,10) / 10)
        }

        pChar = '\u263A'
        pCol = 7

        self.description = self.GenerateDescription()

        Creature.__init__(self, xPos, yPos, pChar, pCol, self.description) 

        self.history = []

    def Act(self):
        
        for n in self.needs:
            self.needs[n].Increment()

        if (self.needs["hunger"].value > 0.5 and self.target is None):
            self.history.append("went looking for food")
            self.target = self.LocateFood()
        
        if (self.target is not None):
            self.MoveTowards(self.target)

    def LocateFood(self):
        closestFoodDist = 10000000000
        closestFood = None
        for f in Foods:
            distance = ((self.localX-f.localX)**2 + (self.localY-f.localY)**2) ** 0.5
            if distance < closestFoodDist:
                closestFood = f
                closestFoodDist = distance
        if closestFood is not None:
            return closestFood
        else:
            return None

            

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
       
        for key in self.baseStats:
            clauses.append(pronoun + " is " + self.baseStats[key].description + ". ")

        random.shuffle(clauses)

        description = self.firstname + " " + self.surname + "\n"

        for i in clauses:
            description += i
        
        return description
