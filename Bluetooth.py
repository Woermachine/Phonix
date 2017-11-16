#External Dependency imports
from bluetooth import *

#Python 3 Standard imports
import threading
import time

#Project Specific imports
import ShotgunMic
import OLED

shotgunMic = None;
oled = None;

bufferIn = []
bufferOut = []

connected = False
running = True

#Global Bluetooth Service
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY)) #bind to any available port
server_sock.listen(1) #Listen for connections
port = server_sock.getsockname()[1] #Get Port
uuid = "b8162268-3e67-4749-9508-cb30b86703c7"

advertise_service(server_sock, "PhonixServer",
    service_id=uuid,
    service_classes=[uuid, SERIAL_PORT_CLASS],
    profiles=[SERIAL_PORT_PROFILE]
)


class BluetoothConnectionThread (threading.Thread):
    """
        Thread Class which handles accepting new connections
    """
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        global connected
        global running
        global client_sock
        global client_info
        
        print("Starting " + self.name)
        while running:
            if not connected:
                print("Waiting for connection on RFCOMM channel %d" % port)
                client_sock, client_info = server_sock.accept()
                print("Accepted connection from ", client_info)
                connected = True
            time.sleep(1) #Don't Destroy CPU Please.
        print("Exiting " + self.name)
		
class BluetoothTextThread (threading.Thread):
    """
        Thread Class which handles receiving text from the Phonix Phone Application.
    """
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        global connected
        global running
        global client_sock
        print("Starting " + self.name)
        
        while running:
            try:
                while connected:
                    data = client_sock.recv(1024)
                    if len(data) != 0:
                        onReceiveText(data)
                    else:
                        connected = False
            except IOError:
                    connected = False
        print("Exiting " + self.name)
		
class BluetoothAudioThread (threading.Thread):
    """
        Thread which handles sending data to Phonix Phone Application if
        connected.
    """
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        global connected
        print("Starting " + self.name)
        while running:
            while connected:
                sendAudio(client_sock)
                time.sleep(1) #Don't destroy Cpu please    
        print("Exiting " + self.name)


def setShotgunMic(driverShotgunMic):
    shotgunMic = driverShotgunMic

def setOLED(driverOLED):
    oled = driverOLED

def onReceiveAudio(audio):
    #puts audio in the bufferOut
    return

"""
    Accepts
"""
def send(data):
    global connected
    global running
    global client_sock
    global client_info

    #sends data from buffer to phone
    if (data.any() and connected):
        try:
            client_sock.send(data)    
        except BluetoothError:
            connected=False
        
def onReceiveText(text):
    #receive text from phone and puts it in bufferIn
    print("received [%s]" % text)
    bufferIn.append(text)
    OLED.queueIncomingText(text.decode("utf-8"))
    return

def isConnected():
    return connected

def sendText():
    #sends text from the bufferIn to display
    return
