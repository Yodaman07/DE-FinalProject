import serial


class Connection:
    def __init__(self):
        self.ser: serial.serialposix = None

    def openSerial(self, port):
        self.ser = serial.Serial(port, baudrate=9600)  # We are only sending numbers that are associated with keystrokes
        # self.ser.reset_input_buffer()
        # self.ser.reset_output_buffer()

    def sendData(self, data):
        self.ser.write(data)

    def closeSerial(self):
        self.ser.close()


if __name__ == "__main__":
    c = Connection()
    c.openSerial("/dev/tty.usbmodem744DBDA149F03")
    c.sendData("".encode())
    # c.sendData("123456788".encode())
    #
    # c.sendData("100".encode())
    # c.sendData("600".encode())
    #
    # c.sendData("123456789".encode())
    c.closeSerial()
