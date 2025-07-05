#PHASE 1
# Smart Doorbell

Smart Doorbell is an Internet of Things (IoT) project, integrating a doorbell with a user's smartphone. This project uses a [NodeMCU](https://en.wikipedia.org/wiki/NodeMCU) board which includes the [ESP8266](https://en.wikipedia.org/wiki/ESP8266) low-cost Wi-Fi microchip.

### Ingredients

<table>
  <tr>
    <th>Item</th>
    <th>Description</th>
    <th>Amount</th>
  </tr>
  <tr>
    <td>NodeMCU</td>
    <td>Single board microcontroller</td>
    <td>2</td>
  </tr>
  <tr>
    <td>TTP223</td>
    <td>Capacitive touch sensor</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Relay 1 channel</td>
    <td>1 channel relay 5V with optocoupler high quality</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Round alarm baby bell</td>
    <td>Small bell 55mm dimension with 220Vac</td>
    <td>1</td>
  </tr>
  <tr>
    <td>LED</td>
    <td>5mm super bright blue color light</td>
    <td>3</td>
  </tr>
  
</table>

### Project Images

<table>
  <tr>
    <td><img src="/_images/img1.jpg" width=400px" height="450px" alt="image1"></td>
  </tr>
  <tr>
    <td><img src="/_images/img2.jpg" width="430px" height="500px" alt="image3"/></td>
  </tr>
  <tr>
    <td><img src="/_images/img3.jpg" width="400px" height="700px" alt="image4"/></td>
  </tr>
  <tr>
    <td><img src="/_images/img4.jpg" width="400px" height="300px" alt="image2"/></td>
  </tr>
</table>



#PHASE 2
# Smart Doorbell with Face Recognition and Telegram Integration

## Overview

Create a smart doorbell system that integrates face recognition technology with a Telegram notification system. The project uses an Arduino, a camera module, and an LCD display. When a visitor is detected, the system captures their face, recognizes whether they are a known face (e.g., the homeowner), and sends a notification to the homeowner on Telegram. The LCD display provides real-time feedback, and additional features such as an audible buzzer and LED indicator enhance the user experience. The integration of Python for face recognition and Arduino for hardware control results in a comprehensive and secure smart doorbell solution.

## Key Features

- **Face Recognition:** Utilizes OpenCV and Python for accurate face recognition.
- **Hardware Control:** Arduino-based control for LED, and LCD display.
- **Telegram Integration:** Sends instant notifications to the homeowner through Telegram by using Telegram Bot.
- **User Feedback:** LCD display offers real-time feedback on the system's status.
- **Security:** Differentiates between recognized faces (homeowner) and strangers.
- **Visual Alerts:** Includes a buzzer for audible notifications and an LED indicator for visual alerts.

## Components annd Hardware setup

- Arduino board.
- Camera module for face capture.
- LCD display for visual feedback with 12C module.
- LED indicator for visual alerts.
- Telegram bot for instant messaging.


## Usage

1. Clone the repository: `git clone https://github.com/TejasriK-888/FaceRecognition.git`
2. Install necessary dependencies for Python.
3. Connect the Arduino and upload the provided sketch.
4. Run the Python script for face recognition.
5. generate telegram Bot.

## Configuration

- Replace placeholders in the Arduino sketch and Python script with your specific details.
- Configure your Telegram bot and obtain the API token for integration.

## Additional Information

### Extensions

- **Cloud Storage:** Implement cloud storage for a face recognition database.
- **Home Automation:** Integrate with home automation systems for extended functionality.
- **Mobile App:** Develop a mobile app for remote monitoring and control.

## Conclusion

The Smart Doorbell project provides an intelligent and user-friendly solution for enhancing home security and convenience. The combination of face recognition technology and Telegram integration ensures that homeowners stay informed about visitors in real time.

Feel free to contribute, open issues, or suggest improvements!
