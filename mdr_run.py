"""For purpose of demo in MDR"""
from ServoSerial import ServoSerial

# angles to rotate around:

Servo = ServoSerial()

while True:
    #first view:
    Servo.write(135)
    Servo.write(25)
    # Second view:
    Servo.write(90)
    Servo.write(65)
    # Third View:
    Servo.write(45)
    Servo.write(90)
    # Fourth View:
    Servo.write(90)
    Servo.write(45)
