# Infrared (IR) Sensors:

Infrared (IR) sensors are electronic devices that detect infrared radiation emitted by objects. They are commonly used in various applications such as proximity sensing, object detection, and motion detection. IR sensors work by detecting changes in the intensity of infrared radiation received by their sensitive components.

## Working Principle:

IR sensors work by detecting changes in the intensity of infrared radiation received by their sensitive components. They typically consist of an emitter that emits infrared radiation and a receiver that detects the radiation. When an object comes within the sensor's range, it reflects or emits IR radiation that is then detected by the receiver.

## Connection with Raspberry Pi GPIO:

To interface an IR sensor with a Raspberry Pi, you can connect the sensor to the Raspberry Pi's GPIO (General Purpose Input/Output) pins. Typically, you would connect the VCC pin of the IR sensor to the 5V pin on the Raspberry Pi, the GND pin to any ground (GND) pin, and the OUT pin to a GPIO pin (e.g., GPIO 18).

For programming the IR sensor with Python and Raspberry Pi, you would use libraries like RPi.GPIO(Already inside the rapberry pi) to interact with the GPIO pins and read data from the IR sensor. This allows you to create applications such as object detection systems, proximity sensors, or automated systems based on IR input.
