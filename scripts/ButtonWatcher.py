#!/usr/bin/env python
 
import RPi.GPIO as GPIO
from time import sleep
import state
from menupage1 import Page1

BUTTON1 = 4
BUTTON2 = 17
BUTTON3 = 21
BUTTON4 = 22
BUTTON5 = 10
BUTTON6 = 9

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)
GPIO.setup(BUTTON3, GPIO.IN)
GPIO.setup(BUTTON4, GPIO.IN)
GPIO.setup(BUTTON5, GPIO.IN)
GPIO.setup(BUTTON6, GPIO.IN)

def main():

    state.current_menu = Page1()

    while True:

        # Default Page

        if (GPIO.input(BUTTON1) == False):

            state.current_menu.button1()


        if (GPIO.input(BUTTON2) == False):

            state.current_menu.button2()


        if (GPIO.input(BUTTON3) == False):

            state.current_menu.button3()


        if (GPIO.input(BUTTON4) == False):

            state.current_menu.button4()


        if (GPIO.input(BUTTON5) == False):

            state.current_menu.button5()

            
        if (GPIO.input(BUTTON6) == False):

            state.current_menu.button6()


        sleep(.25)


main()
