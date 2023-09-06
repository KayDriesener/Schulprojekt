#import ledmatrix as matrix


#text=temperatur, luftdruck, leuftfeuchtigkeit// 23 ist nur ein beispiel// ERSTMAL ANY 
#matrix.display_message(text=23,txt_colour=any,bg_color=any,speed=any)

import sys,tty,termios,os,time

from sense_hat import SenseHat
import ledmatrix as matrix

sense = SenseHat()

#versuchen auf sense hat sensoren zugreifen
#es sollen die Temperaturen auf Luftdruck, Luftfeuchtigkeit und Temperatur ausgelesen werden.
try:
    while True:
        temp=sense.get_temperatur()
        pres=sense.get_pressure()
        humi=sense.get_humidity()

    #Die ausgelesenen werte werden auf eine stelle nach dem Komma gerundet
        temp=round(temp,1)
        pres=round(pres,1)
        humi=round(humi,1)
#Farben Rot und grüen
        if temp >20 and temp<27:
        bg= [0,100,0]
        else:
        bg=[100,0,0]

        msg="Temp=%s,Press=%s,Humi=%s"%(temp,press,humi)

        matrix.display_message(msg,[250,250,50],bg,0.06)

except KeyboardInterrupt:
    sense.set_imu_config(False,False,False)