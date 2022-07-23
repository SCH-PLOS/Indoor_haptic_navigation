# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import *
from vibration import *
import threading
import loc
from location import *
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG1 = 25 #좌측
ECHO1 = 8

TRIG2 = 22 #우측
ECHO2 = 27

GPIO.setup(TRIG1, GPIO.IN)
GPIO.setup(ECHO1, GPIO.IN)

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
time.sleep(1.5)


def left_obstacle():
    while True:
        if loc.left_event.is_set():
            print("Ultrasound thread stopped!")
            return

        GPIO.output(TRIG1, False)
        time.sleep(0.1)
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)

        while GPIO.input(ECHO1) == 0:
            start = time.time()
        
        while GPIO.input(ECHO1) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm " % distance)
        time.sleep(0.1)

        if (distance < 150):                        
            print("There is obstacle on your left !")
            vib_left_for(0.1)
            sleep(0.2)
            vib_right_for(0.8)


def right_obstacle():
    while True:
        if loc.right_event.is_set():
            print("Ultrasound thread stopped!")
            return

        GPIO.output(TRIG2, False)
        time.sleep(0.1)
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)

        while GPIO.input(ECHO2) == 0:
            start = time.time()
        
        while GPIO.input(ECHO2) == 1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm " % distance)
        time.sleep(0.1)

        if (distance < 150):                        
            print("There is obstacle on your right !")
            vib_left_for(0.1)
            sleep(0.2)
            vib_right_for(0.8)