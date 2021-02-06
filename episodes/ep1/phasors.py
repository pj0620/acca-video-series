from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit, BatteryLampCircuitAC
from accalib.particles import Electron

from accalib.lines import DottedLine

from accalib.tools import rule_of_thirds_guide

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
            self.ac_circuit.get_electron_anim(50)
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


class EulersFormulaIntro(Scene):
    CONFIG = {
        "x_color": GREEN_D,
        "y_color": RED_D,
    }
    def construct(self):
        # add eulers identity equation
        eulers_identity = TexMobject(
            "e^{j \\pi} = -1",
            tex_to_color_map={
                "j": PURPLE,
                "\\pi": YELLOW
            }
        )\
            .scale(4)
        self.play(Write(eulers_identity))
        self.wait(14.91)

        # add eulers formula
        eulers_formula = TexMobject(
            "Im \\{ e^{j \\theta} \\}", " = ", "cos(", "\\theta", ")", " + j ", "sin(", "\\theta", ")",
            # tex_to_color_map={
            #     "j": PURPLE,
            #     "\\theta": YELLOW
            # }
        ) \
            .scale(2) \
            .move_to(2.7 * RIGHT + DOWN)
        eulers_formula[2].set_color(self.x_color)
        eulers_formula[4].set_color(self.x_color)
        eulers_formula[6].set_color(self.y_color)
        eulers_formula[8].set_color(self.y_color)
        eulers_formula[0][4].set_color(PURPLE)
        eulers_formula[5][1].set_color(PURPLE)
        eulers_formula[0][5].set_color(YELLOW)
        eulers_formula[3].set_color(YELLOW)
        eulers_formula[-2].set_color(YELLOW)
        imag_label = VGroup(
            *eulers_formula[0][:3],
            eulers_formula[0][-1]
        )
        imag_label.set_opacity(0)
        self.play(
            Transform(
                eulers_identity, eulers_formula
            )
        )

        self.wait(10)


class VideoRecommendEulerIdentity(Scene):
    def construct(self):
        height = 7
        rect = Rectangle(
            height=height,
            width=(16/9)*height
        )\
            .to_edge(DOWN, buff=1)
        self.add(rect)

        title = TextMobject("Understanding e to the i pi in 3.14 minutes | DE5 - 3Blue1Brown")\
            .scale(1.2)\
            .next_to(rect, direction=UP)
        self.play(
            Write(title)
        )

        self.wait(10)


