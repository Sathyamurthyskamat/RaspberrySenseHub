# Raspberry Pi with Firebase - DHT11 Sensor Integration

This project demonstrates how to connect a Raspberry Pi to Firebase and send temperature and humidity data from a DHT11 sensor in real-time.

## Overview

### What is Firebase?

[Firebase](https://firebase.google.com/) is a platform developed by Google for creating mobile and web applications. It offers a Realtime Database, Authentication, Cloud Functions, Hosting, and more.

In this project, we focus on **Firebase Realtime Database** to store and view data collected from a DHT11 temperature and humidity sensor connected to a Raspberry Pi.

## Requirements

- Raspberry Pi (any model with GPIO)
- DHT11 sensor
- Jumper wires
- Python 3
- Internet connection
- Firebase account

##  Wiring the DHT11

- **VCC** → 3.3V on Raspberry Pi
- **GND** → GND on Raspberry Pi
- **DATA** → GPIO pin (e.g., GPIO4)

## Setting up Firebase

1. Go to [Firebase Console](https://console.firebase.google.com/).
2. Create a new project.
3. In the side menu, click **Build > Realtime Database**.
4. Click **Create Database** and choose test mode for quick setup.
5. Note the **database URL**, which will look like: (https://your-project-id.firebaseio.com/)
6. Go to **Project Settings > Service Accounts**, click "Generate new private key", and download the JSON file.

## Python Script

Install required libraries:
```bash
pip install pyrebase4
```

Refer the [**DHT11**](https://github.com/Sathyamurthyskamat/RaspberrySenseHub/tree/main/DHT11) for installation

## Notes
- Ensure your Raspberry Pi has internet access.
- Double-check wiring to avoid sensor read errors.
- You can expand this project with Firebase Auth, web dashboards, or mobile apps.
