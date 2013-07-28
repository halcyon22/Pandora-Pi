import os, pickle, serial, fcntl, logging
from time import sleep

FIFO = '/home/pi/.config/pianobar/ctl'
SHARED_FILE = 'shared.pkl'

LCD = serial.Serial()
LCD.port = '/dev/ttyAMA0'
CLEAR = '\xFE\x01'
TO_LINE1 = '\xFE\x80'
TO_LINE2 = '\xFE\xC0'

logger = logging.getLogger('pandoraUtils')

def writeToLCD(line1 = "", line2 = ""):

    if line2 == "" and len(line1) > 16:
        tempLine = line1
        line1 = tempLine[0:16]
        line2 = tempLine[16:len(tempLine)]

    try:
        LCD.open()
        LCD.write(CLEAR)
        LCD.write(TO_LINE1)
        LCD.write(lcdLine(line1))
        LCD.write(TO_LINE2)
        LCD.write(lcdLine(line2))
    except (serial.SerialException, serial.portNotOpenError):
        pass
    finally:
        if LCD.isOpen():
            LCD.close()


def lcdLine(text):

    if len(text) > 16:
        choppedtext = text[0:13] + "..."
    else:
        choppedtext = text[0:len(text)]

    return choppedtext


def initLogging():
    logging.basicConfig(filename='pandorabox.log', level=logging.DEBUG,
                        format='%(asctime)s %(name)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def parseAndWrite(secDelay = 0, changedStation = False):

    sleep(secDelay)

    logger.debug("parseAndWrite")

    if changedStation:
        writeToLCD("Listening To:", getShared("stationName"))
    else:
        writeToLCD(getShared("song"), getShared("artist"))


def getShared(key):

    try:
        with open(SHARED_FILE) as fp:
            fcntl.lockf(fp, fcntl.LOCK_SH)
            shared = pickle.load(fp)
            return shared[key]
    except IOError:
        return None


def setShared(dictItems):

    with open(SHARED_FILE, "w") as fp:
        fcntl.lockf(fp, fcntl.LOCK_EX)
        pickle.dump(dictItems, fp)


def sendCommand(command):
    os.system('echo "' + command + '" >> ' + FIFO)


