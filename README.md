# Phonix

This repository contains the software which will run on the Raspberry Pi and Arduino. It will compose the Phonix smartglasses software.

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

####Make sure everythings up-to-date

``` sudo apt-get update```

####Install Python3:

``` sudo apt-get install python3```

####Install NLTK

``` sudo pip install nltk``` 

####Install pybluez:

```
sudo apt-get install python-pip python-dev ipython

sudo apt-get install libbluetooth-dev

sudo pip install pybluez
``` 

####Install Git:

```sudo apt-get install git```

####Install OLED stuff:

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

Ctrl-Z to exit

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
sudo pythons OLEDclock.py
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
