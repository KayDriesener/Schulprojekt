import time
import VL53L1X

import RPi.GPIO as io
io.setmode(io.BCM)

tof=VL53L1X.VL53L1X(i2c_bus=1,i2c_address=0x29)

def start_sensor(number):
    io.setup(number,io.OUT)
    io.setup(number,True)
    time.sleep(0.2)

    tof.open()
    tof.start_ranging(1)

def stop_sensor(number):
    tof.stop_ranging()
    io.output(number,False)

def get_distance():
    distance_in_mm=0
    distance_in_mm=tof.get_distance()
    return distance_in_mm
    