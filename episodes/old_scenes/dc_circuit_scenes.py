from manimlib.imports import *
from accalib.circuit_comps import *
from accalib.particles import Electron
from accalib.animations import EllipsesFlash
from accalib.utils import VectorInterpolator
from accalib.hydraulic import *
from functools import partial

class SimpleDCCircuit(Scene):
    CONFIG={
        "start_ang_freq": np.pi,
        "end_ang_freq": 2.5 * np.pi,
        "voltage_color": GREEN_D,  # GREEN_C
        "current_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "show_flowlines": True,
        "rotate_fins": True,
        "num_of_electrons": 9,
        "freeze_electrons": True
    }

    def construct(self):
        # TODO remove
        self.null_dot=Dot().move_to(100 * UR)

        self.wait(6.15)
        self.show_ohms_law() #SS1
        self.add_electrical_circuit() #SS2
        self.introduce_electrical_circuit() #SS3
        self.introduce_vs() #SS4
        self.introduce_r() #SS5
        self.show_real_circuit() #SS6

        self.wait(3)

    def show_ohms_law(self):
        ohms_law = TexMobject(
            "V","=","I","R",
            color="#FFFFFF").scale(5)
        # ohms_law.set_color_by_tex("V",self.voltage_color)
        # ohms_law.set_color_by_tex("I",self.current_color)
        # ohms_law.set_color_by_tex("R",self.resistance_color)

        self.add(
            ohms_law
        )
        self.play(
            EllipsesFlash(
                ohms_law,
                flash_radius_x=7,
                flash_radius_y=4,
                line_length=1.7,
                num_lines=16,
                run_time=1
                # line_stroke_width=5,
            )
        )
        self.wait(4.89)
        self.remove(
            ohms_law
        )

    def add_electrical_circuit(self):
        self.setup_circuit()
        self.setup_electrons()

        # add circuit with electrons
        self.add(
            self.voltage_source,
            self.resistor,
            self.wires,
            self.vs_text,
            self.r_text,
            self.ground,
        )

        self.wait(2.09)

    def introduce_electrical_circuit(self):
        indicate_anim = partial(ShowPassingFlashAround,
                                time_width=0.5)

        # draw rectangle arrow voltage source
        width_vs = self.vs_text.get_width() + self.voltage_source.get_width() + 0.1
        height_vs = self.voltage_source.get_height()
        center_vs_x = 0.5*(self.vs_text.get_left()[0]+self.voltage_source.get_right()[0])
        center_vs_y = self.voltage_source.get_center()[1]
        center_vs = center_vs_x*RIGHT + center_vs_y*UP
        vs_rect = Rectangle(
            width=width_vs,
            height=height_vs,
            stroke_opacity=0,
            opacity=0
        ).move_to(center_vs)
        self.play(
            indicate_anim(
                vs_rect,
                run_time=1
            )
        )
        self.wait(1.45)

        # draw rectangle arrow voltage source
        width_r=self.r_text.get_width() + self.resistor.get_width() + 0.8
        height_r=self.resistor.get_height()
        center_r_x=0.5 * (self.resistor.get_left()[0] + self.r_text.get_right()[0])
        center_r_y=self.resistor.get_center()[1]
        center_r=center_r_x * RIGHT + center_r_y * UP
        r_rect=Rectangle(
            width=width_r,
            height=height_r,
            stroke_opacity=1,
            stroke_color=RED,
            opacity=0
        ).move_to(center_r)
        self.play(
            indicate_anim(
                r_rect
            )
        )

        self.wait(1.01)

        # show "Electrical Circuit"
        electrical_circuit_title=TextMobject("\\underline{Electrical Circuit}") \
            .scale(1.7) \
            .next_to(self.electrical_circuit, direction=UP, buff=0.4)
        electrical_circuit_title.set_y(FRAME_HEIGHT / 2 - electrical_circuit_title.get_height())
        self.play(
            Write(
                electrical_circuit_title,
                run_time=0.85
            )
        )

        circuit_def=TextMobject(
            "interconnection of electrical elements",
            color=YELLOW) \
            .scale(1.5) \
            .to_corner(DOWN,buff=1)
        self.play(
            FadeIn(circuit_def)
        )

        self.wait(1.91)

        comps_rect, comps_list, invisible_dot, block_rect, block_rect2, comps_label=self.get_comps_display()
        r_text_cp = self.r_text.copy()
        self.play(
            FadeIn(invisible_dot),
            FadeIn(comps_rect),
            *[FadeIn(comp) for comp in comps_list],
            FadeIn(block_rect),
            FadeIn(block_rect2),
            FadeIn(r_text_cp)
        )

        self.play(
            Write(comps_label, run_time=0.6),
            ApplyMethod(
                invisible_dot.shift, 12 * LEFT,
                run_time=6,
                # pages[0].shift, 5 * UP,
                # run_time=3,
                rate_func=linear,
            )
        )

        self.play(
            FadeOut(comps_rect),
            *[FadeOut(comp) for comp in comps_list],
            FadeOut(comps_label),
            FadeOut(r_text_cp),
            FadeOut(block_rect),
            FadeOut(block_rect2),
            FadeOut(electrical_circuit_title),
            FadeOut(circuit_def)
        )


    def introduce_hydraulic_circuit(self):
        hydraulic_circuit_title=TextMobject("\\underline{Hydraulic Circuit}") \
            .scale(1.5) \
            .next_to(self.hydraulic_circuit, direction=UP, buff=0.4)\
            .shift(0.5*LEFT)
        hydraulic_circuit_title.set_y(FRAME_HEIGHT / 2 - hydraulic_circuit_title.get_height())
        self.play(
            Write(
                hydraulic_circuit_title,
                run_time=1
            ),
            self.get_rot_anim(
                run_time=1.89
            )
        )

        indicate_anim=partial(ShowPassingFlashAround,
                              time_width=0.5)

        # draw rectangle arrow voltage source
        width_pump=self.hydraulic_circuit.pump_circle.get_width()
        height_pump=self.hydraulic_circuit.pump_circle.get_height()
        center_pump=self.hydraulic_circuit.pump_circle.get_center()
        rect_pump=Rectangle(
            width=width_pump,
            height=height_pump,
            stroke_opacity=0,
            opacity=0
        ).move_to(center_pump)
        self.play(
            indicate_anim(
                rect_pump
            ),
            self.get_rot_anim(
                run_time=1.12
            )
        )

        width_st=self.hydraulic_circuit.rects_top[2].get_width()
        height_st=self.hydraulic_circuit.body.small_tube[0].get_height()
        center_st=self.hydraulic_circuit.small_rect.get_center()
        rect_st=Rectangle(
            width=width_st,
            height=height_st,
            stroke_opacity=1,
            stroke_color=RED,
            opacity=0
        ).move_to(center_st)
        self.play(
            indicate_anim(
                rect_st
            ),
            self.get_rot_anim(
                run_time=1.82
            )
        )

        self.play(
            Indicate(
                VGroup(*self.hydraulic_circuit.body.large_tube),
                scale_factor=1.02
            ),
            self.get_rot_anim(
                run_time=1.21
            )
        )

    def introduce_vs(self):
        orig_vs_loc=self.voltage_source.get_center()
        orig_vs_height=self.voltage_source.get_height()
        self.orig_vs_text=self.vs_text.copy()

        # expand voltage source
        voltage_source_group=VGroup(
            self.vs_text,
            self.voltage_source
        )
        vs_label=self.get_vs_label()
        self.play(
            FadeOut(self.wires),
            FadeOut(self.r_text),
            FadeOut(self.resistor),
            Succession(
                ApplyMethod(voltage_source_group.move_to,
                            (FRAME_WIDTH / 2 - self.voltage_source.get_width() / 2 - 2.7) * LEFT + 0.5*UP,
                            run_time=0.65),
                ApplyMethod(voltage_source_group.set_height,
                            4.7,
                            run_time=0.65)
            ),
            Write(vs_label[0]),
        )

        # Show "Independent Voltage Source"
        self.play(
            Write(vs_label[1]),
        )

        self.wait(1.13)

        vs_text=DecimalNumber(12,
                              num_decimal_places=0,
                              unit="V",
                              edge_to_fix=RIGHT,
                              color=self.voltage_color,
                              digit_to_digit_buff=0.052).scale(2)
        vs_text.move_to(self.voltage_source.get_center() + 3.5 * RIGHT)
        plus=TextMobject("\\textbf{$+$}", color=self.voltage_color) \
            .next_to(
            vs_text,
            direction=UP,
            buff=0.8
        ).scale(2)
        minus=TextMobject("\\textbf{$-$}", color=self.voltage_color) \
            .next_to(
            vs_text,
            direction=DOWN,
            buff=0.9
        ).scale(2)
        voltage_label=VGroup(
            Line(
                start=self.voltage_source.get_top(),
                end=self.voltage_source.get_top() + 3.5 * RIGHT,
                stroke_width=DEFAULT_WIRE_THICKNESS
            ),
            Line(
                start=self.voltage_source.get_bottom(),
                end=self.voltage_source.get_bottom() + 3.5 * RIGHT,
                stroke_width=DEFAULT_WIRE_THICKNESS
            ),
            vs_text,
            plus,
            minus
        )

        voltage_def=TextMobject("electrical element which maintains a constant \\\\voltage difference between its two ports",
                                color=YELLOW) \
            .scale(1.45) \
            .to_corner(DOWN)
        self.play(
            FadeIn(voltage_def),
            FadeIn(voltage_label)
        )

        self.wait(5.63)

        # voltage source examples
        aaa_battery = ImageMobject("images/ep1/SimpleDCCircuit/battery1.jpg")\
            .scale(2)\
            .to_edge(RIGHT)\
            .shift(0.5*UP)
        self.play(
            FadeInFrom(
                aaa_battery,
                direction=RIGHT
            )
        )

        self.wait(2)

        self.play(
            FadeOut(vs_label[0]),
            FadeOut(vs_label[1]),
            FadeOut(aaa_battery),
            FadeOut(voltage_label),
            FadeOut(voltage_def),
            FadeOut(self.vs_text)
        )

        self.play(
            Succession(
                ApplyMethod(self.voltage_source.move_to, orig_vs_loc),
                ApplyMethod(self.voltage_source.set_height, orig_vs_height)
            ),
            # AnimationGroup(
            #     ApplyMethod(self.vs_text.set_height, orig_b_height),
            #     ApplyMethod(self.vs_text.move_to, orig_vs_text_loc),
            # )
        )

        self.play(
            FadeIn(self.resistor),
            FadeIn(self.wires),
            FadeIn(self.orig_vs_text),
            FadeIn(self.r_text),
        )

    def introduce_r(self):
        orig_r_loc=self.resistor.get_center()
        orig_r_height=self.resistor.get_height()
        orig_r_text_loc = self.r_text.get_center()+0.2*RIGHT
        orig_r_text_height = self.r_text.get_height()
        # expand resistor
        resistor_group = VGroup(self.resistor,self.r_text)
        self.play(
            FadeOut(self.wires),
            FadeOut(self.orig_vs_text),
            FadeOut(self.voltage_source),
            Succession(
                ApplyMethod(resistor_group.move_to,
                            (FRAME_WIDTH / 2 - self.voltage_source.get_width() / 2 - 1.1) * LEFT + 0.5 * UP),
                ApplyMethod(resistor_group.set_height, 4.5),
                ApplyMethod(self.resistor.set_stroke, WHITE, DEFAULT_WIRE_THICKNESS * 1.3, run_time=0.01),
            )
        )

        rtitle=self.get_resistor_title()
        self.play(
            Write(rtitle)
        )

        resistor_def=TextMobject(
            "electrical element with a constant resistance to the\\\\ passage of electric current through its two ports.",
            color=YELLOW) \
            .scale(1.45) \
            .to_corner(DOWN)
        self.play(
            FadeIn(resistor_def)
        )

        rimages=self.get_resistor_images_labels()
        for image in rimages:
            self.play(
                FadeIn(image)
            )
        # for label in eq_labels:
        #     self.play(
        #         Write(label, run_time=0.7)
        #     )

        self.wait(2)

        # move resistor back into circuit
        self.play(
            *[FadeOut(img) for img in rimages],
            # *[FadeOut(label) for label in eq_labels],
            FadeOut(rtitle),
            FadeOut(resistor_def)
        )
        self.play(
            Succession(
                ApplyMethod(self.resistor.move_to, orig_r_loc),
                ApplyMethod(self.resistor.set_height, orig_r_height),
            ),
            Succession(
                ApplyMethod(self.r_text.move_to, orig_r_text_loc),
                ApplyMethod(self.r_text.set_height, orig_r_text_height),
            )
        )
        self.play(
            FadeIn(self.voltage_source),
            FadeIn(self.wires),
            FadeIn(self.orig_vs_text)
        )

    def show_real_circuit(self):
        real_circuit = ImageMobject("images/ep1/SimpleDCCircuit/real_circuit.jpg")\
            .scale(2.1)\
            .next_to(self.r_text,direction=RIGHT,buff=2)
        self.play(
            FadeIn(
                real_circuit
            )
        )
        self.wait(2)
        self.play(
            FadeOut(
                real_circuit
            )
        )

    def get_comps_display(self):
        comps_list = [Resistor(),
                      Capacitor().scale(0.9),
                      Inductor(),
                      VoltageSource(),
                      CurrentSource(),
                      DependentCurrentSource(),
                      DependentVoltageSource(),
                      OpAmp(),
                      NPNTransistor(),
                      Mosfet(),
                      EnhancedPChannelMosfet(),
                      ]

        invisible_dot=Dot(color=BLACK, opacity=0)

        comps_rect = Rectangle(height=2.5,width=7.5)
        comps_rect.add(invisible_dot)
        comps_rect.to_edge(RIGHT,buff=0).shift(2.1*UP)

        comps_label = TextMobject("\\underline{Electrical Elements}",
                                  color=YELLOW).scale(1.35)
        comps_label.next_to(comps_rect,direction=UP)

        comps_list[1].add_updater(lambda x: x.move_to(invisible_dot.get_center()))
        comps_list[0].add_updater(lambda x: x.next_to(comps_list[1],direction=LEFT,buff=1))
        for i in range(2,len(comps_list)):
            comps_list[i].add_updater(lambda x,i=i: x.next_to(comps_list[i-1],direction=RIGHT,buff=1))

        def delete_at(mobject,del_point):
            if mobject.get_center()[0] < del_point:
                mobject.set_fill(BLACK,opacity=0)
                mobject.set_stroke(BLACK,opacity=0)

        for comp in comps_list:
            comp.add_updater(lambda x: delete_at(x, -0.3))

        block_rect = Rectangle(color=BLACK,height=comps_rect.get_height(),width=2.5)
        block_rect.set_fill(BLACK,opacity=1)
        block_rect.next_to(comps_rect,direction=LEFT,buff=0.03)
        block_rect.set_height(comps_rect.get_height())
        block_rect2=Rectangle(color=BLACK, height=comps_rect.get_height(), width=2)
        block_rect2.set_fill(BLACK, opacity=1)
        block_rect2.next_to(comps_rect, direction=RIGHT, buff=0.03)
        block_rect2.set_height(comps_rect.get_height())

        return comps_rect , comps_list , invisible_dot , block_rect , block_rect2 , comps_label

    def setup_hydraulic_circuit(self):
        self.hydraulic_circuit=HydraulicCircuit(initial_pressure=30).scale(0.75)
        self.hydraulic_circuit.next_to(self.electrical_circuit,
                                       direction=RIGHT,
                                       aligned_edge=UP,
                                       buff=3.9)
        # self.hydraulic_circuit.shift(0.8 * DOWN)
        self.hydraulic_circuit.add_updater(
            lambda x:
            x.top_pressure.set_value(0.833 * self.voltage_value.get_value() + 30)
        )

    def get_resistor_images_labels(self):
        r_left = ImageMobject("images/ep1/SimpleDCCircuit/resistor2.jpg")\
            .scale(1.6)\
            .next_to(self.r_text,direction=RIGHT,buff=0.4)\
            .shift(1.25*UP)
        r_mid = ImageMobject("images/ep1/SimpleDCCircuit/resistor_in_circuit.jpg")\
            .scale(1.6)\
            .next_to(r_left,direction=RIGHT)
        light = ImageMobject("images/ep1/SimpleDCCircuit/light_bulb.jpg")\
            .scale(1.7)\
            .next_to(r_mid,direction=RIGHT)

        return [r_left, r_mid, light]

    def get_resistor_title(self):
        rtitle = TextMobject("\\underline{Resistor}")
        rtitle.scale(1.8)
        rtitle.to_edge(UP, buff=0.4)
        return rtitle

    def get_vs_label(self):
        vs_label = TextMobject("\\underline{Voltage Source}", " / \\underline{Independent Voltage Source}")
        vs_label.scale(1.6)
        vs_label.to_edge(UP, buff=0.4)
        vs_label.shift(0.2*LEFT)
        return vs_label

    def get_rot_anim(self, run_time=1, ang_freq=np.pi):
        if self.rotate_fins:
            return Rotating(
                self.hydraulic_circuit.fins,
                radians=-run_time * ang_freq,
                run_time=run_time
            )
        else:
            return ShowCreation(self.null_dot)

    def get_electron_anim(self,
                          run_time=1,
                          freq=0.2):
        if self.freeze_electrons:
            return FadeIn(self.null_dot)
        else:
            return ApplyMethod(
                self.electron_loc.increment_value,
                run_time * freq,
                run_time=run_time,
                rate_func=linear
            )

    def vector_field_st(self, p):
        viscosity=8.90E-4
        R=abs(self.vf_x_max - self.vf_x_min) / 2.
        r=p[0] - (self.vf_x_min + self.vf_x_max) / 2.
        scale_factor=0.6E-1
        try:
            dPdx=self.pressure_value.get_value() / (self.hydraulic_circuit.body.small_tube[0].get_height())
        except AttributeError:
            dPdx=10 / (self.hydraulic_circuit.body.small_tube[0].get_height())

        # in small tube
        if self.vf_x_min < p[0] < self.vf_x_max:
            if self.vf_y_min < p[1] < self.vf_y_max:
                # print(f"{p[0]} -> {scale_factor*(1/(4*viscosity))*dPdx*(R**2-r**2)*DOWN}")
                # print(f"r = {r}, R = {R}")
                return scale_factor * (1 / (4 * viscosity)) * dPdx * (R ** 2 - r ** 2) * DOWN

        return 0 * UP

    def vector_field(self, p):
        large_tube=self.hydraulic_circuit.body.large_tube
        small_tube=self.hydraulic_circuit.body.small_tube
        PUM_circle=self.hydraulic_circuit.pump_circle
        mag=1

        # in pump
        if np.linalg.norm(p - self.hydraulic_circuit.body.circle.get_center()) < \
                (self.hydraulic_circuit.body.circle.get_width() / 2) * 0.8:
            return -self.start_ang_freq * self.rot_matrix.dot(p - self.hydraulic_circuit.body.circle.get_center())

        # region 1
        if large_tube[1].get_left()[0] < p[0] < \
                large_tube[0].get_left()[0]:
            if large_tube[1].get_bottom()[1] < p[1] < \
                    large_tube[0].get_top()[1] + 0.1:
                r=abs(p[0] - (large_tube[1].get_left()[0] + large_tube[0].get_left()[0]) / 2.)
                R=abs(large_tube[1].get_left()[0] - large_tube[0].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 2
        if large_tube[0].get_left()[0] < p[0] < \
                large_tube[0].get_right()[0] - 0.3:
            if large_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r=abs(p[1] - (large_tube[0].get_top()[1] + large_tube[1].get_top()[1]) / 2.)
                R=abs(large_tube[0].get_top()[1] - large_tube[1].get_top()[1]) / 2.
                return mag * RIGHT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 3
        if large_tube[0].get_right()[0] - 0.27 < p[0] < \
                large_tube[1].get_right()[0]:
            if small_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r=abs(p[0] - (large_tube[0].get_right()[0] - 0.27 + large_tube[1].get_right()[0]) / 2.)
                R=abs(large_tube[0].get_right()[0] - 0.27 - large_tube[1].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 4
        if large_tube[2].get_right()[0] - 0.3 < p[0] < \
                large_tube[3].get_right()[0]:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[3].get_top()[1]:
                r=abs(p[0] - (large_tube[2].get_right()[0] - 0.3 + large_tube[3].get_right()[0]) / 2.)
                R=abs(large_tube[2].get_right()[0] - 0.3 - large_tube[3].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 5
        if large_tube[2].get_left()[0] < p[0] < \
                large_tube[2].get_right()[0] - 0.3:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[2].get_bottom()[1]:
                r=abs(p[1] - (large_tube[3].get_bottom()[1] + large_tube[2].get_bottom()[1]) / 2.)
                R=abs(large_tube[3].get_bottom()[1] - large_tube[2].get_bottom()[1]) / 2.
                return mag * LEFT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 6
        if large_tube[3].get_left()[0] < p[0] < \
                large_tube[2].get_left()[0]:
            if large_tube[2].get_bottom()[1] < p[1] < \
                    large_tube[2].get_top()[1]:
                r=abs(p[0] - (large_tube[3].get_left()[0] + large_tube[2].get_left()[0]) / 2.)
                R=abs(large_tube[3].get_left()[0] - large_tube[2].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        return 0 * RIGHT

    def setup_vector_fields(self):
        self.vf_x_min=self.hydraulic_circuit.body.small_tube[1].get_center()[0] - 0.01
        self.vf_x_max=self.hydraulic_circuit.body.small_tube[0].get_center()[0] + 0.01
        self.vf_y_min=self.hydraulic_circuit.body.small_tube[1].get_bottom()[1]
        self.vf_y_max=self.hydraulic_circuit.body.small_tube[1].get_top()[1] + 0.2

        # add_hguide(self, large_tube[3].get_left()[0], color=GREEN)
        # add_hguide(self, large_tube[2].get_left()[0], color=RED)
        # add_vguide(self, large_tube[2].get_bottom()[1], color=GREEN)
        # add_vguide(self, large_tube[2].get_top()[1], color=RED)

        self.rot_matrix=np.array([[0, -1, 0],
                                  [1, 0, 0],
                                  [0, 0, 0]])

        # setup vector field in small tube
        self.stream_lines_yellow=StreamLines(
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
        self.stream_lines_st=StreamLines(
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
        self.animated_stream_lines_st=AnimatedStreamLines(
            self.stream_lines_st,
            line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )

        # setup vector field for pump
        stream_lines=StreamLines(
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

        self.animated_stream_lines=AnimatedStreamLines(
            stream_lines,
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3,
            line_anim_class=MyAnim,
            # line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )

    def setup_electrons(self):
        self.electron_vect_inter=VectorInterpolator([
            self.wires[0].get_top(),
            self.wires[1].get_right(),
            self.wires[3].get_bottom(),
            self.wires[4].get_left()
        ])
        self.electons_flowing=True
        self.electron_disps=[0] * self.num_of_electrons
        self.electrons=[]
        self.electron_loc=ValueTracker(0)
        for i in range(self.num_of_electrons):
            self.electrons+=[Electron()]
            self.electrons[-1].add_updater(
                partial(self.electron_updater, i=i),
                call_updater=True
            )

        # voltage source copy
        self.blocking_rect=Rectangle(
            fill_color=BLACK,
            fill_opacity=1,
            stroke_color=BLACK,
            stroke_opacity=1,
            width=self.voltage_source.get_width(),
            height=self.voltage_source.get_width()
        )
        self.blocking_rect.move_to(
            self.voltage_source.get_center()
        )
        self.voltage_source_cp=VoltageSource().scale(1.25)
        self.voltage_source_cp.move_to(self.voltage_source.get_center())
        self.voltage_source_cp.bottom_wire.set_stroke(WHITE, opacity=0)
        self.voltage_source_cp.top_wire.set_stroke(WHITE, opacity=0)

    def electron_updater(self, x, i):
        cur=(self.electron_loc.get_value() + i / self.num_of_electrons + self.electron_disps[i]) % 1

        # always move if electrons are flowing
        if self.electons_flowing:
            x.move_to(
                self.electron_vect_inter.interpolate(cur)
            )
            return

        # change due to random motion
        diff=(2 * random.random() - 1) * 0.005

        # down move if inside voltage source
        if 0.78 < (cur + diff) % 1 < 0.925:
            return

        x.move_to(
            self.electron_vect_inter.interpolate(
                (cur + diff) % 1
            )
        )
        self.electron_disps[i]+=diff

    def add_node_labels(self):
        self.setup_node_labels()
        self.play(
            FadeIn(self.top_node_label),
            FadeIn(self.bottom_node_label),
            FadeIn(self.label_lines)
        )

    def setup_circuit(self):
        self.voltage_value=ValueTracker(12)
        self.resistance_value=ValueTracker(2)
        self.current_value=ValueTracker(6)

        self.current_value.add_updater(
            lambda x:
            x.set_value(
                self.voltage_value.get_value() / self.resistance_value.get_value()
            )
        )

        self.voltage_source=VoltageSource()
        self.voltage_source.scale(1.25)
        self.voltage_source.to_corner(UL)
        self.voltage_source.shift(2.3 * DOWN + 1.8 * RIGHT)
        self.vs_text=DecimalNumber(0,
                                   num_decimal_places=0,
                                   unit="V",
                                   edge_to_fix=RIGHT,
                                   color=self.voltage_color,
                                   digit_to_digit_buff=0.052)
        self.vs_text.scale(1.75)
        self.vs_text.next_to(self.voltage_source, direction=LEFT, buff=0.1)
        self.vs_text.add_updater(
            lambda x:
            x.set_value(self.voltage_value.get_value())
        )
        self.resistor=Resistor().scale(1.25).set_stroke(WHITE, DEFAULT_WIRE_THICKNESS * 1.3)
        self.resistor.next_to(self.voltage_source, direction=RIGHT, buff=1.7)
        self.r_text=DecimalNumber(2,
                                  num_decimal_places=0,
                                  unit="\Omega",
                                  edge_to_fix=RIGHT,
                                  color=self.resistance_color,
                                  digit_to_digit_buff=0.052)
        self.r_text.add_updater(
            lambda x:
            x.set_value(self.resistance_value.get_value())
        )
        self.r_text.scale(1.75)
        self.r_text.next_to(self.resistor, direction=RIGHT, buff=0.4)
        self.wires=VGroup()
        self.wires.add(self.get_wire(self.voltage_source.get_top(),
                                     self.voltage_source.get_top() + 0.65 * UP))
        self.wires[0].shift(0.01 * LEFT)
        self.wires.add(self.get_wire(self.voltage_source.get_top() + 0.65 * UP,
                                     self.resistor.get_top() + 0.65 * UP))
        self.wires.add(self.get_wire(self.resistor.get_top() + 0.65 * UP,
                                     self.resistor.get_top()))
        self.wires.add(self.get_wire(self.resistor.get_bottom(),
                                     self.resistor.get_bottom() - 0.5 * UP))
        self.wires.add(self.get_wire(self.resistor.get_bottom() - 0.5 * UP,
                                     self.voltage_source.get_bottom() - 0.5 * UP))
        self.wires.add(self.get_wire(self.voltage_source.get_bottom() - 0.5 * UP,
                                     self.voltage_source.get_bottom()))

        self.ground=Ground().scale(0.3).next_to(self.wires[4], direction=DOWN, buff=0)
        self.ground.set_opacity(0)

        self.electrical_circuit = VGroup(
            self.voltage_source,
            *self.wires,
            self.resistor
        )

    def get_wire(self, start, end):
        return Line(start=start, end=end, stroke_width=7, color=WHITE)