'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
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
    
            

if __name__ == '__main__':
    pass