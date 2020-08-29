from manimlib.imports import *
from accalib.electrical_circuits import *
from accalib.circuit_comps import *

class WhatIsCircuit(Scene):
    def construct(self):
        section_label = TextMobject(
            "Part 1: \\\\",
            "What Really is an Electric Circuit?"
        ).scale(1.5)
        self.play(
            Write(section_label[0]),
        )
        self.wait()
        self.play(
            Write(section_label[1])
        )
        self.wait()

class IntroduceCircuit(Scene):
    CONFIG={
        "circuit_color": BLUE_C
    }
    def construct(self):
        # show ACCA
        acca_text = TextMobject(
            "AC", "Circuit", "s",
            arg_separator=" ",
        )\
            .scale(2.5)\
            .to_edge(UP, buff=3)
        acca_text[1].center()
        acca_text[0].next_to(acca_text[1], direction=LEFT, buff=0.75)
        acca_text[2].next_to(acca_text[1], direction=RIGHT, buff=0.13, aligned_edge=DOWN)
        self.play(
            FadeInFrom(
                acca_text,
                direction=UP
            )
        )
        self.wait(5.2)

        # expand ACCA
        self.play(
            ApplyMethod(
                acca_text[0].shift,
                2 * LEFT
            ),
            ApplyMethod(
                acca_text[2].shift,
                2 * RIGHT
            ),
        )
        self.wait(0.506)

        # indicate Circuit
        brace_Circuit = Brace(acca_text[1], color=self.circuit_color)
        text_Circuit = brace_Circuit.get_text("???").set_color(self.circuit_color)
        self.play(
            Write(
                VGroup(
                    brace_Circuit, text_Circuit
                )
            ),
            ApplyMethod(
                acca_text[1].set_color,
                self.circuit_color
            )
        )
        self.wait(0.506)

        # move to title
        self.play(
            ApplyMethod(
                acca_text[1].to_edge,
                UP
            ),
            FadeOutAndShift(
                acca_text[0],
                direction=LEFT
            ),
            FadeOutAndShift(
                acca_text[2],
                direction=RIGHT
            ),
            FadeOutAndShift(
                VGroup(brace_Circuit, text_Circuit),
                direction=DOWN
            )
        )
        self.wait(0.506)

        # underline Circuit
        underline = Line(LEFT, RIGHT, color=self.circuit_color)
        underline.match_width(acca_text[1])
        underline.scale(1.1)
        underline.next_to(acca_text[1], DOWN, SMALL_BUFF)
        self.play(
            Write(
                underline
            )
        )
        self.wait(2.57)

        # add phone
        phone = ImageMobject("images/ep1/IntroduceCircuit/iphone-circuit-board.jpg")\
            .scale(1.7)\
            .move_to(-5*RIGHT+0.5*UP)
        phone_rect = SurroundingRectangle(phone, color=YELLOW, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(phone),
                Write(phone_rect),
                lag_ratio=0.1,
                run_time=1.97
            )
        )

        # add car
        car = ImageMobject("images/ep1/IntroduceCircuit/car1.jpg")\
            .scale(1.6)\
            .move_to(0.7*RIGHT-0.5*UP)
        car_rect = SurroundingRectangle(car, color=YELLOW, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(car),
                Write(car_rect),
                lag_ratio=0.1,
                run_time=1.23
            )
        )

        # add home circuit
        home_circuit = ImageMobject("images/ep1/IntroduceCircuit/home-circuit.jpg") \
            .scale(2.8) \
            .move_to(5.5 * RIGHT - 1.25 * UP)
        home_circuit_rect = SurroundingRectangle(home_circuit, color=YELLOW, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(home_circuit),
                Write(home_circuit_rect),
                lag_ratio=0.11,
                run_time=3.6
            )
        )

        # shift up and ask "What really is an electrical circuit?"
        question = TextMobject("What really is an electrical circuit?", color=self.circuit_color) \
            .scale(1.5) \
            .to_corner(DOWN)
        phone_group = Group(phone,phone_rect)
        car_group = Group(car,car_rect)
        home_group = Group(home_circuit,home_circuit_rect)
        new_top = FRAME_HEIGHT/2 - 2
        self.play(
            AnimationGroup(
                AnimationGroup(
                    ApplyMethod(
                        phone_group.shift,
                        (new_top - phone_group.get_center()[1] - phone_group.get_height()/2)*UP
                    ),
                    ApplyMethod(
                        car_group.shift,
                        (new_top - car_group.get_center()[1] - car_group.get_height()/2)*UP
                    ),
                    ApplyMethod(
                        home_group.shift,
                        (new_top - home_group.get_center()[1] - home_group.get_height()/2)*UP
                    ),
                    lag_ratio=0.05
                ),
                Write(question),
                lag_ratio=1
            )
        )

        self.wait()

