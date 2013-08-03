from time import sleep
import menubase, menupage1, menupower
import logging
import pandoraUtils, state

class Page3(menubase.Base):
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

        pandoraUtils.writeToLCD("Shutting Down", "Thanks")
        pandoraUtils.sendCommand('q')

        sleep(2)
        state.current_menu = menupower.MenuPower()
        state.current_menu.show_menu()


    def button6(self):
        self.logger.info('Page 3 - Button 6 - Now Playing')

        state.current_menu = menupage1.Page1()
        pandoraUtils.parseAndWrite()


