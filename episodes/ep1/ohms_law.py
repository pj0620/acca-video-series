from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit
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
        self.wait()


class OhmsLawIntro(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
    }
    def construct(self):
        # Write title
        title = Title(
            "Ohm's Law",
            scale_factor=1.5
        )
        self.play(Write(title))
        self.wait()

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
        self.play(Write(equation[1]))
        self.play(Write(equation[2]))
        self.play(Write(equation[3]))
        self.wait(4.33)

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
        self.wait(0.4)

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
        self.wait(2.93)

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
            self.circuit.get_electron_anim(2.97)
        )

        # write voltage of circuit
        v_label, v_value = self.get_label("V=", 12, "V", color=self.voltage_color)
        v_label.next_to(self.circuit.battery, direction=UL, buff=0)
        v_label.shift(0.25*UP+0.4*RIGHT)
        self.play(
            FadeIn(v_label),
            self.circuit.get_electron_anim(1.53)
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
            AnimationGroup(
                FadeIn(current_arrow),
                FadeIn(i_label),
                lag_ratio=0.9
            ),
            self.circuit.get_electron_anim(4.6)
        )

        # write resistance of circuit
        r_label, r_value = self.get_label("R=", 6, "\\Omega", color=self.resistance_color)
        r_label.next_to(self.circuit.light_bulb, direction=DOWN, buff=0.2)
        r_label.shift(0.25*RIGHT)
        self.play(
            FadeIn(r_label),
            self.circuit.get_electron_anim(2.33)
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
                FadeIn(null_dot, run_time=1.1),
                ReplacementTransform(i_copy, I_plug),
                FadeIn(eq_plug[3]),
                FadeIn(null_dot, run_time=0.73),
                ReplacementTransform(r_copy, R_plug),
                Write(plug_rect),
                lag_ratio=1
            ),
            self.circuit.get_electron_anim(11.37)
        )

        # add updaters
        V_plug.add_updater(lambda x: x.set_value(v_value.get_value()))
        I_plug.add_updater(lambda x: x.set_value(i_value.get_value()))
        R_plug.add_updater(lambda x: x.set_value(r_value.get_value()))

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
            self.circuit.get_electron_acceleration_anim(0.22, run_time=3)
        )
        self.play(
            self.circuit.get_electron_anim(5)
        )

        # double the voltage
        self.play(
            ApplyMethod(
                v_value.set_value, 24,
                rate_func=linear
            ),
            ApplyMethod(
                i_value.set_value, 8,
                rate_func=linear
            ),
            self.circuit.get_electron_acceleration_anim(0.44, run_time=2)
        )
        self.play(
            self.circuit.get_electron_anim(5.77)
        )

        r = lambda: (2*random.random()-1)
        v_r_values = [
            (24 + r()*23, 3 + 2.5*r())
            for _ in range(10)
        ]
        for v, r in v_r_values:
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
            self.play(
                self.circuit.get_electron_anim(0.5)
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
        # self.add(
        #     Rectangle(
        #         width=FRAME_WIDTH,
        #         height=FRAME_HEIGHT,
        #         color=YELLOW
        #     )
        # )

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
        circuit = BatteryLampCircuit() \
            .scale(0.95)\
            .shift(2.25*LEFT)
        circuit.setup_electrons()
        self.add(circuit)
        self.play(
            circuit.get_electron_anim(2.57)
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
            circuit.get_electron_anim(4.47)
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
            circuit.get_electron_anim(2)
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
        equation[3].shift(0.25*RIGHT)
        self.play(
            Write(equation),
            circuit.get_electron_anim(5.23)
        )

        rects = VGroup(*[
            SurroundingRectangle(mob)
            for mob in (equation[2], equation[0], equation[3])
        ])
        rects[0].set_color(PURPLE_C)
        self.play(
            Write(rects[0]),
            circuit.get_electron_anim(1.5)
        )
        self.play(
            Write(rects[1]),
            circuit.get_electron_anim(1.67)
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
            circuit.get_electron_anim(1)
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
            circuit.get_electron_anim(2)
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
            circuit.get_electron_anim(2)
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
            circuit.get_electron_anim(14.33)
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
            circuit.get_electron_anim(2)
        )
        self.play(
            ReplacementTransform(r_copy, r_plug),
            FadeOut(equation_divided_lhs[3]),
            circuit.get_electron_anim(5)
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
            circuit.get_electron_anim(2)
        )

        # move solution into circuit
        self.play(
            TransformFromCopy(
                current_final, i_label[1]
            ),
            FadeOut(question_marks),
            circuit.get_electron_anim(2)
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
