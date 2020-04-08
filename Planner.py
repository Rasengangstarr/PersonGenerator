from State import World
from Plant import Plant

class Goal():
    def __init__(self):
        self.prereqs =	{
            "agentHasPlantTargetted": false,
            
            }
        
class Action():
    def __init__(self, prereqs, effects, cost, goal):
        self.prereqs = prereqs
        self.effects = effects
        self.cost = cost
        self.goal = goal
    
    def calcPrereqs():
        pass

    def calcEffects():
        pass

    def Do():
        pass

class TargetsPlantAction(Action):
    def __init__(self, creature, goal):
        self.creature = creature
        cost = 0
        effects = [targetsPlant]
        prereqs = [knowsAboutAPlantPrereq]
        Action.__init__(self, prereqs, effects, cost, goal)

    def knowsAboutAPlantPrereq():
        return any(isinstance(o, Plant) for o in self.creature.knownObjects)

    def targetsPlantEffect():
        self.creature.target = self.creature.FindObjectOfType(self.creature, Plant)

class MoveTowardsPlantAction(Action):
    def __init__(self, creature):
        self.creature = creature
        cost = 0
        effects = [targetsPlant]
        prereqs = [knowsAboutAPlantPrereq]
        Action.__init__(self, prereqs, effects, cost, goal)

    def hasPlantTargettedPrereq():
        return any(isinstance(o, Plant) for o in self.creature.knownObjects)

    def targetsPlant():
        self.creature.target = self.creature.FindObjectOfType(self.creature, Plant)

    