#imports
import sounddevice as sd
import soundfile as sf
import threading
import queue
import sys

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
bluetooth = None
properties = None

#file = sf.SoundFile("yo.wav", mode="x", samplerate=44100, channels=1, subtype="PCM_24"); 

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())			

def setBluetooth(driverBT):
    bluetooth = driverBT

def getAudioChunk(self):
    #gets a chunk from the buffer
    return

def sendAudioChunk(self):
    #sends audio chunk via bluetooth to the phone
    return

def record(): 
	print("Recording...")
	with sd.InputStream(callback=callback):
		print('#' * 80);
		print('press Ctrl+C to stop recording')
		print('#' * 80);
		#while True:
		#file.write(audio_queue.get())