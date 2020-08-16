from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit
from accalib.hydraulic import HydraulicCircuit, PressureGauge
from accalib.rate_functions import accelerated
import progressbar

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
        "indication_color": BLUE_D
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
                run_time=1
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
        self.play(Write(equation[0]))
        self.play(Write(equation[1], run_time=0.9))
        self.play(Write(equation[2], run_time=0.73))
        self.play(Write(equation[3]))
        self.wait(7.86)

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
        self.wait(2)

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
            Write(i_rect),
            FadeInFrom(i_text, direction=DOWN)
        )
        self.wait(0.17)

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
        self.wait(5.69)

        # add circuit
        self.circuit = BatteryLampCircuit()\
            .scale(0.9)\
            .to_edge(DOWN)\
            .shift(1*UP+2.2*LEFT)
        self.circuit.setup_electrons()
        cover_rect = SurroundingRectangle(
            self.circuit,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )
        self.add(self.circuit, cover_rect)
        self.play(
            FadeOut(cover_rect),
            self.circuit.get_electron_anim()
        )
        self.play(
            self.circuit.get_electron_anim(4.1)
        )

        # write voltage of circuit
        v_label, v_value = self.get_label("V=", 12, "V", color=self.voltage_color)
        v_label.next_to(self.circuit.battery, direction=UL, buff=0)
        v_label.shift(0.25*UP+0.4*RIGHT)
        self.play(
            FadeIn(v_label),
            self.circuit.get_electron_anim(1.93)
        )

        # write current of circuit
        point1 = self.circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label, i_value = self.get_label("I=", 2, "A", color=self.current_color)
        i_label.next_to(current_arrow, direction=UR, buff=0)\
            .shift(0*RIGHT)
        self.play(
            FadeIn(current_arrow),
            self.circuit.get_electron_anim(2.37)
        )
        self.play(
            FadeIn(i_label),
            self.circuit.get_electron_anim(3.67)
        )

        # write resistance of circuit
        r_label, r_value = self.get_label("R=", 6, "\\Omega", color=self.resistance_color)
        r_label.next_to(self.circuit.light_bulb, direction=DOWN, buff=0.2)
        r_label.shift(0.25*RIGHT)
        self.play(
            FadeIn(r_label),
            self.circuit.get_electron_anim(2.56)
        )

        # setup plugged in equation
        V_plug = DecimalNumber(
            12,
            num_decimal_places=1,
            color=self.voltage_color
        )
        eq_tex = TexMobject("=")
        I_plug = DecimalNumber(
            2,
            num_decimal_places=1,
            color=self.current_color
        )
        times_tex = TexMobject("\\times").scale(0.75)
        R_plug = DecimalNumber(
            6,
            num_decimal_places=1,
            color=self.resistance_color
        )
        eq_plug = VGroup(
            V_plug, eq_tex, I_plug, times_tex, R_plug
        )\
            .scale(1.75)\
            .arrange(RIGHT, buff=0.4)
        times_tex.shift(0.2*RIGHT)
        R_plug.shift(0.2*RIGHT)
        eq_plug.next_to(self.circuit.light_bulb, direction=UR)
        eq_plug.shift(0.7*RIGHT+0.1*UP)

        # transform into ohms law with values
        v_copy = v_label[1].copy().clear_updaters()
        i_copy = i_label[1].copy().clear_updaters()
        r_copy = r_label[1].copy().clear_updaters()
        null_dot = Dot().move_to(100*UR)
        plug_rect = SurroundingRectangle(
            eq_plug,
            color=PURPLE_B,
            buff=0.4
        )
        self.play(
            AnimationGroup(
                ReplacementTransform(v_copy, V_plug),
                FadeIn(eq_plug[1]),
                FadeIn(null_dot, run_time=0.8),
                ReplacementTransform(i_copy, I_plug),
                FadeIn(eq_plug[3]),
                ReplacementTransform(r_copy, R_plug),
                Write(plug_rect),
                lag_ratio=1
            ),
            self.circuit.get_electron_anim(14.34)
        )

        # add updaters
        V_plug.add_updater(lambda x: x.set_value(v_value.get_value()))
        I_plug.add_updater(lambda x: x.set_value(i_value.get_value()))
        R_plug.add_updater(lambda x: x.set_value(r_value.get_value()))

        v_label_rect = SurroundingRectangle(v_label[1], buff=0.13, color=self.indication_color)
        i_label_rect = SurroundingRectangle(i_label[1], buff=0.13, color=self.indication_color)
        r_label_rect = SurroundingRectangle(r_label[1], buff=0.13, color=self.indication_color)

        ri_arrow = CurvedArrow(
            start_point=r_label_rect.get_corner(UR)+0.25*UL,
            end_point=i_label_rect.get_corner(DR)+0.1*DOWN,
            color=self.indication_color,
            angle=PI*0.3
        )

        vi_arrow = CurvedArrow(
            start_point=v_label_rect.get_corner(UR)+0.1*UR,
            end_point=i_label_rect.get_corner(UL)+0.05*UP+0.2*LEFT,
            color=self.indication_color,
            angle=-PI*0.3
        )

        # half the resistance
        self.play(
            ApplyMethod(
                i_value.set_value, 4,
                rate_func=linear,
                run_time=3
            ),
            ApplyMethod(
                r_value.set_value, 3,
                rate_func=linear,
                run_time=3
            ),
            Write(
                r_label_rect,
                run_time=1
            ),
            self.circuit.get_electron_acceleration_anim(0.22, run_time=3)
        )
        self.play(
            self.circuit.get_electron_anim()
        )
        self.play(
            AnimationGroup(
                ShowCreation(
                    ri_arrow,
                    run_time=1
                ),
                Write(
                    i_label_rect,
                    run_time=1
                ),
                lag_ratio=1
            ),
            self.circuit.get_electron_anim(2)
        )
        self.play(
            *[
                FadeOut(mob)
                for mob in (r_label_rect, ri_arrow, i_label_rect)
            ],
            self.circuit.get_electron_anim(10.73)
        )

        # double the voltage
        self.play(
            ApplyMethod(
                v_value.set_value, 24,
                rate_func=linear,
                run_time=3
            ),
            ApplyMethod(
                i_value.set_value, 8,
                rate_func=linear,
                run_time=3
            ),
            AnimationGroup(
                Write(
                    v_label_rect,
                    run_time=1
                ),
                FadeIn(null_dot, run_time=0.23),
                ShowCreation(
                    vi_arrow,
                    run_time=1
                ),
                FadeIn(null_dot, run_time=0.77),

                lag_ratio=1
            ),
            self.circuit.get_electron_acceleration_anim(
                0.44,
                run_time=3
            ),
        )
        self.play(
            AnimationGroup(
                FadeIn(null_dot, run_time=0.06),
                Write(
                    i_label_rect,
                    run_time=1
                ),
                lag_ratio=1
            ),
            self.circuit.get_electron_anim(
                run_time=1.06
            )
        )
        self.play(
            self.circuit.get_electron_anim(
                run_time=3.97
            )
        )
        self.play(
            *[
                FadeOut(mob)
                for mob in (v_label_rect, vi_arrow, i_label_rect)
            ],
            self.circuit.get_electron_anim(3.1)
        )

        # setup question
        question = TextMobject(
            "How do we predict current given a circuit?",
            color=YELLOW
        ) \
            .scale(1.5) \
            .to_edge(DOWN, buff=0.5)
        q_rect = SurroundingRectangle(
            question
        ) \
            .set_fill(color=BLACK, opacity=1) \
            .set_stroke(color=BLUE, opacity=0)

        r = lambda: (2*random.random()-1)
        v_r_values = [
            (24 + r()*23, 3 + 2.5*r())
            for _ in range(10)
        ]
        for i, vr_pair in enumerate(v_r_values):
            v = vr_pair[0]
            r = vr_pair[1]
            self.play(
                ApplyMethod(
                    v_value.set_value, v,
                    rate_func=linear
                ),
                ApplyMethod(
                    r_value.set_value, r,
                    rate_func=linear
                ),
                ApplyMethod(
                    i_value.set_value, v/r,
                    rate_func=linear
                ),
                self.circuit.get_electron_acceleration_anim(0.055*(v/r), run_time=2)
            )
            if i == 3:
                self.play(
                    self.circuit.get_electron_anim(1),
                    FadeIn(q_rect),
                    Write(question, run_time=1),
                )
            else:
                self.play(
                    self.circuit.get_electron_anim(0.5),
                )
        self.wait()

    def get_label(self, text, initial_value, unit, **kwargs):
        lhs = TextMobject(text, **kwargs)\
            .scale(1.7)
        decimal_num = DecimalNumber(
            initial_value,
            num_decimal_places=1,
            unit=unit,
            **kwargs
        ) \
            .scale(1.7)\
            .next_to(lhs, direction=RIGHT)
        value = ValueTracker(initial_value)
        decimal_num.add_updater(
            lambda x: x.set_value(value.get_value())
        )
        return VGroup(lhs, decimal_num), value


