""" Code used to parse and present config to rest of the program """

import sys

import yaml

class Cfg(object):
    """docstring for Cfg.
    Params
    ------
    - cfg_path : str --> where the config is stored on disk
    - cfg : dict --> holds the entire config in dict
    - Camera : dict
    - Classifier : dict

    Methods
    -------
    - void : _read_cfg() --> reads file from disk

    """
    def __init__(self, cfg_path = 'cfg.yml'):
        self.cfg_path = cfg_path
        self._cfg = None
        self.Camera = None
        self.Classifier = None
        self.ViewSet = None
        self._read_cfg() #sets all params

    def _read_cfg(self):
        with open(self.cfg_path, 'r') as stream:
            try:
                self._cfg = yaml.load(stream)
                self.Camera = self._cfg['Camera']
                self.Classifier = self._cfg['Classifier']
                self.ViewSet = self._cfg['ViewSet']
            except yaml.YAMLError as exc:
                print(exc)
                sys.exit()
        
