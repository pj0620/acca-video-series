from manimlib.imports import *
from accalib.constants import *
import time

class PressureGauge(SVGMobject):
        CONFIG={
            "max_pressure": 52,
            "min_pressure": 25,
            "initial_pressure": 0,
            "text_color": WHITE,
            "text_direction": RIGHT,
            "text_buff": 0.2,
            "unknown": True
        }

        def __init__(self, mode="plain", **kwargs):
            self.parts_named=False
            svg_file="images/svgs/pressure_gauge.svg"
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)

            self.angle = 0

            self.pressure = ValueTracker(self.initial_pressure)

            self.needle.rotate(180 * DEG_TO_RAD, about_point=self.rings.get_center())
            self.add_updater(lambda x: x.set_pressure(self.pressure.get_value()))

            self.text_num=DecimalNumber(self.initial_pressure,
                                        unit="Pa",
                                        num_decimal_places=1,
                                        color=self.text_color,
                                        edge_to_fix=RIGHT).scale(1.9)
            self.text_unk=TextMobject("???",
                                      color=self.text_color).scale(1.9)
            if self.unknown:
                self.text = self.text_unk
            else:
                self.text = self.text_num

            self.add_updater(lambda x: x.text.next_to(self.rings,
                                                      direction=self.text_direction,
                                                      buff=self.text_buff),
                             call_updater=True)
            self.submobjects.append(self.text)
            self.add_updater(lambda x: x.text_num.set_value(self.pressure.get_value()))

        def set_value_known(self):
            self.text = self.text_num

        def get_pressure(self):
            return self.pressure

        def set_pressure(self,new_pressure):
            new_angle=interpolate(0,
                                  270,
                                  (self.pressure.get_value() - self.min_pressure) / (self.max_pressure - self.min_pressure)
                                  )
            del_angle=new_angle - self.angle
            self.angle = new_angle

            self.needle.rotate(
                -1 * DEG_TO_RAD * del_angle,
                about_point=self.rings.get_center()
            )

        def name_parts(self):
            self.rings = self.submobjects[0]
            self.readings = self.submobjects[1]
            self.needle = self.submobjects[2]
            self.pipe = self.submobjects[3:5]

        def init_colors(self):
            SVGMobject.init_colors(self)

            if not self.parts_named:
                self.name_parts()

            self.rings.set_fill(self.get_color(),opacity=1)
            self.rings.set_stroke(self.get_color(), 3)
            self.readings.set_fill(self.get_color(), opacity=1)
            self.readings.set_stroke(self.get_color(), 1)
            self.needle.set_fill(self.get_color(), opacity=1)
            self.needle.set_stroke(self.get_color(), 2)
            for mob in self.pipe:
                mob.set_stroke(self.get_color(),5)

            return self

