from pi import detect
from pi import arduinoConnect
import threading


def cam():
    detect.run(showStream=False)


def arduino():
    arduinoConnect.Connection().connect()


if __name__ == "__main__":
    # https://www.geeksforgeeks.org/multithreading-python-set-1/
    cam()
    # t1 = threading.Thread(target=cam)
    # t2 = threading.Thread(target=arduino)
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    print("Finished")
