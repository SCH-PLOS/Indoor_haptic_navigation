from threading import Event

event = Event()
mag_event = Event()
left_event = Event()
right_event = Event()

dest_bearing = 'a'

heading_angle = 0
obs_angle = 0

aver_rssi = -100

now_loc = (-1,-1)
now_locs = (4,90,12)

ultra_left = 0.0
ultra_right = 0.0
