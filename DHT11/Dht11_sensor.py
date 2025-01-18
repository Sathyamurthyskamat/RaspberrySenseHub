import Adafruit_DHT
import time

# Set sensor type : DHT11
sensor = Adafruit_DHT.DHT11

# GPIO pin where the DHT11 is connected (e.g., GPIO4)
pin = 4

print("Starting DHT11 Sensor Reading...")

try:
    while True:
        # Read temperature and humidity
        humidity, temperature = Adafruit_DHT.read(sensor, pin)

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f} °C  Humidity: {humidity:.1f} %")
        else:
            print("Failed to retrieve data from sensor. Retrying...")

        # Wait 2 seconds before the next reading
        time.sleep(2)
except KeyboardInterrupt:
    print("Program terminated.")