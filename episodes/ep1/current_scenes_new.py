from manimlib.imports import *
from accalib.particles import Electron, Proton, Neutron
from accalib.electrical_circuits import BatteryLampCircuit, BatteryLampCircuitAC
from functools import partial

class IntroCurrentPart(Scene):
    def construct(self):
        section_label = TextMobject(
            "Part 2: \\\\",
            "Current", " - AC vs DC"
        ).scale(1.5)
        self.play(
            Write(section_label[0]),
        )
        self.wait()
        self.play(
            Write(section_label[1])
        )
        self.wait()
        self.play(
            Write(section_label[2])
        )
        self.wait()

class IntroduceACDC(Scene):
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
        self.play(
            ShowCreation(dividing_line)
        )
        self.wait(1.43)

        # dc title
        dc_title = TextMobject("Direct Current", "(DC)")\
            .scale(1.25)
        dc_title.move_to(
            FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.5 * UP + dc_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        dc_underline = Line(LEFT, RIGHT) \
            .match_width(dc_title) \
            .scale(1) \
            .next_to(dc_title, DOWN, SMALL_BUFF)
        self.play(
            Write(dc_title[0])
        )
        self.wait(0.13)
        self.play(
            Write(dc_title[1]),
            ShowCreation(dc_underline)
        )
        self.wait(0.63)

        # ac title
        ac_title = TextMobject("Alternating Current", "(AC)")\
            .scale(1.25)
        ac_title.move_to(
            FRAME_WIDTH * 0.25 * RIGHT + FRAME_HEIGHT * 0.5 * UP + ac_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        ac_underline = Line(LEFT, RIGHT) \
            .match_width(ac_title) \
            .scale(1) \
            .next_to(ac_title, DOWN, SMALL_BUFF)
        self.play(
            Write(ac_title[0], run_time=1)
        )
        self.play(
            Write(ac_title[1]),
            ShowCreation(ac_underline)
        )
        self.wait(5.97)

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

        # current questions
        different_q = TextMobject(
            "How are they different?",
            color=YELLOW
        )\
            .scale(1.5)\
            .to_edge(DOWN, buff=0.5)
        current_q = TextMobject(
            "Current?",
            color=YELLOW
        )\
            .scale(1.5)\
            .next_to(different_q, direction=UP, buff=0.5)
        bg_rect = SurroundingRectangle(
            VGroup(different_q, current_q)
        )\
            .set_fill(color=BLACK, opacity=1)\
            .set_stroke(color=BLUE, opacity=0)
        self.add(bg_rect)
        self.play(
            Write(current_q)
        )
        self.play(
            Write(different_q)
        )

        self.wait(5.47)


class SimpleCircuit(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "electron_freq_0": 0.11,
        "electron_freq_1": 0.5
    }
    def construct(self):
        # add circuit
        circuit = BatteryLampCircuit(
            electron_freq=self.electron_freq_0
        )\
            .shift(UP)
        self.add(circuit)

        # label elements
        elements_label = VGroup()
        elements_label.add(
            SurroundingRectangle(
                circuit.outer_rect
            ),
            SurroundingRectangle(
                VGroup(
                    circuit.base_big,
                    circuit.base_small,
                    circuit.light_bulb
                )
            )
        )

        self.wait(3.19)
        self.play(
            AnimationGroup(
                *[
                    Write(mob, run_time=1.36)
                    for mob in elements_label
                ],
                lag_ratio=1
            )
        )
        self.play(
            FadeOut(elements_label, run_time=0.91),
        )
        self.wait(0.37)

        # remove battery
        circuit.set_light_bulb_state(False)
        self.play(
            FadeOutAndShift(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
        )
        self.wait(4.47)

        # add battery
        circuit.set_light_bulb_state(True)
        self.play(
            FadeInFrom(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
        )

        # add electrons
        circuit.setup_electrons()
        self.add(*circuit.electrons)
        self.add(circuit.battery, circuit.block_rect, circuit.base_big, circuit.base_small)
        self.play(
            circuit.get_electron_anim(run_time=3.94)
        )

        arrow = CurvedArrow(
            circuit.outer_rect.get_bottom() + 1.0 * RIGHT + 0 * DOWN,
            circuit.outer_rect.get_top() + 1.0 * RIGHT + 0 * UP,
            color=GREEN,
            angle=np.pi * 0.8
        )
        self.play(
            ShowCreationThenFadeOut(
                arrow,
                run_time=4.83
            ),
            circuit.get_electron_anim(4.83)
        )
        self.play(
            circuit.get_electron_anim(2.73)
        )

        # fade in current label
        point1 = circuit.electron_vect_inter.interpolate(0.55)
        point2 = circuit.electron_vect_inter.interpolate(0.5)
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
            .shift(0.5 * RIGHT) \
            .scale(1.5)
        current_value = DecimalNumber(
            2,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        ) \
            .scale(1.5) \
            .next_to(current_text, direction=RIGHT, buff=0.3)
        current_tracker = ValueTracker(2)
        current_value.add_updater(
            lambda x:
            x.set_value(current_tracker.get_value())
        )
        self.play(
            FadeInFrom(current_arrow, direction=UP),
            FadeInFrom(current_text, direction=UP),
            circuit.get_electron_anim()
        )
        self.play(
            circuit.get_electron_anim(run_time=1.14)
        )
        self.play(
            FadeInFrom(current_value, direction=UP),
            circuit.get_electron_anim()
        )
        self.play(
            circuit.get_electron_anim(8.95)
        )

        # remove battery
        circuit.electrons_flowing = False
        circuit.set_light_bulb_state(False)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons + circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(0)
        # stop electrons
        circuit.set_electron_freq(0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 0,
                run_time=1
            ),
            FadeOutAndShift(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            circuit.get_electron_anim(
                run_time=3
            )
        )
        self.play(
            circuit.get_electron_anim(13.35)
        )

        # label no constant flow
        no_flow_text = TexMobject(
            "\\text{No Constant Flow}", "\\Rightarrow", "\\text{No Power Transmitted}"
        )\
            .scale(1.5)\
            .to_edge(DOWN, buff=1)
        self.play(
            Write(no_flow_text[0]),
            circuit.get_electron_anim(4.13)
        )
        self.play(
            Write(VGroup(*no_flow_text[1:])),
            circuit.get_electron_anim(6.29)
        )

        circuit.electrons_flowing = True
        circuit.set_light_bulb_state(True)
        circuit.set_electron_freq(self.electron_freq_0)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons +
                   circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(1)
                circuit.electrons[i].set_stroke(BLUE, opacity=0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 2,
                run_time=1
            ),
            FadeInFrom(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            FadeOut(no_flow_text),
            circuit.get_electron_anim(15.62)
        )

        # show definition
        definition = TextMobject(
            "current - measure of ", "electrons", " per second passing through a circuit",
            color=YELLOW
        ) \
            .scale(1) \
            .to_corner(DOWN)
        self.play(
            Write(
                definition,
                run_time=2
            ),
            circuit.get_electron_anim(run_time=6.35)
        )

        # add question mark next to Amp
        not_eps = TextMobject(
            "???",
            color="#FF0000"
        )\
            .scale(1.75)\
            .next_to(current_value, direction=DR, buff=0.5)\
            .shift(0.2*RIGHT)
        arrow_not_eps = CurvedArrow(
            start_point=not_eps.get_edge_center(UP) + 0.25*UP + 0.25*RIGHT,
            end_point=current_value.get_right() + 0.4*RIGHT,
            color="#FF0000"
        )
        self.play(
            AnimationGroup(
                FadeInFrom(not_eps, direction=RIGHT),
                ShowCreation(arrow_not_eps),
                lag_ratio=1
            ),
            circuit.get_electron_anim(6.42)
        )

        # increase current to 40 Amps
        self.play(
            ApplyMethod(
                current_tracker.increment_value,
                38,
                run_time=2,
                rate_func=linear
            ),
            circuit.get_electron_acceleration_anim(
                self.electron_freq_1,
                run_time=2
            )
        )
        self.play(
            circuit.get_electron_anim(1.13)
        )

        # fadeout definition
        self.play(
            circuit.get_electron_anim(),
            FadeOut(definition),
            FadeOut(not_eps),
            FadeOut(arrow_not_eps)
        )

        # reduce current to 1 Amps
        self.play(
            ApplyMethod(
                current_tracker.set_value,
                1,
                run_time=1,
                rate_func=linear
            ),
            circuit.get_electron_acceleration_anim(
                self.electron_freq_0/2,
                run_time=1
            )
        )

        # label equivalent electrons per second
        elec_per_sec = DecimalNumber(
            6246000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(1.5) \
            .to_edge(DOWN, buff=1.7)
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
            FadeInFrom(
                elec_per_sec,
                direction=DOWN
            ),
            FadeInFrom(
                elec_per_sec_unit,
                direction=DOWN
            ),
            circuit.get_electron_anim(5.89)
        )

        # increase to 2 amps
        def digit_exp_decay(alpha, start):
            return exponential_decay(alpha, half_life=np.log10(2)/np.floor(np.log10(start)))
        self.play(
            circuit.get_electron_acceleration_anim(
                self.electron_freq_0,
                run_time=2
            ),
            ApplyMethod(
                current_tracker.set_value,
                2,
                run_time=2,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 12492000000000000,
                run_time=2,
                # will not work for any great half life values
                rate_func=partial(exponential_decay, half_life=0.025)
            )
        )
        self.play(
            circuit.get_electron_anim(10.16)
        )

        # increase to 40 amps
        self.play(
            circuit.get_electron_acceleration_anim(
                self.electron_freq_0*20,
                run_time=2
            ),
            ApplyMethod(
                current_tracker.set_value,
                40,
                run_time=2,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 249840000000000000,
                run_time=2,
                # will not work for any great half life values
                rate_func=partial(exponential_decay, half_life=0.025)
            )
        )
        self.play(
            circuit.get_electron_anim(10.17)
        )

        # remove battery
        circuit.electrons_flowing = False
        circuit.set_light_bulb_state(False)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons + circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(0)
        # stop electrons
        circuit.set_electron_freq(0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 0,
                run_time=1
            ),
            FadeOutAndShift(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 0,
                run_time=2,
                # will not work for any great half life values
                rate_func=partial(digit_exp_decay, start=249840000000000000)
            ),
            circuit.get_electron_anim(3),
        )
        self.play(
            circuit.get_electron_anim(6.78)
        )

        circuit.electrons_flowing = True
        circuit.set_light_bulb_state(True)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons +
                   circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(1)
                circuit.electrons[i].set_stroke(BLUE, opacity=0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 2,
                run_time=1
            ),
            FadeInFrom(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 12492000000000000,
                run_time=2,
                # will not work for any great half life values
                rate_func=rush_into
            ),
            circuit.get_electron_anim(3)
        )

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
        # fade in dc circuit
        dc_circuit = BatteryLampCircuit(
            electron_freq=self.electron_freq_0
        )\
            .scale(self.circuit_scale)\
            .to_corner(UL, buff=0)\
            .shift(2.5 * DOWN+0.2*RIGHT)
        dc_circuit.setup_electrons()
        block_rect = Rectangle(
            fill_opacity=1,
            fill_color=BLACK,
            stroke_opacity=0
        )\
            .match_width(dc_circuit)\
            .match_height(dc_circuit)\
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
        self.add(dc_circuit, current_arrow, current_text, block_rect)
        self.play(
            FadeOut(block_rect),
            dc_circuit.get_electron_anim(2)
        )
        self.play(
            FadeInFrom(current_value, direction=UP),
            dc_circuit.get_electron_anim(2)
        )

        # label equivalent electrons per second
        elec_per_sec = DecimalNumber(
            6246000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(self.eps_scale)\
            .to_corner(DL)\
            .shift(0.3*LEFT)
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
            FadeInFrom(
                elec_per_sec,
                direction=DOWN
            ),
            FadeInFrom(
                elec_per_sec_unit,
                direction=DOWN
            ),
            dc_circuit.get_electron_anim(2)
        )

        # add dividing line
        dividing_line = DashedLine(
            start=FRAME_HEIGHT * 0.5 * DOWN,
            end=FRAME_HEIGHT * 0.5 * UP,
            dash_length=0.25
        )
        self.play(
            ShowCreation(dividing_line),
            dc_circuit.get_electron_anim()
        )

        # fade in dc circuit
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
            .shift(0.5*LEFT) \
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
        self.play(
            FadeOut(block_rect_ac),
            ApplyMethod(
                phase_tracker_ac.increment_value,
                4*self.ac_electron_freq,
                run_time=4,
                rate_func=linear
            ),
            ac_circuit.get_electron_anim(4),
            dc_circuit.get_electron_anim(4)
        )

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
            lambda x: x.set_value(6246000000000000*np.sin(phase_tracker_ac.get_value()))
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
        )\
            .move_to(VGroup(elec_per_sec_ac, elec_per_sec_unit_ac).get_center())
        self.add(elec_per_sec_ac, elec_per_sec_unit_ac, block_rect_2)
        self.play(
            FadeOut(block_rect_2),
            ac_circuit.get_electron_anim(2),
            dc_circuit.get_electron_anim(2),
            ApplyMethod(
                phase_tracker_ac.increment_value,
                2 * self.ac_electron_freq,
                run_time=2,
                rate_func=linear
            ),
        )

        # dc title
        dc_title = TextMobject("Direct Current", "(DC)") \
            .scale(1.25)
        dc_title.move_to(
            FRAME_WIDTH * 0.25 * LEFT + FRAME_HEIGHT * 0.5 * UP + dc_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        dc_underline = Line(LEFT, RIGHT) \
            .match_width(dc_title) \
            .scale(1) \
            .next_to(dc_title, DOWN, SMALL_BUFF)
        self.play(
            Write(dc_title[0]),
            ac_circuit.get_electron_anim(2),
            dc_circuit.get_electron_anim(2),
            ApplyMethod(
                phase_tracker_ac.increment_value,
                2 * self.ac_electron_freq,
                run_time=2,
                rate_func=linear
            ),
        )
        self.play(
            Write(dc_title[1]),
            ShowCreation(dc_underline),
            ac_circuit.get_electron_anim(2),
            dc_circuit.get_electron_anim(2),
            ApplyMethod(
                phase_tracker_ac.increment_value,
                2 * self.ac_electron_freq,
                run_time=2,
                rate_func=linear
            ),
        )
        
        # ac title
        ac_title = TextMobject("Alternating Current", "(AC)") \
            .scale(1.25)
        ac_title.move_to(
            FRAME_WIDTH * 0.25 * RIGHT + FRAME_HEIGHT * 0.5 * UP + ac_title.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        ac_underline = Line(LEFT, RIGHT) \
            .match_width(ac_title) \
            .scale(1) \
            .next_to(ac_title, DOWN, SMALL_BUFF)
        self.play(
            Write(ac_title[0], run_time=1)
        )
        self.play(
            Write(ac_title[1]),
            ShowCreation(ac_underline)
        )
        self.wait(5.97)
