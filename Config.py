""" Core class that will hold ref to all other composed logic """
import yaml


class Config(object):
    """docstring for Config."""
    def __init__(self, cfg_path = 'cfg.yml'):
        self.cfg_path = cfg_path
        if not os.path.isfile(self.cfg_path):
            raise ValueError("Missing required main config file.")
        self.cfg = grab_config(self.cfg_path) #TODO
        self.views_count = get_views_count()
        self.views_ls = []
        pop_views_ls()

    def get_views_count(self, arg):
        """ Grabs the count of the views from the config """
        pass

    def grab_config(self, arg):
        pass

    def pop_views_ls(self, arg):
        """ Creates a list of View objects and stores ref to them """
        pass


class View(object):
    """docstring for View."""
    def __init__(self, view_info = {}):
        self.view_dict = view_info
        # required fields:
        self.view_name = self.view_dict['view_name']
        self.pan_ang = self.view_dict['pan_ang']
        self.tilt_ang = self.view_dict['tilt_ang']
        self.view_img = None
        self.ps_ls = self.create_ps_ls()
        self.view_path = self.get_view_path() #TODO

        view.state = None


    def process(self, arg):
        """ slice up each parking spot """
        pass

    def log_state(self, arg):
        """ <timestamp> str(view.state) for each view... """
        pass

    def get_view_path(self):
        pass

class ParkingSpot(object):
    """docstring for ParkingSpot."""
    def __init__(self, ranges=()):
        self.
        self.img = None
        self.state = None

    def set_ranges(self, arg):
        pass
    def update_img(self, view_img):
        """ Using the known ranges, takes a index slicing of img matrix """
        pass
    def update_state(self, arg):
        pass

    def run_classifier(self):
        """
        string = 'sudo docker run -it --rm -v $(pwd):/data:ro openalpr -c eu h786poj.jpg'
        test = os.popen(string).read()

        """
        pass
