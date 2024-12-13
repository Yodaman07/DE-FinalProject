import math

from mediapipe.framework.formats import landmark_pb2
import pyautogui
from numpy.core.defchararray import lower, upper


class Analyzer:

    def __init__(self):
        self.data: landmark_pb2.NormalizedLandmarkList() = None
        self.detectionFrame = 0

        # For scaling
        self.control = 0
        self.speed = 0

    def addData(self, data: landmark_pb2.NormalizedLandmarkList()):
        self.data = data

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
        diff_x = abs(self.data.landmark[12].x - self.data.landmark[8].x)
        diff_y = abs(self.data.landmark[12].y - self.data.landmark[8].y)

        diff = math.sqrt(diff_x ** 2 + diff_y ** 2) * 500
        print(diff)
