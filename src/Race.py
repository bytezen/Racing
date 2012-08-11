'''
Created on Aug 10, 2012

@author: rhazesspell
'''

import Track
import Driver
import Qualify
import random
import math


def rollDice(sides=100, times=1):
    roll = 0 
    for i in range(times):
        roll = roll + int(random.uniform(0,sides))

    return roll


class LapResult:
    def __init__(self):
        self._result = {}
        self.runningOrder = []
        self.closed = False
        
    def addDriverResult(self, driverNumber, rolls, pit=False, trouble=None):
        if not self.closed:
            self._result[driverNumber] = {'rolls': rolls,
                                         'speed': sum(rolls),
                                         'pit': pit,
                                         'trouble': trouble }
        else:
            raise Exception, "lap results closed"
        
    def processResults(self):
        self.runningOrder = sorted( self._result.items(), key=lambda x: x[1]['speed'])
        self.runningOrder.reverse()
        self.closed = True
        return self.runningOrder
                        
    def __repr__(self):
        s = ""
        for driver,result in self.runningOrder:
            s += (driver+",speed: "+str(result['speed'])+"\n")  
        return s


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
        self.qualifying = []
        

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
            qualifySpeed, troubleMsg = self._qualifyDriver(driver)
            _qualified[driver.number] = qualifySpeed
            
            if troubleMsg:
                disqualified[driver.number] = troubleMsg
                
        self.qualifying = sorted(_qualified.items(), key=lambda x: x[1])
        self.qualifying.reverse()   
        
        return self.qualifying,disqualified

    
    def _qualifyDriver(self, driver):
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
        
         
    def startEngines(self):
        """ 
            set the starting order with start grid penalties
        """
        lap0 = LapResult()
        
        startingRows = math.ceil( len(self.drivers) / self.track.grid )
        rowsPerPenaltyPoint = max( startingRows / 7, 1 ) 
        
        for i,qualify in enumerate( self.qualifying ):
            row = i / self.track.grid
            penalty = -1 * rowsPerPenaltyPoint * row
            
            
            lap0.addDriverResult(qualify[0], [penalty] )            
        
        lap0.processResults()            
        self.lap.append( lap0 )  #Lap 0 list
        
        return self.lap[0]
        
    

        
if __name__ == '__main__':
    testRace = Race(Track.Atlanta, Driver.allDrivers)
    print "Racing at: ", testRace.track
    print "Drivers: ", testRace.drivers
    
    print "qualifying..."
    print testRace.runQualifying() 
    
    print "gentlemen start your engines...starting grid = "
    print testRace.startEngines()        