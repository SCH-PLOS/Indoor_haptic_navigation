# -*- coding: utf-8 -*-

import io
import blescan
import sys
import bluetooth._bluetooth as bluez
import json
import threading
import time
from collections import Counter
import loc

with io.open('./pair.json') as f:
    info = json.load(f)

beacon_list =[]
pairs = []

dev_id = 0 #scan

#========================================== Definition Of Functions ==================================
def find_pair(mac):
    my_group = info[mac]["group"]
    return my_group


def get_loc():
    return loc.now_loc


def get_rssi():
    return loc.aver_rssi


def location_thread():
    best = []   # 현재 위치(그룹)을 모아 놓은 리스트

    if loc.event.is_set():
        print('Location thread stopped!')
        return

    try:
        sock = bluez.hci_open_dev(dev_id)
        print("ble thread started")

    except:
        print ("error accessing bluetooth device...")
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    beacon_list = []
    while True:
        returnedList = blescan.parse_events(sock, 10)

        for beacon in returnedList:
            if beacon[:5] == "00:19":                       # fc 친구들만 모아
                beacon = beacon.split(",")
                beacon_list.append([beacon[0],beacon[5]])   # MAC, RSSI만 리스트에 넣기

            pair = []                                       # 비콘의 맥, 그룹, rssi
            if len(beacon_list) == 20:                      # 그룹 매칭 단위
                for g in beacon_list:
                    # g[0]: MAC, g[1]: RSSI
                    pair.append([g[0],tuple(find_pair(g[0])),g[1]])    # MAC과 그룹 번호 저장

                result = []                                 # rssi, 그룹 / 커플만 있음.
                i = 0

                for j in pair:
                    for k in pair[i+1:]:                    # pair 전체를 돌면서 쌍 매칭
                        # j[0]: MAC, j[1]: 그룹, j[2]:rssi
                        if j[0] != k[0] and j[1] == k[1]:   # 맥은 다르고 그룹이 같으면
                            j[2] = int(j[2])                
                            aver = int((int(k[2])+int(j[2]))//2)
                            result.append([aver,j[1]])
                    i += 1
                    
                if len(result) > 0:                         # 비콘 그룹이 있을 때
                    group = max(result)
                    loc.aver_rssi = group[0]
                    best.append(group[1])

                beacon_list = []
                if len(best) == 3:                          # 현위치 3개가 모였을 때, 최빈 값 찾는 코드
                    best_count = Counter(best).most_common(1)

                    loc.now_loc = best_count[0][0]
                    best = []


if __name__ == "__main__":
    location_thread()
