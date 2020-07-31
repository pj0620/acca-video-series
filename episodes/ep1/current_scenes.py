from manimlib.imports import *
from accalib.particles import Electron, Proton, Neutron
from accalib.electrical_circuits import BatteryLampCircuit
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
        self.wait(1.83)

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
        self.wait(1.1)

        # outlet
        outlet = ImageMobject(
            "images\ep1\IntroduceACDC\outlet-US.jpg"
        ) \
            .scale(2)\
            .next_to(power_line, direction=LEFT, buff=0.5)
        self.play(
            FadeIn(outlet)
        )
        self.wait(0.26)

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

class IntroCharge(Scene):
    def construct(self):
        title = Title(
            "Charge",
            scale_factor=1.5
        )
        self.play(Write(title))
        self.wait(4.63)

        electron = Electron()\
            .scale(0.75)\
            .to_edge(UP, buff=2.75)
        e_title = TextMobject("\\underline{Electron}", color=RED)\
            .scale(1.2)\
            .next_to(electron, direction=UP, buff=0.3)
        self.play(
            SpinInFromNothing(electron),
            Write(e_title)
        )

        proton = Proton()\
            .scale(0.75)\
            .next_to(electron, direction=LEFT, buff=3)
        p_title = TextMobject("\\underline{Proton}", color="#3fb5de") \
            .scale(1.2)\
            .next_to(proton, direction=UP, buff=0.3)
        self.play(
            SpinInFromNothing(proton),
            Write(p_title)
        )

        neutron = Neutron()\
            .scale(0.75)\
            .next_to(electron, direction=RIGHT, buff=3)
        n_title = TextMobject("\\underline{Neutron}", color=GREY) \
            .scale(1.2)\
            .next_to(neutron, direction=UP, buff=0.3)
        self.play(
            SpinInFromNothing(neutron),
            Write(n_title)
        )

        # expand each particle
        part_scale_factor = 1.5
        for part in (electron, proton, neutron):
            self.play(
                ApplyMethod(
                    part.scale,
                    part_scale_factor
                )
            )
            self.play(
                ApplyMethod(
                    part.scale,
                    1/part_scale_factor
                )
            )
        self.wait(6.66)


        # tiny particle params
        tiny_scale = 0.4
        tiny_buff_x = 1.6
        tiny_buff_y = 0.75
        title_buff = 0.7
        tiny_title_scale = 1.1
        arrow_mag = 1.1
        arrow_kw = {
            "buff": 0,
            "stroke_width": 10,
            "color": YELLOW
        }

        # like charges repel
        e11r = Electron().scale(tiny_scale)\
            .to_corner(DL, buff=1)\
            .shift(1*RIGHT+0.5*DOWN)
        e12r = Electron().scale(tiny_scale)\
            .next_to(e11r, direction=RIGHT, buff=tiny_buff_x)
        p21r = Proton().scale(tiny_scale)\
            .next_to(e11r, direction=UP, buff=tiny_buff_y)
        p22r = Proton().scale(tiny_scale) \
            .next_to(e12r, direction=UP, buff=tiny_buff_y)
        rarrows = VGroup(
            Arrow(start=e11r.get_center(), end=e11r.get_center()+arrow_mag*LEFT, **arrow_kw),
            Arrow(start=e12r.get_center(), end=e12r.get_center()+arrow_mag*RIGHT, **arrow_kw),
            Arrow(start=p21r.get_center(), end=p21r.get_center() + arrow_mag * LEFT, **arrow_kw),
            Arrow(start=p22r.get_center(), end=p22r.get_center() + arrow_mag * RIGHT, **arrow_kw)
        )
        rtitle = TextMobject(
            "\\underline{Likes Repel}",
            color=YELLOW
        )\
            .scale(tiny_title_scale)\
            .next_to(VGroup(p21r, p22r), direction=UP, buff=title_buff)
        self.play(
            FadeIn(VGroup(rarrows, rtitle, p21r, p22r, e11r, e12r))
        )
        self.wait(0.57)

        # opposite charges attract
        p1a = Proton().scale(tiny_scale)
        p2a = Electron().scale(tiny_scale)\
            .next_to(p1a, direction=RIGHT, buff=tiny_buff_x)
        VGroup(p1a, p2a).center()
        VGroup(p1a, p2a).match_y(p21r)
        atitle = TextMobject(
            "\\underline{Unlike Attract}",
            color=YELLOW
        ) \
            .scale(tiny_title_scale) \
            .next_to(VGroup(p1a, p2a), direction=UP, buff=title_buff)
        aarrows = VGroup(
            Arrow(start=p1a.get_center(), end=p1a.get_center() + arrow_mag * RIGHT, **arrow_kw),
            Arrow(start=p2a.get_center(), end=p2a.get_center() + arrow_mag * LEFT, **arrow_kw),
        )
        self.play(
            FadeIn(VGroup(aarrows, p1a, p2a, atitle))
        )
        self.wait(3.43)

        # neutrons unaffected
        n1 = Neutron().scale(tiny_scale)
        p5 = Proton().scale(tiny_scale)\
            .next_to(n1, direction=RIGHT, buff=tiny_buff_x)
        VGroup(n1, p5).match_y(p21r)
        VGroup(n1, p5).match_x(VGroup(p21r, p22r))
        VGroup(n1, p5).shift(-2*RIGHT*VGroup(n1, p5).get_x())
        n2 = Neutron().scale(tiny_scale)
        e5 = Electron().scale(tiny_scale)\
            .next_to(n2, direction=RIGHT, buff=tiny_buff_x)
        VGroup(n2, e5).next_to(VGroup(n1, p5), direction=DOWN, buff=tiny_buff_y)
        un_title = TextMobject(
            "\\underline{Unaffected}",
            color=YELLOW
        ) \
            .scale(tiny_title_scale) \
            .next_to(VGroup(n1, p5), direction=UP, buff=title_buff)
        self.play(
            FadeIn(VGroup(n1, p5, n2, e5, un_title))
        )

        self.wait(8.53)

