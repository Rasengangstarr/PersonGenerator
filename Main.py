import os
import random
from asciimatics.screen import Screen
from Person import Person
from WorldObj import WorldObj
from Food import Food
from State import People
from State import Foods
from State import World
from State import WorldSize
from time import sleep

userInput = 0

objsCreated = 0

for p in range(0,3):
    x = 0
    y = 0
    while any(isinstance(o, WorldObj) for o in World[x][y]):
        x = random.randint(0,WorldSize-1)
        y = random.randint(0,WorldSize-1)
    World[x][y].append(Person(x,y))
    objsCreated += 1

for p in range(0,2):
    x = 0
    y = 0
    while any(isinstance(o, WorldObj) for o in World[x][y]):
        x = random.randint(0,WorldSize-1)
        y = random.randint(0,WorldSize-1)
    World[x][y].append(Food(x,y))
    objsCreated += 1

# for i in range (0,200):
#     Foods.append(Food())

# for p in People:
#     print(p.description)

    
def draw(screen):
    boardX = 0
    boardY = 0
   
    while True:
        screen.clear()
        for x in range(0, WorldSize-1):
            for y in range(0, WorldSize-1):
                for o in World[x][y]:
                    screen.print_at(o.pChar,
                            x, y,
                            colour=o.pCol,
                            bg=0)
                    o.Act()

              
        
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        if ev in (ord('A'), ord('a')):
            boardX += 1
        if ev in (ord('D'), ord('d')):
            boardX -= 1
        if ev in (ord('W'), ord('w')):
            boardY += 1
        if ev in (ord('S'), ord('s')):
            boardY -= 1
        
        screen.refresh()
        sleep(0.2)
        

Screen.wrapper(draw)
