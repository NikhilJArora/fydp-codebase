import serial
from time import sleep

"""Object that exposes simple to use api for the arduino
NOTE: Port on mac: /dev/tty.usbmodem1421
NOTE: Port on linux: /dev/ttyS0
"""
class ServoCtrl(object):
    """docstring for ServoCtrl."""
    def __init__(self, port = '/dev/tty.usbmodem1421'):
        self.port = port
        self.ser = serial.Serial(port)
        self.ser.baudrate = 9600
        if not self.ser.is_open:
            self.ser.open()

    def write(self, ang):
        sleep(3)
        print(self.ser.write(str(ang).encode()))


# Example usage:
Servo = ServoCtrl()

Servo.write(45)
Servo.write(90)
Servo.write(90)
Servo.write(45)
