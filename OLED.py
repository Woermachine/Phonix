#Formerly Formattxt.py

#import gaugette.ssd1306
#import gaugette.platform
#import gaugette.gpio
#import time
#import sys
#import random

import nltk
nltk.download("punkt")


currentText = []
currentCorners = [False,False,False,False] #FL, FR, BL, BR

textQueue = []

def getCurrentCorners():
    return currentCorners


def setCurrentCorners(newCorners):
    global currentCorners
    currentCorners = newCorners
    updateDisplay()


def updateDisplay():
    ##Most of the commented out stuff is what is used to actually display stuff to the screen.

    RESET_PIN = 15  # WiringPi pin 15 is GPIO14.
    DC_PIN = 16  # WiringPi pin 16 is GPIO15.

    spi_bus = 0
    spi_device = 0
    gpio = gaugette.gpio.GPIO()
    spi = gaugette.spi.SPI(spi_bus, spi_device)

    # Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
    led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128)

    # Change rows & cols values depending on your display dimensions.
    led.begin()
    led.clear_display()
    led.display()
    led.invert_display()
    time.sleep(0.5)

    offset = 0  # flips between 0 and 32 for double buffering

    while True:


## write the current time to the display on every other cycle
if offset == 0:
    for i in range(0, len(list) - 1):
        text = list[i]
        text2 = list[i + 1]
        led.draw_text2(0, 10, text, 1)
        led.draw_text2(0, 19, text2, 1)
        led.display()
        time.sleep(1)
        led.clear_display()  # can be changed to change certain pixels

    led.draw_text2(0, 0, "$", 1)
    led.draw_text2(0, 25, "$", 1)
    led.draw_text2(120, 0, "$", 1)
    led.draw_text2(120, 25, "$", 1)
    led.draw_text2(0, 8, "123456789 10 11 12 13 14 15", 1)
    led.display()
    time.sleep(5)
    led.clear_display()
else:
    time.sleep(1)

    ##vertically scroll to switch between buffers
for i in range(0, 32):
    offset = (offset + 1) % 64
    led.command(led.SET_START_LINE | offset)
    time.sleep(0.01)


def formatTXT(list):
    ##Reads in a text file and tokenizes it
    with open("test.txt", "read")as myfile:
        data = myfile.read().replace('\n', '')

    from nltk.tokenize import sent_tokenize, word_tokenize
    list = word_tokenize(data)

    max = 16
    line = ""
    temp = 0
    listb = []
    ##adds the number of characters for each of the tokenized words and makes sure its not over 16
    for i in range(0, len(list) - 1):

        temp = temp + len(list[i])

        if temp <= max:

            line += list[i] + " "
            temp = temp + 1

        elif temp > max:
            listb.append(line[:-1])
            line = list[i] + " "
            temp = len(list[i]) + 1
        else:
            print "list is empty"

    print listb

# name of file as parameter and continue over writing file and keep open function(list of 								text,corners boolean if true put identifier)
