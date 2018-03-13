"""
Creating the training set.
 - grab images from working dir
 - create container dataframe to store data
 - config our HOG descriptor from our config settings
 - for each image:
    - greyscale the image
    - resize the image .resize(im, (200,100))
    - compute the hog of the image
    - write last col as the label
- write out the pandas dataframe to a csv
 - Compute hog dataset for images
"""

import os
from os import listdir
from os.path import isfile, join

import numpy as np
from scipy import stats
import pickle

import pandas as pd
from skimage import (io, feature, color)
from skimage.transform import resize


dataset_path = '/Users/nikhilarora/data/fydp/dataset'
car_b_path = '/Users/nikhilarora/data/fydp/dataset/car'
ncar_b_path = '/Users/nikhilarora/data/fydp/dataset/ncar'

# list all files in dir for car

carfiles = [f for f in listdir(car_b_path) if isfile(join(car_b_path, f))]
ncarfiles = [f for f in listdir(ncar_b_path) if isfile(join(ncar_b_path, f))]

# read files into image list:
car_imgs = [io.imread(join(car_b_path, f)) for f in carfiles]
ncar_imgs = [io.imread(join(ncar_b_path, f)) for f in ncarfiles]

# define container to store hog feature vect and label
feature_vs = []
lbls = []

# first process event instances
for im in car_imgs:
    gray = color.rgb2gray(im)
    # NOTE: might need to do the whole contour thing, can see later...
    gray_rs = resize(gray, (100, 200), mode='constant')

    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(10, 10),\
            cells_per_block=(2, 2), transform_sqrt=True, block_norm='L2-Hys')
    cl = 1
    feature_vs.append(H)
    lbls.append(cl)

# then process image of nonevent class
for im in ncar_imgs:
    gray = color.rgb2gray(im)
    # NOTE: might need to do the whole contour thing, can see later...
    gray_rs = resize(gray, (100, 200), mode='constant')
    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(10, 10),\
            cells_per_block=(2, 2), transform_sqrt=True, block_norm='L2-Hys')
    cl = 0
    feature_vs.append(H)
    lbls.append(cl)

pickle.dump(feature_vs, open(join(dataset_path, 'features.p'), 'wb'))
pickle.dump(lbls, open(join(dataset_path, 'lbls.p'), 'wb'))
