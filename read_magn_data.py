# -*- coding: utf-8 -*-
'''!
  @file read_magn_data.py
  @brief Through the example, you can get the sensor data by using getSensorData:
  @n     get magnetometer data of sensor.
  @n     With the rotation of the sensor, data changes are visible.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [luoyufeng] (yufeng.luo@dfrobot.com)
  @maintainer [Fary](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2021-10-20
  @url https://github.com/DFRobot/DFRobot_BMX160
'''
import sys
sys.path.append('../../')
import time
from DFRobot_BMX160 import BMX160
import math
import loc

pi          = 3.1415926535897932385
bmx = BMX160(1)

#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)


def main():
    while True:
        data= bmx.get_all_data()
        time.sleep(0.2)
        print("magn: x: {0:.2f} uT, y: {1:.2f} uT, z: {2:.2f} uT".format(data[0],data[1],data[2]))

        heading = math.atan2(data[1], data[0])
                
        #Due to declination check for >360 degree
        if(heading > 2*pi):
                heading = heading - 2*pi

        #check for sign
        if(heading < 0):
                heading = heading + 2*pi

        #convert into angle
        heading_angle = int(heading * 180/pi)

        print ("Heading Angle = %d°" %heading_angle)
        angle = math.atan2(data[1],data[0])*180/pi+180;
        print("angle: %d" %angle)
        print(" ")


def geomagnetic_thread():
    while True:
        if loc.mag_event.is_set():
            print('Geomagnetic thread stopped!')
            return

        data= bmx.get_all_data()
        time.sleep(0.2)

        angle = math.atan2(data[1],data[0])*180/pi+180
        # print("angle: %d" %angle)
        loc.heading_angle = int(angle)
        loc.obs_angle = int(angle)


def get_angle():
    return loc.heading_angle


if __name__ == "__main__":
    main()