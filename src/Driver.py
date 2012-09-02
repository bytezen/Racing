from Track import *
        
class DriverStats(object):
    def __init__(self, overall, quality, trouble, trackRatings):
        self.overallRating = overall
        self.qualityRating = quality
        self.troubleRating = trouble
        self.trackRatings = trackRatings
    pass


class RaceStatus(object):
    pass
        
        
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
        self.stats = DriverStats( overall, quality, trouble, trackRatings)
        self.speedChart = [-1]*100
        self.raceSpeed = 0

    def loadDriverSpeedChart(self, trackType):
        dataFile = "../resources/" + self.number + "sr.dat"
        col = None
        
        if trackType == "speed": 
            col = 1
        elif trackType == "short": 
            col = 2
        elif trackType == "super": 
            col = 3
        elif trackType == "road": 
            col = 4
        else:
            msg = "unknown track type: " + trackType
            raise ValueError,  msg 
        
         
        fo = open(dataFile, 'r')
        lines = fo.readline().split('\r') 
        for l in lines[1:]:  #first line is header "roll,trouble"
            _l = l.split(",")
            self.speedChart[int(_l[0])] = int(_l[col])
         
        fo.close()        
        

    def getSpeed(self, roll):
        if self.speedChart[0] < 0:
            raise Exception, " THis should be handled by Race not Driver...The Drivers speed chart for this race has not been initialized"
        
        return self.speedChart[roll]
    
    def setRaceSpeed(self, speed):
        self.raceSpeed = self.raceSpeed + speed
        
    def getTrackRating(self,trackType):
        return self.stats.trackRatings[trackType]
                
                    
    def __repr__(self):
        return "#%s %s" % (self.number, self.name)        
        

        
"""
Load Driver Data
"""        
d48 = Driver("Jimmy Johnson",'48',  'A', 'A', 'A', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'A',ROAD:'A'})
d24 = Driver("Jeff Gordon",'24',  'A', 'A', 'A', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'A',ROAD:'A'})    
d07 = Driver("Clint Bowyer",'07',  'A', 'B', 'A', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'B',ROAD:'A'})
d17 = Driver("Matt Kenseth",'17',  'A', 'B', 'B', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'B',ROAD:'C'})                
d5 = Driver("Kyle Busch",'5',  'A', 'A', 'A', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'C',ROAD:'A'})
d20 = Driver("Tony Stewart",'20',  'A', 'B', 'B', trackRatings = {SPEED:'A' , SHORT:'A', SUPER:'D',ROAD:'A'})
d2 = Driver("Kurt Busch",'2',  'A', 'A', 'A', trackRatings = {SPEED:'B' , SHORT:'B', SUPER:'A',ROAD:'B'})
d31 = Driver("Jeff Burton",'31',  'A', 'B', 'A', trackRatings = {SPEED:'A' , SHORT:'B', SUPER:'C',ROAD:'C'})

allDrivers = [d48,d24,d07,d17,d5,d20,d2,d31]
        