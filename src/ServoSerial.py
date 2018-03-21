import serial
from time import sleep

"""Object that exposes simple to use api for the arduino
NOTE: Port on mac: /dev/tty.usbmodem1421
NOTE: Port on linux: /dev/ttyS0
NOTE: Alt Port on linux: /dev/ttyACM0

"""
class ServoSerial(object):
    """docstring for ServoSerial."""
    def __init__(self, port = '/dev/ttyACM0'):
        self.port = port
        self.ser = serial.Serial(self.port)
        self.ser.baudrate = 9600
        if not self.ser.is_open:
            self.ser.open()
        self.write(90)


    def write(self, ang):
        print('ServoSerial: writing angle {}'.format(str(ang)))
        self.ser.write(str(ang).encode())
        sleep(3)

    def close(self):
        self.ser.close()

    def read(self):
        return self.ser.readline()

# Example usage:
if __name__ == '__main__':

    Servo = ServoSerial()
    Servo.write(90)

    sleep(5)
    Servo.write(45)
    sleep(5)
    Servo.write(110)
    sleep(5)
    Servo.write(60)
