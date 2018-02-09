import serial
from time import sleep

"""Object that exposes simple to use api for the arduino
NOTE: Port on mac: /dev/tty.usbmodem1421
NOTE: Port on linux: /dev/ttyS0
"""
class ServoSerial(object):
    """docstring for ServoSerial."""
    def __init__(self, port = '/dev/ttyACM0'):
        self.port = port
        self.ser = serial.Serial(port)
        self.ser.baudrate = 9600
        if not self.ser.is_open:
            self.ser.open()

    def write(self, ang):
        sleep(3)
        print(self.ser.write(str(ang).encode()))


# Example usage:
if __name__ == '__main__':

    Servo = ServoSerial()

    Servo.write(135)
    Servo.write(25)
    Servo.write(90)
    Servo.write(65)
    Servo.write(45)
    Servo.write(90)
    Servo.write(90)
    Servo.write(45)

    Servo.write(135)
    Servo.write(25)
    Servo.write(90)
    Servo.write(65)
    Servo.write(45)
    Servo.write(90)
    Servo.write(90)
    Servo.write(45)
