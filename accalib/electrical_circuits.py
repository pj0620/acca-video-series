from manimlib.imports import *
from manimlib.constants import *
from accalib.constants import *
from accalib.particles import Electron
import random
from accalib.utils import VectorInterpolator
from functools import partial
from accalib.rate_functions import accelerated
import numpy.polynomial.polynomial as poly

class BatteryLampCircuit(SVGMobject):
    CONFIG={
        "battery_orange": "#f99420",
        "num_of_electrons": 10,
        # "num_of_electrons": 1,
        "bezier_approx_samples": 50,
        "electron_freq": 0.11,
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/battery_lamp_circuit.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(3.5)
        self.battery = VGroup(
            self.top_rect,
            self.bot_rect,
            self.outer_rect,
            self.plus_sign,
            self.minus_sign,
            self.horz_line,
            self.lightning_bolt,
        )

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

    def set_electron_freq(self, new_freq):
        self.electron_freq = new_freq

    def setup_electrons(self, add_electrons=True):
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
            self.electrons+=[Electron().scale(0.2)]
            self.electrons[-1].add_updater(
                partial(self.electron_updater, i=i),
                call_updater=True
            )
        if not add_electrons:
            return
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

    def get_electron_acceleration_anim(self, new_freq, run_time=1):
        acc_anim = ApplyMethod(
            self.electron_loc.increment_value,
            ((self.electron_freq + new_freq) / 2) * run_time,
            run_time=run_time,
            rate_func=partial(accelerated, f0=self.electron_freq, f1=new_freq)
        )
        self.electron_freq = new_freq
        return acc_anim

    def get_electron_anim(self, run_time=1):
        return ApplyMethod(
            self.electron_loc.increment_value,
            run_time * self.electron_freq,
            run_time=run_time,
            rate_func=linear
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
        diff=(2 * random.random() - 1) * 0.005

        # down move if inside voltage source
        if 0.755 < (cur + diff) % 1 < 1:
            return

        x.move_to(
            self.electron_vect_inter.interpolate(
                (cur + diff) % 1
            )
        )
        self.electron_disps[i]+=diff

class BatteryLampCircuitAC(SVGMobject):
    CONFIG={
        "battery_orange": "#f99420",
        "num_of_electrons": 10,
        # "num_of_electrons": 1,
        "bezier_approx_samples": 50,
        "electron_freq": 3.5,
        "electron_amplitude": 0.15
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named=False
        svg_file="images/svgs/battery_lamp_circuit_ac.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(3.5)

        # used to animate changing electron amplitude
        self.changing_elec_amplitude = False
        self.new_amplitude = None
        self.start_amplitude = None

        # used to animate changing electron frequency
        self.changing_elec_freq = False
        self.new_freq = None
        self.inter_coefs = None
        self.start_time = None
        self.change_duration = None

    def name_parts(self):
        self.outer_rect = self.submobjects[0]
        self.circle = self.submobjects[1]
        self.light_bulb = self.submobjects[2]
        self.base_big = self.submobjects[3]
        self.base_small = self.submobjects[4]
        self.wire_bot = self.submobjects[5]
        self.wire_top = self.submobjects[6]
        self.filament = VGroup(*self.submobjects[7:10])
        self.sine_wave = self.submobjects[10]

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(RED,10,opacity=0)
            mob.set_fill(RED,opacity=0)

        if not self.parts_named:
            self.name_parts()

        self.outer_rect.set_stroke(WHITE, 3, opacity=1)
        self.light_bulb.set_stroke(WHITE,5,opacity=1)
        self.light_bulb.set_fill(YELLOW,opacity=0.9)
        self.base_big.set_fill(DARK_GREY,opacity=1)
        self.base_big.set_stroke(DARK_GREY,5,opacity=1)
        self.base_small.set_fill(DARK_GREY, opacity=1)
        self.base_small.set_stroke(DARK_GREY, 5, opacity=1)
        self.filament.set_stroke(BLACK,1,opacity=1)
        self.wire_bot.set_stroke(WHITE,5,opacity=1)
        self.wire_top.set_stroke(WHITE,5,opacity=1)
        self.sine_wave.set_stroke(BLUE_C, 5, opacity=1).scale(0.9)
        self.circle.set_stroke(RED_C, 3, opacity=1)

        self.battery_rect = Rectangle(
            width=self.outer_rect.get_width(),
            height=self.outer_rect.get_height(),
            stroke_opacity=0
        )\
            .move_to(self.outer_rect.get_center())\
            .set_fill(BLACK,1)
        self.block_rect=self.base_big.copy().set_color(BLACK)
        self.block_rect.set_width(self.base_big.get_width()+1.5, stretch=True)
        self.block_rect.shift(1.5*LEFT)

        self.add(
            self.battery_rect,
            self.block_rect,
            self.outer_rect,
            self.base_big,
            self.base_small,
            self.sine_wave,
            self.circle
        )

        return self

    def set_electron_freq_anim(self, new_freq, run_time=1):
        if self.changing_elec_freq:
            raise Exception(f"cannot change freq of sine wave to {new_freq} while "
                            f"still changing amplitude to {self.electron_freq}")

        self.changing_elec_freq = True
        self.new_freq = new_freq
        self.start_time = self.electron_time.get_value()
        self.change_duration = run_time

        # find fit points
        fit_points = []
        N_approx = 3
        T1 = 0.5*((2*PI)/self.electron_freq)
        T2 = 0.5*((2*PI)/self.new_freq)
        for i in range(N_approx):
            # left approx point
            t1 = self.start_time - (T1/N_approx)*i
            y1 = self.electron_amplitude*(1-np.cos(self.electron_freq*t1))
            fit_points.append((t1, y1))

            # right approx point
            t2 = self.start_time + run_time + (T2 / N_approx) * i
            y2 = self.electron_amplitude * (1 - np.cos(self.new_freq * t2))
            fit_points.append((t2, y2))

        # sort by time
        fit_points = sorted(fit_points, key=lambda x: x[0])

        # convert to numpy arrays
        x = np.array([point[0] for point in fit_points])
        y = np.array([point[1] for point in fit_points])

        # polynomial fit
        self.inter_coefs = poly.polyfit(x, y, 2*N_approx)

    def set_electron_amplitude_anim(self, new_amplitude, run_time=1):
        if self.changing_elec_amplitude:
            raise Exception(f"cannot change amplitude of sine wave to {new_amplitude} while "
                            f"still changing amplitude to {self.new_amplitude}")

        self.changing_elec_amplitude = True
        self.new_amplitude = new_amplitude
        self.start_amplitude = self.electron_amplitude
        self.start_time = self.electron_time.get_value()
        self.change_duration = run_time

    def set_electron_freq(self, new_freq):
        self.electron_freq = new_freq

    def setup_electrons(self, add_electrons=True):
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
        self.electron_time=ValueTracker(0)
        for i in range(self.num_of_electrons):
            self.electrons+=[Electron().scale(0.2)]
            self.electrons[-1].add_updater(
                partial(self.electron_updater, i=i),
                call_updater=True
            )
        if add_electrons:
            self.add(
                *self.electrons,
                self.battery_rect,
                self.outer_rect,
                self.block_rect,
                self.base_big,
                self.base_small,
                self.sine_wave,
                self.circle
            )

        self.electron_phase = -np.pi/2 # radians

    def get_instantaneous_current(self):
        return self.electron_amplitude*np.sin(self.electron_time.get_value()*self.electron_freq)

    def get_electron_anim(self, run_time=1):
        return ApplyMethod(
            self.electron_time.increment_value,
            run_time,
            run_time=run_time,
            rate_func=linear
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
        #       ##  Changing Amplitude ##
        #   t  = self.abs_elec_pos.get_value()
        #   t0 = self.start_argument
        #   A1 = self.electron_amplitude
        #   A2 = self.new_amplitude
        #   wT = self.change_duration_rad
        #   w  = angular frequency
        #
        #   l = (A1 + ((t-t0)/wT)*(A2-A1))(1-cos(t))(1/w)
        #
        if self.changing_elec_amplitude:
            alpha = (self.electron_time.get_value() - self.start_time)/self.change_duration
            self.electron_amplitude = self.start_amplitude + alpha * (self.new_amplitude - self.start_amplitude)

            # stop changing amplitude if we are finished
            if alpha >= 1:
                self.electron_amplitude = self.new_amplitude

                self.changing_elec_amplitude = False
                self.new_amplitude = None
                self.start_amplitude = None
                self.start_time = None
                self.change_duration = None
            loc = self.electron_amplitude * (1 - np.cos(self.electron_time.get_value() * self.electron_freq))

        # changing frequency
        elif self.changing_elec_freq:
            alpha = (self.electron_time.get_value() - self.start_time) / self.change_duration
            if alpha >= 1:
                # set to new frequency
                self.electron_freq = self.new_freq

                self.changing_elec_freq = False
                self.new_freq = None
                self.inter_coefs = None
                self.start_time = None
                self.change_duration = None

                loc = self.electron_amplitude * (1 - np.cos(self.electron_time.get_value() * self.electron_freq))
            else:
                loc = poly.polyval(self.electron_time.get_value(), self.inter_coefs)

        # nothing being changed
        else:
            loc = self.electron_amplitude * (1 - np.cos(self.electron_time.get_value() * self.electron_freq))

        cur= (loc + i / self.num_of_electrons + self.electron_disps[i]) % 1

        # always move if electrons are flowing
        if self.electrons_flowing:
            x.move_to(
                self.electron_vect_inter.interpolate(cur)
            )
            return

        # change due to random motion
        diff=(2 * random.random() - 1) * 0.005

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

class SimpleCircuitTimeDomain(SVGMobject):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN,
        "voltage_colors": [GREEN_C, RED_C],
        "unit_color": ORANGE
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named = False
        svg_file = "images/ep1/ACCAApplication/circuit_simple_time.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(4)
        # self.vs_label.shift(0.3*RIGHT)

    def name_parts(self):
        self.arrow_base = self.submobjects[0]
        self.arrow_tip_small = self.submobjects[1]
        self.lines = VGroup(*self.submobjects[2:11])
        self.arrow_current = self.submobjects[11]
        self.i_label = self.submobjects[12]
        self.v_texts = VGroup(
                VGroup(*self.submobjects[13:15]),
                VGroup(*self.submobjects[15:17])
            )
        self.L_text = VGroup(*self.submobjects[17:19])
        self.R_text = VGroup(*self.submobjects[19:21])
        self.vs_text = VGroup(*self.submobjects[21:33])
        self.ground = VGroup(*self.submobjects[33:37])

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
            mob.set_fill(RED, opacity=0)

        if not self.parts_named:
            self.name_parts()

        for i in range(2):
            self.v_texts[i].set_stroke(self.voltage_colors[i], self.get_stroke_width(), opacity=0)
            self.v_texts[i].set_fill(self.voltage_colors[i], opacity=1)

        self.arrow_base.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.arrow_base.set_fill(YELLOW, opacity=0)
        self.arrow_tip_small.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.arrow_tip_small.set_fill(WHITE, opacity=1)
        self.lines.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.lines.set_fill(YELLOW, opacity=0)
        self.arrow_current.set_stroke(WHITE, self.get_stroke_width(), opacity=0)
        self.arrow_current.set_fill(self.current_color, opacity=1)
        self.i_label.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.i_label.set_fill(self.current_color, opacity=1)
        self.L_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.L_text.set_fill(self.unit_color, opacity=1)
        self.R_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.R_text.set_fill(self.unit_color, opacity=1)
        self.vs_text.set_stroke(self.unit_color, self.get_stroke_width(), opacity=0)
        self.vs_text.set_fill(self.unit_color, opacity=1)
        self.ground.set_stroke(self.get_color(), self.get_stroke_width(), opacity=1)
        self.ground.set_fill(YELLOW, opacity=0)

        return self

class SimpleCircuitFreqDomain(SVGMobject):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN_C,
        "voltage_color": RED_C,
        "inductor_color": ORANGE,
        "resistor_color": BLUE_C
    }

    def __init__(self, mode="plain", **kwargs):
        self.parts_named = False
        svg_file = "images/ep1/ACCAApplication/circuit_simple_freq.svg"
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        self.scale(3.5)
        # self.vs_label.shift(0.3*RIGHT)

    def name_parts(self):
        self.arrow_base = self.submobjects[0]
        self.arrow_tip_small = self.submobjects[1]
        self.lines = VGroup(*self.submobjects[2:11])
        self.arrow_current = self.submobjects[11]
        self.L_text = VGroup(*self.submobjects[12:14])
        self.R_text = VGroup(*self.submobjects[14:16])
        self.vs_text = VGroup(*self.submobjects[16:28])
        self.ground = VGroup(*self.submobjects[28:32])
        self.v_label = self.submobjects[32]
        self.i_label = self.submobjects[33]

    def init_colors(self):
        SVGMobject.init_colors(self)

        # set opacity of every submobject to 0
        for mob in self.submobjects:
            mob.set_stroke(self.get_color(), self.get_stroke_width(), opacity=0)
            mob.set_fill(RED, opacity=0)

        if not self.parts_named:
            self.name_parts()

        # for i in range(2):
        #     self.v_texts[i].set_stroke(self.voltage_colors[i], self.get_stroke_width(), opacity=0)
        #     self.v_texts[i].set_fill(self.voltage_colors[i], opacity=1)

        self.arrow_base.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.arrow_base.set_fill(YELLOW, opacity=0)
        self.arrow_tip_small.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.arrow_tip_small.set_fill(WHITE, opacity=1)
        self.lines.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.lines.set_fill(YELLOW, opacity=0)
        self.arrow_current.set_stroke(WHITE, self.get_stroke_width(), opacity=0)
        self.arrow_current.set_fill(self.current_color, opacity=1)
        self.L_text.set_stroke(self.inductor_color, self.get_stroke_width(), opacity=0)
        self.L_text.set_fill(self.inductor_color, opacity=1)
        self.R_text.set_stroke(self.resistor_color, self.get_stroke_width(), opacity=0)
        self.R_text.set_fill(self.resistor_color, opacity=1)
        self.vs_text.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.vs_text.set_fill(self.current_color, opacity=1)
        self.ground.set_stroke(WHITE, self.get_stroke_width(), opacity=1)
        self.ground.set_fill(YELLOW, opacity=0)
        self.v_label.set_stroke(self.voltage_color, self.get_stroke_width(), opacity=0)
        self.v_label.set_fill(self.voltage_color, opacity=1)
        self.i_label.set_stroke(self.current_color, self.get_stroke_width(), opacity=0)
        self.i_label.set_fill(self.current_color, opacity=1)

        return self