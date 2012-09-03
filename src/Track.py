
# track types
SPEED  = "speed"
SHORT = "short"
ROAD = "road"
SUPER = "super"


class RaceTrack(object):
    '''
    classdocs
    '''
    @staticmethod
    def Atlanta():
        return RaceTrack("Atlanta Motor Speedway", SPEED, 20, 2, 8, 1)
    @staticmethod
    def Pocono():
        return RaceTrack("Pocono Raceway",SPEED,10,1,7,2)
    
    @staticmethod
    def AutoClub():
        return RaceTrack("Auto CLub Speedway", SPEED, laps=15, pits=1, pitWindow=10, rolls=2)
    
    def __init__(self, name, type, laps, pits, pitWindow, rolls):
        '''
        Constructor
        '''
        self.name = name
        self.type = type
        self.totalLaps = laps
        self.pitCount = pits
        self.pitWindow = pitWindow
        self.rolls = rolls
        self.grid = 2  # cars per row in starting grid
        
        
        if self.type == SPEED:
            self.qualifyLaps = 4
        elif self.type == SHORT:
            self.qualifyLaps = 3
        elif self.type in [SUPER,ROAD]:
            self.qualifyLaps = 5

    def __repr__(self):
        return self.name
    
# Track variables    
Atlanta = RaceTrack.Atlanta()
Pocono = RaceTrack.Pocono()  
AutoClub = RaceTrack.AutoClub()  


 

