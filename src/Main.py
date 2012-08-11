'''
Created on Jul 29, 2012

@author: rhazesspell
'''
import sys
import Qualify as q
import random
import Track
from Driver import *

from Race import *
    
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
    
    track = Track.Atlanta
    drivers = Driver.allDrivers    
    race = Race(track, drivers)    
    qualified,disqualified = race.runQualifying()
    
    
    print "num\tqualify(mph)"
    print "=================\n"

    
    for num, mph in qualified:
        print "#%s\t%.3f" % (num,mph),
        if mph == 0:
            print "*",
        print   
            
    if len(disqualified) > 0:    
        print "Disqualified:"
        print "+="*10
        
        for num, reason in disqualified.items():    
            print "*%s\t%s" % (num,reason)
    
    #
    #
    # Race time!
    #
    
    running_order = []
    currentLap = 1
    
    for i in qualified:
        for d in drivers:
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