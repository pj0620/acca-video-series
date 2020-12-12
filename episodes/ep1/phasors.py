from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit, BatteryLampCircuitAC
from accalib.particles import Electron


class IntroPhasorsPart(Scene):
    def construct(self):
        section_label = TextMobject(
            "Part 4: \\\\",
            "Imaginary Voltage?"
        ).scale(1.5)
        self.play(
            Write(section_label[0])
        )
        self.wait()
        self.play(
            Write(section_label[1])
        )
        self.wait(1)


class ImaginaryVoltageCircuit(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "circuit_scale": 0.76
    }
    def construct(self):
        # self.add(
        #     Rectangle(
        #         width=FRAME_WIDTH,
        #         height=FRAME_HEIGHT,
        #         color=PURPLE
        #     )
        # )

        # add equation
        color_map = {
            "V": self.voltage_color,
            "I": self.current_color,
            "R": self.resistance_color
        }
        equation = TexMobject(
            "I = {V\\overR}",
            tex_to_color_map=color_map
        ) \
            .scale(3) \
            .to_edge(UP)\
            .shift(1*LEFT)
        self.play(
            FadeIn(equation[2])
        )
        self.wait(4.22)
        self.play(
            FadeIn(equation[:2]),
            FadeIn(equation[3:])
        )
        self.wait(2.04)

        # add first circuit
        circuit1 = BatteryLampCircuit() \
            .scale(self.circuit_scale) \
            .to_corner(DL, buff=0) \
            .shift(2.5*RIGHT+1*UP)
        circuit1.setup_electrons()
        cover_rect1 = SurroundingRectangle(
            circuit1,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )

        # setup circuit labels
        point1 = circuit1.electron_vect_inter.interpolate(0.55)
        point2 = circuit1.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow_1 = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label1, i_value1 = self.get_label("I", 2, "A", color=self.current_color)
        i_label1.next_to(current_arrow_1, direction=UR, buff=0) \
            .shift(0 * RIGHT)

        # write voltage of circuit
        v_label1, v_value1 = self.get_label("V", 12, "V", color=self.voltage_color)
        v_label1.next_to(circuit1.battery, direction=UL, buff=0) \
            .shift(0.25 * UP + 0.4 * RIGHT)

        # write resistance of circuit
        r_label1, r_value1 = self.get_label("R", 6, "\\Omega", color=self.resistance_color)
        r_label1.next_to(circuit1.light_bulb, direction=DOWN, buff=0.2) \
            .shift(0 * RIGHT)

        self.add(circuit1, r_label1, cover_rect1)

        # add second circuit
        circuit2 = BatteryLampCircuit(
            electron_freq=0.33
        ) \
            .scale(self.circuit_scale) \
            .to_corner(DR, buff=0) \
            .shift(0.8 * LEFT + 1 * UP)
        circuit2.setup_electrons()
        cover_rect2 = SurroundingRectangle(
            circuit2,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )

        # setup circuit labels
        point1 = circuit2.electron_vect_inter.interpolate(0.55)
        point2 = circuit2.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow_2 = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        i_label2, i_value2 = self.get_label("I", 4, "A", color=self.current_color)
        i_label2.next_to(current_arrow_2, direction=UR, buff=0) \
            .shift(0 * RIGHT)

        # write voltage of circuit
        v_label2, v_value2 = self.get_label("V", 24, "V", color=self.voltage_color)
        v_label2.next_to(circuit2.battery, direction=UL, buff=0) \
            .shift(0.25 * UP)

        # write resistance of circuit
        r_label2, r_value2 = self.get_label("R", 6, "\\Omega", color=self.resistance_color)
        r_label2.next_to(circuit2.light_bulb, direction=DOWN, buff=0.2) \
            .shift(0 * RIGHT)

        self.add(circuit2, r_label2, cover_rect2)
        self.play(
            FadeOut(cover_rect2),
            FadeOut(cover_rect1),
            circuit1.get_electron_anim(1.04),
            circuit2.get_electron_anim(1.04),
        )

        # FadeIn voltages
        self.play(
            FadeIn(v_label1),
            circuit1.get_electron_anim(2),
            circuit2.get_electron_anim(2),
        )
        self.play(
            FadeIn(v_label2),
            circuit1.get_electron_anim(3.22),
            circuit2.get_electron_anim(3.22),
        )

        # FadeIn currents
        self.play(
            FadeInFrom(i_label1, direction=UP),
            FadeInFrom(current_arrow_1, direction=UP),
            FadeInFrom(i_label2, direction=UP),
            FadeInFrom(current_arrow_2, direction=UP),
            circuit1.get_electron_anim(1),
            circuit2.get_electron_anim(1),
        )

        # label currents
        in_kw = {
            'stroke_opacity': 1,
            'stroke_color': YELLOW,
            'fill_opacity': 0.2,
            'fill_color': YELLOW
        }
        current_rects = VGroup(
            SurroundingRectangle(i_label1, **in_kw),
            SurroundingRectangle(i_label2, **in_kw),
        )
        self.play(
            FadeIn(current_rects),
            circuit1.get_electron_anim(2),
            circuit2.get_electron_anim(2),
        )

        # fadeout current labels
        self.play(
            FadeOut(current_rects, run_time=0.87),
            circuit1.get_electron_anim(0.87),
            circuit2.get_electron_anim(0.87),
        )

        # replace 24 volts with 12 j volts
        new_voltage = TexMobject(
            "12\\textbf{j} V",
            color=self.voltage_color,
            tex_to_color_map={
                "j": PURPLE
            }
        )\
            .scale(1.25)\
            .move_to(v_label2[1].get_center())
        new_voltage.submobjects[0].shift(0.4*RIGHT+0.05*DOWN)
        new_voltage.submobjects[1].shift(0.25*RIGHT+0.05*DOWN)
        new_voltage.submobjects[2].shift(0.05*DOWN)
        v_label2[1].clear_updaters()
        unknown_current = TextMobject(
            "???A",
            color=self.current_color
        )\
            .scale(1.25)\
            .move_to(i_label2[1].get_center() + 0.2*RIGHT)
        i_label2[1].clear_updaters()
        self.play(
            Transform(
                v_label2[1], new_voltage
            ),
            Transform(
                i_label2[1], unknown_current
            ),
            circuit1.get_electron_anim(2),
            circuit2.get_electron_anim(2),
        )

        # show j definition
        j_text = TexMobject(
            "\\textbf{j}", "=\\sqrt{-1}",
            tex_to_color_map={
                "\\textbf{j}": PURPLE
            }
        ) \
            .scale(1.4) \
            .to_edge(UL) \
            .shift(0.75 * RIGHT + 1.5*DOWN)
        j_rect = SurroundingRectangle(
            j_text,
            buff=0.5,
            color=YELLOW
        )
        self.play(
            Write(j_text),
            Write(j_rect),
            circuit1.get_electron_anim(4.3),
            circuit2.get_electron_anim(4.3),
        )

        # transform ??? A to (12 j) / 6
        rhs_complex = TexMobject(
            "{12 \\textbf{j} \\over 6}",
            color=self.current_color,
            tex_to_color_map={
                "12": self.voltage_color,
                "\\textbf{j}": PURPLE,
                "6": self.resistance_color
            }
        )\
            .scale(1.25)\
            .move_to(i_label2[1].get_center() + 0.1*LEFT)
        self.play(
            Transform(
                i_label2[1], rhs_complex
            ),
            circuit1.get_electron_anim(2),
            circuit2.get_electron_anim(2),
        )

        # transform (12 j) / 6 to 2 j A
        final_current = TexMobject(
            "2 \\textbf{j} A",
            color=self.current_color,
            tex_to_color_map={
                "\\textbf{j}": PURPLE
            }
        ) \
            .scale(1.25) \
            .move_to(i_label2[1].get_center() + 0.1 * LEFT)
        final_current.submobjects[1].shift(0.05*RIGHT)
        final_current.submobjects[2].shift(0.1*RIGHT)
        self.play(
            Transform(
                i_label2[1], final_current
            ),
            circuit1.get_electron_anim(3.04),
            circuit2.get_electron_anim(3.04),
        )

        # note the imaginary current
        imag_current = TextMobject(
            "Imaginary Current???",
            color=YELLOW
        )\
            .scale(1.25)\
            .to_corner(UR, buff=0)\
            .shift(3.2*DOWN+0.1*LEFT)
        imag_current_arrow = Arrow(
            imag_current.get_bottom(),
            final_current.get_top(),
            color=YELLOW
        )
        self.play(
            ShowCreation(imag_current_arrow),
            Write(imag_current),
            circuit1.get_electron_anim(6.17),
            circuit2.get_electron_anim(6.17),
        )

        # show electrons per second
        elec_per_sec = TexMobject(
            "6246000000000000\\textbf{j}",
            color=self.current_color,
            tex_to_color_map={
                "\\textbf{j}": PURPLE
            }
        ) \
            .scale(1.3) \
            .move_to(imag_current)\
            .shift(1.25*LEFT)
        elec_per_sec_unit_tex = TexMobject(
            "{1", "\\over", "\\text{second}}"
        ) \
            .scale(1) \
            .next_to(elec_per_sec, direction=RIGHT)
        elec_per_sec_unit_elec = Electron() \
            .scale(0.3) \
            .move_to(elec_per_sec_unit_tex[0])
        elec_per_sec_unit = VGroup(
            elec_per_sec_unit_tex, elec_per_sec_unit_elec
        )
        self.play(
            Transform(
                imag_current,
                VGroup(elec_per_sec, elec_per_sec_unit)
            ),
            circuit1.get_electron_anim(16.96),
            circuit2.get_electron_anim(16.96),
        )

    def get_label(self, text, initial_value, unit, **kwargs):
        lhs = TextMobject(text, "=", **kwargs)\
            .scale(1.25)
        decimal_num = DecimalNumber(
            initial_value,
            num_decimal_places=0,
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


class ACvsDC(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "electron_freq_0": 0.11,
        "electron_freq_1": 0.5,
        "ac_electron_freq": 2,
        "circuit_scale": 0.95,
        "eps_scale": 1.3
    }

    def construct(self):
        # write dc
        dc_title = TextMobject("Direct Current(", "DC", ")") \
            .scale(1.25)
        dc_title.move_to(
            FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.5 * UP + dc_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        dc_underline = Line(LEFT, RIGHT) \
            .match_width(dc_title) \
            .scale(1) \
            .next_to(dc_title, DOWN, SMALL_BUFF)
        self.play(
            Write(dc_title[1], run_time=0.5),
        )

        # write ac
        ac_title = TextMobject("Alternating Current(", "AC", ")") \
            .scale(1.25)
        ac_title.move_to(
            FRAME_WIDTH * 0.25 * RIGHT + FRAME_HEIGHT * 0.5 * UP + ac_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        ac_underline = Line(LEFT, RIGHT) \
            .match_width(ac_title) \
            .scale(1) \
            .next_to(ac_title, DOWN, SMALL_BUFF)
        self.play(
            Write(ac_title[1], run_time=0.5)
        )
        self.wait(2.08)

        # show direct current
        self.play(
            Write(VGroup(dc_title[0], dc_title[2])),
            ShowCreation(dc_underline)
        )

        # fade in dc circuit
        dc_circuit = BatteryLampCircuit(
            electron_freq=self.electron_freq_0
        ) \
            .scale(self.circuit_scale) \
            .to_corner(UL, buff=0) \
            .shift(2.5 * DOWN + 0.2 * RIGHT)
        dc_circuit.setup_electrons()
        block_rect = Rectangle(
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        ) \
            .set_width(dc_circuit.get_width() * 1.3, stretch=True) \
            .set_height(dc_circuit.get_height() * 0.8, stretch=True) \
            .move_to(dc_circuit.get_center())
        # show current label
        point1 = dc_circuit.electron_vect_inter.interpolate(0.55)
        point2 = dc_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        current_text = TextMobject(
            "current", "=",
            color=self.current_color) \
            .next_to(current_arrow, direction=UR) \
            .shift(0 * RIGHT) \
            .scale(1.5)
        current_value = DecimalNumber(
            1,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        ) \
            .scale(1.5) \
            .next_to(current_text, direction=RIGHT, buff=0.3)
        current_tracker = ValueTracker(1)
        current_value.add_updater(
            lambda x:
            x.set_value(current_tracker.get_value())
        )
        self.add(dc_circuit, current_arrow, current_text, current_value, block_rect)

        # label equivalent electrons per second
        elec_per_sec = DecimalNumber(
            6246000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(self.eps_scale) \
            .to_corner(DL) \
            .shift(0.3 * LEFT)
        elec_per_sec_tracker = ValueTracker(6246000000000000)
        elec_per_sec.add_updater(
            lambda x: x.set_value(elec_per_sec_tracker.get_value())
        )
        elec_per_sec_unit_tex = TexMobject(
            "{1", "\\over", "\\text{second}}"
        ) \
            .scale(1.15) \
            .next_to(elec_per_sec, direction=RIGHT)
        elec_per_sec_unit_elec = Electron() \
            .scale(0.3) \
            .move_to(elec_per_sec_unit_tex[0])
        elec_per_sec_unit = VGroup(
            elec_per_sec_unit_tex, elec_per_sec_unit_elec
        )
        self.play(
            FadeOut(block_rect),
            FadeIn(elec_per_sec),
            FadeIn(elec_per_sec_unit),
            dc_circuit.get_electron_anim(5)
        )

        # add dividing line
        dividing_line = DashedLine(
            start=FRAME_HEIGHT * 0.5 * DOWN,
            end=FRAME_HEIGHT * 0.5 * UP,
            dash_length=0.25
        )
        self.play(
            ShowCreation(dividing_line),
            dc_circuit.get_electron_anim(2.87)
        )

        # show alternating current
        self.play(
            Write(VGroup(ac_title[0], ac_title[2])),
            ShowCreation(ac_underline),
            dc_circuit.get_electron_anim(1)
        )

        # fade in ac circuit
        ac_circuit = BatteryLampCircuitAC(
            electron_freq=self.ac_electron_freq
        ) \
            .scale(self.circuit_scale) \
            .to_corner(UR, buff=0) \
            .shift(2.5 * DOWN + 1.0 * LEFT)
        ac_circuit.setup_electrons()
        block_rect_ac = Rectangle(
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0,
            width=7.7,
            height=6
        ) \
            .move_to(ac_circuit.get_center())
        # show current label
        point1 = ac_circuit.electron_vect_inter.interpolate(0.55)
        point2 = ac_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow_ac = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        current_text_ac = TextMobject(
            "current", "=",
            color=self.current_color) \
            .next_to(current_arrow_ac, direction=UR) \
            .shift(0.5 * LEFT) \
            .scale(1.5)
        current_value_ac = DecimalNumber(
            1,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        ) \
            .scale(1.5) \
            .next_to(current_text_ac, direction=RIGHT, buff=0.3)
        phase_tracker_ac = ValueTracker(0)
        current_value_ac.add_updater(
            lambda x:
            x.set_value(np.sin(phase_tracker_ac.get_value()))
        )
        self.add(ac_circuit, current_arrow_ac, current_text_ac, current_value_ac, block_rect_ac)

        # label equivalent electrons per second
        elec_per_sec_ac = DecimalNumber(
            6246000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(self.eps_scale) \
            .to_corner(DR) \
            .shift(1.5 * LEFT)
        elec_per_sec_ac.add_updater(
            lambda x: x.set_value(6246000000000000 * np.sin(phase_tracker_ac.get_value()))
        )
        elec_per_sec_unit_tex_ac = TexMobject(
            "{1", "\\over", "\\text{second}}"
        ) \
            .scale(1.15) \
            .next_to(elec_per_sec_ac, direction=RIGHT)
        elec_per_sec_unit_elec_ac = Electron() \
            .scale(0.3) \
            .move_to(elec_per_sec_unit_tex_ac[0])
        elec_per_sec_unit_ac = VGroup(
            elec_per_sec_unit_tex_ac, elec_per_sec_unit_elec_ac
        )
        block_rect_2 = Rectangle(
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0,
            width=8.5,
            height=3
        ) \
            .move_to(VGroup(elec_per_sec_ac, elec_per_sec_unit_ac).get_center())
        self.add(elec_per_sec_ac, elec_per_sec_unit_ac, block_rect_2)
        self.play(
            FadeOut(block_rect_2),
            FadeOut(block_rect_ac),
            ac_circuit.get_electron_anim(7.57),
            dc_circuit.get_electron_anim(7.57),
            ApplyMethod(
                phase_tracker_ac.increment_value,
                7.57 * self.ac_electron_freq,
                run_time=7.57,
                rate_func=linear
            ),
        )


class ACDCApplications(Scene):
    CONFIG={
        "circuit_color": BLUE_C
    }
    def construct(self):
        # add line dividing screen
        dividing_line = DashedLine(
            start=FRAME_HEIGHT * 0.5 * DOWN,
            end=FRAME_HEIGHT * 0.5 * UP,
            dash_length=0.25
        )
        self.add(dividing_line)

        # dc title
        dc_title = TextMobject("Direct Current", "(DC)")\
            .scale(1.25)
        dc_title.move_to(
            FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.5 * UP + dc_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        dc_underline = Line(LEFT, RIGHT) \
            .match_width(dc_title) \
            .scale(1) \
            .next_to(dc_title, DOWN, SMALL_BUFF)
        self.add(dc_title, dc_underline)

        # ac title
        ac_title = TextMobject("Alternating Current", "(AC)")\
            .scale(1.25)
        ac_title.move_to(
            FRAME_WIDTH * 0.25 * RIGHT + FRAME_HEIGHT * 0.5 * UP + ac_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        ac_underline = Line(LEFT, RIGHT) \
            .match_width(ac_title) \
            .scale(1) \
            .next_to(ac_title, DOWN, SMALL_BUFF)
        self.add(ac_title, ac_underline)
        self.wait(4.96)

        # phone
        phone = ImageMobject(
            "images\ep1\IntroduceACDC\cell-phone.png"
        )\
            .scale(2.2)\
            .to_edge(LEFT, buff=-0.6)\
            .shift(1*UP)
        self.play(
            FadeIn(phone)
        )

        # car
        car = ImageMobject(
            "images\ep1\IntroduceACDC\car.png"
        )\
            .scale(1.5)\
            .next_to(phone, direction=RIGHT, buff=-1.5)
            # .shift(2*DOWN)
        self.play(
            FadeIn(car)
        )
        self.wait(5.9)

        # power lines
        power_line = ImageMobject(
            "images\ep1\IntroduceACDC\power_line5.jpg"
        )\
            .scale(2.7)\
            .to_edge(RIGHT, buff=0.5)\
            .shift(1*UP)
        self.play(
            FadeIn(power_line)
        )
        self.wait(3.06)

        # outlet
        outlet = ImageMobject(
            "images\ep1\IntroduceACDC\outlet-US.jpg"
        ) \
            .scale(2)\
            .next_to(power_line, direction=LEFT, buff=0.5)
        self.play(
            FadeIn(outlet)
        )
        self.wait(4)


class SineWaveCharacteristics(ACvsDC):
    CONFIG={
        "axes_config": {
            "number_line_config": {
                "include_tip": False,
            },
            "x_axis_config": {
                "color": BLUE_C,
            },
            "y_axis_config": {
                "color": BLUE_C,
            },
            "x_min": 0,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "center_point": RIGHT_SIDE + 7 * LEFT + 0.5 * UP,
        },
        "ac_electron_freq": 1,
        "amplitude_color": ORANGE,
        "ang_freq_color": BLUE_C,
        "phase_color": RED_B,
        "base_electron_freq": 1,
        "base_electron_amplitude": 0.15
    }
    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=PURPLE
            )
        )

        # fade in ac circuit
        self.ac_circuit = BatteryLampCircuitAC(
            electron_freq=self.base_electron_freq,
            electron_amplitude=self.base_electron_amplitude
        ) \
            .scale(1.0) \
            .to_edge(LEFT, buff=0.1)
        self.amplitude_value = ValueTracker(1)
        self.freq_value = ValueTracker(1)
        self.phase_value = ValueTracker(0)
        self.ac_circuit.setup_electrons()
        point1 = self.ac_circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.ac_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow_ac = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        current_text_ac = TextMobject(
            "current", "=",
            color=self.current_color) \
            .next_to(current_arrow_ac, direction=UR) \
            .shift(0.5 * LEFT) \
            .scale(1.5)
        current_value_ac = DecimalNumber(
            1,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        ) \
            .scale(1.5) \
            .next_to(current_text_ac, direction=RIGHT, buff=0.3)
        current_value_ac.add_updater(
            lambda x:
            x.set_value((1/self.base_electron_amplitude) * self.ac_circuit.get_instantaneous_current())
        )
        self.add(self.ac_circuit, current_arrow_ac, current_text_ac, current_value_ac)
        self.play(
            self.ac_circuit.get_electron_anim(2*PI-1)
        )

        # add axis
        self.time_axes = Axes(**self.axes_config)
        y_label = self.time_axes.get_y_axis_label("\\text{I(t)}")\
            .shift(0.5 * UP)\
            .scale(1.3)\
            .set_color(self.current_color)
        time_label = self.time_axes.get_x_axis_label("\\text{time}").set_color(BLUE_C)
        self.add(self.time_axes, time_label, y_label)
        self.play(
            FadeIn(self.time_axes),
            FadeIn(y_label),
            FadeIn(time_label),
            self.ac_circuit.get_electron_anim(1)
        )

        #
        # phase must be multiple of 2 pi at this point
        #

        # draw sine wave
        graph_animated = self.time_axes.get_graph(
            np.sin,
        ).set_color(self.current_color)
        self.graph = self.time_axes.get_graph(
            np.sin,
            x_max=20
        ).set_color(self.current_color)
        draw_line = Line(ORIGIN, ORIGIN, color=YELLOW, stroke_width=4)
        draw_dot = Dot(ORIGIN, color=YELLOW)
        self.ac_circuit.electron_time.set_value(0)
        def line_update(line):
            rvec = self.ac_circuit.electron_time.get_value()*RIGHT
            uvec = (self.ac_circuit.get_instantaneous_current()/self.base_electron_amplitude)*UP
            start = self.time_axes.center_point + rvec
            end = self.time_axes.center_point + uvec + rvec + 0.00001*UP
            line.put_start_and_end_on(start, end)
        def dot_update(dot):
            rvec = self.ac_circuit.electron_time.get_value() * RIGHT
            uvec = (self.ac_circuit.get_instantaneous_current() / self.base_electron_amplitude) * UP
            loc = self.time_axes.center_point + uvec + rvec + 0.00001 * UP
            dot.move_to(loc)
        self.play(
            UpdateFromFunc(draw_line, line_update),
            UpdateFromFunc(draw_dot, dot_update),
            ShowCreation(
                graph_animated,
                run_time=7,
                rate_func=linear
            ),
            self.ac_circuit.get_electron_anim(8)
        )
        self.remove(graph_animated)
        self.add(self.graph)

        # add sine wave equation
        equation = TexMobject(
            "I(t) = sin(t)",
            color=self.current_color,
        )\
            .scale(1.75)\
            .to_edge(DOWN, buff=0.1)
        self.play(
            FadeInFrom(equation, direction=DOWN),
            self.ac_circuit.get_electron_anim(8.48)
        )

        # show different sine waves
        self.play(
            self.get_amplitude_anim(2, 0.5),
        )
        self.play(
            self.get_freq_anim(2, 0.5),
        )
        self.play(
            self.get_amplitude_anim(0.25, 0.5),
        )
        self.play(
            self.get_freq_anim(0.7, 0.5),
        )

        #set amplitude to 1
        self.play(
            self.get_amplitude_anim(1, 0.5),
        )
        # set freq to 1
        self.play(
            self.get_freq_anim(1, 0.5),
        )
        self.play(
            self.ac_circuit.get_electron_anim(4.47),
        )

        # transform to general sine wave formula
        equation_general = TexMobject(
            "I(t) = A \\hspace{1mm} sin( \\hspace{1mm} \\omega \\hspace{1mm} t \\hspace{1mm} + \\hspace{1mm} \\phi \\hspace{1mm})",
            color=self.current_color,
            tex_to_color_map={
                "A": self.amplitude_color,
                "\\omega": self.ang_freq_color,
                "\\phi": self.phase_color
            },
            substring_to_isolate=[
                "A",
                "\\omega",
                "\\phi"
            ]
        ) \
            .scale(1.75) \
            .to_edge(DOWN, buff=0.1)
        self.play(
            Transform(equation, equation_general),
            self.ac_circuit.get_electron_anim(2.65)
        )

        # add rectangles around parameters
        rects_kw={
            "buff": 0.15,
            "color": YELLOW,
            "stroke_width": 5
        }
        params = VGroup(
            equation_general.get_part_by_tex("A"),
            equation_general.get_part_by_tex("\\omega"),
            equation_general.get_part_by_tex("\\phi"),
        )
        # rects[-1].shift(0.1*UP)
        self.play(
            *[
                ShowCreationThenDestructionAround(rect)
                for rect in params
            ],
            self.ac_circuit.get_electron_anim(3.39)
        )

        # show amplitude braces with definition
        brace_ampl = Brace(
            equation_general.get_part_by_tex("A"),
            direction=UP,
            color=self.amplitude_color
        )
        brace_ampl_def = brace_ampl.get_text("Amplitude")\
            .scale(1.5)\
            .set_color(self.amplitude_color)
        brace_ampl_val = DecimalNumber(
            1,
            color=self.amplitude_color,
        )\
            .scale(1.5)\
            .move_to(brace_ampl_def.get_center())
        self.play(
            ShowCreation(brace_ampl),
            Write(brace_ampl_def),
            self.ac_circuit.get_electron_anim(6.13)
        )

        # convert amplitude to 1
        self.play(
            Transform(brace_ampl_def, brace_ampl_val),
            self.ac_circuit.get_electron_anim(3)
        )
        brace_ampl_val.add_updater(
            lambda x: x.set_value(self.amplitude_value.get_value())
        )
        # second call to add for updater
        self.remove(brace_ampl_def)
        self.add(brace_ampl_val)

        # show dashed line showing amplitude
        ampl_kw = {
            "color": self.amplitude_color,
            "dash_length": 0.05
        }

        def up_ampl_updator(line):
            line.put_start_and_end_on(
                self.time_axes.center_point + UP * self.amplitude_value.get_value(),
                self.time_axes.center_point + UP * self.amplitude_value.get_value() + 8 * RIGHT
            )

        def down_ampl_updator(line):
            line.put_start_and_end_on(
                self.time_axes.center_point + DOWN * self.amplitude_value.get_value(),
                self.time_axes.center_point + DOWN * self.amplitude_value.get_value() + 8 * RIGHT
            )

        ampl_lines = VGroup(
            DashedLine(**ampl_kw).add_updater(up_ampl_updator, call_updater=True),
            DashedLine(**ampl_kw).add_updater(down_ampl_updator, call_updater=True)
        )

        def up_ampl_label_updator(label):
            label.next_to(
                self.time_axes.center_point + UP * self.amplitude_value.get_value(),
                direction=LEFT
            )
            label.set_value(self.amplitude_value.get_value())

        def down_ampl_label_updator(label):
            label.next_to(
                self.time_axes.center_point + DOWN * self.amplitude_value.get_value(),
                direction=LEFT
            )
            label.set_value(-1 * self.amplitude_value.get_value())

        self.ampl_labels = VGroup(
            DecimalNumber(**ampl_kw).add_updater(up_ampl_label_updator, call_updater=True),
            DecimalNumber(**ampl_kw).add_updater(down_ampl_label_updator, call_updater=True),
        )
        self.play(
            AnimationGroup(
                ShowCreation(ampl_lines),
                FadeInFrom(self.ampl_labels, direction=LEFT),
                lag_ratio=0.8
            ),
            self.ac_circuit.get_electron_anim(4.52)
        )

        # set amplitude to 2 A
        self.play(
            self.get_amplitude_anim(2),
            self.ac_circuit.get_electron_anim(5)
        )

        # set amplitude to 0.25 A
        self.play(
            self.get_amplitude_anim(0.25),
            self.ac_circuit.get_electron_anim(3.57)
        )

        # set amplitude to 1 A
        self.play(
            self.get_amplitude_anim(1),
            self.ac_circuit.get_electron_anim(1.83)
        )

        # show freq braces with definition
        brace_freq = Brace(
            equation_general.get_part_by_tex("\\omega"),
            direction=UP,
            color=self.ang_freq_color
        )
        brace_freq_def = brace_freq.get_text("Angular Frequency") \
            .scale(1.5) \
            .set_color(self.ang_freq_color)
        brace_freq_val = DecimalNumber(
            1,
            color=self.ang_freq_color,
        ) \
            .scale(1.5) \
            .move_to(brace_freq_def.get_center())
        brace_freq_def.shift(2*RIGHT)
        self.play(
            ShowCreation(brace_freq),
            Write(brace_freq_def),
            self.ac_circuit.get_electron_anim(8.13)
        )

        # convert freq to 1
        self.play(
            Transform(brace_freq_def, brace_freq_val),
            self.ac_circuit.get_electron_anim(3)
        )
        brace_freq_val.add_updater(
            lambda x: x.set_value(self.freq_value.get_value())
        )
        # second call to add for updater
        self.remove(brace_freq_def)
        self.add(brace_freq_val)

        # set freq to 2 A
        self.play(
            self.get_freq_anim(2),
            self.ac_circuit.get_electron_anim(5)
        )

        # set freq to 0.5 A
        self.play(
            self.get_freq_anim(0.5),
            self.ac_circuit.get_electron_anim(5)
        )

        # set freq to 1 A
        self.play(
            self.get_freq_anim(1),
            self.ac_circuit.get_electron_anim(8.3)
        )

        # show phase braces with definition
        brace_phase = Brace(
            equation_general.get_part_by_tex("\\phi"),
            direction=UP,
            color=self.phase_color
        )
        brace_phase_def = brace_phase.get_text("Phase") \
            .scale(1.5) \
            .set_color(self.phase_color)
        brace_phase_val = DecimalNumber(
            0,
            color=self.phase_color,
        ) \
            .scale(1.5) \
            .move_to(brace_phase_def.get_center())
        self.play(
            ShowCreation(brace_phase),
            Write(brace_phase_def),
            self.ac_circuit.get_electron_anim(4.65)
        )

        # add graph with negative portion so we can slide left and right
        self.remove(self.graph)
        self.ampl_labels.clear_updaters()
        self.graph = self.time_axes.get_graph(
            np.sin,
            x_max=20,
            x_min=-2.4
        ).set_color(self.current_color)
        self.block_rect = Rectangle(
            width=2.5,
            height=3,
            stroke_opacity=0,
            fill_color=BLACK,
            fill_opacity=1
        ) \
            .next_to(self.time_axes.center_point, direction=LEFT, buff=0)
        self.add(self.graph, self.block_rect, self.time_axes, self.ampl_labels)

        # convert phase to 0
        self.play(
            Transform(brace_phase_def, brace_phase_val),
            self.ac_circuit.get_electron_anim(3)
        )
        brace_phase_val.add_updater(
            lambda x: x.set_value(self.phase_value.get_value())
        )
        # second call to add for updater
        self.remove(brace_phase_def)
        self.add(brace_phase_val)

        # set phase to different values
        self.play(
            self.get_phase_anim(1)
        )
        self.play(
            self.ac_circuit.get_electron_anim(5.52)
        )
        self.play(
            self.get_phase_anim(-1)
        )
        self.play(
            self.ac_circuit.get_electron_anim(1.65)
        )
        self.play(
            self.get_phase_anim(0)
        )
        self.play(
            self.ac_circuit.get_electron_anim(15.13)
        )

    def get_sin(self, ampl=1, ang_freq=1, phase=0):
        return lambda t: ampl * np.sin(ang_freq*t + phase)

    def get_phase_anim(self, new_phase, run_time=1.):
        del_phase = new_phase - self.phase_value.get_value()
        return AnimationGroup(
            ApplyMethod(
                self.graph.shift, -1*del_phase*RIGHT,
                run_time=1
            ),
            ApplyMethod(
                self.phase_value.set_value, new_phase,
                run_time=1
            ),
            ApplyMethod(
                self.block_rect.shift, 0.001*UP,
                rate_func=there_and_back,
                run_time=1
            ),
            ApplyMethod(
                self.ampl_labels.shift, 0.001*UP,
                rate_func=there_and_back,
                run_time=1
            ),
            ApplyMethod(
                self.time_axes.shift, 0.001 * UP,
                rate_func=there_and_back,
                run_time=1
            ),
            self.ac_circuit.get_electron_anim(run_time=run_time)
        )

    def get_freq_anim(self, new_freq, run_time=1.):
        self.ac_circuit.set_electron_freq_anim(new_freq * self.base_electron_freq, run_time=run_time)
        cur_freq = self.freq_value.get_value()
        transform_matrix = np.array(
            [[cur_freq/new_freq, 0, 0],
             [0,                 1, 0],
             [0,                 0, 1]]
        )
        offset = np.array(
            [(1-cur_freq/new_freq)*self.time_axes.center_point[0],
             0,
             0]
        )
        def fun(p):
            return offset + transform_matrix.dot(p)

        return AnimationGroup(
            ApplyPointwiseFunction(
                fun, self.graph,
                run_time=run_time
            ),
            self.ac_circuit.get_electron_anim(run_time=run_time),
            ApplyMethod(
                self.freq_value.set_value, new_freq,
                run_time=run_time
            ),
            lag_ratio=0
        )

    def get_amplitude_anim(self, new_ampl, run_time=1.):
        self.ac_circuit.set_electron_amplitude_anim(new_ampl*self.base_electron_amplitude, run_time=run_time)
        transform_matrix = np.array(
            [[1, 0, 0],
             [0, new_ampl/self.amplitude_value.get_value(), 0],
             [0, 0, 1]]
        )

        def fun(p):
            return self.time_axes.center_point + transform_matrix.dot(p-self.time_axes.center_point)

        return AnimationGroup(
            ApplyPointwiseFunction(
                fun, self.graph,
                run_time=run_time
            ),
            ApplyMethod(
                self.amplitude_value.set_value, new_ampl,
                run_time=run_time
            ),
            self.ac_circuit.get_electron_anim(run_time),
            lag_ratio=0)


class OutletScene(SineWaveCharacteristics):
    CONFIG = {
        "neutral_color": RED,
        "hot_color": GREEN,
        "ground_color": PURPLE,
        "axes_config": {
            "number_line_config": {
                "include_tip": False,
            },
            "x_axis_config": {
                "color": BLUE_C,
            },
            "y_axis_config": {
                "color": BLUE_C,
            },
            "x_min": 0,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "center_point": RIGHT_SIDE + 7 * LEFT + 1.75 * UP,
        },
    }
    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=PURPLE
            )
        )

        # add outlet
        outlet = ImageMobject("images/ep1/CompareACDC/outlet-US.jpg")\
            .scale(3)\
            .to_edge(LEFT, buff=3.5)\
            .shift(1.8*UP)
        self.add(outlet)
        self.wait(12.13)

        # add graph
        self.time_axes = Axes(**self.axes_config)
        y_label = self.time_axes.get_y_axis_label("\\text{Voltage}") \
            .shift(0.5 * UP) \
            .scale(1.3) \
            .set_color(WHITE)
        time_label = self.time_axes.get_x_axis_label("\\text{time}").set_color(BLUE_C)
        self.add(self.time_axes, time_label, y_label)
        self.play(
            FadeIn(self.time_axes),
            FadeIn(y_label),
            FadeIn(time_label),
        )

        # draw sine wave
        graph_animated = self.time_axes.get_graph(
            self.get_sin(ampl=1.7),
            x_max=8
        ).set_color(self.neutral_color)
        self.graph = self.time_axes.get_graph(
            self.get_sin(ampl=1.7),
            x_max=20
        ).set_color(self.neutral_color)
        draw_line = Line(ORIGIN, ORIGIN, color=YELLOW, stroke_width=4)
        draw_dot = Dot(ORIGIN, color=YELLOW)
        time_value = ValueTracker(0)
        def line_update(line):
            rvec = time_value.get_value() * RIGHT
            uvec = 1.7 * np.sin(time_value.get_value()) * UP
            start = self.time_axes.center_point + rvec
            end = self.time_axes.center_point + uvec + rvec + 0.00001 * UP
            line.put_start_and_end_on(start, end)

        def dot_update(dot):
            rvec = time_value.get_value() * RIGHT
            uvec = 1.7 * np.sin(time_value.get_value()) * UP
            loc = self.time_axes.center_point + uvec + rvec + 0.00001 * UP
            dot.move_to(loc)

        self.play(
            ApplyMethod(
                time_value.set_value, 8,
                rate_func=linear,
                run_time=4,
            ),
            UpdateFromFunc(draw_line, line_update),
            UpdateFromFunc(draw_dot, dot_update),
            ShowCreation(
                graph_animated,
                run_time=4,
                rate_func=linear
            ),
        )
        self.remove(graph_animated)
        self.add(self.graph)
        self.wait(1.91)

        outlet_mid = outlet.get_center()
        neutral_center = outlet_mid + UP*1.15 + LEFT*0.36
        hot_center = outlet_mid + UP*1.15 + RIGHT*0.27
        ground_center = outlet_mid + UP*0.55 + LEFT*0.05

        arrow_kw = {
            "stroke_width": 30,
            "tip_length": 10,
            "max_tip_length_to_length_ratio": 0.25
        }

        # neutral label
        neutral_arrow = Arrow(
            neutral_center + 2*LEFT,
            neutral_center,
            buff=0,
            color=self.neutral_color,
            **arrow_kw
        )
        neutral_label = TextMobject(
            "Neutral",
            color=self.neutral_color
        )\
            .scale(1.4)\
            .next_to(neutral_arrow, direction=LEFT, buff=0.3)
        self.play(
            Write(neutral_label),
            ShowCreation(neutral_arrow)
        )

        # hot label
        hot_arrow = Arrow(
            hot_center + 2 * RIGHT,
            hot_center,
            buff=0,
            color=self.hot_color,
            **arrow_kw
        )
        hot_label = TextMobject(
            "Hot",
            color=self.hot_color
        ) \
            .scale(1.4) \
            .next_to(hot_arrow, direction=RIGHT, buff=0.3)
        self.play(
            Write(hot_label),
            ShowCreation(hot_arrow)
        )

        # ground label
        ground_arrow = Arrow(
            ground_center + 2 * RIGHT + 0.5 * DOWN,
            ground_center,
            buff=0,
            color=self.ground_color,
            **arrow_kw
        )
        ground_label = TextMobject(
            "Ground",
            color=self.ground_color
        ) \
            .scale(1.4) \
            .next_to(ground_center + 2 * RIGHT + 0.5 * DOWN, direction=RIGHT, buff=0.3)
        self.play(
            Write(ground_label),
            ShowCreation(ground_arrow)
        )
        self.wait(3.13)

        # add neutral equation
        neutral_eq = TexMobject(
            "V_{\\text{Neutral}}(t) = 170 \\hspace{1mm} sin( \\hspace{1mm} 120\\pi \\hspace{1mm} t )",
            color=self.neutral_color,
            tex_to_color_map={
                "170": self.amplitude_color,
                "120\\pi": self.ang_freq_color,
            },
            substring_to_isolate=[
                "170",
                "120\\pi",
            ]
        ) \
            .scale(1.75) \
            .to_edge(DOWN, buff=0.1)
        self.play(
            FadeInFrom(
                neutral_eq, direction=DOWN
            )
        )

        self.wait(5)

