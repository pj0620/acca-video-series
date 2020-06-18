from manimlib.imports import *
from accalib.electrical_circuits import ComplexCircuitTimeDomain, ComplexCircuitFreqDomain

class Stienmitz(Scene):
    def construct(self):
        self.wait(4.53)

        # show inventors
        inventors=self.get_inventor_images()
        self.play(
            AnimationGroup(
                FadeIn(
                    inventors[0],
                    0.97
                ),
                FadeIn(
                    inventors[1],
                    0.97
                ),
                FadeIn(
                    inventors[2],
                    0.97
                ),
                lag_ratio=1
            )
        )
        self.wait(1.9)

        # reduce height, move up inventors
        self.play(
            *[
            ApplyMethod(
                inventor.set_height,
                2.9,
                run_time=1.7
            )
            for inventor in inventors
            ]
        )
        self.play(
            *[
                ApplyMethod(
                    inventor.shift,
                    (FRAME_HEIGHT*0.5 - inventor.get_height()*0.5 - 1)*UP,
                    buff=2
                )
                for inventor in inventors
            ]
        )
        self.wait(3.23)

        # label early architects
        architects_label = TextMobject("\\underline{Chief Architects}")
        architects_label.next_to(inventors[0],direction=UP)
        self.play(
            FadeInFrom(
                architects_label,direction=UP
            )
        )
        self.wait(2.7)

        # add steinmitz/einstien photo
        ae_cs_image = self.get_einstien_steinmitz_image()
        ae_cs_image.to_edge(DOWN)
        self.play(
            FadeInFrom(
                ae_cs_image, direction=DOWN
            )
        )
        self.wait(0.43)

        # circle stienmitz
        R = 0.32
        cs_circ = Circle(radius=R,stroke_width=4,color=WHITE)\
            .shift(ae_cs_image.get_center() - 0.05*RIGHT + 0.7*UP)
        cs_arrow = Arrow(stroke_width=1000,color=WHITE)
        circ_point = cs_circ.get_center() + R*self.unit_vec(-1*PI/8)
        dir_vec = 0.7*self.unit_vec(-0.15*PI)
        cs_arrow.put_start_and_end_on(circ_point+dir_vec, circ_point)
        cs_text = TextMobject("Charles\\\\Stienmitz")\
            .scale(1.14)\
            .next_to(circ_point+dir_vec,direction=DR)\
            .shift(0.28*UP + 0.4*LEFT)
        self.play(
            GrowArrow(cs_arrow),
            ShowCreation(cs_circ),
            Write(cs_text)
        )
        self.wait(3.97)

        # circle einstein
        ae_circ=Circle(radius=R, stroke_width=4, color=WHITE)
        ae_circ.shift(ae_cs_image.get_center() + 1 * LEFT + 1.2 * UP)
        ae_arrow=Arrow(stroke_width=5, color=WHITE)
        ae_circ_point=ae_circ.get_center() + R * self.unit_vec(1.25*PI)
        ae_dir_vec=0.65 * self.unit_vec(-0.75 * PI)
        ae_arrow.put_start_and_end_on(ae_circ_point + ae_dir_vec, ae_circ_point)
        ae_text=TextMobject("Albert\\\\Einstein!")
        ae_text.scale(1.14)
        ae_text.next_to(ae_circ_point + ae_dir_vec, direction=DOWN)
        ae_text.shift(0.1 * UP )
        self.play(
            GrowArrow(ae_arrow),
            ShowCreation(ae_circ),
            Write(ae_text)
        )

        self.wait(2.2)

    def unit_vec(self,angle):
        return math.cos(angle)*RIGHT + math.sin(angle)*UP

    def get_einstien_steinmitz_image(self):
        cs_ae_image = ImageMobject("images/ep1/Steinmitz/steinmetz-einstien-3.jpg")
        cs_ae_image.scale(2)
        return cs_ae_image

    def get_inventor_images(self, initial_height=8,scale_factor=2.8):
        ben_franklin=ImageMobject("images/ep1/Steinmitz/ben-franklin.jpg")
        ben_franklin.scale(scale_factor)
        ben_franklin.set_height(initial_height)
        tesla=ImageMobject("images/ep1/Steinmitz/tesla.jpg")
        tesla.scale(scale_factor)
        tesla.add_updater(
            lambda x: x.next_to(ben_franklin, direction=RIGHT, buff=0.1)
        )
        tesla.set_height(initial_height)
        edison=ImageMobject("images/ep1/Steinmitz/edison.jpg")
        edison.scale(scale_factor)
        edison.add_updater(
            lambda x: x.next_to(ben_franklin, direction=LEFT, buff=0.1)
        )
        edison.set_height(initial_height)

        return [ben_franklin, tesla, edison]


