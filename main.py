# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import threading
import os
from threading import Event, Thread
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

from find_user import *
from button import *
from ultra import *
from vibration import *
from location import *
from find_route_coor import *
from geo_navigate import *
from read_magn_data import *
import loc


MAG_SCL = 3
MAG_SDA = 2

# 사용 - 1 / 대기 - 0
USING = 0
done  = 0
loc_thread = 0


def intro():
    global USING
    global loc_thread

    while True:
        if USING == 1:
            lth = Thread(target=location_thread)
            lth.daemon =True
            lth.start()                     # 위치 탐색 스레드 시작
            
            try:
                gth = Thread(target=geomagnetic_thread)
                gth.daemon = True
                gth.start()                 # 방향 파악 스레드 시작
            except Exception as e:
                print(e)

            loc_thread = 1

            DEST = set_dest()        # 목적지 정보 획득
            os.system('omxplayer ./mp3/main2/set_dest_final2.mp3')
            print("Your destination is "+str(DEST))

            roth = Thread(target=right_obstacle)    # 장애물 파악 스레드 시작
            roth.daemon = True
            roth.start()

            loth = Thread(target=left_obstacle)
            loth.daemon = True
            loth.start()
            
            os.system('omxplayer ./mp3/main2/move_final.mp3')
            
            perform(DEST)

        elif USING == 0:
            if loc_thread == 1:
                loc_thread = 0
                loc.event.set()
                loc.mag_event.set()
                loc.left_event.set()
                loc.right_event.set()

            USING = detecting_people()


def perform(DEST):   
    global done
    global USING
    done = navigate(DEST)         # 경로 탐색 + 안내, 목적지 도착할 때까지 못빠져나옴.
    
    if done:
        os.system('omxplayer ./mp3/main2/arrive_dest.mp3')
        print("목적지에 도착했습니다.")
        USING = 0


if __name__ == "__main__":
    intro()        
