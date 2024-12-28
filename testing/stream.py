import cv2 as cv

cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Unable to access camera")  # kill the program if the camera is not accessed
    cam.release()
    exit()

cam.set(cv.CAP_PROP_FRAME_WIDTH, 1280/4)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 720/4)

while True:
    retrieved, frame = cam.read()
    if not retrieved:
        print("Stream has likely ended")
        break

    cv.imshow("stream", frame)

    # https://stackoverflow.com/questions/5217519/what-does-opencvs-cvwaitkey-function-do <-- how waitKey works
    if cv.waitKey(1) == ord("q"):  # gets the unicode value for q
        break

cam.release()
cv.destroyAllWindows()
