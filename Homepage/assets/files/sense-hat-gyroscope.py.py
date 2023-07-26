
import sys,tty,termios,os,time


from sense_hat import SenseHat

#Drei Variablen der drei Achsen des Gyroskops auf 0 gesetzt. So werden Fehler verhindert falls Variablen leer sein sollten
x=0
y=0
z=0

sense=SenseHat()

sense.set_imu_config(False,True,False)

try:
    while True:
        x,y,z = sense.get_orientation().values()

        os.system('clear')

        print ("Orientierung mit dem Gyroskop:")
        print("Kippen x (pitch):"), round(x,2)
        print("Rollen y (roll):"), round(y,2)
        print("Drehen z (yaw):"), round(z,2)

        time.sleep(0,1)


except KeyboardInterrupt:
    sense.set_imu_config(False, False, False)