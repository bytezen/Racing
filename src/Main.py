'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
import qualify
import Track



def _initializeGame():
    atlanta = Track("Atlanta Motor Speedway", "speed", 20, 2, 8, 1)
    
    

def race():
    print '''
    Welcome to another exciting Race Day!
    
    Today's Race features:
    
    #48 Jimmy Johnson      #24 Jeff Gordon
    #07 Clint Bowyer       #17 Matt Kenseth
    #5 Kyle Busch          #20 Tony Stewart
    #2 Kurt Busch          #31 Jeff Burton
    '''

    print '''
    Choose a race track:
    
    1 Atlanta
    '''

    
            
        


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
    _initializeGame()
    
    #begin race
    race()
    #select a track
    #select drivers
    #qualify drivers
    
    pass