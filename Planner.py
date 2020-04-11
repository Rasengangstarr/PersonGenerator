from State import World
from Plant import Plant
from Food import Food

actionPaths = [
    "agentKnowsAboutPlant=>agentTargetsPlant=>agentHasPlantTargetted",
    "agentHasPlantTargetted=>agentMovesToTargetPlant=>agentAtTargetPlant",
    "agentTargetGone=>RESET",
    "agentAtTargetPlant=>agentDestroysTargetPlant=>agentKnowsAboutFood",
    "agentKnowsAboutFood=>agentTargetsFood=>agentHasFoodTargetted",
    "agentHasFoodTargetted=>agentMovesToTargetFood=>agentAtTargetFood",
    "agentAtTargetFood=>agentPicksUpFood=>agentHasFood",
    "agentHasFood=>agentEatsFood=>[AGENTHUNGERDECREASED]"
    # "agentKnowsAboutAnimal=>agentTargetsAnimal=>agentHasAnimalTargetted",
    # "agentHasAnimalTargetted=>agentMovesToTargetAnimal=>agentAtTargetAnimal",
    # "agentAtTargetAnimal=>agentKillsTargetAnimal=>agentKnowsAboutFood",
]


def Act(action, 
creature):
    if action == "agentTargetsPlant":
        creature.target = creature.FindObjectOfType(plant)
    elif action == "agentMovesToTargetPlant":
        creature.MoveTowards(creature.target)
    elif action == "agentDestroysTargetPlant":
        creature.target.Destroyed()
    elif action == "agentTargetsFood":
        creature.target = creature.FindObjectOfType(Food)
    elif action == "agentMovesToTargetFood":
        creature.MoveTowards(creature.target)
    elif action == "agentPicksUpFood":
        creature.holding.append(creature.target)
        creature.target.Destroyed()
    elif action == "agentEatsFood":
        for o in creature.holding():
            if isinstance(o, Food):
                creature.holding.remove(0)
                break
        
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

def FindLeafNodes(node, prereqs):
    if node.goal in prereqs:
        if prereqs[node.goal] == True:
            leafNodes.append(node)
            return

    for n in node.children:
        FindLeafNodes(n, prereqs)

def ClimbTree(node, path, goal):
    if node.goal == goal:
        return path

    for n in nodes:
        if n.goal == node.parentGoal:
            path += "=>" + node.action
            return ClimbTree(n, path, goal)

nodes = []


def CalculatePlan(goal, finalAction, creature):

    prereqs = {
        "agentKnowsAboutPlant" : any(isinstance(o, Plant) for o in creature.knownObjects),
        "agentHasPlantTargetted" : isinstance(creature.target, Plant),
        "agentAtTargetPlant" : isinstance(creature.target, Plant) and creature.xPos == creature.target.xPos and creature.yPos == creature.target.yPos,
        "agentKnowsAboutFood" : any(isinstance(o, Food) for o in creature.knownObjects),
        "agentHasFoodTargetted" : isinstance(creature.target, Plant),
        "agentAtTargetFood" :  isinstance(creature.target, Plant) and creature.xPos == creature.target.xPos and creature.yPos == creature.target.yPos,
        "agentHasFood" : any(isinstance(o, Food) for o in creature.holding),
        "agentTargetGone" : False,
        "agentKnowsAboutAnimal" : False,
        "agentHasAnimalTargetted" : False,
        "agentAtTargetAnimal" : False,
    }

    goalNode = Node(goal, None, finalAction)
    nodes = [goalNode]
    BuildPathTree(goalNode)
    FindLeafNodes(goalNode, prereqs)

    print (leafNodes[0].goal)

    for l in leafNodes:
        lpath = ClimbTree(l,"", goal)
        if lpath is not None:
            Act(lpath.split('=>')[1], creature)
    
