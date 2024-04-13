# Importing necessary libraries
import RPi.GPIO as GPIO  # Import the GPIO library for Raspberry Pi
import time  # Import the time library for time-related functions

# Setup Pin, Modes, etc...
GPIO.setmode(GPIO.BCM)  # Set the GPIO numbering mode to Broadcom (BCM)
GPIO.setwarnings(False)  # Disable warnings to prevent clutter
GPIO.setup(3, GPIO.OUT)  # Set 3 as an output pin for the LED

# Print 'LED ON' and 'LED OFF' with GPIO pins.
print("LED ON")
GPIO.output(3, GPIO.HIGH)  # Turn the LED on by setting the pin to HIGH
print("LED OFF")
GPIO.output(3, GPIO.LOW)  # Turn the LED off by setting the pin to LOW

# If you want continuous blinking, uncomment the following code.
# while True:  # Infinite loop to continuously blink the LED
#     print("LED ON")
#     GPIO.output(3, GPIO.HIGH)  # Turn the LED on
#     print("LED OFF")
#     GPIO.output(3, GPIO.LOW)  # Turn the LED off
#     time.sleep(1)  # Wait for 1 second before repeating the loop
