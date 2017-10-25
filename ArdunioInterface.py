from threading import Thread

direction = -1
oled = None
properties = None


def setOLED(driverOLED):
    oled = driverOLED

#to get the threshold value
def setProperties(driverProperties):
    properties = driverProperties

def onReceived():
    direction # = recieved direction

    # Calcualate newCorners
    newCorners = [False,False,False,False]

    directionChanged = False
    currentCorners = oled.getCurrentCorners()
    for i in range(0,len(currentCorners)):
        if newCorners[i] == currentCorners[i]:
            directionChanged = True

    if (directionChanged):  # was changed
        oled.setCurrentCorners(newCorners)
