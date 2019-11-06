from manimlib.imports import *
from accalib.constants import *

class VoltageSource(SVGMobject):
    CONFIG={
        "rit_color": "#F36E21",
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/voltage_source.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.top_wire=self.submobjects[0]
        self.bottom_wire=self.submobjects[1]
        self.vert_plus=self.submobjects[2]
        self.hor_plus=self.submobjects[3]
        self.minus=self.submobjects[4]
        self.circle=self.submobjects[5]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()
        self.top_wire.set_fill(WHITE, opacity=0)
        self.top_wire.set_stroke(self.get_color(), 6)
        self.bottom_wire.set_fill(WHITE, opacity=0)
        self.bottom_wire.set_stroke(self.get_color(), 6)
        self.vert_plus.set_fill(WHITE, opacity=0)
        self.vert_plus.set_stroke(self.get_color(), 6)
        self.hor_plus.set_fill(WHITE, opacity=0)
        self.hor_plus.set_stroke(self.get_color(), 6)
        self.minus.set_fill(WHITE, opacity=0)
        self.minus.set_stroke(self.get_color(), 6)
        self.circle.set_fill(WHITE, opacity=0)
        self.circle.set_stroke(self.get_color(), 6)

        return self

class Resistor(SVGMobject):
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/resistor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.body = self.submobjects[0]

        print("length: ",len(self.body))

        pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()
        self.body.set_fill(WHITE, opacity=0)
        self.body.set_stroke(self.get_color(), 10)

        return self