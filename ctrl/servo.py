from nanpy import Servo
import time

servo = Servo(7)
for move in [0, 90, 180, 90, 0]:
    servo.write(move)
    time.sleep(1)
