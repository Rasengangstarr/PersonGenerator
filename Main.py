import os
import random
from asciimatics.screen import Screen
from Person import Person

userInput = 0

People = []



for i in range(0,10):
    People.append(Person())
    
def draw(screen):
    boardX = 0
    boardY = 0
   
    while True:
        
        for p in People:
            if (boardX+p.localX < screen.width and boardY+p.localY < screen.height):
                screen.print_at('\u263A',
                            boardX+p.localX, boardY+p.localY,
                            colour=7,
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
        screen.Wipe()
        

Screen.wrapper(draw)
