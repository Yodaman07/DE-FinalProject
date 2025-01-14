# Digital Electronics Final Project
### 3D Space Controller


## What does it do

The 3D Space Controller is a device that allows for traversal in 3D environments. You plug it into your computer and turn it on, and through hand gestures the device should allow for the rotation of a 3D landscape (currently only working in Blender) 

## How does it work

Pi: As you move your hand, the camera picks up what is happening and the pi (using mediapipe) processes the coordinates of your pointer finger, and puts it into `pi/data.json`. On a different thread, the pi is connected to the same wifi network as the arduino which enables it to send the data from that file to your "thing" on arduino cloud.

Arduino: The arduino then picks up that data and will move your mouse to those locations on your computer. **NOTE** It is essential to use an HID enabled arduino

## BOM

For the version of the device that I built, here were the materials that I used:

- Microsoft-Life-Cam-3000
- Raspberry Pi 4b
- Raspberry Pi Power supply
- Raspberry Pi 4b Case
- Arduino Nano ESP32
- USB-C to USB-C cable
- Front and Back plates printed in PLA (CAD located in `CAD/`) 
- Duct Tape and Foam from the box of the Arduino (The CAD had some issues which meant I had to be creative with fitting everything together)


## How to use yourself

On the pi inside of a venv (set up with `python -m venv env`, enter with `source env/bin/activate`, and leave with `deactivate`):

- Run `pip install -r requirements.txt` to install the necessary requirements
- Add a `.env` file to the `pi/` directory filled with your Arduino `DEVICE_ID` and `SECRET_KEY`
- Run `main.py`

Arduino Setup:

## Known Issues

It lags really badly - and the camera I'm using does not react well to really bright light

The CAD is kind of broken (things don't fit without some creative solutions) and doesn't needs to be adjusted more closely. The CAD models I ended up using were my prototype files that I printed once. 

## Cut Content (may be added in future versions)

Changing keystroke settings with an lcd
- I started to write code for it in `testing/lcd_controller` but didn't have time to implement it
- Additionally, I wanted to add a functionality with a joystick for manual control but I never got to experimenting with it

