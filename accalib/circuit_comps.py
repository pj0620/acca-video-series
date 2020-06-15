from manimlib.imports import *
from accalib.constants import *

class Ground(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/ground.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    # def name_parts(self):
    #     pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        # if not self.parts_named:
        #     self.name_parts()

        for mob in self.submobjects:
            mob.set_stroke(self.get_color(),self.get_stroke_width())
            mob.set_fill(BLACK,opacity=0)

        return self

class Mosfet(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/mosfet.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.lines=[]
        self.arrows=[]

        self.lines.append(self.submobjects[0])
        self.lines.append(self.submobjects[1])
        self.lines.append(self.submobjects[2])
        self.lines.append(self.submobjects[3])
        self.lines.append(self.submobjects[4])
        self.lines.append(self.submobjects[5])
        self.lines.append(self.submobjects[6])
        self.arrows.append(self.submobjects[7])
        self.lines.append(self.submobjects[8])
        self.lines.append(self.submobjects[9])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for line in self.lines:
            line.set_stroke(self.get_color(), self.get_stroke_width())
            line.set_fill(BLACK, opacity=0)

        for arrow in self.arrows:
            arrow.set_stroke(BLACK, self.get_stroke_width(),opacity=0)
            arrow.set_fill(self.get_color(), opacity=1)

        return self

class Transformer(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/transformer.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.lines=[]
        self.circles=[]

        self.lines.append(self.submobjects[0])
        self.lines.append(self.submobjects[1])
        self.lines.append(self.submobjects[2])
        self.circles.append(self.submobjects[3])
        self.circles.append(self.submobjects[4])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for line in self.lines:
            line.set_stroke(self.get_color(), self.get_stroke_width())
            line.set_fill(BLACK, opacity=0)

        for circle in self.circles:
            circle.set_stroke(self.get_color(), self.get_stroke_width())
            circle.set_fill(self.get_color(), opacity=1)

        return self

class NPNTransistor(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/npn_transistor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.lines = []
        self.arrows = []

        self.lines.append(self.submobjects[0])
        self.lines.append(self.submobjects[1])
        self.lines.append(self.submobjects[2])
        self.lines.append(self.submobjects[3])
        self.arrows.append(self.submobjects[4])
        self.lines.append(self.submobjects[5])
        self.lines.append(self.submobjects[6])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for line in self.lines:
            line.set_stroke(self.get_color(), self.get_stroke_width())
            line.set_fill(BLACK,opacity=0)

        for arrow in self.arrows:
            arrow.set_stroke(self.get_color(), self.get_stroke_width())
            arrow.set_fill(self.get_color(), opacity=1)

        return self

class EnhancedPChannelMosfet(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/enh_p_channel_mosfet.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.lines = []
        self.arrows = []
        self.lines.append(self.submobjects[0])
        self.lines.append(self.submobjects[1])
        self.lines.append(self.submobjects[2])
        self.arrows.append(self.submobjects[3])
        self.lines.append(self.submobjects[4])
        self.lines.append(self.submobjects[5])
        self.lines.append(self.submobjects[6])
        self.circle = self.submobjects[7]
        self.circle2 = self.submobjects[8]
        self.lines.append(self.submobjects[9])
        self.lines.append(self.submobjects[10])
        self.lines.append(self.submobjects[11])
        self.lines.append(self.submobjects[12])
        self.arrows.append(self.submobjects[13])
        self.lines.append(self.submobjects[14])
        self.lines.append(self.submobjects[15])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for line in self.lines:
            line.set_stroke(self.get_color(),self.get_stroke_width())
            line.set_fill(BLACK,opacity=0)

        for arrow in self.arrows:
            arrow.set_fill(self.get_color(),opacity=1)
            # arrow.set_stroke(self.get_color(),self.get_stroke_width())

        self.circle.set_stroke(self.get_color(),self.get_stroke_width())
        self.circle.set_fill(self.get_color(),opacity=1)
        self.circle2.set_stroke(self.get_color(), self.get_stroke_width())
        self.circle2.set_fill(self.get_color(), opacity=1)

        return self

class ZenerDiode(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/zener_diode.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    # def name_parts(self):
    #     pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        # if not self.parts_named:
        #     self.name_parts()

        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class Diode(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/diode.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    # def name_parts(self):
    #     pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(self.get_color(), self.get_stroke_width())

        # if not self.parts_named:
        #     self.name_parts()

        return self

class Capacitor(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/capacitor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(BLACK, self.get_stroke_width())

        self.lplate = self.submobjects[0]
        self.rplate = self.submobjects[1]
        self.lwire = self.submobjects[2]
        self.rwire = self.submobjects[3]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.lplate.set_stroke(self.get_color(),self.get_stroke_width()*2)
        self.rplate.set_stroke(self.get_color(), self.get_stroke_width()*2)
        self.lwire.set_stroke(self.get_color(), self.get_stroke_width())
        self.rwire.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class Inductor(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/inductor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    # def name_parts(self):
    #     pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        # if not self.parts_named:
        #     self.name_parts()
        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class OpAmp(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/op_amp.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    # def name_parts(self):
    #     pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        # if not self.parts_named:
        #     self.name_parts()
        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class DependentCurrentSource(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/current_source_dependent.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=0)
            submobject.set_stroke(BLACK, self.get_stroke_width())

        self.top_wire = self.submobjects[0]
        self.bot_wire = self.submobjects[1]
        self.v_line = self.submobjects[2]
        self.tip = self.submobjects[3]
        self.rhalf = self.submobjects[4]
        self.lhalf = self.submobjects[5]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.top_wire.set_stroke(self.get_color(),self.get_stroke_width())
        self.bot_wire.set_stroke(self.get_color(), self.get_stroke_width())
        self.v_line.set_stroke(self.get_color(), self.get_stroke_width())
        self.tip.set_stroke(self.get_color(),self.get_stroke_width())
        self.tip.set_fill(self.get_color(),opacity=1)
        self.rhalf.set_stroke(self.get_color(),self.get_stroke_width())
        self.lhalf.set_stroke(self.get_color(),self.get_stroke_width())

        return self

class DependentVoltageSource(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/voltage_source_dependent.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        for submobject in self.submobjects:
            submobject.set_fill(BLACK, opacity=1)
            submobject.set_stroke(BLACK, self.get_stroke_width())

        self.top_wire = self.submobjects[0]
        self.bottom_wire = self.submobjects[1]
        self.square = self.submobjects[2]
        self.v_plus = self.submobjects[3]
        self.h_plus = self.submobjects[4]
        self.minus = self.submobjects[5]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.top_wire.set_stroke(self.get_color(), self.get_stroke_width())
        self.top_wire.set_fill(self.get_color(), opacity=0)
        self.bottom_wire.set_stroke(self.get_color(), self.get_stroke_width())
        self.bottom_wire.set_fill(self.get_color(), opacity=0)
        self.square.set_stroke(self.get_color(), self.get_stroke_width())
        self.square.set_fill(RED, opacity=0)
        self.v_plus.set_stroke(self.get_color(),self.get_stroke_width())
        self.h_plus.set_stroke(self.get_color(),self.get_stroke_width())
        self.minus.set_stroke(self.get_color(),self.get_stroke_width())

        return self

class CurrentSource(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/current_source.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        for submobject in self.submobjects:
            submobject.set_fill(WHITE, opacity=0)
            submobject.set_stroke(BLACK, self.get_stroke_width())

        self.v_line = self.submobjects[0]
        self.arrow_tip = self.submobjects[1]
        self.circle = self.submobjects[2]
        self.top_wire = self.submobjects[3]
        self.bottom_wire=self.submobjects[4]
        pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.v_line.set_stroke(self.get_color(),self.get_stroke_width())
        self.arrow_tip.set_stroke(self.get_color(),self.get_stroke_width())
        self.arrow_tip.set_fill(self.get_color(),opacity=1)
        self.arrow_tip.shift(0.5*DOWN+0.1*RIGHT)
        self.arrow_tip.scale(1.4)
        self.circle.set_stroke(self.get_color(),self.get_stroke_width())
        self.top_wire.set_stroke(self.get_color(),self.get_stroke_width())
        self.bottom_wire.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class VoltageSource(SVGMobject):
    CONFIG={
        "stroke_width": DEFAULT_WIRE_THICKNESS,
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
        self.top_wire.set_stroke(self.get_color(), self.get_stroke_width())
        self.bottom_wire.set_fill(WHITE, opacity=0)
        self.bottom_wire.set_stroke(self.get_color(), self.get_stroke_width())
        self.vert_plus.set_fill(WHITE, opacity=0)
        self.vert_plus.set_stroke(self.get_color(), self.get_stroke_width())
        self.hor_plus.set_fill(WHITE, opacity=0)
        self.hor_plus.set_stroke(self.get_color(), self.get_stroke_width())
        self.minus.set_fill(WHITE, opacity=0)
        self.minus.set_stroke(self.get_color(), self.get_stroke_width())
        self.circle.set_fill(WHITE, opacity=0)
        self.circle.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class Resistor(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/resistor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.body = self.submobjects[0]

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()
        self.body.set_fill(WHITE, opacity=0)
        self.body.set_stroke(self.get_color(), self.get_stroke_width())

        self.rotate(-np.pi / 2)

        return self

class BatterySymbol(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/battery_symbol.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.thin_lines = VGroup()
        self.thick_lines = VGroup()

        self.thin_lines.add(self.submobjects[0])
        self.thick_lines.add(self.submobjects[1])
        self.thin_lines.add(*self.submobjects[2:6])
        self.thick_lines.add(self.submobjects[6])
        self.thin_lines.add(self.submobjects[7])
        self.thick_lines.add(self.submobjects[8])
        self.thin_lines.add(*self.submobjects[9:12])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        # for mob in self.submobjects:
        #     mob.set_stroke(BLACK, opacity=0)
        #     mob.set_fill(BLACK, opacity=0)

        self.thin_lines.set_fill(self.get_color(), opacity=1)
        self.thin_lines.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.thick_lines.set_fill(self.get_color(), opacity=1)
        self.thick_lines.set_stroke(self.get_color(), self.get_stroke_width()*2.2, opacity=1)

        return self

class IronCoreInductor(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/iron_core_inductor.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        # for mob in self.submobjects:
        #     mob.set_stroke(BLACK, opacity=0)
        #     mob.set_fill(BLACK, opacity=0)

        self.set_fill(self.get_color(), opacity=0)
        self.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)

        return self

class VacuumTube(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file = "images/svgs/vacuum_tube.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        # for mob in self.submobjects:
        #     mob.set_stroke(BLACK, opacity=0)
        #     mob.set_fill(BLACK, opacity=0)

        self.set_fill(self.get_color(), opacity=0)
        self.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)

        return self

class Potentiometer(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file = "images/svgs/potentiometer.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        pass

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        # for mob in self.submobjects:
        #     mob.set_stroke(BLACK, opacity=0)
        #     mob.set_fill(BLACK, opacity=0)

        self.set_fill(self.get_color(), opacity=0)
        self.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)

        return self

class FullBridgeRectifier(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file = "images/svgs/full_bridge_rectifier.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

    def name_parts(self):
        self.small_lines = VGroup()
        self.triangles = VGroup()

        self.small_lines.add(*self.submobjects[0:8])
        self.triangles.add(self.submobjects[8])
        self.small_lines.add(self.submobjects[9])
        self.triangles.add(self.submobjects[10])
        self.small_lines.add(self.submobjects[11])
        self.triangles.add(self.submobjects[12])
        self.small_lines.add(self.submobjects[13])
        self.triangles.add(self.submobjects[14])
        self.small_lines.add(*self.submobjects[15:21])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.small_lines.set_fill(self.get_color(), opacity=0)
        self.small_lines.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.triangles.set_fill(self.get_color(), opacity=1)
        self.triangles.set_stroke(self.get_color(), self.get_stroke_width()*0.8, opacity=1)

        return self

class Triac(SVGMobject):
    CONFIG = {
        "stroke_width" : DEFAULT_WIRE_THICKNESS,
    }
    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file = "images/svgs/triac.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.lines[-1].shift(0.1 * UP)
        for triangle in self.triangles:
            triangle.scale(0.9)

    def name_parts(self):
        self.lines = VGroup()
        self.triangles = VGroup()

        self.triangles.add(self.submobjects[0])
        self.lines.add(self.submobjects[1])
        self.triangles.add(self.submobjects[2])
        self.lines.add(*self.submobjects[3:7])

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for mob in self.submobjects:
            mob.set_stroke(BLACK, opacity=0)
            mob.set_fill(BLACK, opacity=0)

        # self.new.set_fill(GREEN, opacity=0)
        # self.new.set_stroke(GREEN, self.get_stroke_width(), opacity=1)
        self.lines.set_fill(self.get_color(), opacity=0)
        self.lines.set_stroke(self.get_color(), 1*self.get_stroke_width(), opacity=1)
        self.triangles.set_fill(self.get_color(), opacity=1)
        self.triangles.set_stroke(self.get_color(), self.get_stroke_width()*0.2, opacity=0)

        return self
