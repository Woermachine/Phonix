import time
import serial
from threading import Thread

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
)

direction = -1
oled = None
properties = None


def setOLED(driverOLED):
    oled = driverOLED

#to get the threshold value
def setProperties(driverProperties):
    properties = driverProperties

def onReceived():
    
    # Calcualate newCorners
    newCorners = [False,False,False,False]
    
    while 1:
        whlie ser.in_waiting:
            x=ser.read(1);
            x=x+ser.read(1);
            y=int.from_bytes(x, byteorder='big', signed=True)
            if y>=0 and y<22 or y>=338 and y<=359:
                newCorners = [True,True,False,False];
            if y>=22 and y<67:
                newCorners = [False,True,False,False];
            if y>=67 and y<112:
                newCorners = [False,True,False,True];
            if y>=112 and y<157:
                newCorners = [False,False,False,True];
            if y>=157 and y<202:
                newCorners = [False,False,True,True];
            if y>=202 and y<247:
                newCorners = [False,False,True,False];
            if y>=247 and y<292:
                newCorners = [True,False,True,False];
            if y>=292 and y<338:
                newCorners = [True,False,False,False];
            if y<0:
                newCorners = [False,False,False,False];


    directionChanged = False
    currentCorners = oled.getCurrentCorners()
    for i in range(0,len(currentCorners)):
        if newCorners[i] == currentCorners[i]:
            directionChanged = True

    if (directionChanged):  # was changed
        oled.setCurrentCorners(newCorners)
