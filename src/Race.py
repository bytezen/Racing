'''
Created on Aug 10, 2012

@author: rhazesspell
'''

import Track
import Driver
import Qualify
import random


def rollDice(sides=100, times=1):
    roll = 0 
    for i in range(times):
        roll = roll + int(random.uniform(0,sides))

    return roll



class Race(object):
    '''
    classdocs
    '''


    def __init__(self, track, drivers):
        '''
        Constructor
        '''
        self.track = track
        self.driverSpeedChart = {}
        self.driverQualifyMap = {}
        self._enterDrivers(drivers)
        self.currentLap = 0
        self.lap = []
        

    def __initializeSpeedChart(self, driverNumber):
        """ given a driver load the appropriate speed data file and 
            parse the data based on the track type;
            
            fileName: <driverNumber>sr.dat
            
            data format: roll, speedTrackSpeedRating, shortTrackSpeedRating, SuperSpeedTrackRating, RoadTrackRating 
        """
        dataFile = "../resources/" + driverNumber + "sr.dat"
        col = None
        
        if self.track.type == Track.SPEED: 
            col = 1
        elif self.track.type == Track.SHORT: 
            col = 2
        elif self.track.type == Track.SUPER: 
            col = 3
        else:  # Road course 
            col = 4
            
         
        speedChart = range(100) 
        fo = open(dataFile, 'r')
        lines = fo.readline().split('\r') 
        for l in lines[1:]:  #first line is header "roll,trouble"
            _l = l.split(",")
            speedChart[int(_l[0])] = int(_l[col])
         
        fo.close()
        
        self.driverSpeedChart[driverNumber] = speedChart                    
        
        
    def _enterDrivers(self, drivers):
        self.drivers = drivers
        
        for d in drivers:
            trackRating = d.getTrackRating( self.track.type )
            #Load the qualifying speeds
            self.driverQualifyMap[d.number] = Qualify.getQualifySpeedChart(trackRating)
            #Load the speed ratings for this race
            self.__initializeSpeedChart(d.number)
            pass


    def runQualifying(self, verbose=False):
        """ 
            for the current track and drivers in the race return a sorted dictionary of 
            qualifying speeds indexed by driver number
        """
        _qualified = {}
        disqualified = {}
        for driver in self.drivers:
            qualifySpeed, troubleMsg = self.qualifyDriver(driver)
            _qualified[driver.number] = qualifySpeed
            
            if troubleMsg:
                disqualified[driver.number] = troubleMsg
                
        qualifying = sorted(_qualified.items(), key=lambda x: x[1])
        qualifying.reverse()   
        
        return [qualifying,disqualified]

    
    def qualifyDriver(self, driver):
        """ 
        return tuple of qualifying speed and trouble message if any
        """ 
        speedRatingTotal = 0
        troubleQualifying = False
        
        for i in range(self.track.qualifyLaps):
            roll = rollDice()
            
            speedRating = self.driverQualifyMap[driver.number][roll]
            if( speedRating == Qualify.TROUBLE):
                troubleQualifying = True
                break
            
            speedRatingTotal += speedRating
        
        if troubleQualifying:
            roll = rollDice(sides=10)
            trouble = Qualify.getQualifyTroubleDetail(roll)
            
            return 0.0, trouble
        else:                    
            roll = rollDice()
            speed = Qualify.getAverageSpeed( roll, speedRatingTotal, self.track.type )
            return speed, None        
        
         
    
    



        
if __name__ == '__main__':
    pass         