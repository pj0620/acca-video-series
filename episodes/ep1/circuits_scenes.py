from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit,GeneratorLampCircuit
from accalib import geometry
from functools import partial

class CircuitsIntro(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "electron_freq_0" : 0.11,
        "electron_freq_1" : 0.33
    }
    def construct(self):
        self.wait(5.67)
        # self.show_circuits_questions() #SS1
        self.define_circuit() #SS2,SS3,
        # self.label_simple_circuit() #SS4
        # self.introduce_ohms_law() #SS5
        # self.expand_ohms_law() #SS6

        self.wait(3)

    def show_circuits_questions(self):
        questions=TextMobject(
            "$\\bullet$What is an electrical circuit?",
            "$\\bullet$What is Circuit Analysis?",
            "$\\bullet$AC vs DC")\
            .arrange(DOWN,buff=1)\
            .scale(2)
        questions[1].align_to(questions[0],direction=LEFT)
        questions[2].align_to(questions[1],direction=LEFT)

        self.play(
            Write(
                questions[0],
                run_time=1
            )
        )
        self.wait(1.22)

        self.play(
            Write(
                questions[1],
                run_time=1
            )
        )
        self.wait(1.68)

        # SS1.3
        self.play(
            Write(
                questions[2],
                run_time=1
            )
        )
        self.wait(1.64)
        self.play(
            FadeOutAndShift(
                questions,
                direction=LEFT,
                run_time=1
            )
        )

    def define_circuit(self):
        # show definition of circuit
        definition=TextMobject("electrical circuit - interconnection of electrical elements",color=YELLOW)\
            .scale(1.3)\
            .to_corner(DOWN)
        self.play(
            Write(
                definition,
                run_time=2
            )
        )
        self.wait(1.8)

        # show simple real world circuit
        self.lamp_circuit = BatteryLampCircuit()
        self.play(
            FadeIn(
                self.lamp_circuit,
                run_time=1
            )
        )
        self.wait(7.28)

        indicate_anim=partial(ShowPassingFlashAround,
                              time_width=0.5,
                              remover=True)

        self.play(
            indicate_anim(
                self.lamp_circuit.outer_rect,
                run_time=1
            ),
        )

        self.play(
            indicate_anim(
                VGroup(
                    self.lamp_circuit.base_big,
                    self.lamp_circuit.base_small,
                    self.lamp_circuit.light_bulb
                ),
                run_time=1
            )
        )

        kw = {'color':YELLOW}
        elements_label=VGroup(
            TextMobject("Electrical Elements",**kw).to_corner(UR).shift(1*DOWN+4*LEFT).scale(2)
        )
        elements_label.add(
            Arrow(start=elements_label[0].get_bottom(),
                  end=self.lamp_circuit.light_bulb.get_top(),**kw)
        )
        elements_label.add(
            Arrow(start=elements_label[1].get_start(),
                  end=self.lamp_circuit.outer_rect.get_corner(UR),**kw)
        )
        self.play(
            FadeIn(
                elements_label,
                run_time=1
            )
        )
        self.wait(4.55)
        self.play(
            FadeOut(
                elements_label,
                run_time=1
            )
        )

        # SS3.1
        self.complex_circuit=ImageMobject("images/ep1/CircuitsIntro/complex_circuit.jpg")\
            .to_edge(RIGHT)\
            .scale(2)\
            .shift(1.5*LEFT)
        self.play(
            ApplyMethod(
                self.lamp_circuit.to_edge,
                LEFT,
                buff=0.01,
                run_time=1
            )
        )
        self.play(
            FadeInFrom(
                self.complex_circuit,
                direction=RIGHT,
                run_time=2
            )
        )

        electrical_elem_rects = self.get_elec_element_rects()
        self.add(electrical_elem_rects)

        # self.play(
        #     FadeOutAndShift(
        #         definition,
        #         direction=DOWN,
        #         run_time=1
        #     ),
        #     FadeOutAndShift(
        #         self.complex_circuit,
        #         direction=RIGHT,
        #         run_time=1
        #     ),
        #     ApplyMethod(
        #         self.lamp_circuit.move_to,
        #         1.5*RIGHT+UP
        #     )
        # )

    def label_simple_circuit(self):
        self.wait(4.92)

        # add electrons
        self.lamp_circuit.setup_electrons()
        self.play(
            self.get_electron_anim(
                run_time=10.10
            )
        )

        # fade in current label
        point1 = self.lamp_circuit.electron_vect_inter.interpolate(0.55)
        point2 = self.lamp_circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0]-point1[0])/np.linalg.norm(point2-point1))
        self.current_arrow=ArrowTip(
            start_angle=-1*angle,
            color=self.current_color
        )\
            .scale(2.5)\
            .move_to(point1+0.05*UR)
        self.play(
            FadeIn(
                self.current_arrow,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=1
            )
        )
        self.play(
            self.get_electron_anim(
                run_time=1.37
            )
        )

        self.V_text=TextMobject(
            "V", "=",
            color=self.voltage_color
        ) \
            .next_to(self.lamp_circuit.outer_rect, direction=LEFT, buff=4) \
            .scale(2)
        self.voltage_value=DecimalNumber(
            12,
            unit="V",
            color=self.voltage_color,
            num_decimal_places=2
        ) \
            .scale(2) \
            .next_to(self.V_text, direction=RIGHT, buff=0.3)
        self.voltage_tracker=ValueTracker(12)
        self.voltage_value.add_updater(
            lambda x:
            x.set_value(self.voltage_tracker.get_value())
        )
        # current_text=TextMobject(
        #     "current",
        #     color=self.current_color)\
        #     .next_to(current_arrow,direction=UR)\
        #     .shift(0.5*RIGHT)\
        #     .scale(2)
        self.I_text=TextMobject(
            "I","=",
            color=self.current_color
        ) \
            .next_to(self.current_arrow, direction=UR) \
            .shift(0.5*RIGHT)\
            .scale(2)
        self.current_value = DecimalNumber(
            2,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        )\
            .scale(2)\
            .next_to(self.I_text,direction=RIGHT,buff=0.3)
        self.current_value.add_updater(
            lambda x:
            x.set_value(self.voltage_tracker.get_value()/6.)
        )
        self.play(
            FadeIn(
                self.I_text[0],
                run_time=1
            ),
            self.get_electron_anim(
                run_time=1
            )
        )
        self.play(
            self.get_electron_anim(
                run_time=1.83
            )
        )
        self.play(
            FadeIn(
                self.I_text[1],
                run_time=1
            ),
            FadeIn(
                self.current_value,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=1
            )
        )
        self.play(
            self.get_electron_anim(
                run_time=3.7
            )
        )

        self.play(
            FadeIn(
                self.V_text,
                run_time=1
            ),
            FadeIn(
                self.voltage_value,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=1
            )
        )
        self.play(
            self.get_electron_anim(
                run_time=1.1
            )
        )

        self.R_text=TextMobject(
            "R", "=",
            color=self.resistance_color
        ) \
            .next_to(self.lamp_circuit.light_bulb, direction=DR, buff=0.2) \
            .scale(2)
        self.resistor_value=DecimalNumber(
            6,
            unit="\\Omega",
            color=self.resistance_color,
            num_decimal_places=0
        ) \
            .scale(2) \
            .next_to(self.R_text, direction=RIGHT, buff=0.3)
        self.play(
            FadeIn(
                self.R_text,
                run_time=1
            ),
            FadeIn(
                self.resistor_value,
                run_time=1
            ),
            self.get_electron_anim(
                run_time=1
            )
        )

        self.play(
            self.get_electron_anim(
                run_time=3.06
            )
        )

        tau = 5
        f0 = self.electron_freq_0
        f1 = self.electron_freq_1
        my_rate_func = lambda t: ((f1-f0)/(f1+f0))*(t**2) + ((2*f0)/(f0+f1))*t
        self.play(
            ApplyMethod(
                self.voltage_tracker.increment_value,
                12,
                run_time=tau,
                rate_func=linear
            ),
            ApplyMethod(
                self.lamp_circuit.electron_loc.increment_value,
                ((f0+f1)/2)*tau,
                run_time=tau,
                rate_func=my_rate_func
            )
        )

        self.play(
            self.get_electron_anim(
                freq=f1,
                run_time=12.2
            )
        )

    def introduce_ohms_law(self):
        self.ohms_law_label=TextMobject("Ohm's Law:")\
            .scale(2)\
            .to_edge(DOWN)\
            .shift(4*LEFT+0.5*UP)
        self.play(
            FadeIn(
                self.ohms_law_label,
                run_time=1
            ),
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=1
            )
        )
        self.play(
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=0.5633
            )
        )

        self.ohms_law=TextMobject(
            "\\textit{V}","\\textit{=}","\\textit{I}","\\textit{R}",
            arg_separator=""
        )\
            .scale(3)\
            .next_to(self.ohms_law_label,direction=RIGHT,buff=0.5)
        self.ohms_law[0].set_color(self.voltage_color)
        self.ohms_law[2].set_color(self.current_color)
        self.ohms_law[3].set_color(self.resistance_color)
        self.ohms_law[3].shift(0.2*RIGHT)
        self.play(
            TransformFromCopy(
                self.V_text[0],
                self.ohms_law[0],
                run_time=0.67
            ),
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=0.67
            )
        )
        self.play(
            FadeIn(
                self.ohms_law[1],
                run_time=0.73
            ),
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=0.73
            )
        )
        self.play(
            TransformFromCopy(
                self.I_text[0],
                self.ohms_law[2],
                run_time=0.6
            ),
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=0.6
            )
        )
        self.play(
            TransformFromCopy(
                self.R_text[0],
                self.ohms_law[3],
                run_time=0.61
            ),
            self.get_electron_anim(
                freq=self.electron_freq_1,
                run_time=0.61
            )
        )

    def expand_ohms_law(self):
        # SS6.1
        self.lamp_circuit.remove_electrons()
        self.play(
            FadeOutAndShift(
                VGroup(
                    self.lamp_circuit,
                    self.I_text,
                    self.V_text,
                    self.R_text,
                    self.resistor_value,
                    self.voltage_value,
                    self.current_value,
                    self.current_arrow,
                ),
                direction=UP,
                run_time=1.6
            )
        )
        ohms_law_title = TextMobject("\\underline{Ohm's Law}")\
            .scale(2.4)\
            .to_edge(UP)\
            .shift((FRAME_WIDTH/4)*LEFT)
        self.play(
            Transform(
                self.ohms_law_label,
                ohms_law_title,
                run_time=1.6
            )
        )
        # move ohm's law formula
        self.play(
            ApplyMethod(
                self.ohms_law.move_to,
                ohms_law_title.get_center()+1.5*DOWN,
                run_time=1.6
            )
        )
        self.wait(0.033)

        # highlight each variable
        # SS6.2
        v_rect = SurroundingRectangle(self.ohms_law[0]).set_stroke(self.voltage_color)
        v_text = TextMobject("Voltage",color=self.voltage_color).next_to(v_rect,direction=DOWN).scale(1.2).shift(0.35*LEFT)
        i_rect=SurroundingRectangle(self.ohms_law[2]).set_stroke(self.current_color)
        i_text=TextMobject("Current", color=self.current_color  ).next_to(i_rect, direction=DOWN).scale(1.2).shift(0.2*LEFT)
        r_rect=SurroundingRectangle(self.ohms_law[3]).set_stroke(self.resistance_color)
        r_text=TextMobject("Resistance", color=self.resistance_color).next_to(r_rect, direction=DR).scale(1.2).shift(0.7*LEFT)
        self.play(
            ShowCreation(v_rect),
            FadeInFrom(v_text,UP),
            run_time=0.97
        )

        # SS6.3
        self.play(
            ShowCreation(i_rect),
            FadeInFrom(i_text, UP),
            run_time=0.63
        )

        # SS6.4
        self.play(
            ShowCreation(r_rect),
            FadeInFrom(r_text, UP),
            run_time=1
        )

        self.play(
            FadeOutAndShift(
                VGroup(
                    v_rect,
                    v_text,
                    i_rect,
                    i_text,
                    r_rect,
                    r_text,
                ),
                UP
            )
        )

        circuit = BatteryLampCircuit()\
            .next_to(self.ohms_law,direction=DOWN,buff=1.5)\
            .shift(1.4*RIGHT)\
            .scale(0.8)
        self.play(
            FadeIn(
                circuit
            )
        )
        circuit.setup_electrons()

        def get_electron_anim(freq=0.11, run_time=1):
            return ApplyMethod(
                circuit.electron_loc.increment_value,
                run_time * freq,
                run_time=run_time,
                rate_func=linear
            )

        # label voltage
        V_text2=TextMobject(
            "V", "=",
            color=self.voltage_color,
            arg_sepeartor=""
        ) \
            .next_to(circuit.outer_rect, direction=LEFT, buff=1.6) \
            .scale(1.7)
        V_text2[1].shift(0.1*LEFT)
        voltage_value2=DecimalNumber(
            5,
            unit="V",
            color=self.voltage_color,
            num_decimal_places=0
        ) \
            .scale(1.7) \
            .next_to(V_text2, direction=RIGHT, buff=0.2)
        self.play(
            FadeInFrom(V_text2,LEFT),
            FadeInFrom(voltage_value2,LEFT),
            get_electron_anim()
        )

        point1=circuit.electron_vect_inter.interpolate(0.55)
        point2=circuit.electron_vect_inter.interpolate(0.5)
        angle=np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow2=ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.3) \
            .move_to(point1 + 0.05 * UR)
        I_text2=TextMobject(
            "I", "=",
            color=self.current_color,
            arg_sepeartor=""
        ) \
            .next_to(current_arrow2, direction=UR) \
            .shift(0.2*DOWN) \
            .scale(1.7)
        current_value2=DecimalNumber(
            2,
            unit="A",
            color=self.current_color,
            num_decimal_places=0
        ) \
            .scale(1.7) \
            .next_to(I_text2, direction=RIGHT, buff=0.3)
        self.play(
            FadeIn(current_arrow2),
            FadeIn(I_text2),
            FadeIn(current_value2),
            get_electron_anim()
        )

        R_text2=TextMobject(
            "R", "=",
            color=self.resistance_color,
            arg_sepeartor=""
        ) \
            .next_to(circuit.light_bulb, direction=DOWN, buff=0.4) \
            .shift(1.1*LEFT)\
            .scale(1.7)
        resistor_value2=DecimalNumber(
            2.5,
            unit="\\Omega",
            color=self.resistance_color,
            num_decimal_places=1
        ) \
            .scale(1.7) \
            .next_to(R_text2, direction=RIGHT, buff=0.3)
        resistor_qm=TextMobject(
            "???",
            color=self.resistance_color
        )\
            .scale(1.7) \
            .next_to(R_text2, direction=RIGHT, buff=0.3)
        self.play(
            FadeIn(R_text2),
            FadeIn(resistor_qm),
            get_electron_anim()
        )

        # move ohm's law to the right
        ohms_law_cp = self.ohms_law.copy()
        self.play(
            ApplyMethod(ohms_law_cp.shift,RIGHT*FRAME_WIDTH/2),
            get_electron_anim()
        )

        LHS_0 = VGroup(ohms_law_cp[0])
        RHS_0 = VGroup(*ohms_law_cp[2:4])

        # divide both sides by I
        LHS_1=TexMobject(
            "\\textit{V}", "\\over", "\\textit{I}",
            arg_separator=""
        ) \
            .scale(3) \
            .move_to(LHS_0.get_center())
        LHS_1[2].shift(0.2*LEFT)
        LHS_1[0].set_color(self.voltage_color)
        LHS_1[2].set_color(self.current_color)
        RHS_1=TexMobject(
            "\\textit{I}","\\textit{R}", "\\over", "\\textit{I}",
            arg_seperator=""
        )\
            .scale(3)\
            .move_to(RHS_0.get_center())
        RHS_1[3].shift(0.2 * LEFT)
        RHS_1[1].shift(0.3 * RIGHT)
        RHS_1[0].set_color(self.current_color)
        RHS_1[1].set_color(self.resistance_color)
        RHS_1[3].set_color(self.current_color)
        self.play(
            ReplacementTransform(
                LHS_0,
                LHS_1
            ),
            ReplacementTransform(
                RHS_0,
                RHS_1
            ),
            get_electron_anim()
        )

        # draw line canceling out I on RHS
        cancel_line=Line(
            start=RHS_1[3].get_corner(DR)+0.05*DOWN,
            end=RHS_1[0].get_corner(UL)+0.05*UP,
            stroke_color=RED,
            stroke_width=8

        )
        self.play(
            ShowCreation(cancel_line),
            get_electron_anim()
        )

        # remove I from RHS
        RHS_2=TexMobject(
            "R",
            arg_seperator=""
        )\
            .scale(3)\
            .move_to(RHS_1.get_center())
        RHS_2.set_color(self.resistance_color)
        self.play(
            ReplacementTransform(
                VGroup(RHS_1,cancel_line),
                RHS_2
            ),
            get_electron_anim()
        )

        # swap LHS RHS
        self.play(
            Swap(LHS_1,RHS_2),
            get_electron_anim()
        )

        # plug in voltage
        text_5V = TextMobject(
            "5\\textit{V}"
        )\
            .set_color(self.voltage_color)\
            .scale(3)\
            .move_to(LHS_1[0].get_center())
        self.play(
            Transform(
                LHS_1[0],
                text_5V
            ),
            get_electron_anim()
        )

        # plug in current
        text_2A = TextMobject(
            "2\\textit{A}"
        )\
            .set_color(self.current_color)\
            .scale(3)\
            .move_to(LHS_1[2].get_center())
        self.play(
            Transform(
                LHS_1[2],
                text_2A
            ),
            get_electron_anim()
        )

        # show resulting resistance
        text_2_5_ohm = TextMobject(
            "2.5$\\Omega$"
        )\
            .set_color(self.resistance_color)\
            .scale(3)\
            .move_to(LHS_1.get_center()+0.5*RIGHT)
        self.play(
            Transform(
                LHS_1,
                text_2_5_ohm
            ),
            get_electron_anim()
        )

        # draw arrow from result to R in circuit
        arrow = geometry.CurvedArrow(
            start_point=text_2_5_ohm.get_bottom(),
            end_point=resistor_qm.get_right(),
            angle=-PI/2
        )
        self.play(
            ShowCreationThenDestruction(arrow),
            get_electron_anim()
        )

        # transform question marks in R = ??? to result
        self.play(
            Transform(
                resistor_qm,
                resistor_value2
            ),
            get_electron_anim()
        )

    def get_elec_element_rects(self):
        rects = VGroup()
        kw={
            'width': 0.36,
            'height': 0.36,
            'color': YELLOW_D,
            'stroke_width': 3
        }
        kw_med = {
            'width': 0.40,
            'height': 0.36,
            'color': YELLOW_D,
            'stroke_width': 3
        }
        coors=[
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
        for coor in coors:
            rects.add(
                Rectangle(**kw).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        for coor in coors_med:
            rects.add(
                Rectangle(**kw_med).move_to(self.complex_circuit.get_corner(DL) + coor[0] * RIGHT + coor[1] * UP)
            )
        rects[-1].set_color(GREEN_D)
        return rects

    def get_electron_anim(self,freq=0.11,run_time=1):
        return ApplyMethod(
            self.lamp_circuit.electron_loc.increment_value,
            run_time*freq,
            run_time=run_time,
            rate_func=linear
        )