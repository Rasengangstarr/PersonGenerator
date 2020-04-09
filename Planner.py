from State import World
from Plant import Plant

# agentKnowsAboutPlant => agentTargetsPlant => agentHasPlantTargetted
# agentHasPlantTargetted => agentMovesToTargetPlant => agentAtTargetPlant || agentTargetGone
# agentTargetGone => RESET
# agentAtTargetPlant => agentDestroysTargetPlant => agentKnowsAboutFood || RESET
# agentKnowsAboutFood => agentTargetsFood => AgentHasFoodTargetted
# agentHasFoodTargetted => agentMovesToTargetFood => agentAtTargetFood || agentTargetGone
# agentAtTargetFood => agentPicksUpFood => agentHasFood
# agentHasFood => agentEatsFood => [AGENTHUNGERDECREASED]

actionPaths = [
    "agentKnowsAboutPlant=>agentTargetsPlant=>agentHasPlantTargetted",
    "agentHasPlantTargetted=>agentMovesToTargetPlant=>agentAtTargetPlant",
    "agentTargetGone=>RESET",
    "agentAtTargetPlant=>agentDestroysTargetPlant=>agentKnowsAboutFood",
    "agentKnowsAboutFood=>agentTargetsFood=>agentHasFoodTargetted",
    "agentHasFoodTargetted=>agentMovesToTargetFood=>agentAtTargetFood",
    "agentAtTargetFood=>agentPicksUpFood=>agentHasFood",
    "agentHasFood=>agentEatsFood=>[AGENTHUNGERDECREASED]",
    "agentKnowsAboutAnimal=>agentTargetsAnimal=>agentHasAnimalTargetted",
    "agentHasAnimalTargetted=>agentMovesToTargetAnimal=>agentAtTargetAnimal",
    "agentAtTargetAnimal=>agentKillsTargetAnimal=>agentKnowsAboutFood",
]

prereqs= {
    "agentKnowsAboutPlant" : True,
    "agentHasPlantTargetted" : False,
    "agentAtTargetPlant" : False,
    "agentKnowsAboutFood" : True,
    "agentHasFoodTargetted" : False,
    "agentAtTargetFood" : False,
    "agentHasFood" : False,
    "agentTargetGone" : False,
    "agentKnowsAboutAnimal" : True,
    "agentHasAnimalTargetted" : False,
    "agentAtTargetAnimal" : False,
}

plans = []

class Node():
    def __init__(self, goal, parentGoal, action):
        self.children = []
        self.goal = goal
        self.parentGoal = parentGoal
        self.action = action

def BuildPathTree(node):

    for a in actionPaths:
        action = a.split('=>')
     
        if action[-1] == node.goal:
            goalFound = True
            myGoal = action[-3]
            nodes.append(Node(myGoal, node.goal, action[-2]))
            node.children.append(Node(myGoal, node.goal, action[-2]))
        
    for n in node.children:
        BuildPathTree(n)

leafNodes = []

def FindLeafNodes(node):
    if node.goal in prereqs:
        if prereqs[node.goal] == True:
            leafNodes.append(node)
            return

    for n in node.children:
        FindLeafNodes(n)

def ClimbTree(node, path, goal):
    if node.goal == goal:
        
        return path
    for n in nodes:
        if n.goal == node.parentGoal:
            path += " => " + node.action
            return ClimbTree(n, path, goal)



goalNode = Node("[AGENTHUNGERDECREASED]", None, "agentEatsFood")

nodes = [goalNode]

BuildPathTree(goalNode)

FindLeafNodes(goalNode)

for n in nodes:
    print (n.goal)

for l in leafNodes:
    lpath = ClimbTree(l,"", "[AGENTHUNGERDECREASED]")
    print(lpath + " => " + "[AGENTHUNGERDECREASED]")
   
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

    