import time
import logging

import sys

sys.path.append("lib")

from arduino_iot_cloud import ArduinoCloudClient

DEVICE_ID = b""
SECRET_KEY = b""
#from https://github.com/arduino/arduino-iot-cloud-py

def logging_func():
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )


# This function is executed each time the "test_switch" variable changes
def on_switch_changed(client, value):
    print("Switch Pressed! Status is: ", value)


if __name__ == "__main__":
    logging_func()
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

    client.register("test_value")
    client["test_value"] = 20
    client.register("test_switch", value=None, on_write=on_switch_changed)

    client.start()