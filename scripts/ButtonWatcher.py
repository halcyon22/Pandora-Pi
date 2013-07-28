#!/usr/bin/env python
 
import RPi.GPIO as GPIO
from time import sleep
import state
from menupage1 import Page1

# GPIO.BCM channel numbers
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

state.current_menu = Page1()

def callback_button1(channel):
    state.current_menu.button1()

def callback_button2(channel):
    state.current_menu.button2()

def callback_button3(channel):
    state.current_menu.button3()

def callback_button4(channel):
    state.current_menu.button4()

def callback_button5(channel):
    state.current_menu.button5()

def callback_button6(channel):
    state.current_menu.button6()

BUTTONBOUNCE = 500
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=callback_button1, bouncetime=BUTTONBOUNCE)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=callback_button2, bouncetime=BUTTONBOUNCE)
GPIO.add_event_detect(BUTTON3, GPIO.FALLING, callback=callback_button3, bouncetime=BUTTONBOUNCE)
GPIO.add_event_detect(BUTTON4, GPIO.FALLING, callback=callback_button4, bouncetime=BUTTONBOUNCE)
GPIO.add_event_detect(BUTTON5, GPIO.FALLING, callback=callback_button5, bouncetime=BUTTONBOUNCE)
GPIO.add_event_detect(BUTTON6, GPIO.FALLING, callback=callback_button6, bouncetime=BUTTONBOUNCE)

while state.run:
    sleep(.5)


