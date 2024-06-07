import RPi.GPIO as GPIO
import time
from threading import Thread

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Set pin mode to BCM
GPIO.setwarnings(False)  # Remove warnings from configuring pins
TRIG = 8  # The GPIO pin number for the trigger pin
ECHO = 10  # The GPIO pin number for the ECHO pin

# Initialize the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)  # Set TRIG pin as output
GPIO.setup(ECHO, GPIO.IN)  # Set ECHO pin as input
GPIO.output(TRIG, False)  # Initial value of TRIG is low

def measure_distance():
    # Trigger the sensor
    GPIO.output(TRIG, True)  # TRIG is set high
    time.sleep(0.00001)  # Delay for 10 microseconds
    GPIO.output(TRIG, False)  # Set TRIG to low

    # Wait for the echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for the echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Calculate distance in cm
    distance = round(distance, 2)  # Round to 2 decimal places

    # Print the distance
    print("Distance:", distance, "cm")

    # Check if the distance is less than 10 cm
    if distance <= 10:
        print("stop")
    else:
        print("go")

def main():
    try:
        print("Distance measurement")
        print("Setting up sensor")
        time.sleep(2)  # Allow sensor to settle

        while True:
            # Start a new thread for each measurement
            reader = Thread(target=measure_distance)
            reader.start()
            reader.join()  # Wait for the thread to finish before starting a new one

            # Delay before next measurement
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted")
    
    finally:
        # Cleanup
        GPIO.cleanup()

if __name__ == "__main__":
    main()
