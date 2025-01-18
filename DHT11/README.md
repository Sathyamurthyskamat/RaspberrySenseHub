# DHT11 with Raspberry Pi

## DHT11 Overview

The DHT11 is a highly popular sensor designed for measuring temperature and humidity. It is cost-effective and provides reliable, accurate readings, making it an excellent choice for various environmental monitoring applications. The sensor features an onboard chip that converts analog signals into digital output, simplifying integration with microcontrollers and single-board computers like the Raspberry Pi.

### Key Features of DHT11
- **Temperature range**: 0°C to 50°C
- **Humidity range**: 20% to 90%
- **Sampling rate**: 1 Hz (one reading per second)
- **Operating voltage**: 3.3V to 5.5V

Commonly used in weather stations, home automation systems, and other projects, the DHT11 stands out for its simplicity and ease of use.

---

## How to Connect DHT11 to Raspberry Pi

### Required Components:
- DHT11 sensor module
- Raspberry Pi (any model with GPIO pins)
- Jumper wires
- Breadboard (optional)

### Pin Configuration:
The DHT11 sensor typically comes with three or four pins:
1. **VCC**: Power supply (connect to Raspberry Pi 3.3V pin)
2. **GND**: Ground
3. **DATA**: Data pin (connect to a GPIO pin on the Raspberry Pi)

### Wiring Instructions:
1. Connect the **VCC** pin of the DHT11 to the **3.3V** pin on the Raspberry Pi.
2. Connect the **GND** pin of the DHT11 to the **GND** pin on the Raspberry Pi.
3. Connect the **DATA** pin of the DHT11 to a GPIO pin on the Raspberry Pi (e.g., GPIO4).
4. If your DHT11 module lacks an onboard resistor, connect a 10kΩ pull-up resistor between the **DATA** pin and **VCC**.

---

## Programming the DHT11 Sensor

To communicate with the DHT11, we will use the `Adafruit_DHT` Python library, which provides simple methods for reading sensor data.

### Setting Up the Environment:
1. Ensure Python is installed on your Raspberry Pi.
2. Install the `Adafruit_DHT` library by running:
   ```bash
   pip install Adafruit_DHT

### Running the Script:
Navigate to the directory containing dht11_sensor.py.
Execute the script using:
```bash
   python dht11_sensor.py
```