class EulersFormula(SineWaveCharacteristics):
    CONFIG = {
        "imag_axes_config": {
            "number_line_config": {
                "include_tip": True,
            },
            "x_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 10
            },
            "y_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 10
            },
            "x_min": -2.1,
            "x_max": 2.1,
            "y_min": -2.1,
            "y_max": 2.1,
            "center_point": FRAME_WIDTH*0.25*LEFT + FRAME_HEIGHT*0.25*UP + 0.3*UP + 1.7*LEFT,
        },
        "sin_axes_config": {
            "number_line_config": {
                "include_tip": True,
            },
            "x_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 1
            },
            "y_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 1
            },
            "x_min": -0.2,
            "x_max": 7,
            "y_min": -2.1,
            "y_max": 2.1,
            "center_point": FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.25 * UP + 0.3 * UP + 2*RIGHT,
        },
        "cos_axes_config": {
            "number_line_config": {
                "include_tip": True,
            },
            "x_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 1
            },
            "y_axis_config": {
                "color": BLUE_C,
                "tick_frequency": 1
            },
            "x_min": -0.2,
            "x_max": 7,
            "y_min": -2.1,
            "y_max": 2.1,
            "center_point": FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.25 * UP + 2.2 * DOWN + 1.7*LEFT,
        },
        "x_color": GREEN_D,
        "y_color": RED_D,
        "show_x_graph": False,
        "show_y_graph": False,
        # "amplitude_color": ORANGE,
        # "ang_freq_color": BLUE_C,
        # "phase_color": RED_B,
    }

    def construct(self):
        # add eulers formula
        eulers_formula = TexMobject(
            "Im \\{ e^{j \\theta} \\}", " = ", "cos(", "\\theta", ")"," + j ", "sin(", "\\theta", ")",
            # tex_to_color_map={
            #     "j": PURPLE,
            #     "\\theta": YELLOW
            # }
        ) \
            .scale(2)\
            .move_to(2.5*RIGHT + 1*DOWN)
        eulers_formula[2].set_color(self.x_color)
        eulers_formula[4].set_color(self.x_color)
        eulers_formula[6].set_color(self.y_color)
        eulers_formula[8].set_color(self.y_color)
        eulers_formula[0][4].set_color(PURPLE)
        eulers_formula[5][1].set_color(PURPLE)
        eulers_formula[0][5].set_color(YELLOW)
        eulers_formula[3].set_color(YELLOW)
        eulers_formula[-2].set_color(YELLOW)
        eq_imag_label = VGroup(
            *eulers_formula[0][:3],
            eulers_formula[0][-1]
        )
        eq_imag_label.set_opacity(0)

        self.add(eulers_formula)

        self.wait(3.48)

        self.create_circle_mobs()

        ejt_rect = SurroundingRectangle(
            VGroup(*eulers_formula[0][3:6]),
            fill_color=YELLOW,
            fill_opacity=0.5
        )
        self.play(
            self.get_drawing_anims(1.65),
        )
        self.play(
            FadeInFrom(ejt_rect, direction=UP),
            self.get_drawing_anims(2*PI - 1.65),
        )

        # phase must be a multiple of 2*PI at this point
        self.wait(1)
        self.play(
            FadeOut(ejt_rect)
        )

        self.show_x_graph = True
        self.show_y_graph = True

        self.setup_cos_mobs()
        self.cos_graph = self.cos_axes.get_graph(
            np.cos,
            color=self.x_color,
            x_min=0,
            x_max=2 * PI
        )

        # add sin axes
        self.setup_sine_mobs()
        self.sin_graph = self.sin_axes.get_graph(
            np.sin,
            color=self.y_color,
            x_min=0,
            x_max=2 * PI
        )
        self.add(self.sin_axes)

        cos_rects = VGroup(
            SurroundingRectangle(
                VGroup(*eulers_formula[2:5]),
                color=self.x_color,
                fill_color=self.x_color,
                fill_opacity=0.5
            ),
            SurroundingRectangle(
                VGroup(self.cos_label),
                color=self.x_color,
                fill_color=self.x_color,
                fill_opacity=0.5
            ),
        )

        sin_rects = VGroup(
            SurroundingRectangle(
                VGroup(*eulers_formula[6:]),
                color=self.y_color,
                fill_color=self.y_color,
                fill_opacity=0.5
            ),
            SurroundingRectangle(
                VGroup(self.sin_label),
                color=self.y_color,
                fill_color=self.y_color,
                fill_opacity=0.5
            ),
        )

        # draw graphs
        self.play(
            self.get_drawing_anims(3 * PI),
            ShowCreation(
                self.cos_graph,
                run_time=2*PI,
                rate_func=linear
            ),
            ShowCreation(
                self.sin_graph,
                run_time=2 * PI,
                rate_func=linear
            ),
            AnimationGroup(
                FadeIn(Dot().shift(100 * UR), run_time=1.26),
                FadeIn(cos_rects),
                FadeIn(Dot().shift(100*UR), run_time=3),
                FadeIn(sin_rects),
                lag_ratio=1
            )
        )
        self.play(
            FadeOut(VGroup(sin_rects, cos_rects)),
            self.get_drawing_anims(5.91),
        )

        # only show imaginary part
        self.show_x_graph = False
        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeOut(VGroup(*eulers_formula[2:6])),
                    ApplyMethod(eq_imag_label.set_opacity, 1),
                    lag_ratio=0
                ),
                AnimationGroup(
                    # ApplyMethod(VGroup(*eulers_formula[:2]).shift, 2 * RIGHT),
                    ApplyMethod(VGroup(*eulers_formula[6:]).shift, 4 * LEFT),
                    lag_ratio=0
                ),
                lag_ratio=1
            ),
            FadeOut(self.cos_axes),
            FadeOut(self.time_label2),
            FadeOut(self.cos_label),
            FadeOut(self.cos_dot),
            FadeOut(self.x_draw_line),
            FadeOut(self.cos_graph),
            self.get_drawing_anims(2)
        )

        self.play(
            self.get_drawing_anims(13.17),
        )

        cur_eulers_formula = VGroup(
            *eulers_formula[:2],
            *eulers_formula[6:]
        )
        general_eulers_formula = TexMobject(
            "Im \\{ A e^{j (\\omega t + \\phi)} \\}", " = ", "A", "sin(", "\\omega", "t", "+", "\\phi", ")",
        ) \
            .scale(2)\
            .next_to(cur_eulers_formula, direction=DOWN, buff=0.3)
        VGroup(
            general_eulers_formula[0][3],
            general_eulers_formula[2]
        ).set_color(self.amplitude_color)
        VGroup(
            general_eulers_formula[0][7],
            general_eulers_formula[4]
        ).set_color(self.ang_freq_color)
        VGroup(
            general_eulers_formula[0][10],
            general_eulers_formula[7]
        ).set_color(self.phase_color)
        general_eulers_formula[0][5].set_color(PURPLE)
        VGroup(
            general_eulers_formula[3],
            general_eulers_formula[8]
        ).set_color(self.y_color)
        new_sin_label = TexMobject(
            "A", "sin(", "\\omega", "t", "+", "\\phi", ")",
            tex_to_color_map={
                "A": self.amplitude_color,
                "sin(": self.y_color,
                "\\omega": self.ang_freq_color,
                "\\phi": self.phase_color,
                ")": self.y_color
            }
        ) \
            .next_to(self.sin_axes.y_axis.get_top() + 0.4 * DOWN, direction=RIGHT)
        self.time_label_t = TexMobject("time(t)", color=WHITE) \
            .next_to(self.sin_axes.x_axis.get_right(), direction=RIGHT)
        self.play(
            TransformFromCopy(
                cur_eulers_formula, general_eulers_formula
            ),
            Transform(
                self.sin_label, new_sin_label
            ),
            Transform(
                self.time_label1, self.time_label_t
            ),
            self.get_drawing_anims(4.96)
        )

        # indicate time axis label
        kw_arg = {
            "fill_color": YELLOW,
            "fill_opacity": 0.5
        }
        kw_theta_arg = {
            "fill_color": GREEN_D,
            "fill_opacity": 0.5,
            "stroke_color": GREEN_D
        }
        t_ax_rect = SurroundingRectangle(self.time_label_t, **kw_arg)
        t_gen_rects = VGroup(
            SurroundingRectangle(general_eulers_formula[0][8], **kw_arg),
            SurroundingRectangle(general_eulers_formula[-4], **kw_arg),
        )
        theta_rects = VGroup(
            SurroundingRectangle(eulers_formula[0][5], **kw_theta_arg),
            SurroundingRectangle(eulers_formula[-2], **kw_theta_arg),
        )
        self.play(
            ShowCreation(t_ax_rect),
            self.get_drawing_anims(2.35)
        )
        self.play(
            TransformFromCopy(
                t_ax_rect, t_gen_rects
            ),
            self.get_drawing_anims(1.43)
        )
        self.play(
            FadeIn(
                theta_rects
            ),
            self.get_drawing_anims(2)
        )
        self.play(
            FadeOut(t_ax_rect),
            FadeOut(t_gen_rects),
            FadeOut(theta_rects),
            self.get_drawing_anims(9.86)
        )

        # show rectangles around arguments
        arg_rects = VGroup(
            SurroundingRectangle(VGroup(*general_eulers_formula[0][7:11]), **kw_arg),
            SurroundingRectangle(VGroup(*general_eulers_formula[4:8]), **kw_arg),
            SurroundingRectangle(VGroup(*eulers_formula[0][5]), **kw_arg),
            SurroundingRectangle(eulers_formula[-2], **kw_arg),
        )
        self.play(
            FadeIn(arg_rects),
            self.get_drawing_anims(4.7)
        )

        # show argument formula
        argument_formula = TexMobject(
            "\"Argument\" = \\theta = \\omega", " t + \\phi",
            tex_to_color_map={
                "\"Argument\"": YELLOW,
                "\\theta": YELLOW,
                "\\omega": self.ang_freq_color,
                "\\phi": self.phase_color
            }
        )\
            .scale(2)\
            .next_to(general_eulers_formula, direction=DOWN, buff=0.3)\
            .shift(1.8*LEFT)
        theta_rect = SurroundingRectangle(
            VGroup(self.theta_value, self.theta_label),
            **kw_arg
        )
        self.play(
            Write(argument_formula),
            self.get_drawing_anims(3.22)
        )
        self.play(
            TransformFromCopy(arg_rects, theta_rect),
            self.get_drawing_anims(2)
        )

        # set angle to a multiple of 2*PI
        #   ** will not work when ang_freq != 1
        cur_ang = self.get_ang()
        del_ang = 2*PI*math.ceil(cur_ang/(2*PI))-cur_ang
        self.play(
            self.get_drawing_anims(del_ang+0.00001)
        )
        self.time_value.set_value(0)

        # remove argument rectangles
        self.play(
            FadeOut(arg_rects),
            FadeOut(theta_rect)
        )

        # focus on argument
        self.play(
            FadeOutAndShift(
                cur_eulers_formula, direction=UP
            ),
            ApplyMethod(
                general_eulers_formula.shift, 2*UP
            ),
            FadeOutAndShift(
                VGroup(*argument_formula[:2]), direction=UL
            ),
            ApplyMethod(
                VGroup(*argument_formula[2:]).shift, 2*LEFT + 2*UP
            ),
        )
        self.wait(2.61)

        # remove phase
        phase_mobs = VGroup(
            argument_formula[-1],
            argument_formula[-2][1],
            *general_eulers_formula[0][9:11],
            *general_eulers_formula[6:8]
        )
        self.play(
            ApplyMethod(
                phase_mobs.set_opacity, 0.15
            )
        )

        # add brace for time
        time_brace = Brace(
            argument_formula[5][0],
            direction=DOWN,
            buff=0.1
        )
        time_brace_width = time_brace.get_width()
        time_brace.set_width(1.1 * time_brace_width, stretch=True)
        time_text = time_brace.get_text("0") \
            .scale(1.75) \
            .shift(0.0 * DOWN)
        self.play(
            ShowCreation(time_brace),
        )
        self.wait(1.48)
        self.play(
            FadeInFrom(time_text, direction=DOWN),
        )

        # note that theta is equal to zero
        new_equals = TexMobject("=", color=YELLOW)\
            .scale(2) \
            .next_to(argument_formula[2], direction=LEFT, buff=0.3)
        theta_label2 = DecimalNumber(
            0,
            num_decimal_places=1,
            unit="\\pi",
            edge_to_fix=RIGHT,
            color=YELLOW
        )\
            .scale(2)\
            .next_to(new_equals, direction=LEFT, buff=0.3)
        self.play(
            FadeIn(theta_label2),
            FadeIn(new_equals),
        )
        self.wait(2.61)

        # label complete rotations
        multiples_two_pi = TexMobject(
            "\\text{cycle starts at} \\hspace{1.5mm} \\theta = ",
            *[str(2*i) + "\\pi " for i in range(10)],
            color=YELLOW,
        )
        multiples_two_pi.scale(2)
        multiples_two_pi.arrange(RIGHT, buff=1)\
            .to_edge(LEFT)\
            .shift(3.7*DOWN + 0.5*LEFT)
        self.play(
            FadeIn(multiples_two_pi[0])
        )
        self.play(
            TransformFromCopy(
                theta_label2, multiples_two_pi[1]
            )
        )

        # add updayer for second theta label
        theta_label2.add_updater(
            lambda x: x.set_value(self.get_ang() / PI)
        )

        self.play(
            FadeOut(time_brace),
            FadeOut(time_text),
        )

        # complete one rotation
        self.play(
            self.get_drawing_anims(2*PI)
        )
        self.wait(2.22)

        # copy 2 pi
        self.play(
            Transform(
                theta_label2.copy().clear_updaters(), multiples_two_pi[2]
            )
        )

        self.wait()

        for i in range(3, 5):
            # complete one rotation
            self.play(
                self.get_drawing_anims(2 * PI)
            )

            # copy 2*i*pi
            self.play(
                Transform(
                    theta_label2.copy().clear_updaters(), multiples_two_pi[i]
                )
            )

        # change frequency of wave
        self.play(
            self.get_freq_anim(2)
        )

        # # add T line
        # period_line = DashedLine(
        #     self.sin_axes.center_point + 2*PI*RIGHT + 1.2*UP,
        #     self.sin_axes.center_point + 2*PI*RIGHT + 1.2*DOWN,
        #     color=YELLOW
        # )
        # period_lhs = TexMobject(
        #     "T = ",
        #     color=YELLOW
        # )\
        #     .move_to(self.sin_axes.center_point + 2*PI*RIGHT + 0.65*RIGHT + 0.75*UP)
        # period_label = DecimalNumber(
        #     2*PI,
        #     color=YELLOW
        # )\
        #     .next_to(period_lhs, direction=RIGHT)
        # self.add(
        #     period_label,
        #     period_lhs,
        #     period_line
        # )
        # period_label.add_updater(
        #     lambda x: x.set_value((2*PI)/self.freq_value.get_value())
        # )
        #
        # self.play(
        #     self.get_drawing_anims(2*PI)
        # )

        self.wait()


    def get_drawing_anims(self, run_time=1.):
        anims = [
            ApplyMethod(
                self.time_value.increment_value, run_time*self.freq_value.get_value(),
                rate_func=linear,
                run_time=run_time
            ),
            UpdateFromFunc(
                self.dot, self.dot_update,
                rate_func=linear,
                run_time=run_time
            ),
            UpdateFromFunc(
                self.ang_line, self.ang_line_update,
                rate_func=linear,
                run_time=run_time
            ),
        ]

        if self.show_y_graph:
            anims += [
                UpdateFromFunc(
                    self.y_draw_line, self.y_draw_line_update,
                    rate_func=linear,
                    run_time=run_time
                ),
                UpdateFromFunc(
                    self.sin_dot, self.sin_dot_update,
                    rate_func=linear,
                    run_time=run_time
                )
            ]

        if self.show_x_graph:
            anims += [
                UpdateFromFunc(
                    self.x_draw_line, self.x_draw_line_update,
                    rate_func=linear,
                    run_time=run_time
                ),
                UpdateFromFunc(
                    self.cos_dot, self.cos_dot_update,
                    rate_func=linear,
                    run_time=run_time
                )
            ]

        return AnimationGroup(*anims)


    def ang_line_update(self, l):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        l.put_start_and_end_on(
            self.real_imag_axes.center_point,
            self.real_imag_axes.center_point + x * RIGHT + y * UP
        )

    def y_draw_line_update(self, l):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        l.put_start_and_end_on(
            self.real_imag_axes.center_point + x * RIGHT + y * UP,
            self.sin_axes.center_point + (self.time_value.get_value() % (2*PI))*RIGHT + y*UP
        )

    def x_draw_line_update(self, l):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        l.put_start_and_end_on(
            self.real_imag_axes.center_point + x * RIGHT + y * UP,
            self.cos_axes.center_point + (self.time_value.get_value() % (2*PI))*DOWN + x*RIGHT
        )

    def x_line_update(self, l):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        l.put_start_and_end_on(
            self.real_imag_axes.center_point + y * UP,
            self.real_imag_axes.center_point + x * RIGHT + y * UP
        )

    def y_line_update(self, l):
        x = self.ampl_value.get_value()*np.cos(self.get_ang())
        y = self.ampl_value.get_value()*np.sin(self.get_ang()) + 0.0000001
        l.put_start_and_end_on(
            self.real_imag_axes.center_point + x*RIGHT,
            self.real_imag_axes.center_point + x*RIGHT + y*UP
        )

    def dot_update(self, d):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        d.move_to(self.real_imag_axes.center_point +
                  x*RIGHT + y*UP )

    def sin_dot_update(self, d):
        y = self.ampl_value.get_value() * np.sin(self.get_ang()) + 0.0000001
        d.move_to(self.sin_axes.center_point + (self.time_value.get_value() % (2*PI))*RIGHT + y*UP)

    def cos_dot_update(self, d):
        x = self.ampl_value.get_value() * np.cos(self.get_ang())
        d.move_to(self.cos_axes.center_point + (self.time_value.get_value() % (2*PI))*DOWN + x*RIGHT)

    def get_ang(self):
        return self.phase_value.get_value() + self.time_value.get_value() * self.freq_value.get_value()

    def create_circle_mobs(self):
        self.phase_value = ValueTracker(0)
        self.freq_value = ValueTracker(1)
        self.ampl_value = ValueTracker(1)
        self.time_value = ValueTracker(0)

        # add real - imag axes
        self.real_imag_axes = Axes(**self.imag_axes_config)
        # manually adding tips to left and bottom
        self.real_imag_axes.x_axis.add_tip(at_start=True)
        self.real_imag_axes.y_axis.add_tip(at_start=True)
        # manually remove tick marks
        self.real_imag_axes.x_axis.big_tick_marks.set_opacity(0)
        self.real_imag_axes.y_axis.big_tick_marks.set_opacity(0)

        self.dot = Dot(color=YELLOW) \
            .move_to(self.real_imag_axes.center_point + RIGHT)
        # self.y_line = Line(color=self.y_color)
        # self.x_line = Line(color=self.x_color)

        self.circle = Circle(
            width=2,
            color=PINK,
            stroke_opacity=0.5
        )\
            .move_to(self.real_imag_axes.center_point)

        self.ang_line = Line(
            self.real_imag_axes.center_point,
            self.real_imag_axes.center_point + RIGHT,
            color=YELLOW
        )
        self.ang_arc = Arc(
            arc_center=self.real_imag_axes.center_point,
            radius=0.3,
            color=YELLOW
        )
        self.ang_arc.add_updater(
            lambda m: m.become(
                Arc(
                    radius=0.3,
                    start_angle=0,
                    arc_center=self.real_imag_axes.center_point,
                    angle=self.get_ang() % (2*PI),
                    color=YELLOW
                )
            )
        )

        imag_label = TexMobject(
            "Imag",
            color=self.y_color
        )\
            .scale(0.8)\
            .next_to(self.real_imag_axes.y_axis.get_top()+0.3*DOWN, direction=RIGHT)
        self.add(imag_label)

        real_label = TexMobject(
            "Real",
            color=self.x_color
        ) \
            .scale(0.8) \
            .next_to(self.real_imag_axes.x_axis.get_right(), direction=UP)\
            .shift(0.5*RIGHT)

        self.theta_label = TexMobject("\\theta = ", color=YELLOW) \
            .scale(0.9) \
            .move_to(self.real_imag_axes.center_point + 0.5*UP + 0.5*RIGHT)

        self.theta_value = DecimalNumber(
            0,
            num_decimal_places=1,
            unit="\\pi",
            edge_to_fix=LEFT,
            color=YELLOW
        )\
            .scale(0.9)\
            .next_to(self.theta_label, direction=RIGHT, buff=0.1)

        self.play(
            FadeIn(self.real_imag_axes),
            FadeIn(self.dot),
            FadeIn(self.circle),
            FadeIn(self.ang_line),
            FadeIn(self.ang_arc),
            FadeIn(imag_label),
            FadeIn(real_label),
            FadeIn(self.theta_label),
            FadeIn(self.theta_value)
        )
        self.theta_value.add_updater(
            lambda x: x.set_value((self.get_ang()/PI)%2)
        )

    def setup_cos_mobs(self):
        # add cos axes
        self.cos_axes = Axes(**self.cos_axes_config)
        self.cos_axes.y_axis.add_tip(at_start=True)
        self.cos_axes.y_axis.big_tick_marks.set_opacity(0)
        self.cos_axes.y_axis.tick_marks.set_opacity(0)
        self.cos_axes.rotate(-PI / 2, about_point=self.cos_axes.center_point)

        self.time_label2 = TexMobject("\\theta", color=YELLOW) \
            .next_to(self.cos_axes.x_axis.get_bottom() + 2.25 * UP, direction=LEFT)
        self.add()

        self.cos_label = TexMobject(
            "cos(", "\\theta", ")",
            color=self.x_color,
            tex_to_color_map={
                "\\theta": YELLOW
            }
        ) \
            .next_to(self.cos_axes.y_axis.get_right(), direction=DOWN, buff=0.2)

        self.cos_dot = Dot(color=YELLOW)\
            .move_to(self.cos_axes.center_point + RIGHT)

        self.x_draw_line = DashedLine(
            self.real_imag_axes.center_point + RIGHT,
            self.cos_axes.center_point + RIGHT,
            color=self.x_color,
            stroke_opacity=0.6
        )

        self.play(
            FadeIn(self.cos_axes),
            FadeIn(self.time_label2),
            FadeIn(self.cos_label),
            FadeIn(self.cos_dot),
            FadeIn(self.x_draw_line)
        )

    def setup_sine_mobs(self):
        self.sin_axes = Axes(**self.sin_axes_config)
        self.sin_axes.y_axis.add_tip(at_start=True)
        self.sin_axes.y_axis.big_tick_marks.set_opacity(0)
        self.sin_axes.y_axis.tick_marks.set_opacity(0)

        self.sin_label = TexMobject(
            "sin(", "\\theta", ")",
            color=self.y_color,
            tex_to_color_map={
                "\\theta": YELLOW
            }
        ) \
            .next_to(self.sin_axes.y_axis.get_top() + 0.4 * DOWN, direction=RIGHT)

        self.time_label1 = TexMobject("\\theta", color=YELLOW) \
            .next_to(self.sin_axes.x_axis.get_right(), direction=RIGHT)

        self.sin_dot = Dot(color=YELLOW)\
            .move_to(self.sin_axes.center_point)

        self.y_draw_line = DashedLine(
            self.real_imag_axes.center_point + RIGHT,
            self.sin_axes.center_point,
            color=self.y_color,
            stroke_opacity=0.6
        )

        self.play(
            FadeIn(self.sin_axes),
            FadeIn(self.sin_label),
            FadeIn(self.time_label1),
            FadeIn(self.sin_dot),
            FadeIn(self.y_draw_line)
        )

    def get_freq_anim(self, new_freq, run_time=1.):
        cur_freq = self.freq_value.get_value()
        # transform_matrix = np.array(
        #     [[cur_freq/new_freq, 0, 0],
        #      [0,                 1, 0],
        #      [0,                 0, 1]]
        # )
        # offset = np.array(
        #     [(1-cur_freq/new_freq)*self.sin_axes.center_point[0],
        #      0,
        #      0]
        # )
        # def fun(p):
        #     return offset + transform_matrix.dot(p)

        new_graph = self.sin_axes.get_graph(
            lambda x: self.ampl_value.get_value()*np.sin(x*self.freq_value.get_value()+self.phase_value.get_value()),
            color=self.y_color,
            x_min=0,
            x_max=2 * PI
        )

        return AnimationGroup(
            Transform(
                self.sin_graph, new_graph,
                run_time=run_time
            ),
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
