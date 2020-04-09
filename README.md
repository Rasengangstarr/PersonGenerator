# WorldSim
A vacation project - aiming to create a framework for dwarf fortress inspired world simulation.

Controls:
wasd - move cursor
p - pause simulation
e - examine

Goal Oriented Action Planner:

Actions profiles:

* incidental effect - effect caused by action interaction with world
[] goal state

agentKnowsAboutPlant => agentTargetsPlant => agentHasPlantTargetted
agentHasPlantTargetted => agentMovesToTargetPlant => agentAtTargetPlant || agentTargetGone
agentTargetGone => RESET
agentAtTargetPlant => agentDestroysTargetPlant => agentKnowsAboutFood || RESET
agentKnowsAboutFood => agentTargetsFood => AgentHasFoodTargetted
agentHasFoodTargetted => agentMovesToTargetFood => agentAtTargetFood || agentTargetGone
agentAtTargetFood => agentPicksUpFood => agentHasFood
agentHasFood => agentEatsFood => [AGENTHUNGERDECREASED]
