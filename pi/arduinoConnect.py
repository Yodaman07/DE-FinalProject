import os
from dotenv import load_dotenv
import logging
from arduino_iot_cloud import ArduinoCloudClient
from testing.connecting import logging_func
import time


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
        logging_func()
        client = ArduinoCloudClient(device_id=self.id, username=self.id, password=self.key, sync_mode=True)
        client.register("status", value=False)
        self.client = client

        client.start()

        while True:
            client.update()

            with open("pi/test.txt", "r") as t:
                if t.readline() == "true":
                    client["status"] = True
                    print("true")
                else:
                    client["status"] = False

            time.sleep(0.100)
