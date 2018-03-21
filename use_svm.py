"""
Run pre-build model on new observations

"""
import os
from os import listdir
from os.path import isfile, join
import cPickle as pickle
from skimage import (color, feature, io)
from skimage.transform import resize
from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import classification_report,accuracy_score
import pandas as pd
import numpy as np


# new data point

# do the same data processing to this new point

# consts:
dataset_path = '/Users/nikhilarora/data/fydp/dataset/scaled/'
model_path = '/Users/nikhilarora/data/fydp/dataset/scaled/'
modeloutf = os.path.join(model_path, 'scaled_model_v0.p')

car_b_path = '/Users/nikhilarora/data/fydp/dataset/scaled/car'
ncar_b_path = '/Users/nikhilarora/data/fydp/dataset/scaled/ncar_notusing'


carfiles = [f for f in listdir(car_b_path) if isfile(join(car_b_path, f))]
# carfiles2 = [f for f in listdir(car_b_path2) if isfile(join(car_b_path2, f))]

ncarfiles = [f for f in listdir(ncar_b_path) if isfile(join(ncar_b_path, f))]
# ncarfiles2 = [f for f in listdir(ncar_b_path2) if isfile(join(ncar_b_path2, f))]

# read files into image list:
car_imgs = [io.imread(join(car_b_path, f)) for f in carfiles]
# car_imgs += [io.imread(join(car_b_path2, f)) for f in carfiles2]
print('number of cars: ', len(car_imgs))
ncar_imgs = [io.imread(join(ncar_b_path, f)) for f in ncarfiles]
# ncar_imgs += [io.imread(join(ncar_b_path2, f)) for f in ncarfiles2]
print('number of non-cars: ', len(ncar_imgs))
# define container to store hog feature vect and label
feature_vs = []
lbls = []

# first process event instances
for im in car_imgs:
    gray = color.rgb2gray(im)
    # NOTE: might need to do the whole contour thing, can see later...
    gray_rs = resize(gray, (50, 50), mode='constant')

    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(8, 8),\
            cells_per_block=(2, 2), transform_sqrt=True)
    cl = 1
    feature_vs.append(H)
    lbls.append(cl)

# then process image of nonevent class
for im in ncar_imgs:
    gray = color.rgb2gray(im)
    # NOTE: might need to do the whole contour thing, can see later...
    gray_rs = resize(gray, (50, 50), mode='constant')
    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(8, 8),\
            cells_per_block=(2, 2), transform_sqrt=True)
    cl = 0
    feature_vs.append(H)
    lbls.append(cl)

X = feature_vs
y = lbls

X = np.asarray(X)
y = np.asarray(y)

# load the model from disk
clf = pickle.load(open(modeloutf, 'rb'))
result = clf.score(X, y)
print(result)
for i, H in enumerate(X):
    print(len(H))
    print('Actual: ', bool(y[i]), 'Predicted: ', bool(clf.predict(H.reshape(1, -1))[0]))


# new image processing

def pre_proc_img(im):
    """Takes new image and applies """
    gray = color.rgb2gray(im)
    gray_rs = resize(gray, (100, 200), mode='constant')
    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(10, 10),\
            cells_per_block=(2, 2), transform_sqrt=True, block_norm='L2-Hys')
    return H
    gray_rs = resize(gray, (50, 50), mode='constant')

    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(8, 8),\
            cells_per_block=(2, 2), transform_sqrt=True)
