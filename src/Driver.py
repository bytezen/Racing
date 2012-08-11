        
        
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
        self.speedChart = [-1]*100
        self.raceSpeed = 0

    def initializeSpeedChart(self, trackType):
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
            raise Exception, "Speed chart not initialized"
        
        return self.speedChart[roll]
    
    def setRaceSpeed(self, speed):
        self.raceSpeed = self.raceSpeed + speed
                
                    
    def __repr__(self):
        return "#%s %s" % (self.number, self.name)        
        
        