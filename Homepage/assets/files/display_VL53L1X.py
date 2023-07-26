import read_VL53L1X as dist

#ToF-Sensor am GPIO-Pin 23 wird aktiviert
dist.start_sensor(23)

#es werden 30 messwerte mit der for-schleife ausgegeben
for x in range(30):
    dist_mm=dist.get_distance()
    print("ToF-Sensor hinten - GPIO-Pin 23:")
    print("Entfernung: {}mm".format(dist_mm))

#gewählte ToF-sensor am GPIO-Pin 23 wird inaktiv gesetzt
dist.stop_sensor(23)
time.sleep(0.5)

#gewählte ToF-Sensor am GPIO-Pin 23 wird aktiviert
dist.start_sensor(24)
#es werden 30 messwerte mit der for-schleife ausgegeben
for x in range(30):
    #hier erfolgt der zugriff auf den aktiven tof-sensor
    dist_mm=dist.get_distance()
    print("ToF-Sensor hinten - GPIO-Pin 24:")
    print("Entfernung: {}mm".format(dist_mm))

#der gewählte sensor am GPIO-Pin 24 wird auf inaktiv gesetzt
dist.stop_sensor(24)



