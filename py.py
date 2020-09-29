import pygame, sys
from pygame.locals import *
from math import pi
pygame.init()

#create a new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((300,300))
pygame.display.set_caption('My First Game')

pygame.draw.circle(DISPLAYSURF, (0,255,0), [100,50], 30, 1)
pygame.draw.arc(DISPLAYSURF, (0,255,0), [90, 125, 210, 75], 190, 270, 1)
pygame.draw.circle(DISPLAYSURF, (0,255,0), [200,50], 30, 1)
#pygame.draw.circle(DISPLAYSURF, (0,255,0), [100,50], 30, 1)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
