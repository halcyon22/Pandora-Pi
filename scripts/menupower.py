from subprocess import Popen
import menubase, menupage1
import logging
import pandoraUtils, state

class MenuPower(menubase.Base):
    """PandoraBox power menu"""

    def __init__(self):
        self.logger = logging.getLogger('MenuPower')


    def show_menu(self):
        pandoraUtils.writeToLCD("Pandora OFF", "1: Start Pandora")


    def button1(self):
        self.logger.info('Power - Button 1 - Start Pandora')

        pandoraUtils.writeToLCD("Pandora Pi", "Starting")
        Popen('sudo -u pi pianobar', shell=True)
        state.current_menu = menupage1.Page1()


