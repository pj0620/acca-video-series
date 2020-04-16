from manimlib.imports import *
from accalib.constants import *

class Electron(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/electron.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(0.17)

    def name_parts(self):
        self.circle = self.submobjects[0]
        self.minus = self.submobjects[1]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.circle.set_fill("#3fb5de", opacity=1)
        self.circle.set_stroke(WHITE, opacity=0)
        self.minus.set_fill(WHITE, opacity=1)
        self.minus.set_stroke(WHITE, opacity=0)

        # for mob in self.submobjects:
        #     mob.set_stroke(BLACK, self.get_stroke_width())
        #     mob.set_fill(BLACK, opacity=0)

        return self