class ComplexQuantitiesPaper(Scene):
    def construct(self):
        # create charles stienmitz photo
        cs_image = self.get_stienmitz_image()
        self.play(
            FadeIn(
                cs_image,
                run_time=0.77
            )
        )

        # add pages to screen
        pages = self.get_paper(cs_image, n_pages=5)
        self.play(
            *[
                FadeIn(page)
                for page in pages
            ]
        )

        # scroll pages
        rect=Rectangle(width=8, height=4, color=BLACK, fill_opacity=1)\
            .next_to(pages[0],direction=UP)\
            .shift(2.6*DOWN)
        title_text = TextMobject("\\textbf{Complex Quantities and their}\\\\"
                                 "\\textbf{use in Electrical Engineering}")\
            .scale(1.3)\
            .move_to(rect.get_center())\
            .shift(1*DOWN)
        self.play(
            ApplyMethod(
               pages.shift, 35 * UP,
               run_time=10.05,
               rate_func=linear,
            ),
            FadeIn(
                rect
            ),
            Write(
                title_text
            ),
        )


    def get_paper(self, cs_image, n_pages=20, img_scale=5):
        pages = Group(
            *[
                ImageMobject("images/ep1/ComplexQuantitiesPaper/paper/img-{:02d}.png".format(i))
                .scale(img_scale)
                for i in range(1,n_pages+1)
            ]
        )
        pages\
            .arrange(DOWN, buff=0.1) \
            .next_to(cs_image, direction=RIGHT, buff=2, aligned_edge=UP)

        return pages

    def get_stienmitz_image(self):
        cs_image=ImageMobject("images/ep1/ComplexQuantitiesPaper/portrait_cs_2.jpg")
        cs_image.to_edge(LEFT, buff=1)
        cs_image.scale(4)
        return cs_image

