import os
import random
from asciimatics.screen import Screen
from Person import Person
from Food import Food
from State import People
from State import Foods
from time import sleep

userInput = 0

for i in range(0,50):
    People.append(Person())

for i in range (0,200):
    Foods.append(Food())

for p in People:
    print(p.description)

    
def draw(screen):
    boardX = 0
    boardY = 0
   
    while True:
        screen.clear()
        for p in People:
            p.Act()
            if (boardX+p.localX < screen.width and boardY+p.localY < screen.height):
                screen.print_at('\u263A',
                            boardX+p.localX, boardY+p.localY,
                            colour=7,
                            bg=0)
        for f in Foods:
            if (boardX+f.localX < screen.width and boardY+f.localY < screen.height):
                screen.print_at('f',
                            boardX+f.localX, boardY+f.localY,
                            colour=3,
                            bg=0)
        
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
        sleep(0.5)
        

Screen.wrapper(draw)
