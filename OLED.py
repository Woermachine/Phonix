import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import sys
import random

import nltk

#nltk.download("punkt")

properties = None;
currentText = ["",""]
textQueue = []
currentCorners = [False,False,False,False] #FL, FR, BL, BR

#Initialization of display values
RESET_PIN = 15  # WiringPi pin 15 is GPIO14.
DC_PIN = 16  # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128)
list = list() #Initialize an empty list to prevent exceptions.

#to get the scrollSpeed value
def setProperties(driverProperties):
    properties = driverProperties

def getCurrentCorners():
    return currentCorners


def setCurrentCorners(newCorners):
    global currentCorners
    currentCorners = newCorners
    updateAlerts()

def initDisplay():
    # Change rows & cols values depending on your display dimensions.
    led.begin()
    led.clear_display()
    led.display()
    time.sleep(0.5)

def clearAlerts():
    led.draw_text2(0, 0, " ", 1)
    led.draw_text2(0, 25, " ", 1)
    led.draw_text2(120, 0, " ", 1)
    led.draw_text2(120, 25, " ", 1)

def updateAlerts():
    if(currentCorners[0]):
        led.draw_text2(0, 0, "$", 1)
    elif(currentCorners[1]):
        led.draw_text2(0, 25, "$", 1)
    elif (currentCorners[2]):
        led.draw_text2(120, 0, "$", 1)
    elif (currentCorners[3]):
        led.draw_text2(120, 25, "$", 1)
    led.display()


def updateText():

    #ensures there are at least 2 items in the text queue
    if(len(textQueue) < 2):
        while(len(textQueue) < 2):
            textQueue.append("                    ")

    if((currentText[0] == "") & (currentText[1] == "")):
        currentText[0] = textQueue.pop(0)
        currentText[1] = textQueue.pop(0)
    else:
        currentText[0] = currentText[1]
        currentText[1] = textQueue.pop(0)

    led.draw_text2(0, 8, currentText[0], 1)
    led.draw_text2(0, 17, currentText[1], 1)

    print("Debug: current display: " + currentText[0] + "/" + currentText[1])

    led.display()

    # ##Most of the commented out stuff is what is used to actually display stuff to the screen.
    # offset = 0  # flips between 0 and 32 for double buffering
    #
    #     ## write the current time to the display on every other cycle
    #     if offset == 0:
    #         for i in range(0, len(list) - 1):
    #             text = list[i]
    #             text2 = list[i + 1]
    #             led.draw_text2(0, 10, text, 1)
    #             led.draw_text2(0, 19, text2, 1)
    #             led.display()
    #             time.sleep(1)
    #             led.clear_display()  # can be changed to change certain pixels
    #
    #
    #         led.draw_text2(0, 8, "123456789 10 11 12 13 14 15", 1)
    #         led.display()
    #         time.sleep(5)
    #         led.clear_display()
    #     else:
    #         time.sleep(1)
    #
    #         ##vertically scroll to switch between buffers
    #     for i in range(0, 32):
    #         offset = (offset + 1) % 64
    #         led.command(led.SET_START_LINE | offset)
    #         time.sleep(0.01)


def queueIncomingText(incomingText):
    from nltk.tokenize import regexp_tokenize
    regex = "([ ]|[ +]|[\n]|[\t])"
    wordList = regexp_tokenize(incomingText, regex, gaps=True, discard_empty=True)

    maxLineChars = 20
    displayLine = ""
    charCount = 0

    ##adds the number of characters for each of the tokenized words and makes sure its not over 16
    for i in range(0, len(wordList)):
        charCount = charCount + len(wordList[i])

        if charCount <= maxLineChars:
            displayLine += wordList[i]
        elif charCount > maxLineChars:

            if(len(displayLine) < maxLineChars):
                for j in range(len(displayLine), maxLineChars):
                    displayLine += (" ")

            textQueue.append(displayLine)
            print("Debug: " + displayLine + "\t\tadded to text queue.")
            displayLine = wordList[i]
            charCount = len(wordList[i])

    # gets the last char line
    if(len(displayLine) < maxLineChars):
        for j in range(len(displayLine), maxLineChars):
            displayLine += (" ")

    textQueue.append(displayLine)
    print("Debug: " + displayLine + " added to text queue.")

    print("Debug: End of incoming text.")

# def formatTXT(list):
#     ##Reads in a text file and tokenizes it
#     with open("test.txt", "read")as myfile:
#         data = myfile.read().replace('\n', '')
#
#     from nltk.tokenize import sent_tokenize, word_tokenize
#     list = word_tokenize(data)
#
#     maxDisplayChars = 16
#     displayChunk = ""
#     charCount = 0
#     listb = []
#     ##adds the number of characters for each of the tokenized words and makes sure its not over 16
#     for i in range(0, len(list) - 1):
#
#         charCount = charCount + len(list[i])
#
#         if charCount <= maxDisplayChars:
#
#             displayChunk += list[i] + " "
#             charCount = charCount + 1
#
#         elif charCount > maxDisplayChars:
#             listb.append(displayChunk[:-1])
#             displayChunk = list[i] + " "
#             charCount = len(list[i]) + 1
#         else:
#             print("list is empty")
#
#     print(listb)

# name of file as parameter and continue over writing file and keep open function(list of text,corners boolean if true put identifier)
