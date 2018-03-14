"""
Holds logic related to the classifier that will be used
in predicting the models occupancy.
"""
import os

class Classifier(object):
    """Classifier class that will hold the model and its actions
    Params
    ------
    - cfg_classifier
    - serial_path
    - model
    Methods
    -------
    - bool:predict(feat_vect)
    - sklearn_model:_init_model()
    """
    def __init__(self, cfg_classifier):
        self.cfg_classifier = cfg_classifier
        self.serial_path = self.cfg_classifier['serial_path']
        self.model = self._init_model()

    def _init_model(self):
        """reads serialized model back to mem."""
        return pickle.load(open(self.serial_path, 'rb'))

    def predict(self, feat_vect):
        """returns prediction based on current model"""
        pred_val = self.model.predict(X_test)
        if type(pred_val) == list:
            return bool(pred_val[0])
        else:
            return bool(pred_val)
