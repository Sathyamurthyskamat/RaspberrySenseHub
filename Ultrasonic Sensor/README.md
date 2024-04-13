# Ultrasonic Sensor Basics
Ultrasonic sensors are fascinating devices used for distance measurement and object detection. It works on the principle of sending out ultrasonic sound waves and measuring the time it takes for the waves to bounce back after hitting an object. This time measurement is then used to calculate the distance to the object.

An ultrasonic sensor typically has two main components: a transmitter and a receiver. The transmitter emits ultrasonic waves, while the receiver detects the waves that bounce back. By measuring the time between emission and reception, the sensor can determine the distance to an object.

## Raspberry Pi Connection
To connect an ultrasonic sensor to a Raspberry Pi, you'll typically use GPIO (General Purpose Input Output) pins. GPIO pins allow the Raspberry Pi to communicate with external components like sensors. You'll connect the sensor's VCC pin to a 5V pin on the Pi, the GND pin to a ground pin, and the Echo and Trig pins to two GPIO pins for communication.

## Working Principle
**Triggering the Sensor:** The Trig pin is used to trigger the ultrasonic burst. You send a short pulse to this pin to start the measurement process.

**Receiving the Signal:** The Echo pin receives the ultrasonic signal after it bounces back from an object. By measuring the time between sending the trigger pulse and receiving the echo signal, you can calculate the distance.

**Calculating Distance:** The distance can be calculated using the formula: Distance = Speed of Sound * Time / 2, where the speed of sound is approximately 343 meters per second.
