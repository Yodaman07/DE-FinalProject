import os
from dotenv import load_dotenv
import logging
from arduino_iot_cloud import ArduinoCloudClient

load_dotenv()
id = os.getenv("DEVICE_ID")
key = os.getenv("SECRET_KEY")


# help from https://github.com/arduino/arduino-iot-cloud-py
def logging_func():
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )


if __name__ == "__main__":
    logging_func()
    client = ArduinoCloudClient(device_id=id, username=id, password=key)
    client.register("status")

    client["status"] = False

    client.start()
