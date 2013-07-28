from time import sleep
#from subprocess import Popen
from menubase import Base
import logging
import pandoraUtils, state

class Page3(Base):
    """PandoraBox menu page 3"""

    def __init__(self):
        self.logger = logging.getLogger('MenuPage3')


    def show_menu(self):
        pandoraUtils.writeToLCD("1:Current Station", "2:Off 6:Now Playing")


    def button1(self):
        self.logger.info('Page 3 - Button 1 - Current Station')

        pandoraUtils.writeToLCD(pandoraUtils.getShared("stationName"))
        pandoraUtils.parseAndWrite(2)


    def button2(self):
        self.logger.info('Page 3 - Button 2 - Off')

        pandoraUtils.writeToLCD("Disliking", pandoraUtils.getShared("song"))
        pandoraUtils.sendCommand('-')

        pandoraUtils.parseAndWrite(2)


        # if (GPIO.input(BUTTON3) == False  and current_screen == "menupg2"):

        #   self.logger.info('Button 6 - Menu - Sub 3 - Shutdown')
        #   pandoraUtils.writeToLCD("Shutting Down", "Thanks")
        #   pianobarProcess.terminate()
        #   # os.system('echo "q" >> ' + fifo)

        #   sleep(2)

        #   pandoraUtils.writeToLCD("Pandora Pi: OFF", "1: Turn ON")
        #   current_screen = "off"

        # if ( GPIO.input(BUTTON1) == False  and current_screen == "off"):

        #   pianobarProcess = Popen('sudo -u pi pianobar', shell=True)

        #   PandoraUtils.writeToLCD("Pandora Pi", "Starting")

        #   current_screen = "default"

        #   sleep(4)

        #   pandoraUtils.parseAndWrite()



    def button6(self):
        self.logger.info('Page 3 - Button 6 - Now Playing')

        pandoraUtils.parseAndWrite()


