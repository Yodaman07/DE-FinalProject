import math

from mediapipe.framework.formats import landmark_pb2
import pyautogui
import json


class Analyzer:

    def __init__(self):
        self.data: landmark_pb2.NormalizedLandmarkList() = None
        self.detectionFrame = 0

        self.width = pyautogui.size().width
        self.height = pyautogui.size().height

        # For Scaling
        self.control = 0
        self.speed = 0

        self.detected = False

        self.jsonData = {
            "mouseX": pyautogui.position().x,
            "mouseY": pyautogui.position().y,
            "mouseState": -1
        }
        self.saveData()

        self.lastX = pyautogui.position().x
        self.lastY = pyautogui.position().y
        # self.x = pyautogui.position().x
        # self.y = pyautogui.position().y

    def addData(self, data: landmark_pb2.NormalizedLandmarkList()):
        self.data = data

    @staticmethod
    def normalize(val, minVal, maxVal, minRange, maxRange) -> int:
        # X range is 0 to self.width
        # https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
        normalized = (maxRange - minRange) * ((val - minVal) / (maxVal - minVal)) + minRange
        return normalized

    def release(self):

        self.jsonData["mouseState"] = 31

        self.saveData()
        self.detectionFrame = 0
        # print("mouseUp")
        # pyautogui.mouseUp(button="middle")

    def lock(self):
        self.jsonData["mouseState"] = 30
        self.saveData()
        # print("mouseDown")
        # pyautogui.mouseDown(button="middle")

    def saveData(self):
        with open("pi/data.json", "w") as o:
            o.write(json.dumps(self.jsonData, indent=4))

    def scale(self):
        # iterate #https://stackoverflow.com/questions/71567928/typeerror-normalizedlandmarklist-object-is-not-iterable-mediapipe

        diff_x = abs(self.data.landmark[4].x - self.data.landmark[8].x)
        diff_y = abs(self.data.landmark[4].y - self.data.landmark[8].y)
        diff_z = abs(self.data.landmark[4].z - self.data.landmark[8].z)

        diff = math.sqrt(diff_x ** 2 + diff_y ** 2 + diff_z ** 2) * 500

        if self.detectionFrame == 0:
            self.control = diff

        lowerBound = self.control - 50
        upperBound = self.control + 50

        if lowerBound <= self.control <= upperBound:
            self.speed = abs(self.control - diff)
        else:
            self.speed = 0

        if diff > self.control:
            self.speed *= -1
        # ex:
        # 50 -> 100 is lower
        # 100 -> 150 upper

        # diff = 100 should be the neutral space
        # 0-100 is zooming in
        #

        # print(self.speed, self.control, diff)
        pyautogui.vscroll(0.5)
        #
        # max speed is 5
        self.detectionFrame += 1

    def rotate(self):
        # Idea behind Rotation
        # Upon detection, have the first position of the finger marked as the center.
        # Measure the difference in the x and y-axis
        # Appropriately normalize the new vector to that of the mouse,

        # Measure x-axis
        diff_x = round(self.data.landmark[8].x, 3)  # Pointer finger tip

        # get y-axis data
        diff_y = round(self.data.landmark[8].y, 3)  # Pointer finger tip

        # default scale is from 0 to 1
        if self.detectionFrame == 0:
            self.lock()

        x = self.normalize(diff_x, 0, 1, 0, self.width)
        y = self.normalize(diff_y, 0, 1, 0, self.height)
        # calculate difference

        self.jsonData["mouseX"] = self.lastX - int(x)
        self.jsonData["mouseY"] = int(y) - self.lastY  # calculates and saves x & y differences
        self.saveData()
        # print("X: " + str(self.lastX - int(x)) + " and Y: " + str(int(y) - self.lastY))

        # pyautogui.moveRel(self.lastX - int(x), int(y) - self.lastY)
        self.lastX = int(x)
        self.lastY = int(y)
        self.detectionFrame += 1
