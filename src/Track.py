'''
Created on Aug 1, 2012

@author: spellrh
'''

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
        