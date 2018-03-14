"""
Train the model based on pre-computed HOG feature vectors.
"""

# imports:

import os
import pickle
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

print(X_train.shape)
print(X_test.shape)
# init the svm classifier
clf = svm.SVC()

# train the classifier using the train set
clf.fit(X_train, y_train)


# test the classifier and report the acc score for the model
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy: "+str(acc))
# if acc > 0.90:
#     break
print('\n')
print(classification_report(y_test, y_pred))

modeloutf = os.path.join(model_path, 'finalized_model_v2.p')
pickle.dump(clf, open(modeloutf, 'wb'))
