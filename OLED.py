currentText = []
currentCorners = [False,False,False,False] #FL, FR, BL, BR

textQueue = []

def getCurrentCorners():
    return currentCorners


def setCurrentCorners(newCorners):
    global currentCorners
    currentCorners = newCorners
    updateDisplay()


def formatTXT():
    return


def updateDisplay():
    return