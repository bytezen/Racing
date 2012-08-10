'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
import Qualify as q
import random
import Track
from Driver import RaceDriver

import Race    
    
def qualify(trackName):
    msg = """
    Welcome to another exciting Race Day!
    
    Today's Qualifying  at {name} features:
    
    #48 Jimmy Johnson      #24 Jeff Gordon
    #07 Clint Bowyer       #17 Matt Kenseth
    #5 Kyle Busch          #20 Tony Stewart
    #2 Kurt Busch          #31 Jeff Burton
    """
    
    print msg.format(name=trackName)

def race():
    pass


def rollDice(sides=100, times=1):
    roll = 0 
    for i in range(times):
        roll = roll + int(random.uniform(0,sides))

    return roll

def initializeDriverForRace(driver, trackType):
    rating = driver.getRatingOnTrack(trackType)
    
    pass


        
            

if __name__ == '__main__':
    q.configureData()
    
    atlanta = Track.Atlanta
    pocono = Track.Pocono
    
    racer = range(8)
    racer[0] = RaceDriver("Jimmy Johnson",'48',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'A','road':'A'})
    racer[1] = RaceDriver("Jeff Gordon",'24',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'A','road':'A'})    
    racer[2] = RaceDriver("Clint Bowyer",'07',  'A', 'B', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'B','road':'A'})
    racer[3] = RaceDriver("Matt Kenseth",'17',  'A', 'B', 'B', trackRatings = {'speed':'A' , 'short':'A', 'super':'B','road':'C'})                
    racer[4] = RaceDriver("Kyle Busch",'5',  'A', 'A', 'A', trackRatings = {'speed':'A' , 'short':'A', 'super':'C','road':'A'})
    racer[5] = RaceDriver("Tony Stewart",'20',  'A', 'B', 'B', trackRatings = {'speed':'A' , 'short':'A', 'super':'D','road':'A'})
    racer[6] = RaceDriver("Kurt Busch",'2',  'A', 'A', 'A', trackRatings = {'speed':'B' , 'short':'B', 'super':'A','road':'B'})
    racer[7] = RaceDriver("Jeff Burton",'31',  'A', 'B', 'A', trackRatings = {'speed':'A' , 'short':'B', 'super':'C','road':'C'})
    
    track = pocono
    qualify( track.name)
    
    for d in racer:
        d.initializeSpeedChart(track.type)
    
    
    print "num\tqualify(mph)"
    print "=================\n"
    qualified = {}
    disqualified = {}
    for r in racer:        
        speedRatingTotal = 0
        for i in range(track.qualifyLaps):
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
    currentLap = 1
    
    for i in qualifying:
        for d in racer:
            if d.number == i[0]:
                running_order.append(d)
    
    
    if currentLap < track.totalLaps:  # Just run for one 1 lap to test; track.laps to run fully
        lap_speeds = {}
        for driver in running_order:
            rollTotal = 0
            for r in range(track.rolls):
                roll = rollDice()
                #lookup speed for driver
                spd = driver.getSpeed(roll)
                if spd < 0:
                    print "Need to implement trouble for drivers"
                    
                rollTotal = rollTotal + spd
                
            lap_speeds[driver] = rollTotal     
            driver.setRaceSpeed( rollTotal ) 
    
        lapOrder = sorted( lap_speeds.items(), key=lambda x: x[1] )
        lapOrder.reverse()
        print "\nLap #",currentLap," results\n", "="*10
        
        for i in lapOrder:
            print "#",i[0].number,"\tspeed = ", i[1]
            

        running_order = sorted( lapOrder, key = lambda x : x[0].raceSpeed )
        running_order.reverse()
        print "\nRACE STANDINGS", "=+="*10        
        print running_order
            
        currentLap = currentLap +1
            
            
            
            
    pass