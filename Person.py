import random
from PersonStat import PersonStat

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

        self.stats = {
            "sociability": PersonStat(random.randint(0,10) / 10, ["very shy", "shy", "quite sociable", "very outgoing"]),
            "workethic": PersonStat(random.randint(0,10) / 10, ["very lazy", "lothargic", "quite hardworking", "very industrious"]),
            "speed": PersonStat(random.randint(0,10) / 10, ["sloth-like", "sluggish", "quick", "super speedy"]),
            "strength": PersonStat(random.randint(0,10) / 10, ["weak", "strong"]),
            "trustworthiness": PersonStat(random.randint(0,10) / 10, ["very shady", "shady", "of average trustworthiness", "trustworthy", "truly honourable"]),
            "trustfulness": PersonStat(random.randint(0,10) / 10, ["untrusting to the point of paranoia", "naturally suspicious", "trusting", "overtrusting"])
        }

        self.localX = random.randint(0,100)
        self.localY = random.randint(0,100)

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
       
        for key in self.stats:
            clauses.append(pronoun + " is " + self.stats[key].description + ". ")

        random.shuffle(clauses)

        description = self.firstname + " " + self.surname + "\n"

        for i in clauses:
            description += i
        
        return description
