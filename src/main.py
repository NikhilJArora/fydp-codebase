"""Program entry point."""

"""
Current config values required:
Camera:
- im_base_path

Classifier:
- serial_path (full path where clf is serialized)

ViewSet:
- views:
    - view_id: 1
      theta: 45
      phi: 45
      ps_set:
        - ps_id: 123
        - x_start: 20
        - x_end: 200
        - y_start: 20
        - y_end: 200

"""
import os
import pandas as pd

from cfg import Cfg
from camera import Camera
from classifier import Classifier
from viewset import ViewSet


def main():
    # program start
    print("ParkSmart is starting up...")
    loop_count = 0
    cfg = Cfg()

    camera = Camera(cfg.Camera)
    classifier = Classifier(cfg.Classifier)
    viewset = ViewSet(cfg.ViewSet, classifier)
    print("Now beginning to process the current ViewSet.")

    while True:
        print("Views have been processed {} times.".format(str(loop_count)))
        for view in viewset.views:
            img_pos = view.get_img_pos()
            camera.move(img_pos[0], img_pos[1])
            # NOTE: might need to cal a sleep to give camera time to move
            view_img = camera.capture() # TODO:
            view.update(view_img) # TODO:

        print("The current state:")
        curr_views_dict = viewset.get_set_state()
        df = pd.DataFrame(curr_views_dict)
        df = df[['view_id','id','state','l_update']]
        df.to_csv('output.csv', index=False)
        print(df)
        loop_count += 1


if __name__ == '__main__':
    main()
