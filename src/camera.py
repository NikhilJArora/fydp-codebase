"""
all logic related to camera and its control.

https://www.raspberrypi.org/documentation/usage/camera/python/README.md

Installation:

sudo apt-get update
sudo apt-get install python-picamera
"""
import os
import picamera
import cPickle as pickle

from random import randint
from skimage import (io, transform)

from ServoSerial import ServoSerial


class Camera(object):
    """Class wraps all interation and control of camera and its position."""
    def __init__(self, cfg_camera):
        self.cfg_camera = cfg_camera
        self.im_base_path = self.cfg_camera['im_base_path']
        self.cam = picamera.PiCamera()
        self.servo = ServoSerial()
        self.curr_path = None

    def capture(self):
        self.curr_path = self._gen_path()
        self.cam.capture(self.curr_path)
        print("Image capture complete!")
        return transform.rotate(io.imread(self.curr_path), 180)

    def _gen_path(self):
        # generate random int
        rand_int = randint(0, 9999)
        return os.path.join(
            self.im_base_path,
            'curr_view_im_' + \
            str(rand_int) + \
            '.jpg'
            )

    def move(self, theta, phi):
        """ writes theta and phi to Servo motors via abstracted serial
        connection """
        print('Writing the theta angle: {}'.format(str(theta)))
        self.servo.write(theta)
        #print("Serial Port: " + str(self.servo.read()))
        print('Writing the theta angle: {}'.format(str(phi)))
        self.servo.write(phi)
        #print("Serial Port: " + str(self.servo.read()))

    def get_last_im(self):
        if self.curr_path is not None:
            return io.imread(self.curr_path)
        else:
            return None
