from manimlib.imports import *
from accalib.constants import *

class Electron(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", include_sign=True, **kwargs):
        self.parts_named=False
        svg_file="images/svgs/electron.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(0.17)
        if not include_sign:
            self.remove(self.minus)
        # ignore if not free electron
        self.next_center = None
        self.current_center = None
        self.wait_theta = None
        self.total_theta = 0

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

class CopperAtom(SVGMobject):
    def __init__(self, include_valence=True, electron_color="#3fb5de",mode="plain", **kwargs):
        self.parts_named = False
        svg_file = "images/svgs/copper_atom.svg"
        self.electron_color = electron_color
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        if not include_valence:
            self.electrons = self.electrons[-1]
            self.remove(self.submobjects[-1])

    def name_parts(self):
        self.electrons = VGroup()
        self.rings = VGroup()
        self.plus_sign = VGroup()

        self.nucleus = self.submobjects[0]
        self.plus_sign.add(*self.submobjects[1:3])
        self.rings.add(*self.submobjects[3:7])
        self.electrons.add(*self.submobjects[7:])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for mob in self.submobjects:
            mob.set_stroke(BLACK, self.get_stroke_width())
            mob.set_fill(WHITE, opacity=0)

        self.nucleus.set_fill("#ffc0c0", opacity=1)
        self.plus_sign.set_fill(BLUE,opacity=1)
        self.plus_sign.set_stroke(BLUE,opacity=0.7)
        self.rings.set_stroke(GREY,2, opacity=1)
        self.electrons.set_fill(self.electron_color,opacity=1)
        self.electrons.set_stroke(self.electron_color,opacity=1)

        return self