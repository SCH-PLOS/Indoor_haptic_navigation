# -*- coding: utf-8 -*-

from collections import deque

# as gm
group_by_mac = {                        # 비콘의 그룹을 찾기 위한 딕셔너리
    "00:19:01:73:ec:80":(4,108,12),
    "00:19:01:73:e2:31":(4,108,12),
    "00:19:01:72:9e:d9":(4,100,12),
    "00:19:01:73:ee:62":(4,100,12),
    "00:19:01:70:82:af":(4,90,12),
    "00:19:01:73:ee:74":(4,90,12),
    "00:19:01:73:ec:11":(4,81,12),
    "00:19:01:73:e7:b7":(4,81,12),
    "00:19:01:72:9e:89":(4,72,12),
    "00:19:01:73:e7:1b":(4,72,12),
    "00:19:01:73:e2:1d":(4,72,19),
    "00:19:01:73:ec:a9":(4,72,19),
    "00:19:01:73:ee:53":(4,65,19),
    "00:19:01:73:ee:4a":(4,65,19),
    "00:19:01:72:9e:c7":(4,65,12),
    "00:19:01:73:ec:30":(4,65,12),
    "00:19:01:73:ec:ac":(4,56,12),
    "00:19:01:70:80:d9":(4,56,12),
    "00:19:01:72:9e:eb":(4,48,12),
    "00:19:01:73:e2:a8":(4,48,12),
    "00:19:01:73:e4:c5":(4,45,12),
    "00:19:01:73:ee:af":(4,45,12),
    "00:19:01:73:f3:0a":(4,38,12),
    "00:19:01:73:f3:2e":(4,38,12),
    "00:19:01:72:a1:75":(4,45,2),
    "00:19:01:72:9e:f1":(4,45,2),
    "00:19:01:73:ec:2f":(6,65,19),
    "00:19:01:73:e4:83":(6,65,19),
    "00:19:01:73:e3:56":(6,65,13),
    "00:19:01:73:ee:36":(6,65,13),
    "00:19:01:72:a1:7b":(6,71,13),
    "00:19:01:72:9e:dd":(6,71,13),
    "00:19:01:73:eb:ff":(6,56,13),
    "00:19:01:73:f5:c9":(6,56,13),
    "00:19:01:73:ee:c3":(6,45,13),
    "00:19:01:73:ee:87":(6,45,13),
}

# as gr
group_rssi = {              # 그룹별로 rssi를 저장할 수 있는 딕셔너리 큐 생성
    (4,108,12):deque(),
    (4,100,12):deque(),
    (4,90,12):deque(),
    (4,81,12):deque(),
    (4,72,12):deque(),
    (4,72,19):deque(),
    (4,65,19):deque(),
    (4,65,12):deque(),
    (4,56,12):deque(),
    (4,48,12):deque(),
    (4,45,12):deque(),
    (4,38,12):deque(),
    (4,45,2):deque(),
    (4,64,17):deque(),
    (4,64,11):deque(),
    (4,71,11):deque(),
    (4,79,11):deque(),
    (6,65,19):deque(),
    (6,65,13):deque(),
    (6,71,13):deque(),
    (6,56,13):deque(),
    (6,45,13):deque(),
}

def clean_dq():             
    for k,v in group_rssi.items():
        group_rssi[k].clear()

