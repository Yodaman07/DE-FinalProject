import serial


class Connection:
    def __init__(self):
        self.ser: serial.serialposix = None

    def openSerial(self, port):
        self.ser = serial.Serial(port, baudrate=9600)  # We are only sending numbers that are associated with keystrokes
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def sendData(self, data):
        self.ser.write(data)

    def closeSerial(self):
        self.ser.close()
