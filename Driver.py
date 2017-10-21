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
    bluetooth_thread = Bluetooth.BluetoothThread(1, "Bluetooth-Thread", 1)
    bluetooth_thread.start()

    ShotgunMic.setBluetooth(Bluetooth)

    OLED.setProperties(Properties)
    OLED.initDisplay()
    OLED.updateDisplay()

    exitBool = True
    while(exitBool):
        a = True
    return

main()