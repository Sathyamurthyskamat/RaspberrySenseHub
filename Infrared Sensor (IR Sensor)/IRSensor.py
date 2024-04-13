# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Define GPIO pins for the sensor and buzzer
sensor = 16
buzzer = 18

# Set GPIO mode to BOARD (physical pin numbering)
GPIO.setmode(GPIO.BOARD)

# Setup GPIO pins for sensor as input and buzzer as output
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

# Initially turn off the buzzer
GPIO.output(buzzer, False)

try:
    # Start an infinite loop to continuously monitor the sensor
    while True:
        # Check if the sensor detects an object
        if GPIO.input(sensor):
            # If object detected, turn on the buzzer and print a message
            GPIO.output(buzzer, True)
            print("Object Detected")
            
            # Wait and check if the object is still detected, to avoid continuous buzzing
            while GPIO.input(sensor):
                time.sleep(0.2)
        else:
            # If no object detected, turn off the buzzer
            GPIO.output(buzzer, False)

except KeyboardInterrupt:
    # Clean up GPIO settings on keyboard interrupt
    GPIO.cleanup()
