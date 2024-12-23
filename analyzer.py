import math

from mediapipe.framework.formats import landmark_pb2
import pyautogui
from numpy.core.defchararray import lower, upper
from numpy.random import normal


class Analyzer:

    def __init__(self):
        self.data: landmark_pb2.NormalizedLandmarkList() = None
        self.detectionFrame = 0

        self.width = pyautogui.size().width
        self.height = pyautogui.size().height

        # For Scaling
        self.control = 0
        self.speed = 0

        # For Rotation
        self.initialX = 0

        self.control = 0
        self.minVal = 0
        self.maxVal = 1

        # self.x = pyautogui.position().x
        # self.y = pyautogui.position().y

    def addData(self, data: landmark_pb2.NormalizedLandmarkList()):
        self.data = data

    def normalize(self, val, minVal, maxVal) -> int:
        # range is 0 to self.width
        # https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
        normalized = self.width * ((val - minVal) / (maxVal - minVal))
        return normalized

    def release(self):
        pyautogui.mouseUp(button="middle")
        self.detectionFrame = 0

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
        diff = round(self.data.landmark[8].x, 3)  # Pointer finger tip

        # default scale is from 0 to 1

        if self.detectionFrame == 0:
            pyautogui.mouseDown(button="middle")
        #
        # self.x = (diff - self.control)

        # diff_x = abs(self.data.landmark[12].x - self.data.landmark[8].x)
        # diff_y = abs(self.data.landmark[12].y - self.data.landmark[8].y)
        # print(diff_x * 500, diff_y * 500)

        pyautogui.moveTo(x=self.normalize(diff, 0, 1))
        self.detectionFrame += 1
