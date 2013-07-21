import os, pickle, serial
from time import sleep

fifo = '/home/pi/.config/pianobar/ctl'
LCD = serial.Serial('/dev/ttyAMA0', 9600)

def writeToLCD(line1 = "", line2 = ""):

    if line2 == "" and len(line1) > 16:
        tempLine = line1
        line1 = tempLine[0:16]
        line2 = tempLine[16:len(tempLine)]
    
    LCD.open()

    LCD.write('\xFE\x01')
    LCD.write('\xFE\x80')
    LCD.write(lcdLine(line1))
    LCD.write('\xFE\xC0')
    LCD.write(lcdLine(line2))

    LCD.close()

def lcdLine(text):

    if len(text) > 16:
        choppedtext = text[0:13] + "..."
    else:
        choppedtext = text[0:len(text)]

    return choppedtext

def log(msg):

    f = open('pandorabox.log', 'a+')
    f.write(msg + '\n')
    f.close()

def parseAndWrite(secDelay = 0, changedStation = False):

    sleep(secDelay)

    log("parseAndWrite")

    if changedStation:
        writeToLCD("Listening To:", getShared("stationName"))
    else:
        writeToLCD(getShared("song"), getShared("artist"))

def getShared(key):

    fp = open("shared.pkl")
    shared = pickle.load(fp)
    fp.close()
    
    return shared[key]

def setShared(dictItems):

    fp = open("shared.pkl", "w")
    pickle.dump(dictItems, fp)
    fp.close()

def sendCommand(command):
    os.system('echo "' + command + '" >> ' + fifo)


