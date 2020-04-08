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


for p in range(0,1):
    x = 0
    y = 0
    while any(isinstance(o, WorldObj) for o in World[x][y]):
        x = random.randint(0,WorldSize-1)
        y = random.randint(0,WorldSize-1)
    World[x][y].append(Person(x,y))

for f in range(0,1):
    x = 0
    y = 0
    while any(isinstance(o, WorldObj) for o in World[x][y]):
        x = random.randint(0,WorldSize-1)
        y = random.randint(0,WorldSize-1)
    World[x][y].append(Food(x,y))

    
def draw(screen):
    cursorX = 0
    cursorY = 0
    paused = False
    while True:
        screen.clear()
        for x in range(0, WorldSize-1):
            for y in range(0, WorldSize-1):
                for o in World[x][y]:
                    if not paused:
                        o.Act()

        screen.print_at('X',
                    cursorX, cursorY,
                    colour=2,
                    bg=0)
        
        
        #TODO: find a more efficient way of doing this
        for x in range(0, WorldSize-1):
            for y in range(0, WorldSize-1):
                for o in World[x][y]:
                    o.hasActed = False
                    screen.print_at(o.pChar,
                            x, y,
                            colour=o.pCol,
                            bg=0)


        

              
        
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return

        if ev == ord('e'):
            if len(World[cursorX][cursorY]) > 0:
                o = World[cursorX][cursorY][0]
                screen.clear()
                myY = 0
                for t in o.ExaminationText():
                    screen.print_at(t,
                                    0, myY,
                                    colour=7,
                                    bg=0)
                    myY+=1
                screen.refresh()
                screen.wait_for_input(20)

        if ev == ord('p'):
            paused = not paused

        if ev == ord('a'):
            cursorX -= 1
        if ev == ord('d'):
            cursorX += 1
        if ev == ord('w'):
            cursorY -= 1
        if ev == ord('s'):
            cursorY += 1
        
        screen.refresh()
        sleep(0.2)
        

Screen.wrapper(draw)
