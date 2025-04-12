import Adafruit_DHT
import pyrebase
import time

# Firebase configuration
firebase_config = {
    #Copy the content from the JSON file
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# DHT Sensor setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        data = {
            "temperature": temperature,
            "humidity": humidity
        }
        db.child("sensor").push(data)
        print("Data sent:", data)
    else:
        print("Sensor failure. Check wiring.")
    
    time.sleep(10)
