#!/usr/bin/env python
 
import RPi.GPIO as GPIO
import time
import pandoraUtils, state
import menupage1

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

pandoraUtils.initLogging()
state.current_menu = menupage1.Page1()
time_stamp = time.time()

def callback_button1(channel):
    if (attendEdge()):
        state.current_menu.button1()

def callback_button2(channel):
    if (attendEdge()):
        state.current_menu.button2()

def callback_button3(channel):
    if (attendEdge()):
        state.current_menu.button3()

def callback_button4(channel):
    if (attendEdge()):
        state.current_menu.button4()

def callback_button5(channel):
    if (attendEdge()):
        state.current_menu.button5()

def callback_button6(channel):
    if (attendEdge()):
        state.current_menu.button6()

def attendEdge():
    global time_stamp
    time_now = time.time()

    if (time_now - time_stamp) >= 0.5:
        time_stamp = time_now
        return True
    else:
        return False


GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=callback_button1)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=callback_button2)
GPIO.add_event_detect(BUTTON3, GPIO.FALLING, callback=callback_button3)
GPIO.add_event_detect(BUTTON4, GPIO.FALLING, callback=callback_button4)
GPIO.add_event_detect(BUTTON5, GPIO.FALLING, callback=callback_button5)
GPIO.add_event_detect(BUTTON6, GPIO.FALLING, callback=callback_button6)

try:
    while state.run:
        time.sleep(.5)
finally:
    GPIO.cleanup()


