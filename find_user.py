# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
from button import *

PIR1 = 23
PIR2 = 24
GPIO.setup(PIR1, GPIO.IN)
GPIO.setup(PIR2, GPIO.IN)

def detecting_people():
    while True:
        # PIR 센서 중 하나라도 사람이 인식되면
        if GPIO.input(PIR1) or GPIO.input(PIR2):
            print(GPIO.input(PIR1),GPIO.input(PIR2))
            
            os.system('omxplayer ./mp3/find_user/start_first.mp3')
            os.system('omxplayer ./mp3/find_user/explan_first1.mp3')
            time.sleep(3)
            os.system('omxplayer ./mp3/find_user/explan_first2.mp3')
            print('---PIR 감지 후 버튼 입력 대기 중---')
            
            if detect_start() == 1:     # 시작 버튼이 눌리면
               os.system('omxplayer ./mp3/find_user/dest_button_explan.mp3')
               return 1
        else:
            print("---주변에 사용자 없음---")
            time.sleep(0.1)

