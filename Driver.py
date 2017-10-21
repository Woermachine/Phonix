import OLED
import Bluetooth
import ShotgunMic
import Properties
import ArdunioInterface

def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic with reference objects
    ArdunioInterface.setOLED(OLED)
    ArdunioInterface.setProperties(Properties)

    Bluetooth.setShotgunMic(ShotgunMic)
    Bluetooth.setOLED(OLED)

    ShotgunMic.setBluetooth(Bluetooth)

    OLED.setProperties(Properties)
    OLED.initDisplay()
    OLED.updateDisplay()

    exitBool = True
    while(exitBool):
        a = True
    return

main()