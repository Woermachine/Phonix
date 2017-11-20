#imports
import sounddevice as sd
import time

import Bluetooth
import soundfile as sf
import threading
import queue
import sys, os


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

fs = 8000
sd.default.samplerate = fs
sd.default.latency="high"
sd.default.channels = 1
sd.default.dtype="int16"
#sd.default.blocksize=8192
properties = None
audio_queue = queue.Queue()

PAYLOAD_MAX_CHUNKS = 1

## callback
# indata - Numpy.array (contains multiple frames)
# frames - number of frames recorded
# time - how long its was recording for
# status - error codes (normally NULL)
##
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())	

def getAudioChunk():
    #gets a chunk from the buffer
    chunk = bytes(audio_queue.get())
    #print(chunk)
    return chunk

def sendAudioChunk(self):
    #sends audio chunk via bluetooth to the phone
    return

def record(): 
    print("Recording...")
    while True:
        if Bluetooth.isConnected():
            with sd.InputStream(callback=callback) as stream:
                while stream.active:
                    if Bluetooth.isConnected():
                        payload = createAudioPayload()
                        Bluetooth.send(payload);
                    else:
                        stream.close();
        time.sleep(1) #Please no kill CPU

"""
Creates an audio payload which is just multiple chunks of audio
concatenated together into one long byte string.
"""
def createAudioPayload():
    i = 0
    payload = []
    while i < PAYLOAD_MAX_CHUNKS and audio_queue.qsize() > 0:
        payload.append(bytes(audio_queue.get()))
        i = i + 1
    payload = b''.join(payload)
    #print(len(payload))
    return payload

