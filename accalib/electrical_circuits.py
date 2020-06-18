from manimlib.imports import *
from manimlib.constants import *
from accalib.constants import *
from accalib.particles import Electron
import random
from accalib.utils import VectorInterpolator
from functools import partial

class BatteryLampCircuit(SVGMobject):
    CONFIG={
        "battery_orange": "#f99420",
        "num_of_electrons": 10,
        # "num_of_electrons": 1,
        "bezier_approx_samples": 50
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/battery_lamp_circuit.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(3.5)

    def name_parts(self):
        self.outer_rect = self.submobjects[0]
        self.plus_sign = self.submobjects[1]
        self.minus_sign = self.submobjects[2]
        self.horz_line = self.submobjects[3]
        self.circle = self.submobjects[4]
        self.light_bulb = self.submobjects[5]
        self.base_big = self.submobjects[6]
        self.base_small = self.submobjects[7]
        self.wire_bot = self.submobjects[8]
        self.wire_top = self.submobjects[9]
        self.lightning_bolt = self.submobjects[10]
        self.filament = VGroup(*self.submobjects[11:14])

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(RED,10,opacity=0)
            mob.set_fill(RED,opacity=0)

        if not self.parts_named:
            self.name_parts()

        self.outer_rect.set_stroke(WHITE,1,opacity=1)
        self.plus_sign.set_fill(BLACK,opacity=1)
        self.plus_sign.set_stroke(BLACK,5,opacity=1)
        self.minus_sign.set_stroke(WHITE,11,opacity=1)
        # self.horz_line.set_stroke(WHITE,10,opacity=1)
        # self.circle.set_stroke(WHITE,5,opacity=1)
        self.light_bulb.set_stroke(WHITE,5,opacity=1)
        self.light_bulb.set_fill(YELLOW,opacity=0.9)
        self.base_big.set_fill(DARK_GREY,opacity=1)
        self.base_big.set_stroke(DARK_GREY,5,opacity=1)
        self.base_small.set_fill(DARK_GREY, opacity=1)
        self.base_small.set_stroke(DARK_GREY, 5, opacity=1)
        self.filament.set_stroke(BLACK,1,opacity=1)
        self.wire_bot.set_stroke(WHITE,5,opacity=1)
        self.wire_top.set_stroke(WHITE,5,opacity=1)
        self.lightning_bolt.set_fill(YELLOW,opacity=1)

        self.top_rect = Rectangle(
            width=self.outer_rect.get_width(),
            height=self.outer_rect.get_top()[1]-self.horz_line.get_top()[1],
            stroke_opacity=0
        )\
            .move_to(self.plus_sign.get_center())\
            .set_fill("#a95e27",1)
        self.bot_rect=Rectangle(
            width=self.outer_rect.get_width(),
            height=self.horz_line.get_top()[1]-self.outer_rect.get_bottom()[1],
            stroke_opacity=0
        )\
            .move_to(
                self.outer_rect.get_center()[0]*RIGHT+
                0.5*(self.horz_line.get_bottom()[1]+self.outer_rect.get_bottom()[1])*UP
            )\
            .set_fill(BLACK,1)
        self.block_rect=self.base_big.copy().set_color(BLACK)
        self.block_rect.set_width(self.base_big.get_width()+0.8,stretch=True)
        self.block_rect.shift(0.8*LEFT)

        self.add(
            self.top_rect,
            self.bot_rect,
            self.outer_rect,
            self.plus_sign,
            self.horz_line,
            self.lightning_bolt,
            self.block_rect,
            self.base_big,
            self.base_small,
            self.minus_sign
        )

        return self

    def setup_electrons(self):
        bezier_func_bot=bezier(self.wire_bot.get_points())
        bezier_func_top=bezier(self.wire_top.get_points())
        points=[]
        for i in range(self.bezier_approx_samples):
            points+=[bezier_func_bot(float(i)/ float(self.bezier_approx_samples))]
        for i in range(self.bezier_approx_samples):
            points+=[bezier_func_top(1.-(float(i)/float(self.bezier_approx_samples)))]

        self.electron_vect_inter=VectorInterpolator(points)

        self.electrons_flowing=True
        self.electron_disps=[0] * self.num_of_electrons
        self.electrons=[]
        self.electron_loc=ValueTracker(0)
        for i in range(self.num_of_electrons):
            self.electrons+=[Electron()]
            self.electrons[-1].add_updater(
                partial(self.electron_updater, i=i),
                call_updater=True
            )
        self.add(
            *self.electrons,
            self.top_rect,
            self.bot_rect,
            self.outer_rect,
            self.plus_sign,
            self.horz_line,
            self.lightning_bolt,
            self.minus_sign,
            self.block_rect,
            self.base_big,
            self.base_small
        )

    def remove_electrons(self):
        for electron in self.electrons:
            electron.clear_updaters()
            self.remove(electron)

    # turn on/off light bulb
    def set_light_bulb_state(self,new_state):
        if new_state:
            self.light_bulb.set_fill(YELLOW)
        else:
            self.light_bulb.set_fill(BLACK)

    def electron_updater(self, x, i):
        cur=(self.electron_loc.get_value() + i / self.num_of_electrons + self.electron_disps[i]) % 1

        # always move if electrons are flowing
        if self.electrons_flowing:
            x.move_to(
                self.electron_vect_inter.interpolate(cur)
            )
            return

        # change due to random motion
        diff=(2 * random.random() - 1) * 0.01

        # down move if inside voltage source
        if 0.755 < (cur + diff) % 1 < 1:
            return

        x.move_to(
            self.electron_vect_inter.interpolate(
                (cur + diff) % 1
            )
        )
        self.electron_disps[i]+=diff

class GeneratorLampCircuit(SVGMobject):
    CONFIG={
        "num_of_electrons": 8,
        "bezier_approx_samples": 50
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/generator_lamp_circuit.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(1.9)
        self.add_generator_text()

    def name_parts(self):
        self.light_bulb = self.submobjects[0]
        self.base_big = self.submobjects[1]
        self.base_small = self.submobjects[2]
        self.filament = VGroup(*self.submobjects[3:6])
        self.rect = self.submobjects[6]
        self.top_sine = self.submobjects[7]
        self.bot_sine = self.submobjects[8]
        self.wire_top = self.submobjects[9]
        self.wire_bot = self.submobjects[10]

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(RED,10,opacity=0)
            mob.set_fill(RED,opacity=0)

        if not self.parts_named:
            self.name_parts()

        self.light_bulb.set_stroke(WHITE, 5, opacity=1)
        self.light_bulb.set_fill(YELLOW, opacity=0.9)
        self.base_big.set_fill(DARK_GREY, opacity=1)
        self.base_big.set_stroke(DARK_GREY, 5, opacity=1)
        self.base_small.set_fill(DARK_GREY, opacity=1)
        self.base_small.set_stroke(DARK_GREY, 5, opacity=1)
        self.filament.set_stroke(BLACK, 1, opacity=1)
        self.rect.set_stroke(WHITE, 3, opacity=1)
        self.rect.set_fill(BLACK,opacity=1)
        self.top_sine.set_stroke(WHITE, 2, opacity=1)
        self.bot_sine.set_stroke(WHITE, 2, opacity=1)
        self.wire_bot.set_stroke(WHITE, 5, opacity=1)
        self.wire_top.set_stroke(WHITE, 5, opacity=1)

        self.block_rect=self.base_big.copy().set_color(BLACK)
        self.block_rect.set_width(self.base_big.get_width() + 0.8, stretch=True)
        self.block_rect.shift(0.8 * LEFT)
        self.add(
            self.block_rect,
            self.base_small,
            self.base_big
        )

        self.bot_sine.flip()

        return self

    def add_generator_text(self):
        self.generator_text = TextMobject("Generator")\
            .next_to(self.rect.get_top(),direction=DOWN)
        self.add(
            self.generator_text
        )

    def setup_electrons(self):
        bezier_func_bot=bezier(self.wire_bot.get_points())
        bezier_func_top=bezier(self.wire_top.get_points())
        points=[]
        for i in range(self.bezier_approx_samples):
            points+=[bezier_func_bot(float(i)/ float(self.bezier_approx_samples))]
        points.insert(0,points[0]+LEFT)
        for i in range(self.bezier_approx_samples):
            points+=[bezier_func_top(1.-(float(i)/float(self.bezier_approx_samples)))]
        points.append(points[-1]+LEFT)

        self.electron_vect_inter=VectorInterpolator(points)

        self.electrons_flowing=True
        self.electron_disps=[0] * self.num_of_electrons
        self.electrons=[]
        self.electron_loc=ValueTracker(0)
        for i in range(self.num_of_electrons):
            self.electrons+=[Electron()]
            self.electrons[-1].add_updater(
                partial(self.electron_updater, i=i),
                call_updater=True
            )
        self.add(
            *self.electrons,
            self.rect,
            self.bot_sine,
            self.top_sine,
            self.generator_text,
            self.block_rect,
            self.base_big,
            self.base_small
        )

    def electron_updater(self, x, i):
        cur=(self.electron_loc.get_value() + i / self.num_of_electrons + self.electron_disps[i]) % 1

        # always move if electrons are flowing
        if self.electrons_flowing:
            x.move_to(
                self.electron_vect_inter.interpolate(cur)
            )
            return

        # change due to random motion
        diff=(2 * random.random() - 1) * 0.005

        # # down move if inside voltage source
        # if 0.78 < (cur + diff) % 1 < 0.925:
        #     return

        x.move_to(
            self.electron_vect_inter.interpolate(
                (cur + diff) % 1
            )
        )
        self.electron_disps[i]+=diff

class ComplexCircuitTimeDomain(SVGMobject):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN,
        "voltage_colors": [GREEN_C, RED_C, BLUE_C, TEAL_C, PURPLE_C],
        "unit_color": ORANGE
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named = False
        svg_file = "images/ep1/DiffyEqToComplex/circuit_timedomain.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(4)
        # self.vs_label.shift(0.3*RIGHT)

    def name_parts(self):
        self.lines = VGroup(*self.submobjects[0:22])
        self.plus_minus = VGroup(*self.submobjects[22:26])
        self.capacitor = VGroup(*self.submobjects[26:30])
        self.inductor = self.submobjects[30]
        self.dots = VGroup(*self.submobjects[31:35])
        self.other_text = VGroup(*self.submobjects[35:49])
        self.other_text.add(*self.submobjects[49:73])
        self.vs_label = VGroup(*self.submobjects[49:73])
        self.arrows = VGroup(*self.submobjects[73:80])
        self.i_text = VGroup(*self.submobjects[80:94])
        self.v_texts = VGroup(
            VGroup(*self.submobjects[94:96]),
            VGroup(*self.submobjects[96:98]),
            VGroup(*self.submobjects[98:100]),
            VGroup(*self.submobjects[100:102]),
            VGroup(*self.submobjects[102:104]),
        )
        self.ground = VGroup(*self.submobjects[104:109])

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
            mob.set_fill(RED, opacity=0)

        if not self.parts_named:
            self.name_parts()

        for i in range(5):
            self.v_texts[i].set_stroke(self.voltage_colors[i], self.get_stroke_width(), opacity=0)
            self.v_texts[i].set_fill(self.voltage_colors[i], opacity=1)

        self.lines.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.lines.set_fill(YELLOW, opacity=0)
        self.plus_minus.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.plus_minus.set_fill(YELLOW, opacity=0)
        self.capacitor.set_stroke(self.get_color(), self.get_stroke_width()*2, opacity=1)
        self.capacitor.set_fill(YELLOW, opacity=0)
        self.inductor.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.inductor.set_fill(YELLOW, opacity=0)
        self.dots.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
        self.dots.set_fill(self.get_color(), opacity=1)
        self.other_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.other_text.set_fill(self.unit_color, opacity=1)
        self.arrows.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.arrows.set_fill(self.current_color, opacity=1)
        self.i_text.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.i_text.set_fill(self.current_color, opacity=1)
        self.ground.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.ground.set_fill(YELLOW, opacity=0)

        return self

class ComplexCircuitFreqDomain(SVGMobject):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN_C,
        "voltage_colors": [GREEN ,RED, BLUE, TEAL_C, PURPLE_C],
        "unit_color": ORANGE,
        "j_color": PURPLE_C
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named = False
        svg_file = "images/ep1/DiffyEqToComplex/circuit_freqdomain.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(4)
        # self.volt_text.shift(0.3*RIGHT)

    def name_parts(self):
        self.lines = VGroup(*self.submobjects[0:23])
        self.plus_minus = VGroup(*self.submobjects[23:26])
        self.capacitor = VGroup(*self.submobjects[26:30])
        self.inductor = self.submobjects[30]
        self.dots = VGroup(*self.submobjects[31:35])
        self.other_text = VGroup(*self.submobjects[36:64])
        self.arrows = VGroup(*self.submobjects[64:71])
        self.i_text = VGroup(*self.submobjects[71:85])
        self.v_texts = VGroup(
            VGroup(*self.submobjects[85:87]),
            VGroup(*self.submobjects[87:89]),
            VGroup(*self.submobjects[89:91]),
            VGroup(*self.submobjects[91:93]),
            VGroup(*self.submobjects[93:95]),
        )
        self.ground = VGroup(*self.submobjects[95:99])
        self.volt_src_text = VGroup(*self.submobjects[99:101],*self.submobjects[102:107])
        self.angle_symbol = self.submobjects[101]
        self.j_text = VGroup(*self.submobjects[107:110])

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
            mob.set_fill(RED, opacity=0)

        if not self.parts_named:
            self.name_parts()

        for i in range(5):
            self.v_texts[i].set_stroke(self.voltage_colors[i], self.get_stroke_width(), opacity=0)
            self.v_texts[i].set_fill(self.voltage_colors[i], opacity=1)

        self.lines.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.lines.set_fill(YELLOW, opacity=0)
        self.plus_minus.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.plus_minus.set_fill(YELLOW, opacity=0)
        self.capacitor.set_stroke(self.get_color(), self.get_stroke_width()*2, opacity=1)
        self.capacitor.set_fill(YELLOW, opacity=0)
        self.inductor.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.inductor.set_fill(YELLOW, opacity=0)
        self.dots.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
        self.dots.set_fill(self.get_color(), opacity=1)
        self.volt_src_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.volt_src_text.set_fill(self.unit_color, opacity=1)
        self.other_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.other_text.set_fill(self.unit_color, opacity=1)
        self.arrows.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.arrows.set_fill(self.current_color, opacity=1)
        self.i_text.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.i_text.set_fill(self.current_color, opacity=1)
        self.ground.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.ground.set_fill(YELLOW, opacity=0)
        self.angle_symbol.set_stroke(self.unit_color, self.get_stroke_width()*0.5, opacity=1)
        self.angle_symbol.set_fill(self.unit_color, opacity=0)
        self.j_text.set_stroke(self.j_color, self.get_stroke_width(), opacity=0)
        self.j_text.set_fill(self.j_color, opacity=1)

        return self