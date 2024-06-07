import RPi.GPIO as GPIO
import time
# for the control of the GPIO pins and do delay and measure time. 
GPIO.setmode(GPIO.BCM)# set pin mode to BCM?
GPIO.setwarnings(False)# remove warnings from configuring pins
TRIG =8# the GPIO pin number for the trigger pin
ECHO=10 # the GPIO pin number for the ECHO pin.
print ("Distance measurement")
GPIO.setup(TRIG,GPIO.OUT)# set trig pin as output
GPIO.setup(ECHO,GPIO.IN)# set echo pin as input
GPIO.output(TRIG,False)# initial val of trig is low
print("setting up sensor")
time.sleep(2)
GPIO.output(TRIG,True)# trig is set high for 0.00001 sec
time.sleep(0.00001)
GPIO.output(TRIG,False)# set trig to low
while GPIO.input(ECHO) ==0:# this start timer at start when echo is low. when echo is high it then ends time, to cal distance
    pulse_start =time.time()
while GPIO.input(ECHO)==1:
    pulse_end =time.time()
pulse_duration = pulse_end -pulse_start
distance = pulse_duration* 17150# this will find distance, using the speed of sound/2 in cm
distance =round(distance,2)# rounds the distance to 2 dp.
print ("Distance:",distance,"cm")
# stilllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll need to check the pinds we need to use for the trig and echo. also what are they. also, send the stop when less than 10cm away. 
# trig is set high to send the signal by ultrasound. the echo is high when signal is received back. 
if distance<=10:
    print("stop")
    # still need to be modified to send the signal by the I2C
