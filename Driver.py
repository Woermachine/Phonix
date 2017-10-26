import OLED
import Bluetooth
import ShotgunMic
import Properties
import ArdunioInterface
import time



def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic with reference objects
    ArdunioInterface.setOLED(OLED)
    ArdunioInterface.setProperties(Properties)

    Bluetooth.setShotgunMic(ShotgunMic)
    Bluetooth.setOLED(OLED)
    bluetooth_thread = Bluetooth.BluetoothThread(1, "Bluetooth-Thread", 1)
    bluetooth_thread.start()

    ShotgunMic.setBluetooth(Bluetooth)

    OLED.setProperties(Properties)
    OLED.initDisplay()
    OLED.updateDisplay()

    #code to test the OLED
    testString = "This is a test string to show whether the OlED will update properly. Let's see how this goes."

    OLED.queueIncomingText(testString)

    for i in range(0, 10):
        OLED.updateText()
        time.sleep(2)

    exitBool = True
    while(~exitBool):
        a = True
    return

main()