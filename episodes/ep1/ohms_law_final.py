from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit
from accalib.hydraulic import HydraulicCircuit, PressureGauge
from accalib.rate_functions import accelerated
import progressbar
from accalib.tools import rule_of_thirds_guide
from functools import partial


class IntroOhmsLawPart(Scene):
    def construct(self):
        section_label = TextMobject(
            "Part 3: \\\\",
            "Ohm's Law"
        ).scale(1.5)
        self.play(
            Write(section_label[0])
        )
        self.wait()
        self.play(
            Write(section_label[1])
        )
        self.wait(0.57)


class OhmsLawIntro(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "indication_color": BLUE_D,
        "add_vector_fields": False,
        "pump_ang_freq": 0.5 * PI,
        "A": 3.125  # (r^4)(\\Delta P)/Q [m^4 kPa s / L] from Hagen–Poiseuille equation
    }
    def construct(self):
        # Write title
        title = Title(
            "Ohm's Law",
            scale_factor=1.5
        )
        self.play(
            Write(
                title,
                run_time=0.95
            )
        )

        # add equation
        equation = TexMobject(
            "V", "=", "I", "R",
            tex_to_color_map={
                "V": self.voltage_color,
                "I": self.current_color,
                "R": self.resistance_color
            }
        )\
            .scale(2.4)
        equation[1].shift(0.1*RIGHT)
        equation[2].shift(0.6*RIGHT)
        equation[3].shift(1.3*RIGHT)
        equation.center()
        equation.to_edge(UP, buff=1.75)
        self.play(Write(equation[0], run_time=0.35))
        self.play(Write(equation[1], run_time=0.35))
        self.play(Write(equation[2], run_time=0.35))
        self.play(Write(equation[3], run_time=0.35))
        self.wait(1.1)

        # label voltage
        v_rect = SurroundingRectangle(
            equation[0],
            color=self.voltage_color,
            buff=0.17
        )
        v_text = TextMobject(
            "Voltage",
            color=self.voltage_color
        )\
            .scale(1.45)\
            .next_to(v_rect, direction=DOWN, buff=0.2)\
            .align_to(v_rect, RIGHT)
        self.play(
            Write(v_rect),
            FadeInFrom(v_text, direction=DOWN)
        )
        self.wait(0.83)

        # label current
        i_rect = SurroundingRectangle(
            equation[2],
            color=self.current_color,
            buff=0.17
        )
        i_text = TextMobject(
            "Current",
            color=self.current_color
        ) \
            .scale(1.45) \
            .next_to(i_rect, direction=DOWN, buff=0.25) \
            .align_to(i_rect, RIGHT)
        self.play(
            Write(i_rect, run_time=0.9),
            FadeInFrom(i_text, direction=DOWN, run_time=0.9)
        )

        # label resistance
        r_rect = SurroundingRectangle(
            equation[3],
            color=self.resistance_color,
            buff=0.17
        )
        r_text = TextMobject(
            "Resistance",
            color=self.resistance_color
        ) \
            .scale(1.45) \
            .next_to(r_rect, direction=DOWN, buff=0.27) \
            .align_to(r_rect, LEFT)
        self.play(
            Write(r_rect),
            FadeInFrom(r_text, direction=DOWN)
        )
        self.wait(2.87)

        # add electric circuit
        self.electric_circuit = BatteryLampCircuit()\
            .scale(0.9)\
            .to_edge(DOWN)\
            .shift(1*UP+3*LEFT)
        self.electric_circuit.setup_electrons()
        cover_rect = SurroundingRectangle(
            self.electric_circuit,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )
        self.add(self.electric_circuit, cover_rect)
        self.play(
            FadeOut(cover_rect),
            self.electric_circuit.get_electron_anim(2)
        )

        # setup circuit labels
        point1 = self.electric_circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.electric_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label, i_value = self.get_label("I", 2, "A", color=self.current_color)
        i_label.next_to(current_arrow, direction=UR, buff=0) \
            .shift(0 * RIGHT)

        # write voltage of circuit
        v_label, self.v_value = self.get_label("V", 12, "V", color=self.voltage_color)
        v_label.next_to(self.electric_circuit.battery, direction=UL, buff=0) \
            .shift(0.25 * UP + 0.4 * RIGHT)

        # write resistance of circuit
        r_label, r_value = self.get_label("R", 6, "\\Omega", color=self.resistance_color)
        r_label.next_to(self.electric_circuit.light_bulb, direction=DOWN, buff=0.2) \
            .shift(0 * RIGHT)

        # add hydraulic circuit
        self.hydraulic_circuit = HydraulicCircuit(
            include_water_source=False,
            ang_freq=PI*0.2
        )\
            .scale(0.7)\
            .to_edge(RIGHT, buff=0.2)\
            .shift(3*DOWN+0.5*RIGHT)
        cover_rect_2 = SurroundingRectangle(
            self.hydraulic_circuit,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )
        self.add(self.hydraulic_circuit, cover_rect_2)
        if self.add_vector_fields:
            self.setup_vector_fields()
        self.play(
            FadeOut(cover_rect_2),
            self.hydraulic_circuit.get_rotate_anim(3.33),
            self.electric_circuit.get_electron_anim(3.33)
        )

        # indicate pump
        self.play(
            Indicate(
                self.hydraulic_circuit.body.circle,
                run_time=1
            ),
            self.hydraulic_circuit.get_rotate_anim(1.23),
            self.electric_circuit.get_electron_anim(1.23)
        )

        # indicate large tubes
        self.play(
            Indicate(
                VGroup(*self.hydraulic_circuit.body.large_tube),
                scale_factor=1.08,
                run_time=1
            ),
            self.hydraulic_circuit.get_rotate_anim(2),
            self.electric_circuit.get_electron_anim(2)
        )

        # indicate small tubes
        small_tube_cp = VGroup(*self.hydraulic_circuit.body.small_tube).copy()
        VGroup(*self.hydraulic_circuit.body.small_tube).set_color(YELLOW)
        self.play(
            WiggleOutThenIn(
                VGroup(*self.hydraulic_circuit.body.small_tube),
                scale_factor=1.7,
                n_wiggles=6,
                rotation_angle=0.06 * TAU,
                run_time=2
            ),
            Flash(
                small_tube_cp,
                flash_radius=2,
                line_length=0.8,
                run_time=2
            ),
            self.hydraulic_circuit.get_rotate_anim(2),
            self.electric_circuit.get_electron_anim(2)
        )
        VGroup(*self.hydraulic_circuit.body.small_tube).set_color(WHITE)
        self.play(
            self.hydraulic_circuit.get_rotate_anim(7.46),
            self.electric_circuit.get_electron_anim(7.46)
        )

        # indicate flow
        flow_line = Line(
            start=self.hydraulic_circuit.body.small_tube[0].get_center() + 0.4 * LEFT,
            end=self.hydraulic_circuit.body.small_tube[1].get_center() + 0.4 * RIGHT,
            stroke_width=10,
            color=self.current_color
        )
        flow_arrow = Arrow(
            stroke_width=7,
            color=self.current_color,
            start=0.7 * UP,
            end=ORIGIN,
            buff=0
        ) \
            .next_to(flow_line, direction=LEFT, buff=0.1)
        # flow_var_label = TexMobject(
        #     "Q", "=",
        #     color=self.current_color
        # ) \
        #     .scale(1.25) \
        #     .next_to(flow_arrow, direction=LEFT, buff=1.5)
        flow_label = DecimalNumber(
            2,
            color=self.current_color,
            num_decimal_places=1
        ) \
            .scale(1.25) \
            .next_to(flow_arrow, direction=LEFT, buff=0.7)
        flow_label.add_updater(
            lambda x:
            x.set_value(i_value.get_value() * 0.75)
        )
        flow_unit = TexMobject(
            "{L", "\\over", "s}",
            color=self.current_color
        ) \
            .scale(1.2) \
            .next_to(flow_label, direction=RIGHT, buff=0.2)
        flow_unit[0].shift(0.01 * DOWN)
        flow_unit[2].shift(0.09 * UP)

        # fade in "current ="
        self.play(
            AnimationGroup(
                FadeInFrom(current_arrow, direction=UP),
                FadeInFrom(i_label[0], direction=UP),
                lag_ratio=0.1
            ),
            self.electric_circuit.get_electron_anim(6.26),
            self.hydraulic_circuit.get_rotate_anim(6.26)
        )

        # fade in current arrow
        self.play(
            *[
                FadeIn(mob)
                for mob in (flow_line, flow_arrow)
            ],
            self.electric_circuit.get_electron_anim(1.99),
            self.hydraulic_circuit.get_rotate_anim(1.99)
        )

        # fade in 2A
        self.play(
            FadeInFrom(i_label[1], direction=UP),
            self.electric_circuit.get_electron_anim(3.26),
            self.hydraulic_circuit.get_rotate_anim(3.26)
        )

        # fade in 1.5 L/s
        self.play(
            *[
                FadeIn(mob)
                for mob in (flow_label, flow_unit)
            ],
            self.electric_circuit.get_electron_anim(4.48),
            self.hydraulic_circuit.get_rotate_anim(4.48)
        )

        # fade in voltage label
        self.play(
            FadeIn(v_label),
            self.electric_circuit.get_electron_anim(10.65),
            self.hydraulic_circuit.get_rotate_anim(10.65)
        )

        # indicate pump body
        self.play(
            ShowPassingFlashAround(
                VGroup(
                    self.hydraulic_circuit.body.circle,
                    self.hydraulic_circuit.fins
                ),
                time_width=1,
                run_time=2
            ),
            self.electric_circuit.get_electron_anim(3),
            self.hydraulic_circuit.get_rotate_anim(3)
        )

        in_kw={
            'stroke_opacity': 1,
            'stroke_color': YELLOW,
            'fill_opacity': 0.2,
            'fill_color': YELLOW
        }
        volt_rect = SurroundingRectangle(
            v_label[1], **in_kw
        )
        cur_rect = SurroundingRectangle(
            i_label[1], **in_kw
        )
        pump_rect = SurroundingRectangle(
            VGroup(
                self.hydraulic_circuit.body.circle,
                self.hydraulic_circuit.fins
            ),
            **in_kw
        )
        flow_rect = SurroundingRectangle(
            VGroup(flow_label,flow_unit), **in_kw
        )

        # # increase strength of pump
        # self.hydraulic_circuit.ang_freq = 2*PI
        if self.add_vector_fields:
            self.add(self.animated_stream_lines_2)
        self.play( # remove
            self.hydraulic_circuit.get_rotate_anim(3),
            self.electric_circuit.get_electron_anim(3)
        )
        self.play(
            ApplyMethod(
                self.v_value.set_value, 24,
                rate_func=slow_into,
                run_time=2
            ),
            ApplyMethod(
                i_value.set_value, 4,
                rate_func=slow_into,
                run_time=2
            ),
            AnimationGroup(
                FadeIn(volt_rect),
                FadeIn(pump_rect),
                lag_ratio=0
            ),
            self.hydraulic_circuit.get_rotate_anim(9.61),
            self.electric_circuit.get_electron_anim(9.61)
        )

        # transform rectangle from pump to flow rate
        self.play(
            Transform(pump_rect, flow_rect),
            self.hydraulic_circuit.get_rotate_anim(15.87),
            self.electric_circuit.get_electron_anim(15.87)
        )

        # transform rectangle from voltage label to current label
        self.play(
            Transform(volt_rect, cur_rect),
            self.hydraulic_circuit.get_rotate_anim(3),
            self.electric_circuit.get_electron_anim(3)
        )

        # fade out purple rectangles
        self.play(
            FadeOut(volt_rect),
            FadeOut(pump_rect),
            self.hydraulic_circuit.get_rotate_anim(1.08),
            self.electric_circuit.get_electron_anim(1.08)
        )

        # add resistance label
        self.play(
            FadeIn(r_label),
            self.hydraulic_circuit.get_rotate_anim(9.43),
            self.electric_circuit.get_electron_anim(9.43)
        )

        # show square around resistance label
        r_ind_rect = SurroundingRectangle(
            r_label,
            **in_kw
        )\
            .scale(1.2)\
            .shift(0.1*RIGHT)

        # transform to square around small tube
        r_ind_small_tube = Rectangle(
            width=1.25,
            height=2,
            **in_kw
        )\
            .move_to(VGroup(*self.hydraulic_circuit.body.small_tube).get_center())

        self.play(
            FadeIn(r_ind_rect),
            FadeIn(r_ind_small_tube),
            self.hydraulic_circuit.get_rotate_anim(4.65),
            self.electric_circuit.get_electron_anim(4.65)
        )

        # set small tube radius
        cur_radius = self.hydraulic_circuit.get_small_tube_radius()
        new_radius = 0.07
        del_radius = new_radius - cur_radius
        if self.add_vector_fields:
            self.remove(self.animated_stream_lines_2)
        self.play(
            ApplyMethod(
                self.hydraulic_circuit.body.small_tube[0].shift, del_radius * RIGHT,
                run_time=3
            ),
            ApplyMethod(
                self.hydraulic_circuit.body.small_tube[1].shift, del_radius * LEFT,
                run_time=3
            ),
            ApplyMethod(
                self.hydraulic_circuit.small_rect.set_width, 2 * new_radius - 0.07, True,
                run_time=3
            ),
            ApplyMethod(
                r_value.set_value, 12,
                run_time=3
            ),
            ApplyMethod(
                i_value.set_value, 2,
                run_time=3
            ),
            self.hydraulic_circuit.get_rotate_anim(10.91),
            self.electric_circuit.get_electron_anim(10.91)
        )

        # transform rectangle around small pipe to flow rate label rectangle
        self.play(
            Transform(
                r_ind_small_tube, flow_rect
            ),
            self.hydraulic_circuit.get_rotate_anim(13.65),
            self.electric_circuit.get_electron_anim(13.65)
        )

        # transform rectangle around resistance to current label rectangle
        self.play(
            Transform(
                r_ind_rect, cur_rect
            ),
            self.hydraulic_circuit.get_rotate_anim(2),
            self.electric_circuit.get_electron_anim(2)
        )

        # FadeOut rectangles around current and flow label
        self.play(
            FadeOut(r_ind_rect),
            FadeOut(r_ind_small_tube),
            self.hydraulic_circuit.get_rotate_anim(2),
            self.electric_circuit.get_electron_anim(2)
        )

        v_kw = {
            'stroke_opacity': 1,
            'stroke_color': self.voltage_color,
            'fill_opacity': 0.2,
            'fill_color': self.voltage_color
        }
        volt_rect = SurroundingRectangle(
            v_label, **v_kw
        )
        i_kw = {
            'stroke_opacity': 1,
            'stroke_color': self.current_color,
            'fill_opacity': 0.2,
            'fill_color': self.current_color
        }
        cur_rect = SurroundingRectangle(
            i_label, **i_kw
        )
        r_kw = {
            'stroke_opacity': 1,
            'stroke_color': self.resistance_color,
            'fill_opacity': 0.2,
            'fill_color': self.resistance_color
        }
        r_ind_rect = SurroundingRectangle(
            r_label,
            **r_kw
        ) \
            .scale(1.2) \
            .shift(0.1 * RIGHT)

        # FadeIn rectangle around voltage
        self.play(
            FadeIn(volt_rect, run_time=0.66),
            self.hydraulic_circuit.get_rotate_anim(0.66),
            self.electric_circuit.get_electron_anim(0.66)
        )

        # FadeIn rectangle around current
        self.play(
            FadeIn(cur_rect, run_time=0.91),
            self.hydraulic_circuit.get_rotate_anim(0.91),
            self.electric_circuit.get_electron_anim(0.91)
        )

        # FadeIn rectangle around resistance
        self.play(
            FadeIn(r_ind_rect),
            self.hydraulic_circuit.get_rotate_anim(12.48),
            self.electric_circuit.get_electron_anim(12.48)
        )

    def vector_field_st(self, p):
        # viscosity = 8.90E-4
        # R = abs(self.vf_x_max - self.vf_x_min) / 2.
        # r = p[0] - (self.vf_x_min + self.vf_x_max) / 2.
        # scale_factor = 0.6E-2
        # dPdx = self.voltage_to_pressure(self.v_value.get_value()) / (self.hydraulic_circuit.body.small_tube[0].get_height())

        # in small tube
        if self.vf_x_min+0 < p[0] < self.vf_x_max-0:
            if self.vf_y_min < p[1] < self.vf_y_max:
                # print(f"{p[0]} -> {scale_factor*(1/(4*viscosity))*dPdx*(R**2-r**2)*DOWN}")
                # print(f"r = {r}, R = {R}")
                # return scale_factor * (1 / (4 * viscosity)) * dPdx * (R ** 2 - r ** 2) * DOWN
                return 2 * DOWN

        return 0 * UP

    def vector_field(self, p):
        large_tube = self.hydraulic_circuit.body.large_tube
        small_tube = self.hydraulic_circuit.body.small_tube
        PUM_circle = self.hydraulic_circuit.pump_circle

        # return 1 for any non-zero pressure
        mag = int(bool(self.voltage_to_pressure(self.v_value.get_value())))

        # in pump
        if np.linalg.norm(p - self.hydraulic_circuit.body.circle.get_center()) < \
                (self.hydraulic_circuit.body.circle.get_width() / 2) * 0.8:
            return -self.pump_ang_freq * mag * self.rot_matrix.dot(p - self.hydraulic_circuit.body.circle.get_center())

        # region 1
        if large_tube[1].get_left()[0] < p[0] < \
                large_tube[0].get_left()[0]:
            if large_tube[1].get_bottom()[1] < p[1] < \
                    large_tube[0].get_top()[1] + 0.1:
                r = abs(p[0] - (large_tube[1].get_left()[0] + large_tube[0].get_left()[0]) / 2.)
                R = abs(large_tube[1].get_left()[0] - large_tube[0].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 2
        if large_tube[0].get_left()[0] < p[0] < \
                large_tube[0].get_right()[0] - 0.3:
            if large_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r = abs(p[1] - (large_tube[0].get_top()[1] + large_tube[1].get_top()[1]) / 2.)
                R = abs(large_tube[0].get_top()[1] - large_tube[1].get_top()[1]) / 2.
                return mag * RIGHT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 3
        if large_tube[0].get_right()[0] - 0.27 < p[0] < \
                large_tube[1].get_right()[0]:
            if small_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r = abs(p[0] - (large_tube[0].get_right()[0] - 0.27 + large_tube[1].get_right()[0]) / 2.)
                R = abs(large_tube[0].get_right()[0] - 0.27 - large_tube[1].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 4
        if large_tube[2].get_right()[0] - 0.3 < p[0] < \
                large_tube[3].get_right()[0]:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[3].get_top()[1]:
                r = abs(p[0] - (large_tube[2].get_right()[0] - 0.3 + large_tube[3].get_right()[0]) / 2.)
                R = abs(large_tube[2].get_right()[0] - 0.3 - large_tube[3].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 5
        if large_tube[2].get_left()[0] < p[0] < \
                large_tube[2].get_right()[0] - 0.3:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[2].get_bottom()[1]:
                r = abs(p[1] - (large_tube[3].get_bottom()[1] + large_tube[2].get_bottom()[1]) / 2.)
                R = abs(large_tube[3].get_bottom()[1] - large_tube[2].get_bottom()[1]) / 2.
                return mag * LEFT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 6
        if large_tube[3].get_left()[0] < p[0] < \
                large_tube[2].get_left()[0]:
            if large_tube[2].get_bottom()[1] < p[1] < \
                    large_tube[2].get_top()[1]:
                r = abs(p[0] - (large_tube[3].get_left()[0] + large_tube[2].get_left()[0]) / 2.)
                R = abs(large_tube[3].get_left()[0] - large_tube[2].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        return 0 * RIGHT

    def setup_vector_fields(self):
        self.vf_x_min = self.hydraulic_circuit.body.small_tube[1].get_center()[0] - 0.01
        self.vf_x_max = self.hydraulic_circuit.body.small_tube[0].get_center()[0] + 0.01
        self.vf_y_min = self.hydraulic_circuit.body.small_tube[1].get_bottom()[1]
        self.vf_y_max = self.hydraulic_circuit.body.small_tube[1].get_top()[1] + 0.2

        # add_hguide(self, large_tube[3].get_left()[0], color=GREEN)
        # add_hguide(self, large_tube[2].get_left()[0], color=RED)
        # add_vguide(self, large_tube[2].get_bottom()[1], color=GREEN)
        # add_vguide(self, large_tube[2].get_top()[1], color=RED)

        self.rot_matrix = np.array([[0, -1, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])

        # setup vector field in small tube
        self.stream_lines_yellow_st = StreamLines(
            self.vector_field_st,
            delta_x=0.015,
            delta_y=0.1,
            # bad: 0.1, 0.5
            # good: 0.3, 0.4
            colors=["#FFFF00"],
            x_min=self.vf_x_min,
            x_max=self.vf_x_max,
            y_min=self.vf_y_max - 0.2,
            y_max=self.vf_y_max,
            dt=0.16
            # min_magnitude=4
        )
        self.stream_lines_st = StreamLines(
            self.vector_field_st,
            delta_x=0.015,
            delta_y=0.1,
            # bad: 0.1, 0.5
            # good: 0.3, 0.4
            colors=[WHITE],
            x_min=self.vf_x_min,
            x_max=self.vf_x_max,
            y_min=self.vf_y_max - 0.2,
            y_max=self.vf_y_max,
            dt=0.16
            # min_magnitude=4
        )
        self.animated_stream_lines_st = AnimatedStreamLines(
            self.stream_lines_st,
            line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )
        self.add(self.animated_stream_lines_st)

        # setup vector field for pump
        stream_lines = StreamLines(
            self.vector_field,
            delta_x=0.2,
            delta_y=0.2,
            # dt=0.1,
            # virtual_time=1.8,
            colors=[WHITE],
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3
            # min_magnitude=4
        )

        class MyAnim(ShowPassingFlashWithThinningStrokeWidth):
            def __init__(self, vmobject, **kwargs):
                super().__init__(vmobject, **kwargs, remover=False)

        self.animated_stream_lines = AnimatedStreamLines(
            stream_lines,
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3,
            line_anim_class=MyAnim,
            # line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )
        self.add(self.animated_stream_lines)

        stream_lines_2 = StreamLines(
            self.vector_field,
            delta_x=0.1,
            delta_y=0.1,
            # dt=0.1,
            # virtual_time=1.8,
            colors=[WHITE],
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3
            # min_magnitude=4
        )
        self.animated_stream_lines_2 = AnimatedStreamLines(
            stream_lines_2,
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3,
            line_anim_class=MyAnim,
            line_anim_config={
                "run_time": 2,
                "rate_func": linear,
                "time_width": 0.3,
            },
            # line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )

    def voltage_to_pressure(self, voltage):
        return 100 + 40 * voltage

    def get_label(self, text, initial_value, unit, **kwargs):
        lhs = TextMobject(text, "=", **kwargs)\
            .scale(1.25)
        decimal_num = DecimalNumber(
            initial_value,
            num_decimal_places=1,
            unit=unit,
            **kwargs
        ) \
            .scale(1.25)\
            .next_to(lhs, direction=RIGHT)
        value = ValueTracker(initial_value)
        decimal_num.add_updater(
            lambda x: x.set_value(value.get_value())
        )
        return VGroup(lhs, decimal_num), value


class CurrentCalculation(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
    }
    def construct(self):
        # add circuit
        circuit = BatteryLampCircuit(num_of_electrons=20) \
            .scale(0.95)\
            .shift(2.25*LEFT)
        circuit.setup_electrons()
        self.add(circuit)
        self.play(
            circuit.get_electron_anim(2.17)
        )

        # add current question
        point1 = circuit.electron_vect_inter.interpolate(0.55)
        point2 = circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label, i_value = self.get_label("I=", 2, "A", color=self.current_color)
        i_label.next_to(current_arrow, direction=UR, buff=0) \
            .shift(0 * RIGHT)
        question_marks = TextMobject("???", color=self.current_color) \
            .scale(1.7) \
            .move_to(i_label[1].get_center())
        self.play(
            AnimationGroup(
                FadeIn(current_arrow),
                FadeIn(i_label[0]),
                Write(question_marks),
                lag_ratio=0.9
            ),
            circuit.get_electron_anim(3.65)
        )

        # write voltage of circuit
        v_label, v_value = self.get_label("V=", 12, "V", color=self.voltage_color)
        v_label.next_to(circuit.battery, direction=UL, buff=0)
        v_label.shift(0.25 * UP + 0.4 * RIGHT)
        self.play(
            FadeIn(v_label),
            circuit.get_electron_anim(2.9)
        )

        # write resistance of circuit
        r_label, r_value = self.get_label("R=", 6, "\\Omega", color=self.resistance_color)
        r_label.next_to(circuit.light_bulb, direction=DOWN, buff=0.2)
        r_label.shift(0 * RIGHT)
        self.play(
            FadeIn(r_label),
            circuit.get_electron_anim(4.17)
        )

        color_map = {
            "V": self.voltage_color,
            "I": self.current_color,
            "R": self.resistance_color
        }
        equation = TexMobject(
            "V", "=", "I", "R",
            tex_to_color_map=color_map
        ) \
            .scale(2) \
            .to_corner(UR) \
            .shift(1.5*LEFT + 2*DOWN)
        equation_orig = TexMobject(
            "V", "=", "I", "R",
            tex_to_color_map=color_map
        ) \
            .scale(2) \
            .next_to(equation, direction=DOWN, buff=2.75)
        equation[3].shift(0.25*RIGHT)
        self.play(
            Write(equation),
            circuit.get_electron_anim(5.46)
        )

        rects = VGroup(*[
            SurroundingRectangle(mob)
            for mob in (equation[2], equation[0], equation[3])
        ])
        rects[0].set_color(PURPLE_C)
        self.play(
            Write(rects[0]),
            circuit.get_electron_anim(1.63)
        )
        self.play(
            Write(rects[1]),
            circuit.get_electron_anim(1.26)
        )
        self.play(
            Write(rects[2]),
            circuit.get_electron_anim(2)
        )
        self.play(
            *[
                FadeOut(rect)
                for rect in rects
            ],
            circuit.get_electron_anim(1.63)
        )

        # divide both sides by R
        equation_divided_lhs = TexMobject(
            "{", "V", "\\over", "R", "}",
            tex_to_color_map=color_map
        )\
            .scale(2)\
            .move_to(equation[0].get_center())
        equation_divided_rhs = TexMobject(
            "{", "I", "R", "\\over", "R", "}",
            tex_to_color_map=color_map
        )\
            .scale(2)\
            .move_to(VGroup(*equation[2:]).get_center())
        self.play(
            ReplacementTransform(
                equation[0], equation_divided_lhs
            ),
            ReplacementTransform(
                VGroup(*equation[2:]), equation_divided_rhs
            ),
            circuit.get_electron_anim(1.14)
        )

        # cancel R on RHS
        cancel_out = Line(
            start=equation_divided_rhs[4].get_corner(DL)+0.25*DOWN+0.05*LEFT,
            end=equation_divided_rhs[2].get_corner(UR)+0.25*UP+0.05*RIGHT,
            color="#FF0000",
            stroke_width=8
        )
        self.play(
            Write(cancel_out),
            circuit.get_electron_anim(3.57)
        )

        # replace RHS with I
        I_tex = TexMobject(
            "I",
            tex_to_color_map=color_map
        )\
            .scale(2) \
            .move_to(equation_divided_rhs.get_center())
        self.play(
            ReplacementTransform(
                VGroup(equation_divided_rhs, cancel_out), I_tex
            ),
            circuit.get_electron_anim(2)
        )

        # swap RHS and LHS
        self.play(
            Swap(
                I_tex, equation_divided_lhs
            ),
            circuit.get_electron_anim(4)
        )

        # draw rectangles again
        rects = VGroup(*[
            SurroundingRectangle(mob)
            for mob in (I_tex, equation_divided_lhs[1], equation_divided_lhs[3])
        ])
        rects[0].set_color(PURPLE_C)
        self.play(
            Write(rects[0]),
            circuit.get_electron_anim(1.46)
        )
        self.play(
            Write(rects[1]),
            circuit.get_electron_anim(1)
        )
        self.play(
            Write(rects[2]),
            circuit.get_electron_anim(1.27)
        )
        self.play(
            *[
                FadeOut(rect)
                for rect in rects
            ],
            circuit.get_electron_anim(1)
        )

        # copy voltage and resistance
        v_copy = v_label[1].copy().clear_updaters()
        r_copy = r_label[1].copy().clear_updaters()
        v_plug = TexMobject(
            "12", color=self.voltage_color
        )\
            .scale(2) \
            .move_to(equation_divided_lhs[1].get_center())
        r_plug = TexMobject(
            "6", color=self.resistance_color
        )\
            .scale(2) \
            .move_to(equation_divided_lhs[3].get_center())
        self.play(
            ReplacementTransform(v_copy, v_plug),
            FadeOut(equation_divided_lhs[1]),
            circuit.get_electron_anim(1.6)
        )
        self.play(
            ReplacementTransform(r_copy, r_plug),
            FadeOut(equation_divided_lhs[3]),
            circuit.get_electron_anim(2.33)
        )

        # solve RHS
        current_final = DecimalNumber(
            2,
            num_decimal_places=0,
            unit="A",
            color=self.current_color
        ) \
            .scale(1.6)\
            .move_to(equation_divided_lhs.get_center())
        self.play(
            Transform(
                VGroup(v_plug, r_plug, equation_divided_lhs[2]), current_final
            ),
            circuit.get_electron_anim(3.73)
        )

        # move solution into circuit
        self.play(
            TransformFromCopy(
                current_final, i_label[1]
            ),
            FadeOut(question_marks),
            circuit.get_electron_anim(7.9)
        )

    def get_label(self, text, initial_value, unit, **kwargs):
        lhs = TextMobject(text, **kwargs)\
            .scale(1.6)
        decimal_num = DecimalNumber(
            initial_value,
            num_decimal_places=0,
            unit=unit,
            **kwargs
        ) \
            .scale(1.6)\
            .next_to(lhs, direction=RIGHT)
        value = ValueTracker(initial_value)
        decimal_num.add_updater(
            lambda x: x.set_value(value.get_value())
        )
        return VGroup(lhs, decimal_num), value


class CircuitsTable(CurrentCalculation):
    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=PURPLE
            )
        )

        # add circuits table
        circuits_table = ImageMobject(
            "images/ep1/CircuitsTable/circuits_table.PNG"
        )\
            .set_width(FRAME_WIDTH)\
            .move_to(FRAME_HEIGHT*0.25*UP)
        self.add(circuits_table)

        rect_kw = {
            'stroke_opacity': 0,
            'fill_opacity': 1,
            'fill_color': BLACK
        }
        rect_1 = SurroundingRectangle(
            circuits_table, **rect_kw
        )
        rect_2 = SurroundingRectangle(
            circuits_table, **rect_kw
        )\
            .shift(1.5*DOWN)
        rect_3 = SurroundingRectangle(
            circuits_table, **rect_kw
        ) \
            .shift(2.3 * DOWN)
        self.add(rect_1, rect_2, rect_3)

        self.play(FadeOut(rect_1))
        self.play(FadeOut(rect_2))
        self.play(FadeOut(rect_3))

        # add ohms law
        ohms_law_label = TextMobject(
            "Ohm's Law: "
        )\
            .scale(2.4)
        equation = TexMobject(
            "V", "=", "I", "R",
            tex_to_color_map={
                "V": self.voltage_color,
                "I": self.current_color,
                "R": self.resistance_color
            }
        ) \
            .scale(2.4)
        equation[1].shift(0.1 * RIGHT)
        equation[2].shift(0.6 * RIGHT)
        equation[3].shift(1.3 * RIGHT)
        equation\
            .center()\
            .to_edge(DOWN, buff=4)
        # VGroup(ohms_law_label, equation)\
        #     .arrange(RIGHT, aligned_edge=DOWN, buff=1)\
        #     .center()\
        #     .to_edge(DOWN, buff=1.75)\
        #     .shift(2*LEFT)
        self.play(
            FadeIn(equation)
        )

        # label voltage
        v_rect = SurroundingRectangle(
            equation[0],
            color=self.voltage_color,
            buff=0.17
        )
        v_text = TextMobject(
            "Voltage",
            color=self.voltage_color
        ) \
            .scale(1.45) \
            .next_to(v_rect, direction=DOWN, buff=0.2) \
            .align_to(v_rect, RIGHT)

        # label current
        i_rect = SurroundingRectangle(
            equation[2],
            color=self.current_color,
            buff=0.17
        )
        i_text = TextMobject(
            "Current",
            color=self.current_color
        ) \
            .scale(1.45) \
            .next_to(i_rect, direction=DOWN, buff=0.25) \
            .align_to(i_rect, RIGHT)

        # label resistance
        r_rect = SurroundingRectangle(
            equation[3],
            color=self.resistance_color,
            buff=0.17
        )
        r_text = TextMobject(
            "Resistance",
            color=self.resistance_color
        ) \
            .scale(1.45) \
            .next_to(r_rect, direction=DOWN, buff=0.27) \
            .align_to(r_rect, LEFT)

        self.play(
            Write(r_rect),
            FadeInFrom(r_text, direction=DOWN),
            Write(i_rect),
            FadeInFrom(i_text, direction=DOWN),
            Write(v_rect),
            FadeInFrom(v_text, direction=DOWN)
        )

        self.wait(10)