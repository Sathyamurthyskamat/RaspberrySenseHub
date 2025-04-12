# I2C LCD with Raspberry Pi (16x2 / 20x4 LCD Display)

Display custom messages on a 16x2 or 20x4 LCD using the I2C interface on a Raspberry Pi. This project walks you through setting up the hardware and using Python to control your LCD with just two GPIO pins.

---

## What is an LCD?

An **LCD (Liquid Crystal Display)** is a small screen commonly used in DIY electronics to display text. The most popular models are:

- **16x2 LCD** – 16 characters per line, 2 lines
- **20x4 LCD** – 20 characters per line, 4 lines

They’re great for:
- Displaying system status
- Showing sensor readings
- User feedback in embedded systems

Normally, these displays require 6–10 GPIO pins, but that’s where **I2C** comes in!

---

## What is I2C?

**I2C (Inter-Integrated Circuit)** is a communication protocol that allows devices to communicate using just **two wires**:

- **SDA** – Serial Data Line
- **SCL** – Serial Clock Line

An **I2C backpack** attached to the LCD lets you control the whole display with only 2 pins from the Raspberry Pi, making wiring simpler and keeping other GPIO pins free.

### Benefits of Using I2C with LCD:
- Minimal wiring
- Saves GPIO pins
- Easy to use with multiple devices
- Clean and modular setup

---

## Features

- Supports 16x2 and 20x4 LCDs with I2C (PCF8574)
- Simple Python code, no complex libraries needed
- Displays dynamic or static messages
- Easily customizable

---

## Requirements

- Raspberry Pi (any model with GPIO header)
- I2C LCD Display 
- Jumper Wires
- Python 3

---

## Wiring

| LCD Pin | Raspberry Pi Pin    |
|---------|---------------------|
| GND     | GND (Pin 6)         |
| VCC     | 5V (Pin 2)          |
| SDA     | GPIO2 (SDA, Pin 3)  |
| SCL     | GPIO3 (SCL, Pin 5)  |

---

## Setup Instructions

### 1. Enable I2C Interface

```bash
sudo raspi-config
```
### 2. Install Required Packages

```bash
sudo apt update
sudo apt install -y i2c-tools python3-smbus
```

### 3. Detect Your I2C Address

```bash
i2cdetect -y 1
```
### 4. Run the Code

```bash
python3 lcd_display.py
```

### License
This project is licensed under the MIT License.