class CurrentQuestionSetup(Scene):
    def construct(self):
        question = TextMobject(
            "How do we predict the current that will pass through a circuit?",
            # color=YELLOW
        )\
            .scale(1.22) \
            .shift(2 * UP)
        answer = TextMobject(
            "Ohm's Law"
        ) \
            .scale(1.22) \
            .shift(2 * DOWN)
        arrow = Arrow(
            start=question.get_bottom(),
            end=answer.get_top(),
            stroke_width=10
        )
        self.play(
            Write(question)
        )
        self.wait(0.04)

        self.play(
            ShowCreation(arrow)
        )

        self.play(
            Write(answer)
        )
        self.wait(1.43)


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
            circuit.get_electron_anim(5.17)
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
            circuit.get_electron_anim(6.56)
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
            circuit.get_electron_anim(3.57)
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
            circuit.get_electron_anim(5.2)
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
            circuit.get_electron_anim(5)
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


class HydraulicAnalogy(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "pump_ang_freq": np.pi,
        "add_vector_fields": True,
        "A": 5e-4  # (r^4)(\\Delta P)/Q , from Hagen–Poiseuille equation
    }

    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=YELLOW
            )
        )

        # setup electric circuit
        electric_circuit = BatteryLampCircuit() \
            .scale(0.95) \
            .shift(2.25 * LEFT)
        electric_circuit.setup_electrons()

        # add current question
        point1 = electric_circuit.electron_vect_inter.interpolate(0.55)
        point2 = electric_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label, i_value = self.get_label("I=", 0, "A", color=self.current_color)
        i_label.next_to(current_arrow, direction=UR, buff=0) \
            .shift(0 * RIGHT)

        # write voltage of circuit
        v_label, self.v_value = self.get_label("V=", 0, "V", color=self.voltage_color)
        v_label.next_to(electric_circuit.battery, direction=UL, buff=0)\
            .shift(0.25 * UP + 0.4 * RIGHT)

        # write resistance of circuit
        r_label, r_value = self.get_label("R=", 6, "\\Omega", color=self.resistance_color)
        r_label.next_to(electric_circuit.light_bulb, direction=DOWN, buff=0.2)\
            .shift(0 * RIGHT)

        # setup hydraulic circuit
        self.hydraulic_circuit = HydraulicCircuit(initial_pressure=0)\
            .scale(0.8)\
            .to_edge(LEFT)\
            .shift(0.5*DOWN)
        self.hydraulic_circuit.add_updater(
            lambda x:
            x.top_pressure.set_value(self.voltage_to_pressure(self.v_value.get_value()))
        )
        self.add(self.hydraulic_circuit)

        # indicate pump
        self.play(
            Indicate(
                VGroup(
                    self.hydraulic_circuit.body.circle,
                    self.hydraulic_circuit.fins
                )
            )
        )

        # indicate large tubes
        self.play(
            Indicate(
                VGroup(*self.hydraulic_circuit.body.large_tube),
                scale_factor=1.08
            )
        )

        # indicate small tubes
        self.play(
            Indicate(
                VGroup(*self.hydraulic_circuit.body.small_tube),
            )
        )

        # fade in pressure gauges
        bot_gauge = PressureGauge(initial_pressure=0, text_color=self.voltage_color)\
            .scale(0.6)\
            .next_to(self.hydraulic_circuit.rects_bot[1], direction=UP, buff=0)
        top_gauge = PressureGauge(initial_pressure=0, text_color=self.voltage_color) \
            .scale(0.6) \
            .next_to(self.hydraulic_circuit.rects_top[1], direction=UP, buff=0)\
            .shift(0.5*RIGHT)
        top_gauge.add_updater(
            lambda x:
            x.pressure.set_value(self.voltage_to_pressure(self.v_value.get_value()))
        )
        self.play(
            FadeIn(bot_gauge),
            FadeIn(top_gauge)
        )

        # indicate water source
        self.play(
            Indicate(
                VGroup(
                    self.hydraulic_circuit.body.water_source_text,
                    VGroup(*self.hydraulic_circuit.body.box),
                    VGroup(*self.hydraulic_circuit.body.tube)
                )
            )
        )

        self.play(
            self.get_rot_anim(1),
            ApplyMethod(
                self.v_value.set_value, 5,
                rate_func=rush_into
            )
        )
        if self.add_vector_fields:
            self.setup_vector_fields()

        self.play(
            self.get_rot_anim()
        )

        # setup hydraulic circuit labels
        radius_label, radius_value = self.get_label("r = ", 0.1, "m", color=self.resistance_color)
        radius_label.next_to(self.hydraulic_circuit.rects_bot[2], direction=RIGHT) \
            .shift(0.5 * UP)

        del_p_label, del_p_value = self.get_label("$\\Delta P = $", 10, "Pa", color=self.voltage_color)
        del_p_label\
            .next_to(self.hydraulic_circuit, direction=UR)\
            .shift(1*LEFT+0*UP)

        flow_line = Line(
            start=self.hydraulic_circuit.body.small_tube[0].get_center()+0.4*LEFT,
            end=self.hydraulic_circuit.body.small_tube[1].get_center()+0.4*RIGHT,
            stroke_width=10,
            color=self.current_color
        )
        flow_arrow = Arrow(
            stroke_width=7,
            color=self.current_color,
            start=0.7*UP,
            end=ORIGIN,
            buff=0
        )\
            .next_to(flow_line, direction=RIGHT, buff=0.1)
        flow_var_label = TexMobject(
            "Q =",
            color=self.current_color
        )\
            .scale(1.25)\
            .next_to(flow_arrow, direction=RIGHT, buff=0.2)
        flow_label = DecimalNumber(
            2,
            color=self.current_color,
            num_decimal_places=1
        )\
            .scale(1.25)\
            .next_to(flow_var_label, direction=RIGHT, buff=0.2)
        flow_label.add_updater(
            lambda x:
            x.set_value(((radius_value.get_value()**4) * self.voltage_to_pressure(self.v_value.get_value()))/self.A)
        )
        flow_unit = TexMobject(
            "{L", "\\over", "s}",
            color=self.current_color
        )\
            .scale(1.2)\
            .next_to(flow_label, direction=RIGHT, buff=0.25)
        flow_unit[0].shift(0.01*DOWN)
        flow_unit[2].shift(0.09*UP)
        self.play(
            *[
                FadeIn(mob)
                for mob in (flow_line, flow_arrow, flow_label, flow_unit, flow_var_label)
            ],
            self.get_rot_anim(2)
        )
        self.play(
            FadeIn(del_p_label),
            self.get_rot_anim(2)
        )

        self.play(
            FadeIn(radius_label),
            self.get_rot_anim()
        )

        self.play(
            self.get_rot_anim(3)
        )

        hagen_poiseuille_title = TextMobject(
            "\\underline{Hagen–Poiseuille Equation}"
        )\
            .scale(1.15)\
            .to_corner(DR, buff=0)\
            .shift(3*UP+0.5*LEFT)
        hagen_poiseuille_equation = TexMobject(
            "\\Delta P", "=",
            "{8", "\\mu", "L", "Q", "\\over", "\\pi", "r^4}",
            tex_to_color_map={
                "Q": self.current_color,
                "r^": self.resistance_color,
                "\\Delta P": self.voltage_color
            }
        )\
            .scale(1.4)\
            .next_to(hagen_poiseuille_title, direction=DOWN, buff=0.3)
        self.play(
            AnimationGroup(
                Write(hagen_poiseuille_title),
                FadeInFrom(hagen_poiseuille_equation, direction=DOWN)
            ),
            self.get_rot_anim(5)
        )

        # double pressure
        self.play(
            ApplyMethod(
                self.v_value.set_value, 10
            ),
            ApplyMethod(
                del_p_value.set_value, 20
            ),
            self.get_rot_anim(5, ang_freq=1.5*np.pi)
        )

    def get_rot_anim(self, run_time=1, ang_freq=np.pi):
        return Rotating(
            self.hydraulic_circuit.fins,
            radians=-run_time * ang_freq,
            run_time=run_time
        )

    def voltage_to_pressure(self, voltage):
        return 2 * voltage

    def get_label(self, text, initial_value, unit, **kwargs):
        lhs = TextMobject(text, **kwargs)\
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

    def vector_field_st(self, p):
        viscosity = 8.90E-4
        R = abs(self.vf_x_max - self.vf_x_min) / 2.
        r = p[0] - (self.vf_x_min + self.vf_x_max) / 2.
        scale_factor = 0.6E-1
        dPdx = self.voltage_to_pressure(self.v_value.get_value()) / (self.hydraulic_circuit.body.small_tube[0].get_height())

        # in small tube
        if self.vf_x_min < p[0] < self.vf_x_max:
            if self.vf_y_min < p[1] < self.vf_y_max:
                # print(f"{p[0]} -> {scale_factor*(1/(4*viscosity))*dPdx*(R**2-r**2)*DOWN}")
                # print(f"r = {r}, R = {R}")
                return scale_factor * (1 / (4 * viscosity)) * dPdx * (R ** 2 - r ** 2) * DOWN

        return 0 * UP

    def vector_field(self, p):
        large_tube = self.hydraulic_circuit.body.large_tube
        small_tube = self.hydraulic_circuit.body.small_tube
        PUM_circle = self.hydraulic_circuit.pump_circle
        mag = self.voltage_to_pressure(self.v_value.get_value())/10

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
        self.stream_lines_yellow = StreamLines(
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
            delta_x=0.4,
            delta_y=0.6,
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
