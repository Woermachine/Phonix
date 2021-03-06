# Phonix

This repository contain the software for the Phonix Smartglasses Prototype which will runs on the Raspberry Pi and Arduino. The companion Android app is available here: https://github.com/Woermachine/PhonixAndroidApp

The software is licensed under GNU GPLv3. See License.txt for details.

# Setup

The following are the pin numbers counting from the sd card side used to wire the display: these are the actual numbers starting at 1 not what diagrams on wiring will say. 

Data:19
Clk:23
DC:10
RST:8
CS:24
Vin:1
GND:6

## Update/Install
Be connected to internet

#### Make sure everythings up-to-date

``` sudo apt-get update```

#### Install Python3:

``` sudo apt-get install python3```



#### Install pybluez:

```
sudo apt-get install python3-pip python3-dev ipython

sudo apt-get install libbluetooth-dev

sudo pip3 install pybluez
```

#### Install NLTK

``` sudo pip3 install nltk``` 
 

#### Install NumPy
NumPy arrays are sometimes used in this project, as they are more versatile than regular python lists. If you are on raspbian-lite (Which is what a 'production' model should be running) you will need to install it manually:
```
sudo apt-get install python-numpy
```

#### Configure Pybluez Bluetooth Service:
the bluetooth service running on the raspberry pi will not have compatibility mode enabled by default, disabling the ability to set
bluetooth profiles via command-line impossible: First thing we need to do is add -C to the bluetooth.service

```
sudo nano /lib/systemd/system/bluetooth.service
ExecStart=/user/lib/bluetooth/bluetoothd -C
```

Then we can enable serial profile with the following:

```sudo sdptool add SP```

#### Install Sound Module Dependencies
sounddevice is used to listen to shotgun mic, for it to install correctly, we need to first install libportaudio2, cffi and its c dependendency ffi, as well as libsndfile1(soundfile dependency):
```
sudo apt-get install libportaudio2 libffi-dev libsndfile1
sudo pip3 install cffi
```

Then install sounddevice & soundfile modules:
```
sudo pip3 install sounddevice
sudo pip3 install soundfile

```

#### Install Git:

```sudo apt-get install git```

#### Install OLED stuff:

///You may need this:
```
sudo apt-get install git-core

sudo nano /etc/modprobe.d/raspi-blacklist.conf
```

Ctrl-Z to exit

```
sudo nano /etc/modules
```

make sure this file reads

```
i2c-bcm2708

i2c-dev
```

Ctrl-O to write out

Ctrl-X to exit

**Open in Raspbian home menu, open preferences>interfaces and change ssh, and spi to enabled**

When prompted reboot the system


After system reboot
```
git clone https://github.com/the-raspberry-pi-guy/OLED
cd OLED
sh OLEDinstall.sh
```

This will clone the OLED library and install the gaugette library

run one of the example programs to test that the screen is functioning

```
cd python-examples
sudo python3 OLEDclock.py
```

```
sudo pip3 install spidev serial
```
#Install this repository Clone

After preforming the previous steps, clone this repository

```
cd ~/Desktop/
git clone https://github.com/Woermachine/Phonix
```

NLTK
PiBluez
and follow the instructions in this video https://www.youtube.com/watch?v=BeBfpJnN9SE

Py-Gaugette-
To install gaugette and it's dependencies look at its gitHub page: https://github.com/stephen-mw/ssd1306-128x64-lib

# Install PIL Fork (Pillow)
sudo pip3 install Pillow


#Make phonix softare run at startup
```
sudo cp /Phonix/phonix.service /etc/systemd/system/phonix.service
sudo systemctl enable phonix.service
```

