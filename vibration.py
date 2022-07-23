# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
LEFT = 12
RIGHT = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)


def vib_left():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')

def vib_right():
	GPIO.output(RIGHT, True)
	os.system('omxplayer ./mp3/vibration/right.mp3')

def vib_stop():
    GPIO.output(LEFT, False)
    GPIO.output(RIGHT, False)

def vib_left_2s():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')# 좌회전 음성
	#time.sleep(2)
	GPIO.output(LEFT, False)

def vib_right_2s():
	GPIO.output(RIGHT, True)
	os.system('omxplayer ./mp3/vibration/right.mp3') 
	time.sleep(2)
	GPIO.output(RIGHT, False)

def vib_left_4s():					# time은 회전 각도에 따라
	GPIO.output(LEFT, True)
	os.system('omxplayer ./mp3/vibration/left.mp3')
	time.sleep(4)
	GPIO.output(LEFT, False)

def vib_right_for(t):
    GPIO.output(RIGHT, True)
    os.system('omxplayer ./mp3/vibration/obstacle_left_2.mp3')
    time.sleep(t)
    GPIO.output(RIGHT, False)

def vib_left_for(t):
    GPIO.output(LEFT, True)
    os.system('omxplayer ./mp3/vibration/obstacle_right_2.mp3')
    time.sleep(t)
    GPIO.output(LEFT, False)