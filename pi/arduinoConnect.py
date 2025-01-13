import os
from dotenv import load_dotenv
import logging
from arduino_iot_cloud import ArduinoCloudClient
import time
import json


class Connection:

    def __init__(self):
        load_dotenv()
        self.id = os.getenv("DEVICE_ID")
        self.key = os.getenv("SECRET_KEY")
        self.client: ArduinoCloudClient = None

    # help from https://github.com/arduino/arduino-iot-cloud-py

    @staticmethod
    def logging_func():
        logging.basicConfig(
            datefmt="%H:%M:%S",
            format="%(asctime)s.%(msecs)03d %(message)s",
            level=logging.INFO,
        )

    def connect(self):
        self.logging_func()
        client = ArduinoCloudClient(device_id=self.id, username=self.id, password=self.key, sync_mode=True)
        client.register("mouseState", value=-1)
        client.register("mouseX", value=-1)
        client.register("mouseY", value=-1)
        self.client = client

        client.start()

        while True:
            client.update()

            with open("pi/data.json", "r") as o:
                json_obj = json.load(o)

            print(json_obj)
            client["mouseState"] = json_obj["mouseState"]
            client["mouseX"] = json_obj["mouseX"]
            client["mouseY"] = json_obj["mouseY"]

            time.sleep(0.100)
