# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os
import loc
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Start_Pin = 7

floor_pin = 21
room_pin = 16

GPIO.setup(Start_Pin, GPIO.IN)
GPIO.setup(floor_pin, GPIO.IN)
GPIO.setup(room_pin, GPIO.IN)


# 목적지에 대한 정보 {좌표, 방위}
desination_coor = {
    'ML604': {'location':(6,65,13),'bearing':'n'},
    'startup': {'location':(6,71,13),'bearing':'e'},
    'parking_lot6': {'location':(6,65,19),'bearing':'n'}, 
    'toilet': {'location':(4,48,12),'bearing':'n'},
    'parking_lot4': {'location':(6,65,19),'bearing':'n'},
    'ground': {'location':(4,45,2),'bearing':'e'},
    'ML416': {'location':(4,56,12),'bearing':'s'},
    'ML417': {'location':(4,38,12),'bearing':'s'},
    'working': {'location':(4,72,12),'bearing':'n'}
}

floors = [4,6]
places = [['toilet','parking_lot4','ground','ML416','ML417','working'],
            ['parking_lot6','ML604','startup']]
floors_count = len(floors)

def set_dest():
    f_now = 0
    r_now = 0

    while True:
        if GPIO.input(floor_pin) == 0:      # 층 버튼이 눌리면
            f_now += 1
            if f_now == floors_count:
                f_now = 0
            floor_now = floors[f_now]
            os.system('omxplayer ./mp3/button/floor_'+floor_now+'.mp3')

        if GPIO.input(room_pin) == 0:       # 장소 버튼이 눌리면
            r_now += 1
            if r_now >= len(places[f_now]):
                r_now = 0
            place_now = places[f_now][r_now]
            os.system('omxplayer ./mp3/button/'+place_now+'.mp3')

        if GPIO.input(Start_Pin) == 0:
            break
        
    loc.dest_bearing = desination_coor[place_now]['bearing']
    return desination_coor[place_now]['location']


def detect_start():
    start_time = time.time()
    while True:
        if time.time() - start_time > 60:   # 1분 이상 버튼을 안누르면
            return 0
        if GPIO.input(Start_Pin) == 0:
            print("시작 버튼 눌림")
            os.system('omxplayer ./mp3/button/start_on.mp3')
            return 1
        else:
            print("--시작 버튼 감지 파트--")
            time.sleep(0.2)