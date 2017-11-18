import time
import serial
import threading
import OLED

ser = serial.Serial(
    #port='/dev/ttyACM0',
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
)

direction = -1
oled = None
properties = None

class ArduinoThread (threading.Thread):
    """
        Thread Class which handles Running the EA system
    """
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        onReceived()
        print("Exiting " + self.name)


def setOLED(driverOLED):
    oled = driverOLED

#to get the threshold value
def setProperties(driverProperties):
    properties = driverProperties

def onReceived():
    
    # Calcualate newCorners
    newCorners = [False,False,False,False]
    
    while 1:
        OLED.clearAlerts()
        while ser.in_waiting:
            a=ser.readline();
            a=a[:-2]
            #b=ser.read(1);
            print("a: "+str(a))
            #b=a.decoded("utf-8")
            #print("b decode: "+str(b))
            #rint("b: "+str(b))
            #a=int.from_bytes(a, byteorder='big', signed=True)
            #b=int.from_bytes(b, byteorder='big', signed=False)
            y = int(a)
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
                newCorners = [False,False,False,False]
            print("y: "+str(y)+"\n\n")
        directionChanged = False
        currentCorners = OLED.getCurrentCorners()
        for i in range(0,len(currentCorners)):
            if newCorners[i] != currentCorners[i]:
                directionChanged = True
        
        if (directionChanged):  # was changed
            OLED.setCurrentCorners(newCorners)

        time.sleep(0.1)
