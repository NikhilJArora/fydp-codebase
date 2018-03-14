"""
Run pre-build model on new observations

"""
import os
import pickle
from skimage import (color, feature)
from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import classification_report,accuracy_score
import pandas as pd
import numpy as np


# new data point

# do the same data processing to this new point

# consts:
dataset_path = '/Users/nikhilarora/data/fydp/dataset'
model_path = '/Users/nikhilarora/data/fydp/models'
modeloutf = os.path.join(model_path, 'finalized_model_v2.p')

# read train.p into mem
#ds_df = pd.read_pickle(os.path.join(dataset_path, 'train.p'))
with open(os.path.join(dataset_path, 'features_v2.p'), 'rb') as f:
    X = pickle.load(f)
with open(os.path.join(dataset_path, 'lbls_v2.p'), 'rb') as f:
    y = pickle.load(f)

X = np.asarray(X)
y = np.asarray(y)

# load the model from disk
loaded_model = pickle.load(open(modeloutf, 'rb'))
result = loaded_model.score(X, y)
print(result)

# new image processing

def pre_proc_img(im):
    """Takes new image and applies """
    gray = color.rgb2gray(im)
    gray_rs = resize(gray, (100, 200), mode='constant')
    H = feature.hog(gray_rs, orientations=9, pixels_per_cell=(10, 10),\
            cells_per_block=(2, 2), transform_sqrt=True, block_norm='L2-Hys')
    return H