class CircuitDefinition(Scene):
    def construct(self):
        # show textbook
        textbook = ImageMobject("images/ep1/CircuitDefinition/textbook2.png") \
            .scale(3.5) \
            .to_edge(LEFT)
        self.play(
            FadeIn(textbook)
        )
        self.wait(3.34)

        # show definition of circuit
        definition = TextMobject(
            "electrical circuit ", "-", " interconnection ", "of", " electrical elements",
            arg_separator=" ",
            color=YELLOW) \
            .scale(1.3) \
            .to_corner(DOWN)
        self.play(
            Write(
                definition,
                run_time=2
            )
        )
        self.wait(7.56)

        brace_ee = Brace(definition[4], color=YELLOW, direction=UP)
        text_ee = brace_ee.get_text("???").set_color(YELLOW)
        self.play(
            AnimationGroup(
                FadeIn(brace_ee),
                FadeIn(text_ee),
                lag_ratio=0.05
            )
        )
        self.wait(0.77)

        brace_inter = Brace(definition[2], color=YELLOW, direction=UP)
        text_inter = brace_inter.get_text("???").set_color(YELLOW)
        self.play(
            AnimationGroup(
                FadeIn(brace_inter),
                FadeIn(text_inter),
                lag_ratio=0.05
            )
        )
        self.wait(3.8)

        # show simple real world circuit
        self.lamp_circuit = BatteryLampCircuit().to_edge(LEFT)
        self.play(
            AnimationGroup(
                FadeInFrom(
                    self.lamp_circuit,
                    direction=LEFT
                ),
                ApplyMethod(
                    textbook.to_edge,
                    RIGHT
                ),
                lag_ratio=0.05
            ),
            FadeOut(
                Group(
                    brace_inter, brace_ee,
                    text_inter, text_ee
                )
            )
        )
        self.wait(4.7)

        # add Electrical Element label
        elements_text = TextMobject("2 electrical elements", color=YELLOW)\
            .scale(1.4) \
            .to_edge(UP)\
            .shift(1*DOWN+2.5*LEFT)
        self.play(
            Write(
                elements_text,
                run_time=1.77
            )
        )
        self.wait(1.93)

        # add rectangles around electrical elements
        elements_label = VGroup()
        elements_label.add(
            SurroundingRectangle(
                self.lamp_circuit.outer_rect
            ),
            SurroundingRectangle(
                VGroup(
                    self.lamp_circuit.base_big,
                    self.lamp_circuit.base_small,
                    self.lamp_circuit.light_bulb
                )
            )
        )
        self.play(
            Write(elements_label[0], run_time=0.77)
        )
        self.play(
            Write(elements_label[1], run_time=0.77)
        )

        kw = {'color': YELLOW}
        arrows = VGroup(
        Arrow(start=elements_text.get_bottom(),
              end=self.lamp_circuit.light_bulb.get_top(), **kw),
        Arrow(start=elements_text.get_bottom(),
              end=self.lamp_circuit.outer_rect.get_corner(UR), **kw)
        )
        self.play(
            AnimationGroup(
                *[
                    ShowCreation(arrow)
                    for arrow in arrows
                ]
            )
        )
        self.wait(0.57)

        underline1 = Line(LEFT, RIGHT, color=RED_C) \
            .match_width(definition[2]) \
            .scale(1) \
            .next_to(definition[2], DOWN, SMALL_BUFF)
        underline2 = Line(LEFT, RIGHT, color=BLUE_C) \
            .match_width(definition[4]) \
            .scale(1) \
            .next_to(definition[4], DOWN, SMALL_BUFF)
        self.play(
            AnimationGroup(
                ApplyMethod(
                    definition[4].set_color,
                    BLUE_C,
                    run_time=0.8
                ),
                ShowCreation(
                    underline2,
                    run_time=0.8
                ),
                lag_ratio=0.01
            ),
        )
        self.play(
            AnimationGroup(
                ApplyMethod(
                    definition[2].set_color,
                    RED_C,
                    run_time=0.8
                ),
                ShowCreation(
                    underline1,
                    run_time=0.8
                ),
                lag_ratio=0.01
            ),
            ApplyMethod(
                VGroup(
                    self.lamp_circuit.wire_bot,
                    self.lamp_circuit.wire_top
                ).set_color,
                RED_C
            )
        )

        self.wait(6.21)

    def get_elec_element_rects(self):
        rects = VGroup()
        kw = {
            'width': 0.36,
            'height': 0.36,
            'color': YELLOW_E,
            'stroke_width': 4
        }
        kw_med = {
            'width': 0.40,
            'height': 0.36,
            'color': YELLOW_E,
            'stroke_width': 4
        }
        kw_lrg = {
            'width': 0.45,
            'height': 0.45,
            'color': YELLOW_E,
            'stroke_width': 4
        }
        kw_lrg2 = {
            'width': 0.49,
            'height': 0.49,
            'color': YELLOW_E,
            'stroke_width': 4
        }
        coors = [
            (0.81, 2.46),
            (1.23, 2.46),
            (1.37, 2.04),
            (1.80, 2.04),
            (2.20, 1.08),
            (2.50, 3.22),
            (2.90, 1.08),
            (3.18, 1.85),
            (3.18, 2.20),
            (3.70, 1.75),
            (3.77, 2.10),
            (3.79, 3.02),
            (3.79, 3.40),
            (4.13, 2.10),
            (4.17, 1.00),
            (4.42, 3.33),
            (4.65, 2.10),
            (5.28, 3.38),
            (5.28, 2.90),
            (5.28, 2.45),
            (5.28, 1.80),
            (5.28, 1.25),
            (5.82, 2.57),
            (5.82, 2.19),
            (6.68, 2.57),
            (6.68, 2.19),
            (7.21, 2.23),
            (7.26, 1.85),
            (7.30, 3.40),
            (7.65, 2.50),
            (7.75, 3.40),
            (7.78, 0.60),
        ]
        coors_med = [
            (7.30, 0.60),
            (7.93, 0.88),
            (7.93, 3.70),
        ]
        coors_lrg = [
            (2.23, 2.40),
            (2.81, 2.40),
            (4.50, 2.87),
            (3.85, 1.35),
            (4.58, 1.37),
        ]
        coors_lrg2 = [
            (5.86, 1.61),
            (6.72, 1.58),
            (5.86, 3.00),
            (6.72, 3.00),
        ]
        for coor in coors:
            rects.add(
                Rectangle(**kw).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        for coor in coors_med:
            rects.add(
                Rectangle(**kw_med).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        for coor in coors_lrg:
            rects.add(
                Rectangle(**kw_lrg).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        for coor in coors_lrg2:
            rects.add(
                Rectangle(**kw_lrg2).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        rects.sort(point_to_num_func=lambda x: x[0])
        return rects

    def get_electron_anim(self, freq=0.11, run_time=1):
        return ApplyMethod(
            self.lamp_circuit.electron_loc.increment_value,
            run_time * freq,
            run_time=run_time,
            rate_func=linear
        )

class CompsDisplay(Scene):
    def construct(self):
        # store raw electrical elements in VGroup
        raw_comps = VGroup(
            # Ground(),
            Mosfet(),
            Transformer(),
            NPNTransistor(),
            EnhancedPChannelMosfet(),
            ZenerDiode().rotate(PI/2).scale(0.4),
            Diode().rotate(PI/2).scale(0.4),
            Capacitor().rotate(PI/2).scale(0.9),
            Inductor(),
            OpAmp(),
            DependentCurrentSource(),
            DependentVoltageSource(),
            CurrentSource(),
            VoltageSource(),
            Resistor(),
            BatterySymbol(),
            IronCoreInductor().rotate(-PI/2).scale(0.5),
            VacuumTube(),
            Potentiometer().rotate(-PI/2).scale(0.5),
            FullBridgeRectifier(),
            Triac().scale(0.7)
        )\
            .scale(1.25)

        # add electrical elements
        comps = VGroup(
            *[self.create_comp_box(comp)
            for comp in raw_comps]
        )
        # add copy of comps shuffled to make list longer
        comps_cp = list(comps.deepcopy())
        comps.add(*comps_cp)
        comps.arrange(RIGHT)
        comps.to_edge(LEFT, buff=2)

        comps_box = Rectangle(
            width=FRAME_WIDTH*0.8,
            height=comps.get_height()+0.2,
            color=YELLOW
        )
        kw_side = {
            "width": 4,
            "height": comps.get_height() + 0.2,
            "fill_color": BLACK,
            "fill_opacity": 1,
            "stroke_color": BLACK
        }
        lbox = Rectangle(**kw_side)\
            .next_to(comps_box,direction=LEFT,buff=0)
        rbox = Rectangle(**kw_side) \
            .next_to(comps_box, direction=RIGHT, buff=0)
        self.add(comps)
        comps_group = VGroup(
            lbox,
            rbox,
            comps_box
        )
        self.add(comps_group)

        """ very important """
        total_travel_dist = comps.get_width()-comps_box.get_width()-0.1
        comps_vel = 3
        def get_comps_anim(run_time=1):
            return ApplyMethod(
                comps.shift,
                comps_vel * run_time * LEFT,
                run_time=run_time,
                rate_func=linear
            )

        # shift electrical elements to left
        ee_text = TextMobject("\\underline{electrical elements}", color=YELLOW)\
            .scale(1.2)\
            .next_to(comps_box, direction=UP, buff=0.2)
        comps_group.add(ee_text)
        self.play(
            get_comps_anim(run_time=14.93),
            Write(ee_text)
        )

        # shift up and add note about other EE
        circuit = BatteryLampCircuit()
        battery = VGroup(
            circuit.top_rect,
            circuit.bot_rect,
            circuit.outer_rect,
            circuit.plus_sign,
            circuit.horz_line,
            circuit.lightning_bolt,
            circuit.minus_sign
        ).scale(0.9)
        light_bulb = VGroup(
            circuit.base_big,
            circuit.base_small,
            circuit.light_bulb,
            circuit.filament
        ).scale(0.95)
        ee2_group = VGroup(battery, light_bulb)\
            .scale(1.0)\
            .arrange(RIGHT, buff=1)\
            .to_edge(DOWN)
        ee2_group.add(
            SurroundingRectangle(ee2_group,color=YELLOW, buff=0.2)
        )
        self.play(
            ApplyMethod(
                comps_group.to_edge,
                UP,
                buff=0,
                rate_func=linear
            ),
            ApplyMethod(
                comps.shift,
                1*comps_vel*LEFT + 2.2139*UP,
                rate_func=linear
            ),
            FadeInFrom(
                ee2_group,
                direction=DOWN,
                buff=0
            ),
        )
        self.play(
            get_comps_anim(
                run_time=6.693
            )
        )

        # add arrow showing connection
        con_arrow = Arrow(
            start=ee2_group.get_top(),
            end=comps_box.get_bottom(),
            stroke_width=10,
            color=BLUE_C
        )\
            .scale(1.2)
        con_text = TextMobject(
            "build a deeper understanding",
            color=BLUE_C
        )\
            .next_to(con_arrow, direction=RIGHT)
        # con_text[-1].set_fill(BLUE_C, opacity=1)
        # con_text[-1].set_stroke(BLUE_C, opacity=1)
        self.play(
            AnimationGroup(
                ShowCreation(con_arrow),
                Write(con_text),
                lag_ratio=0.1
            ),
            get_comps_anim(13.2),
        )

    def create_comp_box(self, comp):
        width = 2.7
        rect = Rectangle(
            stroke_opacity=0,
            width=width,
            height=width
        )
        rect.add(comp)
        return rect

class ComplexCircuitOverview(Scene):
    def construct(self):
        # add definition
        definition = TextMobject(
            "electrical circuit ", "-", " interconnection ", "of", " electrical elements",
            arg_separator=" ",
            color=YELLOW) \
            .scale(1.4) \
            .to_corner(DOWN)
        underline1 = Line(LEFT, RIGHT, color=BLUE_C)\
            .match_width(definition[2])\
            .scale(1)\
            .next_to(definition[2], DOWN, SMALL_BUFF)
        underline2 = Line(LEFT, RIGHT, color=BLUE_C) \
            .match_width(definition[4]) \
            .scale(1) \
            .next_to(definition[4], DOWN, SMALL_BUFF)
        self.add(
            definition,
        )

        # needed for positioning boxes
        scale_factor = 1.5
        self.complex_circuit = ImageMobject("images/ep1/CircuitsIntro/complex_circuit.jpg") \
            .scale(2*scale_factor)
        self.play(
            FadeInFrom(
                self.complex_circuit,
                direction=RIGHT,
                run_time=2
            )
        )
        self.wait(3.4)

        electrical_elem_label = TextMobject("\\underline{44 Electrical Elements}", color=YELLOW) \
            .scale(1.5) \
            .next_to(self.complex_circuit, direction=UP)
        electrical_elem_rects = self.get_elec_element_rects(scale_factor=scale_factor)
        self.play(
            LaggedStartMap(
                # SpinInFromNothing, FadeInFrom, FadeInFromLarge, ShowCreation, FadeIn, GrowFromCenter, Write, DrawBorderThenFill,
                # FadeInFrom, FadeInFromLarge
                SpinInFromNothing,
                electrical_elem_rects,
                run_time=7.5,
                lag_ratio=0.25
            ),
            LaggedStart(
                AnimationGroup(
                    FadeInFrom(
                        electrical_elem_label,
                        direction=UP,
                        run_time=0.5
                    ),
                    AnimationGroup(
                        ApplyMethod(
                            definition[2].set_color,
                            BLUE_C,
                            run_time=0.53
                        ),
                        ShowCreation(
                            underline1,
                            run_time=0.53
                        ),
                        lag_ratio=0.01
                    ),
                    AnimationGroup(
                        ApplyMethod(
                            definition[4].set_color,
                            BLUE_C,
                            run_time=0.53
                        ),
                        ShowCreation(
                            underline2,
                            run_time=0.53
                        ),
                        lag_ratio=0.01
                    ),
                    lag_ratio=1
                )
            )
        )
        self.wait(0.8)

    def get_elec_element_rects(self, scale_factor=2.):
        stroke_mult = 2/(1+np.exp(1*(-scale_factor+1)))

        rects = VGroup()
        kw = {
            'width': 0.36*scale_factor,
            'height': 0.36*scale_factor,
            'color': YELLOW_E,
            'stroke_width': 4*stroke_mult
        }
        kw_med = {
            'width': 0.40*scale_factor,
            'height': 0.36*scale_factor,
            'color': YELLOW_E,
            'stroke_width': 4*stroke_mult
        }
        kw_lrg = {
            'width': 0.45*scale_factor,
            'height': 0.45*scale_factor,
            'color': YELLOW_E,
            'stroke_width': 4*stroke_mult
        }
        kw_lrg2 = {
            'width': 0.49*scale_factor,
            'height': 0.49*scale_factor,
            'color': YELLOW_E,
            'stroke_width': 4*stroke_mult
        }
        coors = [
            (0.81, 2.46),
            (1.23, 2.46),
            (1.37, 2.04),
            (1.80, 2.04),
            (2.20, 1.08),
            (2.50, 3.22),
            (2.90, 1.08),
            (3.18, 1.85),
            (3.18, 2.20),
            (3.70, 1.75),
            (3.77, 2.10),
            (3.79, 3.02),
            (3.79, 3.40),
            (4.13, 2.10),
            (4.17, 1.00),
            (4.42, 3.33),
            (4.65, 2.10),
            (5.28, 3.38),
            (5.28, 2.90),
            (5.28, 2.45),
            (5.28, 1.80),
            (5.28, 1.25),
            (5.82, 2.57),
            (5.82, 2.19),
            (6.68, 2.57),
            (6.68, 2.19),
            (7.21, 2.23),
            (7.26, 1.85),
            (7.30, 3.40),
            (7.65, 2.50),
            (7.75, 3.40),
            (7.78, 0.60),
        ]
        coors_med = [
            (7.30, 0.60),
            (7.93, 0.88),
            (7.93, 3.70),
        ]
        coors_lrg = [
            (2.23, 2.40),
            (2.81, 2.40),
            (4.50, 2.87),
            (3.85, 1.35),
            (4.58, 1.37),
        ]
        coors_lrg2 = [
            (5.86, 1.61),
            (6.72, 1.58),
            (5.86, 3.00),
            (6.72, 3.00),
        ]
        for coor in coors:
            rects.add(
                Rectangle(**kw).move_to(self.complex_circuit.get_corner(DL) + (coor[0] * RIGHT + coor[1] * UP)*scale_factor)
            )
        for coor in coors_med:
            rects.add(
                Rectangle(**kw_med).move_to(self.complex_circuit.get_corner(DL) + (coor[0] * RIGHT + coor[1] * UP)*scale_factor)
            )
        for coor in coors_lrg:
            rects.add(
                Rectangle(**kw_lrg).move_to(self.complex_circuit.get_corner(DL) + (coor[0] * RIGHT + coor[1] * UP)*scale_factor)
            )
        for coor in coors_lrg2:
            rects.add(
                Rectangle(**kw_lrg2).move_to(self.complex_circuit.get_corner(DL) + (coor[0] * RIGHT + coor[1] * UP)*scale_factor)
            )
        rects.sort(point_to_num_func=lambda x: x[0])
        return rects

class Summary(Scene):
    def construct(self):
        # add definition
        definition = TextMobject(
            "electrical circuit ", "-", " interconnection ", "of", " electrical elements",
            arg_separator=" ",
            color=YELLOW) \
            .scale(1.4) \
            .to_corner(DOWN)
        underline1 = Line(LEFT, RIGHT, color=BLUE_C) \
            .match_width(definition[2]) \
            .scale(1) \
            .next_to(definition[2], DOWN, SMALL_BUFF)
        underline2 = Line(LEFT, RIGHT, color=BLUE_C) \
            .match_width(definition[4]) \
            .scale(1) \
            .next_to(definition[4], DOWN, SMALL_BUFF)
        self.add(
            definition,
        )

        self.wait(3.37)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    ApplyMethod(
                        definition[4].set_color,
                        BLUE_C,
                        run_time=0.53
                    ),
                    ShowCreation(
                        underline2,
                        run_time=0.53
                    ),
                    lag_ratio=0.01
                ),
                AnimationGroup(
                    ApplyMethod(
                        definition[2].set_color,
                        BLUE_C,
                        run_time=0.53
                    ),
                    ShowCreation(
                        underline1,
                        run_time=0.53
                    ),
                    lag_ratio=0.01
                ),
                lag_ratio=1
            )
        )
        self.wait(0.77)

        home_circuit = ImageMobject(
            "images\ep1\Summary\home_circuit.jpg"
        )\
            .move_to(FRAME_WIDTH*0.25*LEFT)\
            .scale(2.25)
        home_rect = SurroundingRectangle(home_circuit, color=YELLOW, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(home_circuit),
                Write(home_rect),
                lag_ratio=0.1,
            )
        )
        self.wait(1.96)

        circuit_board = ImageMobject(
            "images\ep1\Summary\circuit-board.jpg"
        ) \
            .move_to(FRAME_WIDTH * 0.25 * RIGHT) \
            .scale(2.25)
        circuit_rect = SurroundingRectangle(circuit_board, color=YELLOW, buff=0.05)
        self.play(
            AnimationGroup(
                FadeIn(circuit_board),
                Write(circuit_rect),
                lag_ratio=0.1,
            )
        )
        self.wait(1.33)