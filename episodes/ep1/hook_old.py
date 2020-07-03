from manimlib.imports import *
from accalib.electrical_circuits import ComplexCircuitTimeDomain, ComplexCircuitFreqDomain, SimpleCircuitTimeDomain

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
               run_time=7.68,
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
        "dt_color": YELLOW,
        # "x_min": -10,
        # "x_max": 10,
        # "y_min": -1.5,
        # "y_max": 1.5,
        # "graph_origin": ORIGIN,
        # "function_color": RED,
        # "axes_color": GREEN,
        # "x_labeled_nums": range(-10, 12, 2),
    }
    def construct(self):
        # add time domain circuit
        time_domain_circuit = ComplexCircuitTimeDomain(
            current_color=self.current_color,
            voltages_color=self.voltage_colors,
        )\
            .scale(0.75)\
            .to_corner(UL, buff=0)\
            .shift(0.1*DOWN)
        self.play(
            FadeIn(time_domain_circuit)
        )
        self.wait(4.7)

        # add unknown variables
        unknown_variables = VGroup(
            *[
                SingleStringTexMobject(f"V_{i}").set_color(self.voltage_colors[i])
                for i in range(5)
            ]
        ) \
            .scale(1) \
            .arrange(RIGHT, buff=0.5) \
            .to_corner(UR)\
            .shift(2*DOWN)
        uv_brace = Brace(unknown_variables, direction=UP)
        uv_text = uv_brace.get_text("Nodal Voltages")
        self.play(
            Write(uv_text)
        )
        self.play(
            AnimationGroup(
                *[
                    TransformFromCopy(
                        time_domain_circuit.v_texts[i],
                        unknown_variables[i],
                        run_time=0.44
                    )
                    for i in range(5)
                ],
                lag_ratio=0.5
            )
        )

        # label nodal voltages
        self.play(
            GrowFromCenter(uv_brace),
        )
        self.wait(2.33)

        # move to top corner
        self.play(
            Succession(
                ApplyMethod(
                    time_domain_circuit.scale, 0.666,
                ),
                ApplyMethod(
                    time_domain_circuit.to_corner, UL,
                    buff=0
                )
            )
        )
        self.wait(1.03)

        # add diff eq
        diff_eqs = self.get_diff_eqs() \
            .scale(0.56) \
            .next_to(time_domain_circuit, direction=DOWN, aligned_edge=LEFT)
        methods_arrow = CurvedArrow(
            start_point=time_domain_circuit.get_right() + 0.2 * RIGHT,
            end_point=diff_eqs.get_corner(UR) + 0.5 * UL,
            angle=-TAU / 4
        )
        methods_list = BulletedList(
            "KVL",
            "KCL",
            "Ohm's Law"
        ) \
            .scale(0.8) \
            .next_to(methods_arrow, direction=UR) \
            .shift(0.5*LEFT + 0.5*DOWN)
        self.play(
            AnimationGroup(
                *[
                    FadeIn(method)
                    for method in methods_list
                ],
                lag_ratio=1
            )
        )
        self.play(
            ShowCreation(methods_arrow)
        )
        self.wait(0.4)
        self.play(
            Write(diff_eqs)
        )
        self.wait(6.93)

        very_difficult = TextMobject(
            "Difficult To Solve",
            color=RED
        ) \
            .scale(1.5) \
            .next_to(diff_eqs, direction=RIGHT)
        self.play(
            Write(
                very_difficult
            )
        )
        self.wait(2.07)

        self.remove(very_difficult)
        solutions_arrow = CurvedArrow(
            start_point=diff_eqs.get_corner(DR)+2*LEFT+1*UP,
            end_point=diff_eqs.get_corner(DR)+3*RIGHT+1.5*UP,
            angle=TAU / 8
        )
        solve_diff_eq = TextMobject("Solve") \
            .scale(0.8) \
            .next_to(solutions_arrow, direction=DOWN)
        self.play(
            AnimationGroup(
                ShowCreation(solutions_arrow),
                Write(solve_diff_eq),
                lag_ratio=0.1
            )
        )

        solutions = self.get_time_domain_solutions() \
            .scale(0.9) \
            .next_to(diff_eqs.get_corner(DR)+3*RIGHT+1.5*UP, direction=UR) \
            .shift(0.4*LEFT)
        self.play(
            Write(solutions)
        )
        self.wait(4.97)

        self.play(
            *[
                FadeOut(mob)
                for mob in (time_domain_circuit, solutions_arrow, diff_eqs, methods_list, methods_arrow, uv_brace,
                            uv_text, unknown_variables, solve_diff_eq, solutions)
            ],
        )

        plane = NumberPlane(
            # x_line_frequency=1,
            # y_line_frequency=5,
        )

        funcs = [
            lambda x: 0.05*40     * np.cos(4*x*0.5+5.934),
            lambda x: 0.05*18.344 * np.cos(4*x*0.5+5.36),
            lambda x: 0.05*10.372 * np.cos(4*x*0.5+5.538),
            lambda x: 0.05*15.155 * np.cos(4*x*0.5+5.703),
            lambda x: 0.05*10.171 * np.cos(4*x*0.5+5.34),
        ]
        func_graphs = [
            plane.get_graph(funcs[i], color=self.voltage_colors[i])
            for i in range(5)
        ]
        self.play(
            ShowCreation(plane, lag_ratio=0.5)
        )
        solutions.to_corner(UL, buff=0.1)
        solutions.add_background_rectangle(BLACK,opacity=1)
        self.play(
            FadeIn(solutions)
        )
        self.wait(3.17)
        sine_label = TextMobject(
            "Sine waves",
            color=YELLOW
        )\
            .scale(1.5)\
            .next_to(func_graphs[0], direction=UP)\
            .shift(2*RIGHT)
        self.play(
            AnimationGroup(*[
                ShowCreation(func_graph)
                for func_graph in func_graphs
            ],
            lag_ratio=0.9
            ),
            AnimationGroup(
                FadeIn(Dot().shift(100*UR),run_time=5.53),
                Write(sine_label),
                lag_ratio=1,
            )
        )

        self.wait(14.09)

    def get_time_domain_solutions(self):
        solutions = TexMobject(
            "V_0", "&=", "40",     "\\hspace{1mm}cos(4t+5.934)\\textit{V}\\\\",
            "V_1", "&=", "18.344", "\\hspace{1mm}cos(4t+5.36)\\textit{V}\\\\",
            "V_2", "&=", "10.372", "\\hspace{1mm}cos(4t+5.538)\\textit{V}\\\\",
            "V_3", "&=", "15.155", "\\hspace{1mm}cos(4t+5.703)\\textit{V}\\\\",
            "V_4", "&=", "10.171", "\\hspace{1mm}cos(4t+5.34) \\textit{V} \\\\",
            substrings_to_isolate=[*[f"$V_{i}$" for i in range(5)], "$&=$"],
            alignment="",
            color=YELLOW
        )
        for i in range(5):
            solutions.get_part_by_tex(f"V_{i}").set_color(self.voltage_colors[i])
        solutions.get_parts_by_tex("&=").set_color(WHITE)
        Group(
            *[
                Group(*solutions.submobjects[4*i:4*(i+1)])
                for i in range(len(solutions)//4)
            ]
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        solutions[3].next_to(solutions[7], direction=UP, aligned_edge=LEFT, buff=0.25)
        return solutions

    def setup_matrices(self):
        self.a_matrix = Matrix(
            [["0"],
             ["0"],
             ["0"],
             ["0"],
             ["20 \\angle 15^\\circ"],
             ],
            element_alignment_corner=0*RIGHT,
            v_buff=1.5
        )
        self.M_matrix = Matrix(
            [
                ["{1\\over150}", "-{1\\over150}-{1\\over100}-j0.012", "{1\\over100}", "j0.004", "0"],
                ["0", "-{1\\over100}", "{1\\over200}+{1\\over100}-j0.05", "-{1\\over200}", "j0.05"],
                ["0", "j0.004", "{1\\over200}", "-{1\\over200}-j0.004", "0"],
                ["0", "0", "-j0.05", "0", "-{1\\over100}+j0.05"],
                ["1", "0", "0", "0", "0"]
            ],
            element_alignment_corner=0 * RIGHT,
            h_buff=4.5,
            v_buff=1.5
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
            v_buff=1.5
        )
        self.equals_matrix = TexMobject("=")

        volt_mobs = list(self.V_matrix.get_mob_matrix().flatten())
        for i, mob in enumerate(volt_mobs):
            mob.set_color(self.voltage_colors[i])

        unit_locs = [
            (0, 2), (0, 3), (0, 4),
            (1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18),
            (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
            (6, 3), (6, 4), (6, 5),
            (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10), (7, 13), (7, 14), (7, 15), (7, 16),
            (8, 3), (8, 4), (8, 5),
            (9, 1), (9, 2), (9, 3), (9, 4),
            (11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
            (12, 2), (12, 3), (12, 4),
            (13, 3), (13, 4), (13, 5), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12),
            (17, 2), (17, 3), (17, 4), (17, 5),
            (19, 3), (19, 4), (19, 5), (19, 8), (19, 9), (19, 10), (19, 11),
            (20, 0),
        ]
        matrix_mobs = list(self.M_matrix.get_mob_matrix().flatten())
        for x, y in unit_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.unit_color)

        j_locs = [
            (1, 13),
            (3, 0),
            (7, 12),
            (9, 0),
            (11, 0),
            (13, 7),
            (17, 1),
            (19, 7)
        ]
        for x, y in j_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.j_color)

        # color 20 \angle 15^\circ
        list(self.a_matrix.get_mob_matrix().flatten())[-1].set_color(self.unit_color)

        return VGroup(
            self.a_matrix,
            self.equals_matrix,
            self.M_matrix,
            self.V_matrix
        )\
            .scale(0.7)\
            .arrange(RIGHT)

    def get_freq_eqs(self):
        self.freq_eq1 = TexMobject(
            "0", "=",
            "{1", "\\over", "150}", "V_0", "+",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "-", "j", "0.012", "\\Bigg)", "V_1", "+",
            "{1", "\\over", "100}", "V_2", "+",
            "j", "0.004", "V_3"
        )
        self.freq_eq2 = TexMobject(
            "0", "=",
            "-{1", "\\over", "100}", "V_1", "+",
            "\\Bigg(", "{1", "\\over", "200}", "+", "{1", "\\over", "100}", "-", "j", "0.05", "\\Bigg)", "V_2", "+",
            "-{1", "\\over", "200}", "V_3", "+",
            "j", "0.05", "V_4"
        )
        self.freq_eq3 = TexMobject(
            "0", "=",
            "j", "0.004", "V_1", "+"
                                 "{1", "\\over", "200}", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "200}", "-", "j", "0.004", "\\Bigg)", "V_3",
        )
        self.freq_eq4 = TexMobject(
            "0", "=",
            "-", "j", "0.05", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "100}", "+", "j", "0.05", "\\Bigg)", "V_4",
        )
        self.freq_eq5 = TexMobject(
            "20 \\angle 15^{\\circ}", "=", "V_0",
        )
        self.second_last_eq = self.freq_eq4
        self.last_eq = self.freq_eq5

        self.V_texs = VGroup(
            VGroup(self.freq_eq1[5], self.freq_eq5[-1]),
            VGroup(self.freq_eq1[19], self.freq_eq2[5], self.freq_eq3[4]),
            VGroup(self.freq_eq1[-5], self.freq_eq2[-10], self.freq_eq3[-11], self.freq_eq4[5]),
            VGroup(self.freq_eq1[-1], self.freq_eq2[-5], self.freq_eq3[-1]),
            VGroup(self.freq_eq2[-1], self.freq_eq4[-1]),
        )
        for i in range(5):
            self.V_texs[i].set_color(self.voltage_colors[i])

        self.freq_eqs = VGroup(self.freq_eq1, self.freq_eq2, self.freq_eq3, self.freq_eq4, self.freq_eq5) \
            .arrange(DOWN, aligned_edge=LEFT)
        self.j_texs = VGroup(
            *[self.freq_eq1[i] for i in (16, -3)],
            *[self.freq_eq2[i] for i in (16, -3)],
            *[self.freq_eq3[i] for i in (2, -4)],
            *[self.freq_eq4[i] for i in (3, -4)],
        )
        self.j_texs.set_color(self.j_color)
        unit_texs = VGroup(
            *[self.freq_eq1[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq2[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq3[i] for i in (3, 7, 13, 16)],
            *[self.freq_eq4[i] for i in (4, 10, 13)],
            self.freq_eq5[0]
        )
        unit_texs.set_color(self.unit_color)

        brace = Brace(self.freq_eqs, direction=LEFT)
        eqs_group = VGroup(
            brace,
            self.freq_eqs
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
            "20", "cos(", "4", "t - ", "15^{\\circ}", ")", "=", "v_0"
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
            *[diff_eq5[i] for i in (0, 2, 4)],
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


class DiffyEqToComplexCopy(Scene):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN_C,
        # "voltage_color": RED_C,
        "voltage_colors": [GREEN ,RED, BLUE, TEAL_C, PURPLE_C],
        "unit_color": ORANGE,
        "j_color": YELLOW,
        "dt_color": YELLOW,
        # "x_min": -10,
        # "x_max": 10,
        # "y_min": -1.5,
        # "y_max": 1.5,
        # "graph_origin": ORIGIN,
        # "function_color": RED,
        # "axes_color": GREEN,
        # "x_labeled_nums": range(-10, 12, 2),
    }
    def construct(self):
        # add time domain circuit
        time_domain_circuit = ComplexCircuitTimeDomain(
            current_color=self.current_color,
            voltages_color=self.voltage_colors,
        )\
            .scale(0.5)\
            .to_corner(UL, buff=0)\
            .shift(0.1*DOWN)
        self.play(
            FadeIn(time_domain_circuit)
        )

        # add diff eq
        diff_eqs = self.get_diff_eqs() \
            .scale(0.56) \
            .next_to(time_domain_circuit, direction=DOWN, aligned_edge=LEFT)
        methods_arrow = CurvedArrow(
            start_point=time_domain_circuit.get_right() + 0.2 * RIGHT,
            end_point=diff_eqs.get_corner(UR) + 0.5 * UL,
            angle=-TAU / 4
        )
        methods_list = BulletedList(
            "KVL",
            "KCL",
            "Ohm's Law"
        ) \
            .scale(0.8) \
            .next_to(methods_arrow, direction=UR) \
            .shift(0.5*LEFT + 0.5*DOWN)
        self.play(
            AnimationGroup(
                *[
                    FadeIn(method)
                    for method in methods_list
                ],
                lag_ratio=1
            )
        )
        self.play(
            ShowCreation(methods_arrow)
        )
        self.wait(0.4)
        self.play(
            Write(diff_eqs)
        )
        self.wait(3.2)

        solutions_arrow = CurvedArrow(
            start_point=diff_eqs.get_corner(DR)+2*LEFT+1*UP,
            end_point=diff_eqs.get_corner(DR)+3*RIGHT+1.5*UP,
            angle=TAU / 8
        )
        solve_diff_eq = TextMobject("Solve") \
            .scale(0.8) \
            .next_to(solutions_arrow, direction=DOWN)
        self.play(
            AnimationGroup(
                ShowCreation(solutions_arrow),
                Write(solve_diff_eq),
                lag_ratio=0.1
            )
        )
        self.wait(2.07)

        solutions = self.get_time_domain_solutions() \
            .scale(0.9) \
            .next_to(diff_eqs.get_corner(DR)+3*RIGHT+1.5*UP, direction=UR) \
            .shift(0.4*LEFT)
        self.play(
            Write(solutions)
        )
        self.wait(2.97)

        self.play(
            Indicate(
                VGroup(
                    solve_diff_eq,
                    solutions_arrow
                ),
                run_time=3
            )
        )
        self.wait(8.1)

        self.play(
            Indicate(
                diff_eqs,
                run_time=3
            )
        )
        self.wait(8.96)

    def get_time_domain_solutions(self):
        solutions = TexMobject(
            "V_0", "&=", "40",     "\\hspace{1mm}cos(4t+5.934)\\textit{V}\\\\",
            "V_1", "&=", "18.344", "\\hspace{1mm}cos(4t+5.36)\\textit{V}\\\\",
            "V_2", "&=", "10.372", "\\hspace{1mm}cos(4t+5.538)\\textit{V}\\\\",
            "V_3", "&=", "15.155", "\\hspace{1mm}cos(4t+5.703)\\textit{V}\\\\",
            "V_4", "&=", "10.171", "\\hspace{1mm}cos(4t+5.34) \\textit{V} \\\\",
            substrings_to_isolate=[*[f"$V_{i}$" for i in range(5)], "$&=$"],
            alignment="",
            color=YELLOW
        )
        for i in range(5):
            solutions.get_part_by_tex(f"V_{i}").set_color(self.voltage_colors[i])
        solutions.get_parts_by_tex("&=").set_color(WHITE)
        Group(
            *[
                Group(*solutions.submobjects[4*i:4*(i+1)])
                for i in range(len(solutions)//4)
            ]
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        solutions[3].next_to(solutions[7], direction=UP, aligned_edge=LEFT, buff=0.25)
        return solutions

    def setup_matrices(self):
        self.a_matrix = Matrix(
            [["0"],
             ["0"],
             ["0"],
             ["0"],
             ["20 \\angle 15^\\circ"],
             ],
            element_alignment_corner=0*RIGHT,
            v_buff=1.5
        )
        self.M_matrix = Matrix(
            [
                ["{1\\over150}", "-{1\\over150}-{1\\over100}-j0.012", "{1\\over100}", "j0.004", "0"],
                ["0", "-{1\\over100}", "{1\\over200}+{1\\over100}-j0.05", "-{1\\over200}", "j0.05"],
                ["0", "j0.004", "{1\\over200}", "-{1\\over200}-j0.004", "0"],
                ["0", "0", "-j0.05", "0", "-{1\\over100}+j0.05"],
                ["1", "0", "0", "0", "0"]
            ],
            element_alignment_corner=0 * RIGHT,
            h_buff=4.5,
            v_buff=1.5
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
            v_buff=1.5
        )
        self.equals_matrix = TexMobject("=")

        volt_mobs = list(self.V_matrix.get_mob_matrix().flatten())
        for i, mob in enumerate(volt_mobs):
            mob.set_color(self.voltage_colors[i])

        unit_locs = [
            (0, 2), (0, 3), (0, 4),
            (1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18),
            (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
            (6, 3), (6, 4), (6, 5),
            (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10), (7, 13), (7, 14), (7, 15), (7, 16),
            (8, 3), (8, 4), (8, 5),
            (9, 1), (9, 2), (9, 3), (9, 4),
            (11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
            (12, 2), (12, 3), (12, 4),
            (13, 3), (13, 4), (13, 5), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12),
            (17, 2), (17, 3), (17, 4), (17, 5),
            (19, 3), (19, 4), (19, 5), (19, 8), (19, 9), (19, 10), (19, 11),
            (20, 0),
        ]
        matrix_mobs = list(self.M_matrix.get_mob_matrix().flatten())
        for x, y in unit_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.unit_color)

        j_locs = [
            (1, 13),
            (3, 0),
            (7, 12),
            (9, 0),
            (11, 0),
            (13, 7),
            (17, 1),
            (19, 7)
        ]
        for x, y in j_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.j_color)

        # color 20 \angle 15^\circ
        list(self.a_matrix.get_mob_matrix().flatten())[-1].set_color(self.unit_color)

        return VGroup(
            self.a_matrix,
            self.equals_matrix,
            self.M_matrix,
            self.V_matrix
        )\
            .scale(0.7)\
            .arrange(RIGHT)

    def get_freq_eqs(self):
        self.freq_eq1 = TexMobject(
            "0", "=",
            "{1", "\\over", "150}", "V_0", "+",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "-", "j", "0.012", "\\Bigg)", "V_1", "+",
            "{1", "\\over", "100}", "V_2", "+",
            "j", "0.004", "V_3"
        )
        self.freq_eq2 = TexMobject(
            "0", "=",
            "-{1", "\\over", "100}", "V_1", "+",
            "\\Bigg(", "{1", "\\over", "200}", "+", "{1", "\\over", "100}", "-", "j", "0.05", "\\Bigg)", "V_2", "+",
            "-{1", "\\over", "200}", "V_3", "+",
            "j", "0.05", "V_4"
        )
        self.freq_eq3 = TexMobject(
            "0", "=",
            "j", "0.004", "V_1", "+"
                                 "{1", "\\over", "200}", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "200}", "-", "j", "0.004", "\\Bigg)", "V_3",
        )
        self.freq_eq4 = TexMobject(
            "0", "=",
            "-", "j", "0.05", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "100}", "+", "j", "0.05", "\\Bigg)", "V_4",
        )
        self.freq_eq5 = TexMobject(
            "20 \\angle 15^{\\circ}", "=", "V_0",
        )
        self.second_last_eq = self.freq_eq4
        self.last_eq = self.freq_eq5

        self.V_texs = VGroup(
            VGroup(self.freq_eq1[5], self.freq_eq5[-1]),
            VGroup(self.freq_eq1[19], self.freq_eq2[5], self.freq_eq3[4]),
            VGroup(self.freq_eq1[-5], self.freq_eq2[-10], self.freq_eq3[-11], self.freq_eq4[5]),
            VGroup(self.freq_eq1[-1], self.freq_eq2[-5], self.freq_eq3[-1]),
            VGroup(self.freq_eq2[-1], self.freq_eq4[-1]),
        )
        for i in range(5):
            self.V_texs[i].set_color(self.voltage_colors[i])

        self.freq_eqs = VGroup(self.freq_eq1, self.freq_eq2, self.freq_eq3, self.freq_eq4, self.freq_eq5) \
            .arrange(DOWN, aligned_edge=LEFT)
        self.j_texs = VGroup(
            *[self.freq_eq1[i] for i in (16, -3)],
            *[self.freq_eq2[i] for i in (16, -3)],
            *[self.freq_eq3[i] for i in (2, -4)],
            *[self.freq_eq4[i] for i in (3, -4)],
        )
        self.j_texs.set_color(self.j_color)
        unit_texs = VGroup(
            *[self.freq_eq1[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq2[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq3[i] for i in (3, 7, 13, 16)],
            *[self.freq_eq4[i] for i in (4, 10, 13)],
            self.freq_eq5[0]
        )
        unit_texs.set_color(self.unit_color)

        brace = Brace(self.freq_eqs, direction=LEFT)
        eqs_group = VGroup(
            brace,
            self.freq_eqs
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
            "20", "cos(", "4", "t - ", "15^{\\circ}", ")", "=", "v_0"
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
            *[diff_eq5[i] for i in (0, 2, 4)],
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

class DiffyEqToComplexOnlyMath(Scene):
    CONFIG = {
        "stroke_width": 3,
        "current_color": GREEN_C,
        # "voltage_color": RED_C,
        "voltage_colors": [GREEN ,RED, BLUE, TEAL_C, PURPLE_C],
        "unit_color": ORANGE,
        "j_color": YELLOW,
        "dt_color": YELLOW,
        # "x_min": -10,
        # "x_max": 10,
        # "y_min": -1.5,
        # "y_max": 1.5,
        # "graph_origin": ORIGIN,
        # "function_color": RED,
        # "axes_color": GREEN,
        # "x_labeled_nums": range(-10, 12, 2),
    }
    def construct(self):
        # add diff eq
        diff_eqs = self.get_diff_eqs() \
            .scale(0.5) \
            .to_corner(UL, buff=0.1)\
            .shift(0.5*DOWN)
        freq_eqs = self.get_freq_eqs() \
            .scale(0.5) \
            .to_corner(UR, buff=0.1)\
            .shift(0.5*DOWN)
        self.play(
            FadeInFrom(
                diff_eqs,
                direction=LEFT
            )
        )

        complex_arrow = CurvedArrow(
            start_point=5*LEFT+freq_eqs.get_corner(DL),
            end_point=freq_eqs.get_corner(DL)+0.2*LEFT
        )
        complex_text = TextMobject("Using Complex Numbers")\
            .scale(0.9)\
            .next_to(complex_arrow, direction=DOWN)
        self.play(
            ShowCreation(complex_arrow),
            Write(complex_text)
        )
        self.wait(3.67)

        self.play(
            FadeInFrom(
                freq_eqs,
                direction=RIGHT
            )
        )
        self.wait(15.3)

        self.play(
            FadeOut(diff_eqs),
            FadeOut(complex_arrow),
            FadeOut(complex_text),
            ApplyMethod(
                freq_eqs.to_corner,
                UL
            )
        )
        self.wait(3.57)

        matrix_group = self.setup_matrices() \
            .scale(0.8) \
            .to_corner(DL)

        # add unknown variables
        unknown_variables = VGroup(
            *[
                SingleStringTexMobject(f"V_{i}").set_color(self.voltage_colors[i])
                for i in range(5)
            ]
        ) \
            .scale(1) \
            .arrange(RIGHT, buff=0.5) \
            .next_to(freq_eqs, direction=RIGHT, buff=2)
        self.play(
            AnimationGroup(
                *[
                    TransformFromCopy(
                        self.V_texs[i],
                        unknown_variables[i]
                    )
                    for i in range(5)
                ],
                lag_ratio=0
            )
        )

        # label unknown variables
        uv_brace = Brace(unknown_variables, direction=UP)
        uv_text = uv_brace.get_text("Unknown Variables")
        self.play(
            GrowFromCenter(uv_brace),
            Write(uv_text)
        )

        self.wait(2.5)

        # transform lhs of matrix equation elements (no brackets)
        lhs_elems = VGroup(
            *[
                eq[0]
                for eq in self.freq_eqs
            ]
        )
        lhs_entries = self.a_matrix.get_entries()
        self.play(
            AnimationGroup(
                *[
                    TransformFromCopy(
                        lhs_elems[i],
                        lhs_entries[i]
                    )
                    for i in range(5)
                ],
                lag_ratio=0
            )
        )

        # transform coefficients in equations to matrix
        eq_coef = [
            [VGroup(*self.freq_eq1[2:5]), VGroup(*self.freq_eq1[8:18]), VGroup(*self.freq_eq1[21:24]),
             VGroup(*self.freq_eq1[25:32]), None],
            [None, VGroup(*self.freq_eq2[2:5]), VGroup(*self.freq_eq2[8:18]), VGroup(*self.freq_eq2[21:24]),
             VGroup(*self.freq_eq2[26:32]), None],
            [None, VGroup(*self.freq_eq3[2:4]), VGroup(*self.freq_eq3[6:8]), VGroup(*self.freq_eq3[11:17]), None],
            [None, None, VGroup(*self.freq_eq4[2:5]), None, VGroup(*self.freq_eq4[8:14]), None],
            [None, None, None, None, None, None]
        ]
        for i in range(5):
            row_anims = []
            for j in range(5):
                if eq_coef[i][j] is None:
                    row_anims.append(
                        FadeIn(self.M_matrix.get_mob_matrix()[i, j])
                    )
                else:
                    row_anims.append(
                        TransformFromCopy(
                            eq_coef[i][j], self.M_matrix.get_mob_matrix()[i, j]
                        )
                    )
            self.play(AnimationGroup(*row_anims, lag_ratio=0))

        self.play(
            *[
                TransformFromCopy(
                    unknown_variables[i],
                    list(self.V_matrix.get_mob_matrix().flatten())[i]
                )
                for i in range(5)
            ]
        )

        self.play(
            *[
                Write(matrix.brackets)
                for matrix in (self.a_matrix, self.M_matrix, self.V_matrix)
            ],
            FadeIn(
                self.equals_matrix
            )
        )
        self.wait(19.27)

        c_brace = Brace(self.a_matrix, direction=UP)
        c_text = c_brace.get_text("$\\vec{c}$").shift(0.1 * DOWN).set_color(RED)
        self.play(
            ShowCreation(c_brace),
            Write(c_text)
        )
        M_brace = Brace(self.M_matrix, direction=UP)
        M_text = M_brace.get_text("$\\vec{M}$").shift(0.1 * DOWN).set_color(GREEN)
        self.play(
            ShowCreation(M_brace),
            Write(M_text)
        )
        x_brace = Brace(self.V_matrix, direction=UP)
        x_text = x_brace.get_text("$\\vec{x}$").shift(0.1 * DOWN).set_color(BLUE)
        self.play(
            ShowCreation(x_brace),
            Write(x_text)
        )

        self.wait(7)

    def get_time_domain_solutions(self):
        solutions = TexMobject(
            "V_0", "&=", "40",     "\\hspace{1mm}cos(4t+5.934)\\textit{V}\\\\",
            "V_1", "&=", "18.344", "\\hspace{1mm}cos(4t+5.36)\\textit{V}\\\\",
            "V_2", "&=", "10.372", "\\hspace{1mm}cos(4t+5.538)\\textit{V}\\\\",
            "V_3", "&=", "15.155", "\\hspace{1mm}cos(4t+5.703)\\textit{V}\\\\",
            "V_4", "&=", "10.171", "\\hspace{1mm}cos(4t+5.34) \\textit{V} \\\\",
            substrings_to_isolate=[*[f"$V_{i}$" for i in range(5)], "$&=$"],
            alignment="",
            color=YELLOW
        )
        for i in range(5):
            solutions.get_part_by_tex(f"V_{i}").set_color(self.voltage_colors[i])
        solutions.get_parts_by_tex("&=").set_color(WHITE)
        Group(
            *[
                Group(*solutions.submobjects[4*i:4*(i+1)])
                for i in range(len(solutions)//4)
            ]
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        solutions[3].next_to(solutions[7], direction=UP, aligned_edge=LEFT, buff=0.25)
        return solutions

    def setup_matrices(self):
        self.a_matrix = Matrix(
            [["0"],
             ["0"],
             ["0"],
             ["0"],
             ["20 \\angle 15^\\circ"],
             ],
            element_alignment_corner=0*RIGHT,
            v_buff=1.5
        )
        self.M_matrix = Matrix(
            [
                ["{1\\over150}", "-{1\\over150}-{1\\over100}-j0.012", "{1\\over100}", "j0.004", "0"],
                ["0", "-{1\\over100}", "{1\\over200}+{1\\over100}-j0.05", "-{1\\over200}", "j0.05"],
                ["0", "j0.004", "{1\\over200}", "-{1\\over200}-j0.004", "0"],
                ["0", "0", "-j0.05", "0", "-{1\\over100}+j0.05"],
                ["1", "0", "0", "0", "0"]
            ],
            element_alignment_corner=0 * RIGHT,
            h_buff=4.5,
            v_buff=1.5
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
            v_buff=1.5
        )
        self.equals_matrix = TexMobject("=")

        volt_mobs = list(self.V_matrix.get_mob_matrix().flatten())
        for i, mob in enumerate(volt_mobs):
            mob.set_color(self.voltage_colors[i])

        unit_locs = [
            (0, 2), (0, 3), (0, 4),
            (1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18),
            (2, 2), (2, 3), (2, 4),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
            (6, 3), (6, 4), (6, 5),
            (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10), (7, 13), (7, 14), (7, 15), (7, 16),
            (8, 3), (8, 4), (8, 5),
            (9, 1), (9, 2), (9, 3), (9, 4),
            (11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
            (12, 2), (12, 3), (12, 4),
            (13, 3), (13, 4), (13, 5), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12),
            (17, 2), (17, 3), (17, 4), (17, 5),
            (19, 3), (19, 4), (19, 5), (19, 8), (19, 9), (19, 10), (19, 11),
            (20, 0),
        ]
        matrix_mobs = list(self.M_matrix.get_mob_matrix().flatten())
        for x, y in unit_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.unit_color)

        j_locs = [
            (1, 13),
            (3, 0),
            (7, 12),
            (9, 0),
            (11, 0),
            (13, 7),
            (17, 1),
            (19, 7)
        ]
        for x, y in j_locs:
            matrix_mobs[x].submobjects[0].submobjects[y].set_color(self.j_color)

        # color 20 \angle 15^\circ
        list(self.a_matrix.get_mob_matrix().flatten())[-1].set_color(self.unit_color)

        return VGroup(
            self.a_matrix,
            self.equals_matrix,
            self.M_matrix,
            self.V_matrix
        )\
            .scale(0.7)\
            .arrange(RIGHT)

    def get_freq_eqs(self):
        self.freq_eq1 = TexMobject(
            "0", "=",
            "{1", "\\over", "150}", "V_0", "+",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "-", "j", "0.012", "\\Bigg)", "V_1", "+",
            "{1", "\\over", "100}", "V_2", "+",
            "j", "0.004", "V_3"
        )
        self.freq_eq2 = TexMobject(
            "0", "=",
            "-{1", "\\over", "100}", "V_1", "+",
            "\\Bigg(", "{1", "\\over", "200}", "+", "{1", "\\over", "100}", "-", "j", "0.05", "\\Bigg)", "V_2", "+",
            "-{1", "\\over", "200}", "V_3", "+",
            "j", "0.05", "V_4"
        )
        self.freq_eq3 = TexMobject(
            "0", "=",
            "j", "0.004", "V_1", "+"
                                 "{1", "\\over", "200}", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "200}", "-", "j", "0.004", "\\Bigg)", "V_3",
        )
        self.freq_eq4 = TexMobject(
            "0", "=",
            "-", "j", "0.05", "V_2", "+",
            "\\Bigg(", "-{1", "\\over", "100}", "+", "j", "0.05", "\\Bigg)", "V_4",
        )
        self.freq_eq5 = TexMobject(
            "20 \\angle 15^{\\circ}", "=", "V_0",
        )
        self.second_last_eq = self.freq_eq4
        self.last_eq = self.freq_eq5

        self.V_texs = VGroup(
            VGroup(self.freq_eq1[5], self.freq_eq5[-1]),
            VGroup(self.freq_eq1[19], self.freq_eq2[5], self.freq_eq3[4]),
            VGroup(self.freq_eq1[-5], self.freq_eq2[-10], self.freq_eq3[-11], self.freq_eq4[5]),
            VGroup(self.freq_eq1[-1], self.freq_eq2[-5], self.freq_eq3[-1]),
            VGroup(self.freq_eq2[-1], self.freq_eq4[-1]),
        )
        for i in range(5):
            self.V_texs[i].set_color(self.voltage_colors[i])

        self.freq_eqs = VGroup(self.freq_eq1, self.freq_eq2, self.freq_eq3, self.freq_eq4, self.freq_eq5) \
            .arrange(DOWN, aligned_edge=LEFT)
        self.j_texs = VGroup(
            *[self.freq_eq1[i] for i in (16, -3)],
            *[self.freq_eq2[i] for i in (16, -3)],
            *[self.freq_eq3[i] for i in (2, -4)],
            *[self.freq_eq4[i] for i in (3, -4)],
        )
        self.j_texs.set_color(self.j_color)
        unit_texs = VGroup(
            *[self.freq_eq1[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq2[i] for i in (4, 10, 14, 17, 23, 27)],
            *[self.freq_eq3[i] for i in (3, 7, 13, 16)],
            *[self.freq_eq4[i] for i in (4, 10, 13)],
            self.freq_eq5[0]
        )
        unit_texs.set_color(self.unit_color)

        brace = Brace(self.freq_eqs, direction=LEFT)
        eqs_group = VGroup(
            brace,
            self.freq_eqs
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
            "20", "cos(", "4", "t - ", "15^{\\circ}", ")", "=", "v_0"
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
            *[diff_eq5[i] for i in (0, 2, 4)],
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

class SolveMatrixProblem(Scene):
    CONFIG = {
        "voltage_colors": [GREEN, RED, BLUE, TEAL_C, PURPLE_C],
    }
    def construct(self):
        vec = lambda s: "\\vec{\\textbf{%s}}" % s
        inv = TexMobject("M^{-1}").shift(UP)
        inv.set_color(GREEN)
        inv2 = inv.copy()

        start = TexMobject("M", vec("x"), "=", vec("c"))
        interim = TexMobject("M^{-1}", "M", vec("x"), "=", "M^{-1}", vec("c"))
        end = TexMobject(vec("x"), "=", "M^{-1}", vec("c"))

        A, x, eq, v = start.split()
        A.set_color(GREEN)
        x.set_color(BLUE)
        v.set_color(RED)
        interim_mobs = [inv, A, x, eq, inv2, v]
        for i, mob in enumerate(interim_mobs):
            mob.interim = mob.copy().move_to(interim.split()[i])

        self.add(start)

        self.wait(14.03)
        self.play(
            Indicate(x)
        )
        self.wait(4.33)

        self.play(
            *[Transform(m, m.interim) for m in interim_mobs]
        )
        self.wait()

        product = VGroup(A, inv)
        product.brace = Brace(product)
        product.words = product.brace.get_text(
            "Cancels out"
        )
        product.words.set_color(BLUE)
        self.play(
            GrowFromCenter(product.brace),
            Write(product.words, run_time=1),
            product.set_color, BLUE
        )
        self.wait()
        self.play(*[
            ApplyMethod(m.set_color, BLACK)
            for m in (product, product.brace, product.words)
        ])
        self.wait()

        final_eq = VGroup(x, eq, v, inv2)
        self.play(
            ApplyMethod(
                final_eq.shift,
                5*LEFT
            )
        )

        V_matrix = Matrix(
            [
                ["V_0"],
                ["V_1"],
                ["V_2"],
                ["V_3"],
                ["V_4"],
            ],
            element_alignment_corner=0 * RIGHT,
            v_buff=1.5
        )\
            .next_to(final_eq, direction=RIGHT,buff=3)
        volt_mobs = list(V_matrix.get_mob_matrix().flatten())
        for i, mob in enumerate(volt_mobs):
            mob.set_color(self.voltage_colors[i])

        matrix_eq = TexMobject("&=").next_to(V_matrix, direction=RIGHT)
        res_matrix = Matrix(
            [
                ["40 \\angle 15^\\circ \\textit{V}"],
                ["18.344 \\angle 57.87^\\circ \\textit{V}"],
                ["10.372 \\angle 47.703^\\circ \\textit{V}"],
                ["15.155 \\angle 38.265^\\circ \\textit{V}"],
                ["10.171 \\angle 59.013^\\circ \\textit{V}"],
            ],
            element_alignment_corner=0 * RIGHT,
            v_buff=1.5
        ) \
            .next_to(matrix_eq, direction=RIGHT)

        implies = Arrow(
            start=final_eq.get_right(),
            end=V_matrix.get_left()
        )
        self.play(
            ShowCreation(implies),
            FadeIn(V_matrix),
            FadeIn(matrix_eq),
            FadeIn(res_matrix),
        )

        self.wait()