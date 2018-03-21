"""
Module holds logic related to managing views and parking spots.
"""
from datetime import datetime
from skimage import (io, feature, color)
from skimage.transform import resize


class ViewSet(object):
    """Container singleton that holds all the current views to be processed.
    Params
    ------
    - dict : cfg_viewset
    - views : list(View)
    - clf : Classifier

    Methods
    -------
    - dict : get_set_state() --> get state update from each view
    - void : _populate_views(self.cfg_viewset)
    """
    def __init__(self, cfg_viewset, classifier):
        self.cfg_viewset = cfg_viewset
        self.classifier = classifier
        self.views = list()
        self._populate_views(self.cfg_viewset)

    def _populate_views(self, cfg_viewset):
        for cfg_view in cfg_viewset['views']:
            self.views.append(View(cfg_view, self.classifier))

    def get_set_state(self):
        _vs_state = {
            'view_id': [],
            'id': [],
            'state': [],
            'l_update' : []
        }
        for view in self.views:
            for ps in view.ps_set:
                _vs_state['view_id'].append(view.view_id)
                _vs_state['id'].append(ps.ps_id)
                _vs_state['state'].append(ps.state)
                _vs_state['l_update'].append(ps.l_update)
        return _vs_state


class View(object):
    """docstring for View.
    Params
    ------
    - view_id : int
    - ps_set : list(ParkingSpot)
    - _img_pos : dict( int:theta, int:phi )


    Methods
    -------
    - void : _populate_parking_spots()
    - void : update(view_img)

    """
    def __init__(self, cfg_view, classifier):
        self.cfg_view = cfg_view
        self.view_id = self.cfg_view['view_id']
        self._img_pos = tuple([self.cfg_view['theta'], self.cfg_view['phi']])
        self.classifier = classifier
        self.ps_set = list()
        self._populate_ps_set(self.cfg_view)

    def _populate_ps_set(self, cfg_view):
        for cfg_ps in cfg_view['ps_set']:
            self.ps_set.append(ParkingSpot(cfg_ps, self.classifier))

    def update(self, view_img):
        for ps in self.ps_set:
            ps.update(view_img)

    def get_img_pos(self):
        return self._img_pos


class ParkingSpot(object):
    """Template for a ParkingSpot.
    Params
    ------
    - classifier : Classifier
    - ps_id : int
    - state : bool
    - l_update : date_time (YYYYmmDDhhMMss)


    Methods
    -------
    - void : _set_im_ranges() --> used to set cut ranges from cfg
    - void : update(view_img)
    - bool : get_last_state() --> grabs last computed state
    - r_im : _slice_img(view_img) --> uses defined ranges to slice image
    - im : _pre_proc(r_im) --> pre_procs shape of image prior to feature gen
    - hog_feat : _hog_compute(im) --> computes hog feature from transformed im
    - bool : _predict(hog_feat) --> uses self.classifier to predict state

    """
    def __init__(self, cfg_ps, classifier):
        self.cfg_ps = cfg_ps
        self.ps_id = self.cfg_ps['ps_id']
        self.x_range = None
        self.y_range = None
        self._set_im_ranges()
        self.state = None
        self.l_update = ''
        self.classifier = classifier

    def _set_im_ranges(self):
        self.x_range = tuple([
                self.cfg_ps['x_start'],
                self.cfg_ps['x_end']
        ])
        self.y_range = tuple([
                self.cfg_ps['y_start'],
                self.cfg_ps['y_end']
        ])

    def update(self, view_im):
        r_im = self._slice_img(view_im)
        im = self._pre_proc_im(r_im)
        hog_feat = self._hog_compute(im)
        self.state = self._predict(hog_feat)
        self.l_update = get_time_str()
        return None

    def get_last_state(self):
        return self.state

    def _slice_img(self, view_im):
        """ Uses defined ranges to slice view image """
        return view_im[self.y_range[0]:self.y_range[1] ,\
                        self.x_range[0]:self.x_range[1]]

    def _pre_proc_im(self, r_im):
        """ greyscale and downscale im to (x,y):(100,200) """
        gray = color.rgb2gray(r_im)
        gray_rs = resize(gray, (50, 50), mode='constant')
        return gray_rs

    def _hog_compute(self, im):
        """ Takes pre-proced im and produces the histogram of gradients
        feature """
        H = feature.hog(im, orientations=9, pixels_per_cell=(8, 8),\
                cells_per_block=(2, 2), transform_sqrt=True)
        return H

    def _predict(self, H):
        return self.classifier.predict(H)

def get_time_str():
    return datetime.now().strftime('%Y%m%d %H%M%S')
