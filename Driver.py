import OLED
import Bluetooth
import Properties
import ArdunioInterface

def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic

    ArdunioInterface.setOLED(OLED)
    exitBool = True
    while(1):
        if(~exitBool):
            return
    return

main()