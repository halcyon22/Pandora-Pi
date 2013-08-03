import menubase, menupage2
from random import randint
import logging
import pandoraUtils, state

class Page1(menubase.Base):
    """PandoraBox menu page 1"""

    def __init__(self):
        self.logger = logging.getLogger('MenuPage1')

    def button1(self):
        self.logger.info('Page 1 - Button 1 - Skip Song')

        pandoraUtils.writeToLCD("Skipping", "Song")
        pandoraUtils.sendCommand('n')


    def button2(self):
        self.logger.info('Page 1 - Button 2 - Next Station')

        current_station = pandoraUtils.getShared("stationNumber")
        station_count = pandoraUtils.getShared("stationCount")
        next_station = current_station + 1
        if (next_station >= station_count):
            next_station = 0

        self.logger.info('next station: '+str(next_station))

        pandoraUtils.writeToLCD("Next", "Station")
        pandoraUtils.sendCommand('s'+str(next_station))

        # "listening to .."
        pandoraUtils.parseAndWrite(8, True)
        # display song
        pandoraUtils.parseAndWrite(3)


    def button3(self):
        self.logger.info('Page 1 - Button 3 - Vol Down')
    
        pandoraUtils.writeToLCD("Volume", "Down")
        pandoraUtils.sendCommand('((((')

        pandoraUtils.parseAndWrite(2)


    def button4(self):
        self.logger.info('Page 1 - Button 4 - Vol Up')

        pandoraUtils.writeToLCD("Volume", "Up")
        pandoraUtils.sendCommand('))))')

        pandoraUtils.parseAndWrite(2)


    def button5(self):
        self.logger.info('Page 1 - Button 5 - Play/Pause')

        if state.playing_stream == "Playing":
            pandoraUtils.writeToLCD("Paused")
            state.playing_stream = "Paused"
        else:
            pandoraUtils.writeToLCD("Playing")
            state.playing_stream = "Playing"
            pandoraUtils.parseAndWrite(2)

        pandoraUtils.sendCommand('p')


    def button6(self):
        self.logger.info('Page 1 - Button 6 - Menu')

        state.current_menu = menupage2.Page2()
        state.current_menu.show_menu()


