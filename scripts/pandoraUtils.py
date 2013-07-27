import os, pickle, serial, fcntl
from time import sleep

FIFO = '/home/pi/.config/pianobar/ctl'
SHARED_FILE = 'shared.pkl'
LCD = serial.Serial('/dev/ttyAMA0', 9600)
CLEAR = '\xFE\x01'
TO_LINE1 = '\xFE\x80'
TO_LINE2 = '\xFE\xC0'

def writeToLCD(line1 = "", line2 = ""):

    if line2 == "" and len(line1) > 16:
        tempLine = line1
        line1 = tempLine[0:16]
        line2 = tempLine[16:len(tempLine)]
    
    LCD.open()

    LCD.write(CLEAR)
    LCD.write(TO_LINE1)
    LCD.write(lcdLine(line1))
    LCD.write(TO_LINE2)
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

    fp = open(SHARED_FILE)
    fcntl.lockf(fp, fcntl.LOCK_SH)

    shared = pickle.load(fp)

    fcntl.lockf(fp, fcntl.LOCK_UN)
    fp.close()
    
    return shared[key]


def setShared(dictItems):

    fp = open(SHARED_FILE, "w")
    fcntl.lockf(fp, fcntl.LOCK_EX)

    pickle.dump(dictItems, fp)

    fcntl.lockf(fp, fcntl.LOCK_UN)
    fp.close()


def sendCommand(command):
    os.system('echo "' + command + '" >> ' + FIFO)


