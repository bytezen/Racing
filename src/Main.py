'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
import qualify


    
    
def race():
    print '''
    Welcome to another exciting Race Day!
    
    Today's Qualifying  at Atlanta Speedway features:
    
    #48 Jimmy Johnson      #24 Jeff Gordon
    #07 Clint Bowyer       #17 Matt Kenseth
    #5 Kyle Busch          #20 Tony Stewart
    #2 Kurt Busch          #31 Jeff Burton
    '''

def getQualifyRollCountForTrack(type):
    return 3
    pass


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


class Track(object):
    '''
    classdocs
    '''


    def __init__(self, name, type, laps, pits, pitWindows, rolls):
        '''
        Constructor
        '''
        self.name = name
        self.type = type
        self.laps = laps
        self.pitCount = pits
        self.pitWindow = pitWindows
        self.rolls = rolls


        
class Driver(object):
    '''
    classdocs
    '''


    def __init__(self,name, number, overall, quality, trouble, trackRatings = {}):
        '''
        Constructor
        '''
        self.name = name
        self.number = number
        self.overallRating = overall
        self.qualityRating = quality
        self.troubleRating = trouble
        self.trackRatings = trackRatings
        
        
                
            

if __name__ == '__main__':
    race()
    
    atlanta = Track("Atlanta Motor Speedway", "speed", 20, 2, 8, 1)
    racer = range(8)
    
    racer[0] = Driver("Jimmy Johnson",'48',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'A','road':'A'})
    racer[1] = Driver("Jeff Gordon",'24',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'A','road':'A'})    
    racer[2] = Driver("Clint Bowyer",'07',  'A', 'B', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'B','road':'A'})
    racer[3] = Driver("Matt Kenseth",'17',  'A', 'B', 'B', trackRatings = {'speed':'A' , 'short':'A', 'super':'B','road':'C'})                
    racer[4] = Driver("Kyle Busch",'5',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'C','road':'A'})
    racer[5] = Driver("Tony Stewart",'20',  'A', 'B', 'B', trackRatings = {'speed':'A' , 'short':'A', 'super':'D','road':'A'})
    racer[6] = Driver("Kurt Busch",'2',  'A', 'A', 'A', trackRatings = {'speed':'B' , 'short':'B', 'super':'A','road':'B'})
    racer[7] = Driver("Jeff Burton",'31',  'A', 'B', 'A', trackRatings = {'speed':'A' , 'short':'B', 'super':'C','road':'C'})
    
    track = atlanta
    qualRollCount = getQualifyRollCountForTrack( track.type )
    print qualRollCount
    
         
    #begin race
    
    #select a track
    #select drivers
    #qualify drivers
    
    pass