"""
Train the model based on pre-computed HOG feature vectors.
"""

# imports:

import os
import cPickle as pickle
from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import classification_report,accuracy_score
import pandas as pd
import numpy as np

# consts:
dataset_path = '/Users/nikhilarora/data/fydp/dataset'
model_path = '/Users/nikhilarora/data/fydp/models'

# read train.p into mem
#ds_df = pd.read_pickle(os.path.join(dataset_path, 'train.p'))
with open(os.path.join(dataset_path, 'features_v2.p'), 'rb') as f:
    X = pickle.load(f)
with open(os.path.join(dataset_path, 'lbls_v2.p'), 'rb') as f:
    y = pickle.load(f)

X = np.asarray(X)
y = np.asarray(y)

# split into train test at a 80/20 split
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

print("Train split:")
print(X_train.shape)
print("Test split:")
print(X_test.shape)

# init the svm classifier
clf = svm.SVC()

# train the classifier using the train set
clf.fit(X_train, y_train)


# test the classifier and report the acc score for the model
y_pred_test = clf.predict(X_test)
y_pred_train = clf.predict(X_train)
acc_test = accuracy_score(y_test, y_pred_test)
acc_train = accuracy_score(y_train, y_pred_train)
print("Accuracy (on test set): "+str(acc_test))
print("Accuracy (on train set): "+str(acc_train))
# if acc > 0.90:
#     break
#print('\n')
#print(classification_report(y_test, y_pred))

modeloutf = os.path.join(model_path, 'finalized_model_v5.p')
pickle.dump(clf, open(modeloutf, 'wb'))
