direction = -1
oled = None


def setOLED(driverOLED):
    oled = driverOLED


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
