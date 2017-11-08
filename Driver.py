import OLED
import Bluetooth
import ShotgunMic
import Properties
#import ArdunioInterface
import time



def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic with reference objects
    #ArdunioInterface.setOLED(OLED)
    #ArdunioInterface.setProperties(Properties)
    #arduino_thread = ArdunioInterface.ArduinoThread(1,"Arduino-Thread",1)
    #arduino_thread.start()

    Bluetooth.setShotgunMic(ShotgunMic)
    Bluetooth.setOLED(OLED)
    bluetooth_thread = Bluetooth.BluetoothConnectionThread(1, "BluetoothConnection-Thread", 1)
    bluetooth_thread.start()

    bluetooth_thread2 = Bluetooth.BluetoothTextThread(1, "BluetoothText-Thread", 1)
    bluetooth_thread2.start()
    
    bluetooth_thread3 = Bluetooth.BluetoothAudioThread(1, "BluetoothAudio-Thread", 1)
    bluetooth_thread3.start()
    
    shotgun_thread = ShotgunMic.ShotgunMicThread(2, "ShotgunMic-Thread", 2)
    shotgun_thread.start()
	
    ShotgunMic.setBluetooth(Bluetooth)

    OLED.setProperties(Properties)
    OLED.initDisplay()

    #code to test the OLED
    testString = "This is a test string to show whether the OLED will update properly Let's see how this goes"

    OLED.queueIncomingText(testString)

    for i in range(0, 10):
        OLED.updateText()
        time.sleep(Properties.scrollSpeed)

   

    exitBool = True
    while(~exitBool):
        a = True
    return

main()
