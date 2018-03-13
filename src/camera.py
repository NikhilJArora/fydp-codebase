"""
all logic related to camera and its control.

https://www.raspberrypi.org/documentation/usage/camera/python/README.md

Installation:

sudo apt-get update
sudo apt-get install python-picamera
"""
import os
import picamera
import pickle

from random import randint
from skimage import (io)

from ServoSerial import ServoSerial


class Camera(object):
    """Class wraps all interation and control of camera and its position."""
    def __init__(self, cfg_camera):
        self.cfg_camera = cfg_camera
        self.im_base_path = self.cfg_camera['im_base_path']
        self.camera = picamera.PiCamera()
        self.servo = ServoSerial()
        self.curr_path = None

    def capture(self, arg):
        self.curr_path = self._gen_path()
        camera.capture(curr_path)
        return io.imread(self.curr_path)

    def _gen_path(self):
        # generate random int
        rand_int = randint(0, 9999)
        return os.path.join(
            self.im_base_path,
            rand_int,
            '.jpg'
            )

    def move(self, theta, phi):
        """ writes theta and phi to Servo motors via abstracted serial connection """
        Servo.write(theta)
        Servo.write(phi)

    def get_last_im(self):
        if self.curr_path not None:
            return io.imread(self.curr_path)
        else:
            return None
