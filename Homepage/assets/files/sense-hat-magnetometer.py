import sys,tty,termios,os,time

from sense_hat import SenseHat

degree=0

sense=SenseHat()

sense.set_imu_config(True,False,False)

s_h_direction=180

new_degree=0

try:
    while True:
        north=sense.get_compass()
        degree=float(north)

        new_degree = degree
        if degree <=s_h_direction and s_h_direction !=0:
            new_degree=degree + s_h_direction
        else:
            new_degree =degree - s_h_direction

        os.system('clear')

        print("Orienterung mit dem Kompass:")
        print("Nordrichtung: %s" %round(new_degree,1))

        time.sleep(0.1)
except KeyboardInterrupt:
    sense.set_imu_config(False,False,False)