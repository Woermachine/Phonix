#imports
import sounddevice as sd
import Bluetooth
import soundfile as sf
import threading
import queue
import sys


audio_queue = queue.Queue()

class ShotgunMicThread (threading.Thread):
    """
        Thread Class which handles Running the Bluetooth RFComm server
        away from ther seperate thread.
    """
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        record()
        print("Exiting " + self.name)

fs = 44100
sd.default.device = "USB audio device"
sd.default.samplerate = fs
sd.default.channels = 1
properties = None
audio_queue = queue.Queue()

CHUNK_NUM_BYTES = 128

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())			

def getAudioChunk():
    #gets a chunk from the buffer
    chunk=[]
    
    if audio_queue.qsize() >= 128:
        for i in range (0, 128):
            chunk[i] = audio_queue.get()
        print("Pop goes the weasel!")
        return chunk
    else:
        return False

def sendAudioChunk(self):
    #sends audio chunk via bluetooth to the phone
    return

def record(): 
    print("Recording...")
    sd.InputStream(callback=callback)
    while True:
        if ~Bluetooth.isConnected():
            audio_queue.get()
