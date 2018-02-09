""" Entrypoint for camera occupancy detection system """
from ServoSerial import ServoSerial
""" https://www.raspberrypi.org/documentation/usage/camera/python/README.md """
import picamera
import Config
# some setup code:

# read in config file giving the current set of views that will be used
cfg = Config() #TODO
print("Current setup contains {} views".format(cfg.views_count))
camera = picamera.PiCamera()
# setup connection with arduino via serial
ser = ServoSerial()
ser.write(90)
ser.write(45)
# enter a main loop:
try:
    while True:
        for view in cfg.views_gen():
            ser.write(view['pan_ang'])
            ser.write(view['tilt_ang'])
            sleep(5) # can change later
            camera.capture(view['view_path'])
            sleep(5) # can change later
            view.process() # basically means do what you need to do...
            print("The current State of the view: {}".format(str(view.state)))
            view.log_state() # <timestamp> str(view.state) for each view...

except KeyboardInterrupt:
    print("KeyboardInterrupt raised, exiting program.")
    pass
