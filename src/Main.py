'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import pygame, sys
from pygame.locals import *
import qualify



def qualify(trackType, qualifyRating):
    return 0


def get_qualifying_rolls(trackType):
    num_of_rolls = 0
    
    if trackType == "speed":
        num_of_rolls = 4
    elif trackType == "short":
        num_of_rolls = 3
    elif trackType == "superSpeed":
        num_of_rolls = 5
    elif trackType == "road":
        num_of_rolls = 5                
    
    return num_of_rolls    
    


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Racing')

#fontObj = pygame.font.Font("freesansbold.ttf",16)
msg = "waiting for an entry"
msgDirty = True

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                msg = "qualifying..."
                print get_qualifying_rolls("short")
                msgDirty = True
            
                
    if msgDirty == True:                
        print msg
        msgDirty = False
           
#    msgSurfaceObj = fontObj.render(msg,False,pygame.Color(0,0,255))
#    msgRectObj = msgSurfaceObj.get_rect()
#    msgRectObj.topleft = (10,20)
#    DISPLAYSURF.blit(msgSurfaceObj, msgRectObj)
    
    pygame.display.update()
            

if __name__ == '__main__':
    pass