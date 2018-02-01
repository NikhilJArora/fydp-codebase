from nanpy import (ArduinoApi, SerialManager, Servo)
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG)

# define the servo pins for pan and tilt kit:
# SERVO_PAN = 9
SERVO_TILT = 10

# establish serial connection
connection = SerialManager(device='/dev/tty.usbmodem1421')
# connection = SerialManager(device='/dev/ttyS0', connection=connection)
# panservo=Servo(SERVO_PAN)

tiltservo=Servo(SERVO_TILT, connection=connection)

sleep(2)
# panservo.write(80)
sleep(1)
tiltservo.write(80)
sleep(5)
# panservo.write(90)
sleep(1)
tiltservo.write(90)
sleep(5)
print("Finished")

del tiltservo
del panservo
