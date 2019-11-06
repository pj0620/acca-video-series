#!/usr/bin/env python

from manimlib.imports import *
from phasorlib.constants import *
from phasorlib.tools import *
from functools import partial
import sys
import datetime

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was1
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

class AmplitudeScene(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 8,
        "x_axis_width": 14,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$t$",
        "y_min": -2,
        "y_max": 2,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$Im\{z - z_0\}$",
        "axes_color": AXIS_COLOR,
        "graph_origin": ORIGIN,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": [BLUE, GREEN, RED],
        "default_derivative_color": GREEN,
        "default_input_color": RED,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
        T_sim = 3   #sec
        T_real = 25
        N = 80
        dt_sim = float(T_sim)/float(N)  # sec
        dt_real = float(T_real)/float(N) # sec
        ang_freq = (3/2)*PI         # rad/sec
        ampl = 2
        phase = PI/4       #rad/s

        # create grid
        self.setup_axes(animate=True)

        # create sin wave
        func_graph = self.get_graph(
                                    partial(self.sin, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    WHITE,
                                    x_min=0
                                    )
        func_graph.color_using_background_image("images/func_bg.png")
        # graph_lab = self.get_graph_label(self.sin, label="sin(x)")
        self.play(FadeIn(func_graph))

        init_circ_point = np.array([self.cos(0, ang_freq=ang_freq, ampl=ampl, phase=phase) - ampl,
                                    self.sin(0, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    0])
        init_sin_point  = np.array([0,
                                    self.sin(0, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    0])

        # create path circle
        circle = Circle(radius=ampl)
        circle.move_to(LEFT*ampl)
        circle.color_using_background_image("images/func_bg.png")
        self.play(FadeIn(circle))

        # initialize arrow
        phasor = Arrow(LEFT*ampl)
        phasor.color_using_background_image("images/func_bg.png")
        phasor.put_start_and_end_on(LEFT*ampl, init_circ_point)
        self.play(GrowArrow(phasor))

        # initialize line from phasor tip to point on circle
        height_line = Line(start=init_circ_point,end=init_sin_point)
        height_line.set_color(LINE_COLOR)
        self.play(FadeIn(height_line))

        # write z0 label/dot
        z0_dot = Dot(LEFT * ampl)
        z0_dot.set_color(Z0_DOT_COLOR)
        self.play(FadeIn(z0_dot))
        z0_label = TextMobject("$z_0$")
        z0_label.move_to(LEFT*ampl+DOWN*Z0_LABEL_OFFSET)
        self.play(Write(z0_label))

        # write z label/dot
        z_dot = Dot(init_circ_point)
        z_dot.set_color(Z_DOT_COLOR)
        self.play(FadeIn(z_dot))
        z_label = TextMobject("$z$")
        z_label.move_to(init_circ_point + Z_LABEL_OFFSET_INIT*(RIGHT+UP))
        self.play(Write(z_label))

        # write sine properties
        props_text = TextMobject("$V_M = " + "{0:.1f}".format(ampl) + "$" + "\\linebreak" +
                                 "$\\omega = " + frac_pi_str(ang_freq) + "\\hspace{1mm} \\frac{rad}{s}$" + "\\linebreak" +
                                 "$\\phi = " + frac_pi_str(phase) + "\\hspace{1mm} rad$"
                                )
        props_text.move_to(2*LEFT*ampl + LEFT*SINE_PROP_OFFSET_X + UP*SINE_PROP_OFFSET_Y)
        self.play(FadeIn(props_text))

        # initialize phasor equation
        complex_eq_text = TextMobject("$z - z_0 = V_M e^{j (\\omega t + \\phi ) }$",
                                      "$\\implies Im\{z-z_0\} = V_M sin(\\omega t + \\phi)$")
        complex_eq_text.move_to(1 * LEFT + 3.5 * UP)
        self.play(Write(complex_eq_text[0]))
        self.wait(2)
        self.play(Write(complex_eq_text[1]))

        print("real world time-delta " + str(dt_real) + " seconds")
        print("simulation time-delta " + str(dt_sim) + " seconds")

        # simulation time
        t_sim = 0  # s

        # rotate arrow loop
        for i in range(N+1):

            # wait for r
            self.wait(dt_real)

            # tip of phasor on circle
            circle_point = np.array(
                [self.cos(t_sim, ang_freq, ampl, phase) - ampl,
                 self.sin(t_sim, ang_freq, ampl, phase),
                 0]
                                    )

            # rotate arrow
            phasor.put_start_and_end_on(LEFT*ampl,circle_point)

            # update line from tip of phasor to sine wave
            sine_point = np.array([t_sim,
                                   self.sin(t_sim,ang_freq,ampl,phase),
                                   0]
                                  )
            height_line.put_start_and_end_on(start=circle_point,end=sine_point)

            # update z dot/label
            r_unit_vector = np.array([self.cos(t_sim,ang_freq=ang_freq,ampl=ampl,phase=phase),
                                      self.sin(t_sim,ang_freq=ang_freq,ampl=ampl,phase=phase),
                                      0])
            z_dot.move_to(circle_point)
            z_label.move_to(circle_point + Z_LABEL_OFFSET*r_unit_vector)

            t_sim += dt_sim

            update_progress(t_sim/T_sim,label="Rendering")

        self.wait(0.5)

    # create clock
    def setup_clock(self):
        clock = Clock()
        clock.set_height(1)
        clock.to_corner(UR)
        clock.shift(MED_LARGE_BUFF * LEFT)

        time_lhs = TextMobject("Time: ")
        time_label = DecimalNumber(
            0, num_decimal_places=2,
        )
        time_rhs = TextMobject("s")
        time_group = VGroup(
            time_lhs,
            time_label,
            # time_rhs
        )
        time_group.arrange(RIGHT, aligned_edge=DOWN)
        time_rhs.shift(SMALL_BUFF * LEFT)
        time_group.next_to(clock, DOWN)

        self.time_group = time_group
        self.time_label = time_label
        self.clock = clock

    # sine and cosine
    def sin(self, t, ang_freq=1, ampl=1, phase=0):
        return ampl*np.sin(ang_freq*t+phase)
    def cos(self, t, ang_freq=1, ampl=1, phase=0):
        return ampl*np.cos(ang_freq*t+phase)

class PhasorScene2(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 8,
        "x_axis_width": 14,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$t$",
        "y_min": -2,
        "y_max": 2,
        "y_axis_height": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$Im\{z - z_0\}$",
        "axes_color": AXIS_COLOR,
        "graph_origin": ORIGIN,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": [BLUE, GREEN, RED],
        "default_derivative_color": GREEN,
        "default_input_color": RED,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
        T_sim = 3   #sec
        T_real = 25
        N = 80
        dt_sim = float(T_sim)/float(N)  # sec
        dt_real = float(T_real)/float(N) # sec
        ang_freq = (0.02)*PI         # rad/sec
        ampl = 1.5
        phase = PI/8       #rad/s

        # create grid
        self.setup_axes(animate=True)

        # create sin wave
        func_graph = self.get_graph(
                                    partial(self.sin, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    WHITE,
                                    x_min=0
                                    )
        func_graph.color_using_background_image("images/func_bg.png")
        # graph_lab = self.get_graph_label(self.sin, label="sin(x)")
        self.play(FadeIn(func_graph))

        init_circ_point = np.array([self.cos(0, ang_freq=ang_freq, ampl=ampl, phase=phase) - ampl,
                                    self.sin(0, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    0])
        init_sin_point  = np.array([0,
                                    self.sin(0, ang_freq=ang_freq, ampl=ampl, phase=phase),
                                    0])

        # create path circle
        circle = Circle(radius=ampl)
        circle.move_to(LEFT*ampl)
        circle.color_using_background_image("images/func_bg.png")
        self.play(FadeIn(circle))

        # initialize arrow
        phasor = Arrow(LEFT*ampl)
        phasor.color_using_background_image("images/func_bg.png")
        phasor.put_start_and_end_on(LEFT*ampl, init_circ_point)
        self.play(GrowArrow(phasor))

        # initialize line from phasor tip to point on circle
        height_line = Line(start=init_circ_point,end=init_sin_point)
        height_line.set_color(LINE_COLOR)
        self.play(FadeIn(height_line))

        # write z0 label/dot
        z0_dot = Dot(LEFT * ampl)
        z0_dot.set_color(Z0_DOT_COLOR)
        self.play(FadeIn(z0_dot))
        z0_label = TextMobject("$z_0$")
        z0_label.move_to(LEFT*ampl+DOWN*Z0_LABEL_OFFSET)
        self.play(Write(z0_label))

        # write z label/dot
        z_dot = Dot(init_circ_point)
        z_dot.set_color(Z_DOT_COLOR)
        self.play(FadeIn(z_dot))
        z_label = TextMobject("$z$")
        z_label.move_to(init_circ_point + Z_LABEL_OFFSET_INIT*(RIGHT+UP))
        self.play(Write(z_label))

        # write sine properties
        props_text = TextMobject("$V_M = " + "{0:.1f}".format(ampl) + "$" + "\\linebreak" +
                                 "$\\omega = " + frac_pi_str(ang_freq) + "\\hspace{1mm} \\frac{rad}{s}$" + "\\linebreak" +
                                 "$\\phi = " + frac_pi_str(phase) + "\\hspace{1mm} rad$"
                                )
        props_text.move_to(2*LEFT*ampl + LEFT*SINE_PROP_OFFSET_X + UP*SINE_PROP_OFFSET_Y)
        self.play(FadeIn(props_text))

        # initialize phasor equation
        complex_eq_text = TextMobject("$z - z_0 = V_M e^{j (\\omega t + \\phi ) }$",
                                      "$\\implies Im\{z-z_0\} = V_M sin(\\omega t + \\phi)$")
        complex_eq_text.move_to(1 * LEFT + 3.5 * UP)
        self.play(Write(complex_eq_text[0]))
        self.wait(2)
        self.play(Write(complex_eq_text[1]))

        print("real world time-delta " + str(dt_real) + " seconds")
        print("simulation time-delta " + str(dt_sim) + " seconds")

        # simulation time
        t_sim = 0  # s

        # rotate arrow loop
        for i in range(N+1):

            # wait for r
            self.wait(dt_real)

            # tip of phasor on circle
            circle_point = np.array(
                [self.cos(t_sim, ang_freq, ampl, phase) - ampl,
                 self.sin(t_sim, ang_freq, ampl, phase),
                 0]
                                    )

            # rotate arrow
            phasor.put_start_and_end_on(LEFT*ampl,circle_point)

            # update line from tip of phasor to sine wave
            sine_point = np.array([t_sim,
                                   self.sin(t_sim,ang_freq,ampl,phase),
                                   0]
                                  )
            height_line.put_start_and_end_on(start=circle_point,end=sine_point)

            # update z dot/label
            r_unit_vector = np.array([self.cos(t_sim,ang_freq=ang_freq,ampl=ampl,phase=phase),
                                      self.sin(t_sim,ang_freq=ang_freq,ampl=ampl,phase=phase),
                                      0])
            z_dot.move_to(circle_point)
            z_label.move_to(circle_point + Z_LABEL_OFFSET*r_unit_vector)

            t_sim += dt_sim

            update_progress(t_sim/T_sim,label="Rendering")

        self.wait(0.5)

    # create clock
    def setup_clock(self):
        clock = Clock()
        clock.set_height(1)
        clock.to_corner(UR)
        clock.shift(MED_LARGE_BUFF * LEFT)

        time_lhs = TextMobject("Time: ")
        time_label = DecimalNumber(
            0, num_decimal_places=2,
        )
        time_rhs = TextMobject("s")
        time_group = VGroup(
            time_lhs,
            time_label,
            # time_rhs
        )
        time_group.arrange(RIGHT, aligned_edge=DOWN)
        time_rhs.shift(SMALL_BUFF * LEFT)
        time_group.next_to(clock, DOWN)

        self.time_group = time_group
        self.time_label = time_label
        self.clock = clock

    # sine and cosine
    def sin(self, t, ang_freq=1, ampl=1, phase=0):
        return ampl*np.sin(ang_freq*t+phase)
    def cos(self, t, ang_freq=1, ampl=1, phase=0):
        return ampl*np.cos(ang_freq*t+phase)
