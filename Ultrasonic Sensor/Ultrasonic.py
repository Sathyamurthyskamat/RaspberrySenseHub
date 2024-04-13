# Importing necessary libraries
import RPi.GPIO as Gpio  # Using "Gpio" as an alias for RPi.GPIO
import time

# Set GPIO mode to BOARD (physical pin numbering)
Gpio.setmode(Gpio.BOARD)
Gpio.setwarnings(False)  # Disable GPIO warnings
Gpio.setup(8, Gpio.OUT)  # Set pin 8 as output

# Define GPIO pins for ultrasonic sensor
Gpio_TRIGGER = 10  # Trigger pin
Gpio_ECHO = 12     # Echo pin

# Set GPIO pin directions (Trigger as OUTPUT, Echo as INPUT)
Gpio.setup(Gpio_TRIGGER, Gpio.OUT)
Gpio.setup(Gpio_ECHO, Gpio.IN)

# Function to measure distance using ultrasonic sensor
def distance():
    Gpio.output(Gpio_TRIGGER, True)  # Set Trigger pin to HIGH
    time.sleep(0.00001)              # Wait for a short duration
    Gpio.output(Gpio_TRIGGER, False) # Set Trigger pin back to LOW

    StartTime = time.time()  # Record the start time
    StopTime = time.time()   # Record the stop time

    # Wait for the Echo pin to go HIGH (start of pulse)
    while Gpio.input(Gpio_ECHO) == 0:
        StartTime = time.time()

    # Wait for the Echo pin to go LOW again (end of pulse)
    while Gpio.input(Gpio_ECHO) == 1:
        StopTime = time.time()

    # Calculate the time difference between start and stop
    TimeElapsed = StopTime - StartTime

    # Calculate distance based on the speed of sound
    # (divided by 2 because sound travels to the object and back)
    distance = (TimeElapsed * 34300) / 2

    return distance

# Main program
if __name__ == '__main__':
    try:
        while True:
            dist = distance()  # Get distance from the ultrasonic sensor
            print("Measured Distance = %.1f cm" % dist)  # Print the distance
            time.sleep(1)  # Wait for 1 second

            # Example: Control an output based on distance
            # Uncomment and modify as needed
            
            #if dist < 10:
            #    Gpio.output(8, Gpio.HIGH)  # Turn ON an output
            #    time.sleep(3)  # Wait for 3 seconds
            #    Gpio.output(8, Gpio.LOW)  # Turn OFF the output
            #    time.sleep(1)  # Wait for 1 second
            
            
    except KeyboardInterrupt:  # Handle CTRL+C interrupt
        print("Measurement stopped by User")
        Gpio.cleanup()  # Clean up GPIO resources
