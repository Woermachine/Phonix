import OLED
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