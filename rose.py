import pygame, sys
from pygame.locals import *

pygame.init()

#create a new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((400,400))
pygame.display.set_caption('My First Rose')
#stebel
pygame.draw.rect(DISPLAYSURF, (144, 238, 144), (140,140,20,140))
#lists
pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (60,200,40,40))
pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (100,240,40,40))
pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (100,220,20,20))
pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (80,240,20,20))
#lepestki
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (120,100,60,40))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (100,100,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (180,100,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (80,80,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (200,80,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (100,60,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (180,60,20,20))
pygame.draw.rect(DISPLAYSURF, (139, 0, 0), (120,40,60,20))


pygame.draw.rect(DISPLAYSURF, (220, 20, 60), (120,60,60,40))
pygame.draw.rect(DISPLAYSURF, (220, 20, 60), (180,80,20,20))
pygame.draw.rect(DISPLAYSURF, (220, 20, 60), (100,80,20,20))



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
