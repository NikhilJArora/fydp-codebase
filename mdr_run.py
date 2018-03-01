"""For purpose of demo in MDR"""
import os
from ServoSerial import ServoSerial
from time import sleep


# angles to rotate around:

Servo = ServoSerial()
img1 = 'raspistill -o test_img_1.jpg'
img2 = 'raspistill -o test_img_2.jpg'
img3 = 'raspistill -o test_img_3.jpg'
img4 = 'raspistill -o test_img_4.jpg'

try:
    #first view:
    Servo.write(30)
    Servo.write(90)
    sleep(2)
    os.popen(img1)
    sleep(5)
    # Second view:
    Servo.write(60)
    Servo.write(90)
    sleep(2)
    os.popen(img2)
    sleep(5)
    # Third View:
    Servo.write(90)
    Servo.write(90)
    sleep(2)
    os.popen(img3)
    sleep(5)
    # Fourth View:
    Servo.write(120)
    Servo.write(45)
    sleep(2)
    os.popen(img4)
    sleep(5)

except:
    Servo.close()
