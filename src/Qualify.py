'''
Created on Jul 29, 2012

@author: rhazesspell
'''

# A QUALIFY RATING TABLE
qualify_a = [0]*100
for i in range(10):
    qualify_a[i] = 12
for i in range(10,20):
    qualify_a[i] = 13
for i in range(20,30):
    qualify_a[i] = 14
for i in range(30,50):
    qualify_a[i] = 15
for i in range(50,66):
    qualify_a[i] = 16
for i in range(66,75):
    qualify_a[i] = 17
for i in range(75,99):
    qualify_a[i] = 18

qualify_a[99] = "trouble"


# B QUALIFY RATING TABLE
qualify_b = [0]*100
for i in range(15):
    qualify_b[i] = 12
for i in range(15,25):
    qualify_b[i] = 13
for i in range(25,35):
    qualify_b[i] = 14
for i in range(35,55):
    qualify_b[i] = 15
for i in range(55,71):
    qualify_b[i] = 16
for i in range(71,80):
    qualify_b[i] = 17
for i in range(80,99):
    qualify_b[i] = 18

qualify_b[99] = "trouble"

# C QUALIFY RATING TABLE
qualify_c = [0]*100
for i in range(20):
    qualify_c[i] = 12
for i in range(20,30):
    qualify_c[i] = 13
for i in range(30,40):
    qualify_c[i] = 14
for i in range(40,60):
    qualify_c[i] = 15
for i in range(60,76):
    qualify_c[i] = 16
for i in range(76,85):
    qualify_c[i] = 17
for i in range(85,99):
    qualify_c[i] = 18

qualify_c[99] = "trouble"

# D QUALIFY RATING TABLE
qualify_d = [0]*100
for i in range(25):
    qualify_d[i] = 12
for i in range(25,35):
    qualify_d[i] = 13
for i in range(35,45):
    qualify_d[i] = 14
for i in range(45,65):
    qualify_d[i] = 15
for i in range(65,81):
    qualify_d[i] = 16
for i in range(81,90):
    qualify_d[i] = 17
for i in range(90,99):
    qualify_d[i] = 18

qualify_d[99] = "trouble"

# E QUALIFY RATING TABLE
qualify_e = [0]*100
for i in range(30):
    qualify_e[i] = 12
for i in range(30,40):
    qualify_e[i] = 13
for i in range(40,50):
    qualify_e[i] = 14
for i in range(50,70):
    qualify_e[i] = 15
for i in range(70,86):
    qualify_e[i] = 16
for i in range(86,95):
    qualify_e[i] = 17
for i in range(95,99):
    qualify_e[i] = 18

qualify_e[99] = "trouble"


# SPEED CHARTS
# SHORT TRACK
speed_short = { 36: 126.5, 
               37: 126.6,
               38: 126.7,
               39: 126.8,
               40: 126.9,
               41: 127.0,
               42: 127.1,
               43: 127.2,
               44: 127.3,
               45: 127.4,
               46: 127.5,
               47: 127.6,
               48: 127.7,
               49: 127.8,
               50: 127.9,
               51: 128.0,
               52: 128.1,
               53: 128.2,
               54: 128.3 }

speed_speedway = { 48: 187.5, 
               49: 187.6,
               50: 187.7,
               51: 187.8,
               52: 187.9,
               53: 188.0,
               54: 188.1,
               55: 188.2,
               56: 188.3,
               57: 188.4,
               58: 188.5,
               59: 188.6,
               60: 188.7,
               61: 188.8,
               62: 188.9,
               63: 189.0,
               64: 189.1,
               65: 189.2,
               66: 189.3,
               67: 189.4,
               68: 189.5,
               69: 189.6,                              
               70: 189.7,
               71: 189.8,
               72: 189.9 }

#TODO: Implement superspeedway

#TODO: Implement road course


def getSpeedRating(roll,qualifyRating):
    if qualifyRating == 'A':
        return qualify_a[roll]
    elif qualifyRating == 'B':
        return qualify_b[roll]
    elif qualifyRating == 'C':
        return qualify_c[roll]
    elif qualifyRating == 'D':
        return qualify_d[roll]
    elif qualifyRating == 'E':
        return qualify_e[roll]
    else:
        print "Can not get speed for roll=", roll," qualifyRatin = ", qualifyRating
        return -1


def getAverageSpeed(speedRatingTotal, trackType):
    if trackType == 'speedway':
        return speed_speedway[speedRatingTotal]
    elif trackType == 'short':
        return speed_short[speedRatingTotal]
    elif trackType == 'super':
        pass
    elif trackType == 'road':
        pass
    else:
        print "Can not get average Speed for speedRatingTotal: ", speedRatingTotal, " track type: ",trackType

    return -1

if __name__ == '__main__':
    pass