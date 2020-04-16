from manimlib.imports import *

class CurvedArrow(ArcBetweenPoints):
    def __init__(self, start_point, end_point, angle=TAU/4, **kwargs):
        ArcBetweenPoints.__init__(self, start_point, end_point, angle, **kwargs)
        self.add_tip()