import socket, logging
from time import sleep
import menubase, menupage3
import pandoraUtils, state

class Page2(menubase.Base):
    """PandoraBox menu page 2"""

    def __init__(self):
        self.logger = logging.getLogger('MenuPage2')


    def show_menu(self):
        pandoraUtils.writeToLCD("Pandora Pi", "Menu")
        sleep(.75)

        pandoraUtils.writeToLCD("1:Like 2:Dislike", "3:IP 4:Next Pg")

    def button1(self):
        self.logger.info('Page 2 - Button 1 - Like')

        pandoraUtils.writeToLCD("Liking", pandoraUtils.getShared("song"))
        pandoraUtils.sendCommand('+')

        pandoraUtils.parseAndWrite(2)


    def button2(self):
        self.logger.info('Page 2 - Button 2 - DisLike')

        pandoraUtils.writeToLCD("Disliking", pandoraUtils.getShared("song"))
        pandoraUtils.sendCommand('-')

        pandoraUtils.parseAndWrite(2)


    def button3(self):
        self.logger.info('Page 2 - Button 3 - IP Address')
        IPaddr = getIPAddress()
        pandoraUtils.writeToLCD("IP Address:", IPaddr)

        pandoraUtils.parseAndWrite(5)


    def button6(self):
        self.logger.info('Page 2 - Button 6 - Menu')

        state.current_menu = menupage3.Page3()
        state.current_menu.show_menu()


    def getIPAddress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        IPaddr = s.getsockname()[0]
        return IPaddr
    

