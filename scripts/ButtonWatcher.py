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

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)
GPIO.setup(BUTTON3, GPIO.IN)
GPIO.setup(BUTTON4, GPIO.IN)
GPIO.setup(BUTTON5, GPIO.IN)
GPIO.setup(BUTTON6, GPIO.IN)

def main():

    state.current_menu = Page1()

    GPIO.add_event_detect(BUTTON1, GPIO.FALLING, bouncetime=500)
    GPIO.add_event_detect(BUTTON2, GPIO.FALLING, bouncetime=500)
    GPIO.add_event_detect(BUTTON3, GPIO.FALLING, bouncetime=500)
    GPIO.add_event_detect(BUTTON4, GPIO.FALLING, bouncetime=500)
    GPIO.add_event_detect(BUTTON5, GPIO.FALLING, bouncetime=500)
    GPIO.add_event_detect(BUTTON6, GPIO.FALLING, bouncetime=500)

    while True:

        if (GPIO.event_detected(BUTTON1)):

            state.current_menu.button1()


        if (GPIO.event_detected(BUTTON2)):

            state.current_menu.button2()


        if (GPIO.event_detected(BUTTON3)):

            state.current_menu.button3()


        if (GPIO.event_detected(BUTTON4)):

            state.current_menu.button4()


        if (GPIO.event_detected(BUTTON5)):

            state.current_menu.button5()

            
        if (GPIO.event_detected(BUTTON6)):

            state.current_menu.button6()


        sleep(.25)


main()