class PumpBody(SVGMobject):
    CONFIG={
        "stroke_width": 4,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/pump_body.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.water_source_text = TextMobject("Water\\\\Source").scale(0.3)
        rect_center = 0.5*(self.box[0].get_center() + self.box[1].get_center())
        self.water_source_text.move_to(rect_center)
        self.add(self.water_source_text)

    def name_parts(self):
        self.circle = self.submobjects[0]
        self.large_tube = []
        self.large_tube.append(self.submobjects[1])
        self.large_tube.append(self.submobjects[2])
        self.large_tube.append(self.submobjects[3])
        self.large_tube.append(self.submobjects[4])
        self.small_tube = []
        self.small_tube.append(self.submobjects[5])
        self.small_tube.append(self.submobjects[6])
        self.box = self.submobjects[7:9]
        self.tube = self.submobjects[9:11]


    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        for submobject in self.submobjects:
            submobject.set_fill(WHITE, opacity=0)
            submobject.set_stroke(self.get_color(), self.get_stroke_width())

        return self

class Fins(SVGMobject):
    CONFIG={
        "stroke_width": 4,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/fins.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

        self.ang_v = (2*np.pi)*0.01
        self.angle = ValueTracker(0)
        # self.add_updater(lambda x: x.rotate_in_place(-1*self.ang_v))

    def init_colors(self):
        SVGMobject.init_colors(self)

        for submobject in self.submobjects:
            submobject.set_fill(WHITE, opacity=0)
            submobject.set_stroke(self.get_color(),self.get_stroke_width())

    # def set_angle(self):
    #     del_angle=new_angle - self.angle
    #     self.angle = new_angle
    #
    #     self.needle.rotate(
    #         -1 * DEG_TO_RAD * del_angle,
    #         about_point=self.rings.get_center()
    #     )
    #
    #     return self

class HydraulicCircuit(Mobject):
    CONFIG={
        "max_pressure": 52,
        "min_pressure": 25,
        "initial_pressure": 25,
        "start_color": 	(0.110, 0.639, 0.925),
        "end_color": (0.039, 0.267, 0.434),
        "include_water_source": False
    }

    def __init__(self,**kwargs):
        kwargs.setdefault('radius',1)
        super().__init__(**kwargs)

        self.fins = Fins().scale(1.4)
        self.body = PumpBody().scale(4.6)

        self.fins.move_to(self.body.circle.get_center())

        if not self.include_water_source:
            for mob in self.body.box:
                mob.set_opacity(0)
            for mob in self.body.tube:
                mob.set_opacity(0)
            self.body.water_source_text.set_opacity(0)

        self.angle = ValueTracker(0)
        self.radius = ValueTracker(self.get_small_tube_radius())

        self.bot_pressure = ValueTracker(self.initial_pressure)
        self.top_pressure = ValueTracker(self.initial_pressure)

        self.initialize_water()

        self.add_updater(
            lambda x:
            x.set_small_tube_radius(self.radius.get_value())
        )

        self.submobjects.extend([*self.rects_top,*self.rects_bot,self.pump_circle,self.body,self.small_rect,self.fins])

    def initialize_water(self):
        self.pump_circle=Circle(color=self.get_pressure_color(self.initial_pressure),
                                radius=self.fins.get_height() / 2.).scale(1.15)
        self.pump_circle.set_fill(color=self.get_pressure_color(self.initial_pressure),
                                  opacity=1)
        self.pump_circle.move_to(self.fins.get_center())
        self.pump_circle.add_updater(
            lambda x: x.set_color(
                [self.get_pressure_color(self.bot_pressure.get_value()),
                 self.get_pressure_color(self.top_pressure.get_value())]
            )
        )

        self.rects_top=[]

        w1=self.body.large_tube[0].get_left()[0] - self.body.large_tube[1].get_left()[0]
        rect1=Rectangle(height=self.body.large_tube[1].get_height(),
                        width=w1,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect1.next_to(self.body.large_tube[1].get_left(), buff=0)
        rect1.add_updater(lambda x: x.set_color(self.get_pressure_color(self.top_pressure.get_value())))
        self.rects_top.append(rect1)

        w2=self.body.large_tube[1].get_left()[0] - self.body.large_tube[1].get_right()[0]
        h2=self.body.large_tube[1].get_top()[1] - self.body.large_tube[0].get_top()[1]
        rect2=Rectangle(height=h2,
                        width=w2,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect2.next_to(self.body.large_tube[1].get_top(), direction=DOWN, buff=0)
        rect2.add_updater(lambda x: x.set_color(self.get_pressure_color(self.top_pressure.get_value())))
        self.rects_top.append(rect2)

        h3=self.body.large_tube[1].get_right()[0] - self.body.large_tube[0].get_right()[0]
        w3=self.body.large_tube[1].get_top()[1] - self.body.large_tube[0].get_top()[1]
        rect3=Rectangle(height=h3,
                        width=w3,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect3.next_to(rect2, direction=DOWN, buff=0, aligned_edge=RIGHT)
        rect3.shift(0.05 * LEFT)
        rect3.add_updater(lambda x: x.set_color(self.get_pressure_color(self.top_pressure.get_value())))
        self.rects_top.append(rect3)

        self.rects_bot = []

        w4=self.body.large_tube[3].get_left()[0]-self.body.large_tube[2].get_left()[0]
        h4=self.body.large_tube[2].get_top()[1]-self.body.large_tube[3].get_bottom()[1]
        rect4=Rectangle(height=h4,
                        width=w4,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect4.next_to(self.body.large_tube[3].get_left(), direction=RIGHT, buff=0)
        rect4.shift(0.2*UP)
        rect4.add_updater(lambda x: x.set_color(self.get_pressure_color(self.bot_pressure.get_value())))
        self.rects_bot.append(rect4)

        w5=self.body.large_tube[3].get_left()[0] - self.body.large_tube[3].get_right()[0]
        h5=self.body.large_tube[2].get_bottom()[1] - self.body.large_tube[3].get_bottom()[1]
        rect5=Rectangle(height=h5,
                        width=w5,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect5.next_to(self.body.large_tube[3].get_bottom(), direction=UP, buff=0)
        rect5.add_updater(lambda x: x.set_color(self.get_pressure_color(self.bot_pressure.get_value())))
        self.rects_bot.append(rect5)

        w6=h5
        h6=self.body.small_tube[0].get_bottom()[1] - self.body.large_tube[3].get_bottom()[1]
        rect6=Rectangle(height=h6,
                        width=w6,
                        fill_color=self.get_pressure_color(self.initial_pressure),
                        fill_opacity=1,
                        color=self.get_pressure_color(self.initial_pressure))
        rect6.next_to(self.body.small_tube[0].get_bottom(), direction=DOWN, buff=0)
        rect6.shift(0.1*LEFT)
        rect6.add_updater(lambda x: x.set_color(self.get_pressure_color(self.bot_pressure.get_value())))
        self.rects_bot.append(rect6)

        width=self.body.small_tube[0].get_left()[0] - self.body.small_tube[1].get_left()[0] - 0.13
        height=self.body.small_tube[0].get_height()+0.45
        self.small_rect=Rectangle(width=width,
                                  height=height,
                                  color=self.get_pressure_color(self.initial_pressure),
                                  fill_color=self.get_pressure_color(self.initial_pressure),
                                  fill_opacity=1)
        self.small_rect.next_to(self.body.small_tube[1], direction=RIGHT, buff=0.045)
        self.small_rect.add_updater(
            lambda x: x.set_color(
                [self.get_pressure_color(self.bot_pressure.get_value()),
                 self.get_pressure_color(self.top_pressure.get_value())]
            )
        )

    def get_pressure_color(self,pressure):
        alpha = (pressure-self.min_pressure)/(self.max_pressure-self.min_pressure)
        color_rgb = (
            self.start_color[0] + (self.end_color[0]-self.start_color[0])*alpha,
            self.start_color[1] + (self.end_color[1]-self.start_color[1])*alpha,
            self.start_color[2] + (self.end_color[2]-self.start_color[2])*alpha,
        )
        return rgb_to_color(color_rgb)

    def set_angle(self, new_angle):
        del_angle=new_angle - self.angle.get_value()
        self.angle.set_value(new_angle)

        self.fins.rotate_in_place(
            -1 * DEG_TO_RAD * del_angle
        )

    def get_small_tube_radius(self):
        return (self.body.small_tube[0].get_center()[0] -
                self.body.small_tube[1].get_center()[0])/2.

    def set_small_tube_radius(self, radius):
        cur_radius = self.get_small_tube_radius()
        del_radius = radius - cur_radius
        self.body.small_tube[0].shift(del_radius*RIGHT)
        self.body.small_tube[1].shift(del_radius*LEFT)
        self.small_rect.set_width(2*radius - 0.07, stretch=True)

class SealedBox(Mobject):
    def __init__(self, **kwargs):
        kwargs.setdefault('width', 4)
        kwargs.setdefault('height', 4)

        super().__init__(**kwargs)

        width = kwargs['width']
        N = 100
        dw = float(width)/float(N)
        self.rects = [[Mobject() for _ in range(N)] for __ in range(N)]
        for ix, x in enumerate(np.linspace(0, width, N)):
            for iy, y in enumerate(np.linspace(0, width, N)):
                rect_color = (0,1,0)
                self.rects[ix][iy] = Rectangle(width=dw,
                                               height=dw,
                                               color=rgb_to_color(rect_color))
                self.rects[ix][iy].move_to(x*RIGHT+y*UP)
                self.submobjects.append(self.rects[ix][iy])

