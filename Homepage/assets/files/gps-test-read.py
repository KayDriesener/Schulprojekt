#hier wird der GPS empfänger ausgelesen
import os
from gps import *
import time 
import subprocess


#Zaehler wie oft di Koordinaten ausgelesen worden sind
count=0 

#gpsd-daemon im hintergrund
print("Der gpsd-Daemon wird mit dem USB-Geraet /dev/ttyACMO gestartet.")
process=subprocess.Popen(["sudo","gpsd","-b","/dev/ttyACMO","-F","/var/run/gpsd.sock","-G"])
print("GPSD PID: ",process.pid)

print("Der gpsd-Daemon wurde gestartet.")
time.sleep(2)

#Erzeugen der Session für den Zugriff auf den Empfänger
session=gps(mode=WATCH_ENABLE)

try:
    while True:
        time.sleep(0.5)

        os.system('clear')
    #Ausgabe der Statuszeile, dass das Programm läuft
        print ('Auslesen der GPS-Koordinaten')

        count= count +1

    #Der Anwender wird über Lesezugriff informiert
        print("Zaehler: ",count,"Lesezugriffe")
        session.next()

        if session.fix.latitude==0.0:
            print('----------------------------------------------------')
            print('Es wurden keine GPS-Informationen empfangen')
            print('Wurde der gpsd-Daemon schon gestartet?')
            print('----------------------------------------------------')

        else:
            print('------------GPS-Informationen---------------')
            print('Breitengrad: ',session.fix.latitude)
            print('Laengengrad:', session.fix.longitude)
            print('Zeit utc: ', session.utc,\
                  session.fix.time)
            print('--------------------------------------------')

except KeyboardInterrupt:
    print("Programm beendet: ")


