import OLED
import ArdunioInterface

def main():
    #  Instantiate Screen, Bluetooth, Arduino Interface, ShotgunMic
    OLED.updateDisplay();
    # Start thread
    ArdunioInterface.setOLED(OLED)
    exitBool = True
    while(1):
        if(~exitBool):
            return
    return

main()