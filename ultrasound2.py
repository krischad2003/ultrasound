from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor 
# we use threading for threading. the lib bpiozero has distancesensor which is good for distance detection. 

reading = True # controls if we should continue reading or not. 
sensor = DistanceSensor(echo=8, trigger=10)# initialize object with pins for echo and trigger

def safe_exit(signum, frame): # the function wait to be called when there is sigterm, sighup
    exit(1)

def read_distance():# reads tje distance  from sensor.val as 2dp.
    while reading:
        message = f"Distance: {sensor.value:1.2f} m"
        print(message)
        if sensor.value< 0.1:
                print("stop")# will nee
        else:
                print("go")


        sleep(0.1)
# try runs with multi threads and then stops, until the condition for execpt block is met, where it pass to finally. 
try:# when signterm or sigup is received, it will call safeexit
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    reader = Thread(target=read_distance, daemon=True)# thread to call the distance function, and closes when end bc of daemon=true
    reader.start()# start the thread

    pause()

except KeyboardInterrupt:# ctrl c to exit
    pass

finally:# this is runned after the ctrl c is used, so that we stop reading. 
    reading = False
    reader.join()       
    sensor.close()