class ElementaryCharge(Scene):
    CONFIG = {
        "elementary_charge_color": GREEN
    }

    def construct(self):
        electron = Electron().scale(0.5)
        proton = Proton().scale(0.5)
        eq_mid = TexMobject(
            "=", "-",
            color=WHITE
        )\
            .scale(2)
        eq_mid[1].shift(0.1*RIGHT)
        eq1 = VGroup(
            electron, eq_mid, proton
        )\
            .arrange(RIGHT, buff=0.25)\
            .to_edge(UP)

        self.play(
            AnimationGroup(
                *[
                    FadeIn(mob, run_time=2)
                    for mob in (electron, proton, eq_mid)
                ],
                lag_ratio=1
            )
        )
        self.wait(3.83)

        # transform equations
        eq2 = TexMobject(
            "-", "1.602 \\times 10^{-19} C", "=", "-", "1.602 \\times 10^{-19} C",
            tex_to_color_map={"1.602 \\times 10^{-19} C": self.elementary_charge_color}
        )\
            .scale(1.5)\
            .next_to(eq1, direction=DOWN, buff=1)
        self.play(
            TransformFromCopy(
                eq1[0], VGroup(eq2[0:2])
            )
        )
        self.wait(7.13)
        self.play(
            TransformFromCopy(
                eq1[2], eq2[4]
            )
        )
        self.wait(6.76)
        self.play(
            TransformFromCopy(
                eq_mid, VGroup(eq2[2:4])
            )
        )
        self.wait(3.7)

        # elementary charge label
        ec_text = TexMobject(
            "q_e", "=", "\\text{elementary charge}", "=", "1.602 \\times 10^{-19} C",
            tex_to_color_map={
                "1.602 \\times 10^{-19} C": self.elementary_charge_color,
                "q_e": self.elementary_charge_color,
                "\\text{elementary charge}": self.elementary_charge_color
            }
        ) \
            .scale(1.5)\
            .next_to(eq2, direction=DOWN, buff=1)
        self.play(
            TransformFromCopy(eq2[4], ec_text[4])
        )
        self.wait(4.96)
        self.play(
            FadeIn(VGroup(ec_text[2:4]))
        )
        self.wait(2.27)
        self.play(
            FadeIn(VGroup(ec_text[0:2]))
        )

        # relabel using elementary charge
        electron2 = Electron().scale(0.5)\
            .next_to(ec_text, direction=DOWN, buff=1, aligned_edge=LEFT)
        electron_eq = TexMobject(
            "= -", "q_e",
            tex_to_color_map={"q_e": self.elementary_charge_color}
        )\
            .scale(1.5)\
            .next_to(electron2, RIGHT, buff=0.25)
        proton2 = Proton().scale(0.5) \
            .next_to(electron2, direction=DOWN, buff=1)
        proton_eq = TexMobject(
            "= ", "q_e",
            tex_to_color_map={"q_e": self.elementary_charge_color}
        ) \
            .scale(1.5) \
            .next_to(proton2, RIGHT, buff=0.25)
        neutron2 = Neutron().scale(0.5) \
            .next_to(electron2, direction=RIGHT, buff=4)
        neutron_eq = TexMobject(
            "= ", "0",
        ) \
            .scale(1.5) \
            .next_to(neutron2, RIGHT, buff=0.25)
        VGroup(electron2, electron_eq, proton2, proton_eq, neutron2, neutron_eq).set_x(0)
        rect = SurroundingRectangle(
            VGroup(electron2, electron_eq, proton2, proton_eq, neutron2, neutron_eq),
            buff=0.4
        )

        self.wait(2.97)
        self.play(
            Write(rect)
        )
        self.play(
            FadeIn(electron2),
            Write(electron_eq)
        )
        self.play(
            FadeIn(proton2),
            Write(proton_eq)
        )
        self.wait(7.63)
        self.play(
            FadeIn(neutron2),
            Write(neutron_eq)
        )
        self.wait(4.16)

        question = TextMobject(
            "What does this have to do with Current?",
            color=YELLOW
        ) \
            .scale(1.5) \
            .to_edge(DOWN, buff=0.5)
        q_rect = SurroundingRectangle(
            question
        ) \
            .set_fill(color=BLACK, opacity=1) \
            .set_stroke(color=BLUE, opacity=0) \
            .scale(1.5)
        self.play(
            FadeIn(q_rect),
            Write(question)
        )

        self.wait(2)

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
        self.circuit = BatteryLampCircuit()\
            .shift(UP)
        self.add(self.circuit)

        # label elements
        elements_label = VGroup()
        elements_label.add(
            SurroundingRectangle(
                self.circuit.outer_rect
            ),
            SurroundingRectangle(
                VGroup(
                    self.circuit.base_big,
                    self.circuit.base_small,
                    self.circuit.light_bulb
                )
            )
        )

        self.wait(3.27)
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
        self.circuit.set_light_bulb_state(False)
        self.play(
            FadeOutAndShift(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
        )
        self.wait(4.47)

        # add battery
        self.circuit.set_light_bulb_state(True)
        self.play(
            FadeInFrom(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
        )

        # add electrons
        self.circuit.setup_electrons()
        self.add(*self.circuit.electrons)
        self.add(self.circuit.battery, self.circuit.block_rect, self.circuit.base_big, self.circuit.base_small)
        self.play(
            self.get_electron_anim(run_time=4.17)
        )

        arrow = CurvedArrow(
            self.circuit.outer_rect.get_bottom() + 1.0 * RIGHT + 0 * DOWN,
            self.circuit.outer_rect.get_top() + 1.0 * RIGHT + 0 * UP,
            color=GREEN,
            angle=np.pi * 0.8
        )
        self.play(
            ShowCreationThenFadeOut(
                arrow,
                run_time=4.83
            ),
            self.get_electron_anim(
                run_time=4.83
            )
        )
        self.play(
            self.get_electron_anim(4.83)
        )

        # add current label
        # fade in current label
        point1 = self.circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.circuit.electron_vect_inter.interpolate(0.5)
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
            self.get_electron_anim()
        )
        self.play(
            self.get_electron_anim(run_time=1.87)
        )
        self.play(
            FadeInFrom(current_value, direction=UP),
            self.get_electron_anim()
        )
        self.play(
            self.get_electron_anim(run_time=2.64)
        )

        self.circuit.electrons_flowing = False
        self.circuit.set_light_bulb_state(False)
        for i in range(len(self.circuit.electrons)):
            cur = (self.circuit.electron_loc.get_value() + i / self.circuit.num_of_electrons + self.circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                self.circuit.electrons[i].set_opacity(0)

        self.play(
            ApplyMethod(
                current_tracker.set_value, 0,
                run_time=1
            ),
            FadeOutAndShift(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            self.get_electron_anim(
                freq=0,
                run_time=3
            )
        )
        self.play(
            self.get_electron_anim(
                freq=0,
                run_time=26.5
            )
        )

        self.circuit.electrons_flowing = True
        self.circuit.set_light_bulb_state(True)
        for i in range(len(self.circuit.electrons)):
            cur = (self.circuit.electron_loc.get_value() + i / self.circuit.num_of_electrons +
                   self.circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                self.circuit.electrons[i].set_opacity(0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 2,
                run_time=1
            ),
            FadeInFrom(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=16.06
            )
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
            self.get_electron_anim(run_time=11.7)
        )

        # replace with charge
        charge = TextMobject(
            "charge",
            color="#FF0000"
        )\
            .next_to(definition[1], direction=UP)
        cross_out = Line(
            start=definition[1].get_corner(DL) + 0.1*DL,
            end=definition[1].get_corner(UR) + 0.1*UR,
            stroke_width=5,
            color="#FF0000"
        )
        self.play(
            AnimationGroup(
                Write(cross_out),
                FadeInFrom(charge, direction=UP),
                lag_ratio=0.1
            ),
            self.get_electron_anim(7.5)
        )

        not_eps = TextMobject(
            "not electrons per second",
            color="#FF0000"
        )\
            .next_to(current_value, direction=DOWN, buff=0.5)
        arrow_not_eps = CurvedArrow(
            start_point=not_eps.get_corner(UR) + 0.25*UP,
            end_point=current_value.get_right() + 0.25*RIGHT,
            color="#FF0000"
        )
        self.play(
            AnimationGroup(
                FadeInFrom(not_eps, direction=RIGHT),
                ShowCreation(arrow_not_eps),
                lag_ratio=1
            ),
            self.get_electron_anim(16.03)
        )

        tau = 2
        f0 = self.electron_freq_0
        f1 = self.electron_freq_1
        my_rate_func = lambda t: ((f1 - f0) / (f1 + f0)) * (t ** 2) + ((2 * f0) / (f0 + f1)) * t
        self.play(
            ApplyMethod(
                current_tracker.increment_value,
                38,
                run_time=tau,
                rate_func=linear
            ),
            ApplyMethod(
                self.circuit.electron_loc.increment_value,
                ((f0+f1)/2)*tau,
                run_time=tau,
                rate_func=my_rate_func
            )
        )

        self.play(
            self.get_electron_anim(4.43, self.electron_freq_1)
        )

    def get_electron_anim(self, run_time=1., freq=0.11):
        return ApplyMethod(
            self.circuit.electron_loc.increment_value,
            run_time * freq,
            run_time=run_time,
            rate_func=linear
        )

class Amperes(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "charge_color": ORANGE,
        "second_color": RED_D,
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
    }
    def construct(self):
        title = Title(
            "Ampere",
            scale_factor=1.5
        )
        self.play(Write(title, run_time=1.22))

        short_text = TextMobject(
            "shortened to \"", "Amp", "\"", ", written as \"", "A", "\"",
            tex_to_color_map={
                "Amp": self.current_color,
            }
        )\
            .scale(1.1)\
            .next_to(title, direction=DOWN, buff=0.5)
        short_text[4].set_color(self.current_color)
        self.play(Write(VGroup(*short_text[0:3]), run_time=1.22))
        self.play(Write(VGroup(*short_text[3:]), run_time=1.22))
        self.wait(3.27)

        andre = ImageMobject(
            "images/ep1/Amperes/andre-marie-ampere.jpg"
        ) \
            .scale(3) \
            .shift(DOWN)
        text = TextMobject(
            "André-Marie Ampère"
        ) \
            .scale(1.25) \
            .next_to(andre, direction=DOWN)
        self.play(
            AnimationGroup(
                FadeIn(andre),
                Write(text),
                lag_ratio=0.01
            )
        )
        self.wait(3.07)
        self.play(
            FadeOut(andre),
            FadeOut(text)
        )

        # show Amp as fraction, and charge of electron
        eq_form = TexMobject(
            "1 ", "A", "=", "1",
            "{\\text{Coulomb}", "\\over", "\\text{second}}"
        )\
            .scale(1.15)\
            .next_to(short_text, direction=DOWN, buff=0.75)
        electron_eq = VGroup(
            Electron().scale(0.3),
            TexMobject(" = ", "-", "1.602 \\times 10^{-19}").scale(1.12),
            TexMobject("\\text{Coulomb}").scale(1.12)
        )\
            .arrange(RIGHT)\
            .next_to(eq_form, direction=DOWN, buff=0.5)
        VGroup(eq_form, electron_eq)\
            .arrange(RIGHT, buff=3)\
            .next_to(short_text, direction=DOWN, buff=0.75)
        electron_eq[0].shift(0.1*DOWN)
        electron_eq[-1].set_color(self.charge_color)
        eq_form[1].set_color(self.current_color)
        eq_form[4].set_color(self.charge_color)
        eq_form[6].set_color(self.second_color)
        self.play(
            Write(eq_form)
        )
        self.wait(7.1)
        self.play(
            FadeIn(electron_eq[0]),
            Write(electron_eq[1]),
            Write(electron_eq[2]),
        )
        self.wait(7.37)

        # label elementary charge
        qe_brace = Brace(VGroup(electron_eq[1][1:3]))
        qe_text = qe_brace.get_text("$q_e$")
        self.play(
            ShowCreation(qe_brace),
            Write(qe_text)
        )
        self.wait(6.1)

        self.play(
            # WiggleOutThenIn
            # FocusOn, Flash, CircleIndicate
            WiggleOutThenIn(electron_eq[1][1],
                            scale_value=2,
                            rotation_angle=0.1*TAU,
                            )
        )

        # add current direction displays
        line_neg = Line(end=4*RIGHT)\
            .to_corner(DL)\
            .shift(UP)
        self.electrons_neg = VGroup(
            *[
                Electron().scale(0.2).move_to(line_neg.get_end() + 2*LEFT*i)
                for i in range(1, 50)
            ]
        )
        block_kw = {
            "stroke_opacity": 0,
            "fill_color": BLACK,
            "fill_opacity": 1,
            "width": 15
        }
        block_rects_neg = VGroup(
            Rectangle(**block_kw).move_to(line_neg.get_start()+0.5*LEFT*block_kw["width"]),
            Rectangle(**block_kw).move_to(line_neg.get_end()+0.5*RIGHT*block_kw["width"]),
        )
        current_arrow_neg = ArrowTip(
            start_angle=PI,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(0.5*(line_neg.get_start() + line_neg.get_end()))
        self.play(
            FadeIn(line_neg),
            FadeIn(self.electrons_neg)
        )
        self.add(block_rects_neg)

        line_pos = Line(end=4 * RIGHT) \
            .next_to(line_neg, direction=UP, buff=2)
        self.electrons_pos = VGroup(
            *[
                Proton().scale(0.2).move_to(line_pos.get_end() + 2 * LEFT * i)
                for i in range(1, 50)
            ]
        )
        block_rects_pos = VGroup(
            Rectangle(**block_kw).move_to(line_pos.get_start() + 0.5 * LEFT * block_kw["width"]),
            Rectangle(**block_kw).move_to(line_pos.get_end() + 0.5 * RIGHT * block_kw["width"]),
        )
        current_arrow_pos = ArrowTip(
            start_angle=0,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(0.5 * (line_pos.get_start() + line_pos.get_end()))
        self.play(
            self.get_electron_wire_anim(13.6),
            FadeIn(current_arrow_neg),
        )
        self.play(
            FadeIn(line_pos),
            FadeIn(self.electrons_pos),
            self.get_electron_wire_anim(1)
        )
        self.add(block_rects_pos)
        self.play(
            self.get_electron_wire_anim(3),
            self.get_electron_pos_wire_anim(3),
            FadeIn(current_arrow_pos),
        )
        self.play(
            self.get_electron_wire_anim(3.86),
            self.get_electron_pos_wire_anim(3.86),
        )

        # copy amp fraction to bottom right
        eq_form_cp = eq_form.copy()
        self.play(
            ApplyMethod(
                eq_form_cp.move_to,
                line_pos.get_right() + 3*RIGHT
            ),
            self.get_electron_wire_anim(1),
            self.get_electron_pos_wire_anim(1),
        )
        self.play(
            self.get_electron_wire_anim(3.73),
            self.get_electron_pos_wire_anim(3.73),
        )

        # add multiply by 1 over qe
        conv_text = TexMobject(
            "{1",  "\\over ", "1.602 \\times 10^{-19}", "\\text{Coulomb}", "}",
            tex_to_color_map={
                "\\text{Coulomb}": self.charge_color
            }
        )\
            .scale(1.1)\
            .next_to(eq_form_cp, direction=RIGHT, buff=0.2)\
            .shift(0.05*DOWN)
        eq_electron = Electron().scale(0.3).move_to(conv_text[0])
        self.play(
            FadeIn(eq_electron),
            FadeIn(conv_text[1]),
            FadeIn(conv_text[3]),
            TransformFromCopy(
                electron_eq[1][2], conv_text[2]
            ),
            self.get_electron_wire_anim(1),
            self.get_electron_pos_wire_anim(1),
        )
        self.play(
            self.get_electron_wire_anim(2.47),
            self.get_electron_pos_wire_anim(2.47),
        )

        # cancel out Coulomb
        cross_out1 = self.get_cross_out(conv_text[3])
        cross_out2 = self.get_cross_out(eq_form_cp[4])
        self.play(
            Write(cross_out1),
            Write(cross_out2),
            self.get_electron_wire_anim(3),
            self.get_electron_pos_wire_anim(3),
        )

        final_text = TexMobject(
            "{1", "\\over ", "1.602 \\times 10^{-19}", "}",
        )\
            .next_to(eq_form_cp[2], direction=RIGHT)
        new_unit = TexMobject(
            "{1", "\\over ", "\\text{second}", "}",
            tex_to_color_map={"\\text{second}": self.second_color}
        )\
            .next_to(final_text, direction=RIGHT)
        self.play(
            # transform into final_text
            ReplacementTransform(
                eq_form_cp[3], final_text[0]
            ),
            ReplacementTransform(
                conv_text[2], final_text[2]
            ),
            FadeIn(final_text[1]),

            # remove parts that will be removed
            FadeOut(cross_out1),
            FadeOut(cross_out2),
            FadeOut(conv_text[3]),
            FadeOut(eq_form_cp[4]),
            FadeOut(eq_form_cp[5]),
            FadeOut(conv_text[1]),

            # transform into new_unit
            ReplacementTransform(
                eq_form_cp[6], new_unit[2]
            ),
            FadeIn(new_unit[1]),
            ApplyMethod(
                eq_electron.move_to,
                new_unit[0]
            ),

            self.get_electron_wire_anim(),
            self.get_electron_pos_wire_anim(),
        )
        self.play(
            self.get_electron_wire_anim(7.06),
            self.get_electron_pos_wire_anim(7.06),
        )

        # solve final_text
        final_calculated = TexMobject(
            "6,246,000,000,000,000,000"
        )\
            .next_to(eq_form_cp[2], direction=RIGHT)
        self.play(
            Transform(
                final_text, final_calculated
            ),
            ApplyMethod(
                VGroup(*new_unit[1:]).shift,
                3*RIGHT
            ),
            ApplyMethod(
                eq_electron.shift,
                3*RIGHT
            ),
            self.get_electron_wire_anim(),
            self.get_electron_pos_wire_anim(),
        )

        self.play(
            self.get_electron_wire_anim(15),
            self.get_electron_pos_wire_anim(15),
        )

    def get_electron_pos_wire_anim(self, run_time=1.):
        return ApplyMethod(
            self.electrons_pos.shift,
            2 * run_time * RIGHT,  # 2*run_time
            run_time=run_time,
            rate_func=linear
        )

    def get_electron_wire_anim(self, run_time=1.):
        return ApplyMethod(
            self.electrons_neg.shift,
            2 * run_time * RIGHT,
            run_time=run_time,
            rate_func=linear
        )

    def get_cross_out(self, mob):
        return Line(
            start=mob.get_corner(DL),
            end=mob.get_corner(UR),
            stroke_width=5,
            color="#FF0000"
        )


class BackToSimpleCircuit(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "electron_freq_0": 0.11,
        "electron_freq_1": 0.5
    }
    def construct(self):
        # add circuit
        self.circuit = BatteryLampCircuit(
            num_of_electrons=20
        )\
            .shift(UP)
        self.add(self.circuit)

        # add electrons
        self.circuit.setup_electrons()
        self.add(*self.circuit.electrons)
        self.add(self.circuit.battery, self.circuit.block_rect, self.circuit.base_big, self.circuit.base_small)
        self.play(
            self.get_electron_anim(run_time=4.17)
        )

        # fade in current label
        point1 = self.circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.circuit.electron_vect_inter.interpolate(0.5)
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
            *[
                FadeIn(mob)
                for mob in (current_arrow, current_text, current_value)
            ],
            self.get_electron_anim(2.93)
        )

        # label equivalent electrons per second
        elec_per_sec = DecimalNumber(
            124920000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(1.5) \
            .to_edge(DOWN, buff=1.7)
        elec_per_sec_tracker = ValueTracker(12492000000000000)
        elec_per_sec.add_updater(
            lambda x: x.set_value(elec_per_sec_tracker.get_value())
        )
        elec_per_sec_unit_tex = TexMobject(
            "{1", "\\over", "\\text{second}}"
        )\
            .scale(1.15)\
            .next_to(elec_per_sec, direction=RIGHT)
        elec_per_sec_unit_elec = Electron()\
            .scale(0.3)\
            .move_to(elec_per_sec_unit_tex[0])
        elec_per_sec_unit=VGroup(
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
            self.get_electron_anim(5.33)
        )

        self.circuit.electrons_flowing = False
        self.circuit.set_light_bulb_state(False)
        for i in range(len(self.circuit.electrons)):
            cur = (self.circuit.electron_loc.get_value() + i / self.circuit.num_of_electrons + self.circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                self.circuit.electrons[i].set_opacity(0)

        def digit_exp_decay(alpha, start):
            return exponential_decay(alpha, half_life=np.log10(2)/np.floor(np.log10(start)))

        # set value to zero
        self.play(
            ApplyMethod(
                current_tracker.set_value, 0,
                run_time=2,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 0,
                run_time=2,
                rate_func=partial(digit_exp_decay, start=12492000000000000)
            ),
            FadeOutAndShift(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            self.get_electron_anim(
                freq=0,
                run_time=16.17
            )
        )

        block_rect = Rectangle(
            stroke_opacity=0,
            fill_color=BLACK,
            fill_opacity=1,
            width=self.circuit.battery.get_width(),
            height=self.circuit.battery.get_height()
        )\
            .move_to(self.circuit.battery.get_center())
        self.add(
            block_rect
        )

        # set to 2 Amps
        self.circuit.electrons_flowing = True
        self.circuit.set_light_bulb_state(True)
        for i in range(len(self.circuit.electrons)):
            cur = (self.circuit.electron_loc.get_value() + i / self.circuit.num_of_electrons +
                   self.circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                self.circuit.electrons[i].set_opacity(1)
                self.circuit.electrons[i].set_stroke(BLACK, opacity=0)
        self.play(
            ApplyMethod(
                current_tracker.set_value, 2,
                run_time=2,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 12492000000000000,
                run_time=2,
                rate_func=partial(digit_exp_decay, start=1249200000000000)
            ),
            FadeInFrom(
                self.circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=4.07
            )
        )

        # set current  to 40 amps
        tau = 1
        f0 = self.electron_freq_0
        f1 = self.electron_freq_1
        my_rate_func = lambda t: ((f1 - f0) / (f1 + f0)) * (t ** 2) + ((2 * f0) / (f0 + f1)) * t
        self.play(
            ApplyMethod(
                current_tracker.increment_value,
                38,
                run_time=tau,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 249840000000000000000,
                run_time=tau,
                # rate_func=partial(digit_exp_decay, start=10)
            ),
            ApplyMethod(
                self.circuit.electron_loc.increment_value,
                ((f0+f1)/2)*tau,
                run_time=tau,
                rate_func=my_rate_func
            )
        )

        self.play(
            self.get_electron_anim(1.33, self.electron_freq_1)
        )

        # set current to 20 amps
        tau = 1
        f0 = self.electron_freq_1
        f1 = self.electron_freq_1/2
        my_rate_func = lambda t: ((f1 - f0) / (f1 + f0)) * (t ** 2) + ((2 * f0) / (f0 + f1)) * t
        self.play(
            ApplyMethod(
                current_tracker.increment_value,
                -20,
                run_time=tau,
                rate_func=linear
            ),
            ApplyMethod(
                elec_per_sec_tracker.set_value, 124920000000000000000,
                run_time=tau,
                # rate_func=partial(digit_exp_decay, start=10)
            ),
            ApplyMethod(
                self.circuit.electron_loc.increment_value,
                ((f0 + f1) / 2) * tau,
                run_time=tau,
                rate_func=my_rate_func
            )
        )
        self.play(
            self.get_electron_anim(3.13, self.electron_freq_1 / 2)
        )

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
            # .scale(1.5)
        self.play(
            FadeIn(q_rect),
            Write(question),
            self.get_electron_anim(3, self.electron_freq_1/2)
        )

        self.play(
            self.get_electron_anim(3.33, self.electron_freq_1/2)
        )

    def get_electron_anim(self, run_time=1., freq=0.11):
        return ApplyMethod(
            self.circuit.electron_loc.increment_value,
            run_time * freq,
            run_time=run_time,
            rate_func=linear
        )