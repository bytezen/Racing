'''
Created on Aug 10, 2012

@author: rhazesspell
'''

import Track
import Driver
import Qualify
import random
import math
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



def rollDice(sides=100, times=1):
    roll = 0 
    for i in range(times):
        roll = roll + int(random.uniform(0,sides))

    return roll


class LapResult:
    def __init__(self):
        self._result = {}
        self.runningOrder = [] # list of 2-tuple driverNumber,speed
        self.closed = False
        
    def addDriverResult(self, driverNumber, rolls, initialLapSpeed, pit=False, trouble=None):
        if not self.closed:
            self._result[driverNumber] = {'rolls': rolls,
                                         'speed': sum(rolls) + initialLapSpeed,
                                         'pit': pit,
                                         'trouble': trouble }
        else:
            raise Exception, "lap results closed"
        
    def processResults(self):
        self.runningOrder = sorted( self._result.items(), key=lambda x: x[1]['speed'])
        self.runningOrder.reverse()
        self.closed = True
        return self.runningOrder
                        
    def getRunningOrder(self):
        return self.runningOrder
    
    def getResult(self):
        return self.result
                                
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
        self.driverQualifyMap = {}
        self._initDrivers(drivers)
        self.currentLap = 0
        self.lapResult = []
        self.qualifying = []
        

    def __initializeSpeedChart(self, driver):
        """ given a driver load the appropriate speed data file and 
            parse the data based on the track type;
            
            fileName: <driverNumber>sr.dat
            
            data format: roll, speedTrackSpeedRating, shortTrackSpeedRating, SuperSpeedTrackRating, RoadTrackRating 
        """
        logging.info("initializing speed chart for: %s" % driver.number,)
        dataFile = "../resources/" + driver.number + "sr.dat"
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
        
        driver.setRaceSpeedChart( speedChart )                    
        
        
    def _initDrivers(self, drivers):
        self.drivers = drivers
        
        for d in drivers:
            trackRating = d.getTrackRating( self.track.type )
            #Load the qualifying speeds
            self.driverQualifyMap[d.number] = Qualify.getQualifySpeedChart(trackRating)
            #Load the speed ratings for this race
            self.__initializeSpeedChart(d)            


    def runQualifying(self, verbose=False):
        """ 
            return:  pair;
                    sorted dictionary of qualifying speeds indexed by driver number,
                    disqualified drivers w/ disqualification reason
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
            # TODO:
            # Output the results per lap
        
        if troubleQualifying:
            roll = rollDice(sides=10)
            trouble = Qualify.getQualifyTroubleDetail(roll)
            
            return 0.0, trouble
        else:                    
            roll = rollDice()
            speed = Qualify.getAverageSpeed( roll, speedRatingTotal, self.track.type )
            return speed, None        
        
         
    def setStartingGrid(self):
        """ 
            set the starting order with start grid penalties
            return: list of LapResults
        """
        lap0 = LapResult()
        
        startingRows = math.ceil( len(self.drivers) / self.track.grid )
        #max penalty for starting position is 6; use 7 because row 0 has no penalty        
        rowsPerPenaltyPoint = max( startingRows / 7, 1 )  
        
        for i,qualify in enumerate( self.qualifying ):
            row = i / self.track.grid
            penalty = -1 * rowsPerPenaltyPoint * row    
            
            lap0.addDriverResult(qualify[0], rolls = [penalty], initialLapSpeed = 0 )            
        
        lap0.processResults()            
        self.lapResult.append( lap0 )  #Lap 0 list
        
        return self.lapResult[0]


    def getPreviousLapResult(self):
        prev = self.currentLap - 1
        if prev < 0:
            logging.warn("previous lap is less than zero; returning results for lap 0")
            return self.lapResult[0]
        else:
            return self.lapResult[prev]

    def runLap(self, driver, qualifying=False):
        """
            simulate a lap
            return: the the driver's {rolls =[], speed = #} after the lap
        """        
        speedRolls = []
        
        if not qualifying:
            for r in range(self.track.rolls):
                r = rollDice()
                s = driver.calculateSpeed(r)
                speedRolls.append(s)
                
                if s < 0:
                    print "Need to implement trouble for drivers"
                    
        return speedRolls
    
    def calculateLapResults(self, prevLapResult, lapspeeds):
        """
            return: LapResult
        """
        lapResult = LapResult()
        for pDriver, pSpeed in prevLapResult.getRunningOrder():
            speed = None
            for d,rolls in lapspeeds:
                if d == pDriver:
                    speed = rolls
            if speed:
                pass
            else:
                logging.error("could not find previous speed (lap %s ) for driver %s" % (self.currentLap -1, pDriver) )

                
    def getRunningOrder(self, lapNumber=-1):
        if lapNumber < 0:
            return self.lapResult[self.currentLap]
        else: 
            return self.lapResult[lapNumber]
        
       
    def lookupDriver(self, number):
        driver = None
        for d in self.drivers:
            if d.number == number:
                return d


        
if __name__ == '__main__':
    testRace = Race(Track.Atlanta, Driver.allDrivers)
    print "Racing at: ", testRace.track
    print "Drivers: ", testRace.drivers
    
    print "qualifying..."
    print testRace.runQualifying() 
    
    print "gentlemen start your engines...starting grid = "
    print testRace.setStartingGrid()        