class DiffyEqToComplex(Scene):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN_C,
        # "voltage_color": RED_C,
        "voltage_colors": [GREEN ,RED, BLUE, TEAL_C, PURPLE_C],
        "unit_color": ORANGE,
        "j_color": YELLOW,
        "dt_color": YELLOW
    }
    def construct(self):
        time_domain_circuit = ComplexCircuitTimeDomain(
            current_color=self.current_color,
            voltages_color=self.voltage_colors,
        )\
            .scale(0.5)\
            .to_corner(UL, buff=0)\
            .shift(0.1*DOWN)
        diff_eqs = self.get_diff_eqs()\
            .scale(0.56)\
            .next_to(time_domain_circuit, direction=DOWN, aligned_edge=LEFT)
        self.play(
            FadeIn(time_domain_circuit)
        )
        self.play(
            Write(diff_eqs)
        )
        self.wait(0.53)

        not_easy = TextMobject(
            "Not an easy to solve"
        )\
            .scale(1.5)\
            .next_to(diff_eqs, direction=RIGHT)
        self.play(
            FadeInFrom(
                not_easy,
                direction=RIGHT
            )
        )

        self.wait(6)

        freq_domain_circuit = ComplexCircuitFreqDomain(
            current_color=self.current_color,
            voltage_colors=self.voltage_colors,
            j_color=self.j_color
        ) \
            .scale(0.5) \
            .to_corner(UR, buff=0) \
            .shift(0.1 * DOWN + 2.1 * LEFT)
        freq_eqs = self.get_freq_eqs()\
            .scale(0.56)\
            .next_to(freq_domain_circuit, direction=DOWN, aligned_edge=LEFT)

        arrow1 = CurvedArrow(
            start_point=time_domain_circuit.get_right()+0.2*RIGHT,
            end_point=freq_domain_circuit.get_left()+0.5*RIGHT,
            angle=-TAU / 4
        )
        complex_num_text = TextMobject(
            "Using Complex Numbers"
        )\
            .scale(0.7)\
            .next_to(arrow1, direction=UP)
        self.remove(not_easy)
        self.play(
            ShowCreation(arrow1),
            FadeIn(complex_num_text),
        )
        self.wait(0.33)

        self.play(
            FadeIn(freq_domain_circuit),
            FadeIn(freq_eqs),
        )

        self.wait(9.83)

        # easier_to_solve = TextMobject(
        #     "Much easier to solve"
        # ) \
        #     .scale(0.8) \
        #     .next_to(freq_eqs, direction=LEFT, aligned_edge=DOWN) \
        #     .shift(0.5 * LEFT)
        # arrow2 = Arrow(
        #     start=easier_to_solve.get_right(),
        #     end=freq_eqs.get_corner(DL) + UP + 0.5 * RIGHT
        # )
        # self.play(
        #     Write(easier_to_solve),
        #     ShowCreation(arrow2)
        # )
        # self.wait(5.37)
        #
        # linear_algebra = TextMobject(
        #     "Solved with Linear Algebra"
        # ) \
        #     .scale(0.8) \
        #     .next_to(freq_eqs, direction=LEFT, aligned_edge=DOWN) \
        #     .shift(0.5 * LEFT)
        # self.play(
        #     Transform(
        #         easier_to_solve,
        #         linear_algebra
        #     )
        # )
        # self.wait(6.74)

        # self.play(
        #     Indicate(
        #         self.dt_texs,
        #         run_time=2
        #     )
        # )
        # self.wait(4.63)
        #
        # # fade out everything except freq_eqs
        # self.play(
        #     FadeOut(diff_eqs),
        #     FadeOut(freq_domain_circuit),
        #     FadeOut(time_domain_circuit),
        #     FadeOut(linear_algebra),
        #     FadeOut(easier_to_solve),
        #     FadeOut(arrow1),
        #     FadeOut(arrow2),
        #     FadeOut(complex_num_text),
        #     ApplyMethod(
        #         freq_eqs.to_edge,
        #         UL
        #     )
        # )

        # # TO SKIP SETUP UNCOMMENT
        # freq_eqs = self.get_freq_eqs() \
        #     .scale(0.56)\
        #     .to_edge(UL)
        # self.add(freq_eqs)

        # replace last freq_eq
        # new_last_eq = TexMobject(
        #     "V_0", " = ",
        #     "20 \\angle 15^{\\circ}",
        # ) \
        #     .scale(0.56)\
        #     .move_to(self.last_eq)
        # new_last_eq.align_to(self.second_last_eq, direction=LEFT)
        # new_last_eq[0].set_color(self.voltage_color)
        # new_last_eq[2].set_color(self.unit_color)
        # self.play(
        #     ReplacementTransform(
        #         self.last_eq,
        #         new_last_eq
        #     )
        # )

        # matrix_group = self.setup_matrices()\
        #     .to_corner(DL)
        # self.add(
        #     self.a_matrix,
        #     self.equals_matrix,
        #     self.M_matrix,
        #     self.V_matrix
        # )
        #
        # unknown_variables = VGroup(
        #     *[
        #         SingleStringTexMobject(f"V_{i}")
        #         for i in range(5)
        #     ]
        # ) \
        #     .scale(1) \
        #     .arrange(RIGHT, buff=0.5) \
        #     .next_to(freq_eqs, direction=RIGHT, buff=2)
        #
        # self.play(
        #     AnimationGroup(
        #         *[
        #             TransformFromCopy(
        #                 self.V_texs[i],
        #                 unknown_variables[i]
        #             )
        #             for i in range(5)
        #         ],
        #         lag_ratio=1
        #     )
        # )

        self.wait()

    def setup_matrices(self):
        self.a_matrix = Matrix(
            [["0"],
             ["0"],
             ["0"],
             ["0"],
             ["20 \\angle 15^\\circ"],
             ],
            element_alignment_corner=0*RIGHT,
        )
        self.M_matrix = Matrix(
            [
                ["0.0067", "- 0.0167 - j0.0012", "0.01", "j0.004", "0"],
                ["0", "-0.0067", "0.015 - j0.05", "-0.005", "j0.05"],
                ["0", "j0.004", "0.005", "-0.005-j0.004", "0"],
                ["0", "0", "-j0.05", "0.005", "-0.001+j0.05"],
                ["1", "0", "0", "0", "0"]
            ],
            element_alignment_corner=0 * RIGHT,
            h_buff=3.7,
        )
        self.V_matrix = Matrix(
            [
                ["V_0"],
                ["V_1"],
                ["V_2"],
                ["V_3"],
                ["V_4"],
            ],
            element_alignment_corner=0 * RIGHT,
        )
        self.equals_matrix = TexMobject("=")

        volt_mobs = list(self.V_matrix.get_mob_matrix().flatten())
        for mob in volt_mobs:
            mob.set_color(self.voltage_color)

        matrix_mobs = list(self.M_matrix.get_mob_matrix().flatten())
        for i in (0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 17, 18, 19, 20):
            matrix_mobs[i].set_color(self.unit_color)

        a_mobs = list(self.a_matrix.get_mob_matrix().flatten())
        for mob in a_mobs:
            mob.set_color(self.unit_color)

        return VGroup(
            self.a_matrix,
            self.equals_matrix,
            self.M_matrix,
            self.V_matrix
        )\
            .scale(0.7)\
            .arrange(RIGHT)


    def get_freq_eqs(self):
        eq1 = TexMobject(
            "0 = ",
            "{1", "\\over", "150}", "V_0", "+",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "-", "j", "0.012", "\\Bigg)", "V_1", "+",
            "{1", "\\over", "100}", "V_2", "+",
            "j", "0.004", "V_3"
        )
        eq2 = TexMobject(
            "0 = ",
            "-{1", "\\over", "100}", "V_1", "+",
            "\\Bigg(", "{1", "\\over", "200}", "+", "{1", "\\over", "100}", "-", "j", "0.05", "\\Bigg)", "V_2", "+",
            "-{1", "\\over", "200}", "V_3", "+",
            "j", "0.05", "V_4"
        )
        eq3 = TexMobject(
            "0 = ",
            "j", "0.004", "V_1", "+"
            "{1", "\\over", "200}", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "200}", "-", "j", "0.004", "\\Bigg)", "V_3",
        )
        eq4 = TexMobject(
            "0 = ",
            "-", "j", "0.05", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "100}", "+", "j", "0.05", "\\Bigg)", "V_4",
        )
        eq5 = TexMobject(
            "0 = ",
            "20 \\angle 15^{\\circ}", "-", "V_0",
        )
        self.second_last_eq = eq4
        self.last_eq = eq5

        self.V_texs = VGroup(
            VGroup(eq1[4], eq5[-1]),
            VGroup(eq1[18], eq2[4], eq3[3]),
            VGroup(eq1[-5], eq2[-10], eq3[-11], eq4[4]),
            VGroup(eq1[-1], eq2[-5], eq3[-1]),
            VGroup(eq2[-1], eq4[-1]),
        )
        for i in range(5):
            self.V_texs[i].set_color(self.voltage_colors[i])

        eqs = VGroup(eq1, eq2, eq3, eq4, eq5)\
            .arrange(DOWN,aligned_edge=LEFT)
        self.j_texs = VGroup(
            *[eq1[i] for i in (15, -3)],
            *[eq2[i] for i in (15, -3)],
            *[eq3[i] for i in (1, -4)],
            *[eq4[i] for i in (2, -4)],
        )
        self.j_texs.set_color(self.j_color)
        # voltage_texs = VGroup(
        #     *[eq1[i] for i in (4, 18, 23, 27)],
        #     *[eq2[i] for i in (4, 18, 23, 27)],
        #     *[eq3[i] for i in (3, 7, -1)],
        #     *[eq4[i] for i in (4, -1)],
        #     eq5[-1]
        # )
        # voltage_texs.set_color(self.voltage_color)
        unit_texs = VGroup(
            *[eq1[i] for i in (3, 9, 13, 16, 22, 26)],
            *[eq2[i] for i in (3, 9, 13, 16, 22, 26)],
            *[eq3[i] for i in (2, 6, 12, 15)],
            *[eq4[i] for i in (3, 9, 12)],
            eq5[1]
        )
        unit_texs.set_color(self.unit_color)

        brace = Brace(eqs, direction=LEFT)
        eqs_group = VGroup(
            brace,
            eqs
        )

        return eqs_group

    def get_diff_eqs(self):
        diff_eq1 = TexMobject(
            "0 = ",
            "{1", "\\over", "150}", "v_0", " + ",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "\\Bigg)", "v_1", "+"
            "{1", "\\over", "100}", "v_2", "-",
            "0.003", "{d", "v_1", "\\over", "dt}", "+",
            "0.001", "{d", "v_3", "\\over", "dt}",
        )
        diff_eq2 = TexMobject(
            "0 = ",
            "-{1", "\\over", "100}", "{d", "v_1", "\\over", "dt}", "+",
            "\\Bigg(", "{1", "\\over", "200}", "+", "{1", "\\over", "100}", "\\Bigg)", "{d", "v_2", "\\over", "dt}",
            "-",
            "{1", "\\over", "200}", "{d", "v_3", "\\over", "dt}", "+",
            "{1", "\\over", "5}", "v_2", "-",
            "{1", "\\over", "5}", "v_4",
        )
        diff_eq3 = TexMobject(
            "0 = ",
            "{1", "\\over", "200}", "v_2", "-",
            "{1", "\\over", "200}", "v_3", "-",
            "0.001", "{d", "v_3", "\\over", "dt}", "-",
            "0.001", "{d", "v_1", "\\over", "dt}",
        )
        diff_eq4 = TexMobject(
            "0 = "
            "{1", "\\over", "5}", "v_2", "-",
            "{1", "\\over", "5}", "v_4", "+",
            "{1", "\\over", "100}", "{d", "v_4", "\\over", "dt}",
        )
        diff_eq5 = TexMobject(
            "0 =",
            "20", "cos(", "4", "t - ", "15^{\\circ}", ")", "-", "v_0"
        )

        # coloring
        self.V_texs = VGroup(
            VGroup(diff_eq1[4], diff_eq5[-1]),
            VGroup(diff_eq1[15], diff_eq2[5], diff_eq1[-9], diff_eq3[-3]),
            VGroup(diff_eq1[19], diff_eq2[-6], diff_eq2[-21], diff_eq3[4], diff_eq4[3]),
            VGroup(diff_eq1[-3], diff_eq2[-13], diff_eq3[-9], diff_eq3[-13]),
            VGroup(diff_eq2[-1], diff_eq4[-3], diff_eq4[-9])
        )
        for i in range(5):
            self.V_texs[i].set_color(self.voltage_colors[i])

        self.dt_texs = VGroup(
            *[diff_eq1[i] for i in (-1, -2, -4, -7, -8, -10)],
            *[diff_eq2[i] for i in (4, 6, 7, 18, 20, 21, 26, 28, 29)],
            *[diff_eq3[i] for i in (12, 14, 15, 18, 20, 21)],
            *[diff_eq4[i] for i in (-1, -2, -4)],
        )
        self.dt_texs.set_color(self.dt_color)
        unit_texs = VGroup(
            *[diff_eq1[i] for i in (3, 9, 13, 18, 21, 27)],
            *[diff_eq2[i] for i in (3, 12, 16, 25, 33, 38)],
            *[diff_eq3[i] for i in (3, 8, 11, 17)],
            *[diff_eq4[i] for i in (2, 7, 12)],
            *[diff_eq5[i] for i in (1, 3, 5)],
        )
        unit_texs.set_color(self.unit_color)
        # voltage_texs = VGroup(
        #     *[diff_eq1[i] for i in (4, 15, 19, 23, 29)],
        #     *[diff_eq2[i] for i in (5, 19, 27, 34, 39)],
        #     *[diff_eq3[i] for i in (4, 9, 13, 19)],
        #     *[diff_eq4[i] for i in (3, 8, 14)],
        #     diff_eq5[-1]
        # )
        # voltage_texs.set_color(self.voltage_color)
        diff_eqs = VGroup(diff_eq1, diff_eq2, diff_eq3, diff_eq4, diff_eq5) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        diff_eqs_brace = Brace(diff_eqs, direction=LEFT)
        diff_eqs_group = VGroup(
            diff_eqs_brace,
            diff_eqs
        )

        return diff_eqs_group
