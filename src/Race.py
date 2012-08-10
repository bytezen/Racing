'''
Created on Aug 10, 2012

@author: rhazesspell
'''

import Track
from Driver import RaceDriver

class Race(object):
    '''
    classdocs
    '''


    def __init__(self, track):
        '''
        Constructor
        '''
        self.track = track
        self.drivers = []
        self.driverSpeedMap = {}
        self.driverQualifyMap = {}
        

    def __initializeSpeedChart(self, driverNumber):
        """ given a driver load the appropriate speed data file and 
            parse the data based on the track type;
            
            fileName: <driverNumber>sr.dat
            
            data format: roll, speedTrackSpeedRating, shortTrackSpeedRating, SuperSpeedTrackRating, RoadTrackRating 
        """
        dataFile = "../resources/" + driverNumber + "sr.dat"
        col = None
        
        if self.type == Track.SPEED: 
            col = 1
        elif self.type == Track.SHORT: 
            col = 2
        elif self.type == Track.SUPER: 
            col = 3
        else:  # Road course 
            col = 4
         
        fo = open(dataFile, 'r')
        lines = fo.readline().split('\r') 
        for l in lines[1:]:  #first line is header "roll,trouble"
            _l = l.split(",")
            self.speedChart[int(_l[0])] = int(_l[col])
         
        fo.close()                    
        
        
    def addRacers(self, drivers):
        self.drivers = drivers
        
        for d in drivers:
            #Load the qualifying speeds
            self.__initializeSpeedChart(d.number)
            #Load the speed ratings for this race
            pass




        
if __name__ == '__main__':
    test = Race( Track.Atlanta() )         