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
sd.default.latency="high"
sd.default.channels = 1
sd.default.dtype="int16"
sd.default.blocksize=50000
properties = None
audio_queue = queue.Queue()

CHUNK_NUM_BYTES = 128

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())	

def getAudioChunk():
    #gets a chunk from the buffer
    chunk = audio_queue.get()
    #print(chunk)
    return chunk

def sendAudioChunk(self):
    #sends audio chunk via bluetooth to the phone
    return

def record(): 
    print("Recording...")
    with sf.SoundFile("test.wav", mode="x", samplerate=fs, channels=1, subtype="PCM_16") as file:
        with sd.InputStream(callback=callback):
            while True:
                if ~Bluetooth.isConnected():
                    file.write(audio_queue.get());
