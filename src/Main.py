'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
import Qualify as q
import random

    
    
def qualify():
    print '''
    Welcome to another exciting Race Day!
    
    Today's Qualifying  at Atlanta Speedway features:
    
    #48 Jimmy Johnson      #24 Jeff Gordon
    #07 Clint Bowyer       #17 Matt Kenseth
    #5 Kyle Busch          #20 Tony Stewart
    #2 Kurt Busch          #31 Jeff Burton
    '''

def race():
    pass




def getQualifyingRollCountForTrack(trackType):
    num_of_rolls = 0
    
    if trackType == "speedway":
        num_of_rolls = 4
    elif trackType == "short":
        num_of_rolls = 3
    elif trackType == "superSpeed":
        num_of_rolls = 5
    elif trackType == "road":
        num_of_rolls = 5                
    
    return num_of_rolls    

def rollDice(sides=100, times=1):
    roll = 0 
    for i in range(times):
        roll = roll + int(random.uniform(0,sides))

    return roll

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

    def __repr__(self):
        return "#%s %s" % (self.number, self.name)        
        
                
            

if __name__ == '__main__':
    q.configureData()
    qualify()
    
    atlanta = Track("Atlanta Motor Speedway", "speedway", 20, 2, 8, 1)
    
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
    qualRollCount = getQualifyingRollCountForTrack( track.type )
    
    
    print "num\tqualify(mph)"
    print "=================\n"
    qualified = {}
    disqualified = {}
    for r in racer:        
        speedRatingTotal = 0
        for i in range(qualRollCount):
            roll = rollDice()
            
            if roll == 99:  # TODO: Implement Trouble
                speedRatingTotal = -1
                break
            sr = q.getSpeedRating(roll, r.qualityRating)
            
            speedRatingTotal = speedRatingTotal + sr
        
        if speedRatingTotal > 0:
            qualifyingAvgSpeed = q.getAverageSpeed( speedRatingTotal, track.type )
            thousands = rollDice() / 1000.
            qualifyingAvgSpeed = qualifyingAvgSpeed + thousands    
            qualified[r.number] = qualifyingAvgSpeed    
        else: # TODO: Implement car trouble
            roll = rollDice(sides=10)
            trouble = q.qualify_trouble_result[roll]
            disqualified[r.number] = trouble
        
            
    qualifying = sorted(qualified.items(), key=lambda x: x[1])
    qualifying.reverse()   

    if len(disqualified) > 0:
        for i in disqualified.items():
            qualifying.append( (i[0],0.0))
    
    for num, mph in qualifying:
        print "#%s\t%.3f" % (num,mph)
    
    if len(disqualified) > 0:
        print "Disqualified:"
        print "+="*10
        for num,dq in disqualified.items():
            print "%s\t%s" % (num,dq)
    
    #
    #
    # Race time!
    #
    
    running_order = []
    for i in qualifying:
        for d in racer:
            if d.number == i[0]:
                running_order.append(d)
    
    
    for l in range(1):
        lap_speeds = []
        for driver in running_order:
            rollTotal = 0
            for r in range(track.rolls):
                roll = rollDice()
                #lookup speed for driver
    
    
    pass