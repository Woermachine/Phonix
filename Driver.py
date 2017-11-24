import OLED
import Bluetooth
import ShotgunMic
import Properties
import ArdunioInterface
import time



def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic with reference objects
    #ArdunioInterface.setOLED(OLED)
    #ArdunioInterface.setProperties(Properties)
    arduino_thread = ArdunioInterface.ArduinoThread(1,"Arduino-Thread",1)
    arduino_thread.start()

    bluetooth_thread = Bluetooth.BluetoothConnectionThread(1, "BluetoothConnection-Thread", 1)
    bluetooth_thread.start()

    bluetooth_thread2 = Bluetooth.BluetoothTextThread(1, "BluetoothText-Thread", 1)
    bluetooth_thread2.start()

    oled_thread = OLED.OLEDThread(1, "OLED-Thread", 1);
    oled_thread.start()

    #bluetooth_thread3 = Bluetooth.BluetoothAudioThread(1, "BluetoothAudio-Thread", 1)
    #bluetooth_thread3.start()

    shotgun_thread = ShotgunMic.ShotgunMicThread(1, "ShotgunMic-Thread", 1)
    shotgun_thread.start()

   #OLED.setProperties(Properties)
   #OLED.initDisplay()

   #code to test the OLED
   #testString = "This is a test string to show whether the OLED will update properly Let's see how this goes"

   #OLED.queueIncomingText(testString)

    #while(True):
    #    OLED.updateText()
    #    time.sleep(Properties.scrollSpeed)

    #exitBool = True
    #while(~exitBool):
    #    a = True
    # Wait until all threads close
    arduino_thread.join()
    bluetooth_thread.join()
    bluetooth_thread2.join()
    shotgun_thread.join()

    return

main()
