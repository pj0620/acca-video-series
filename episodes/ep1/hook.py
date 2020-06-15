from manimlib.imports import *
from accalib.electrical_circuits import ComplexCircuitTimeDomain

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
        pages = self.get_paper(cs_image,n_pages=3)
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
               pages.shift, 20 * UP,
               run_time=5.96,
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
        "voltage_color": RED_C,
        "unit_color": ORANGE
    }
    def construct(self):
        time_domain_circuit = ComplexCircuitTimeDomain(
            current_color=self.current_color,
            voltage_color=self.voltage_color)\
            .scale(0.47)\
            .to_corner(UL, buff=0)\
            .shift(0.1*DOWN)
        diff_eqs = self.get_diff_eqs()\
            .scale(0.57)\
            .next_to(time_domain_circuit, direction=RIGHT)
        self.add(time_domain_circuit,diff_eqs)

        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT
            )
        )

        self.wait()

    def get_branch_currents(self):
        branch_currents = VGroup(
            TexMobject(
                "i_1", "=", "{v_0", "-", "v_1", "\\over", "150}"
            ),
            TexMobject(
                "i_2", "=", "0.001", "{d", "\\over", "dt}", "(", "v_3", "-", "v_1", ")"
            ),
            TexMobject(
                "i_3", "=", "{v_2", "-", "v_1", "\\over", "100}"
            ),
            TexMobject(
                "i_4", "=", "0.002", "{d", "v_1", "\\over", "dt}"
            ),
            TexMobject(
                "5", "{d", "i_5", "\\over", "dt}", "=", "v_2", "-", "v_4"
            ),
            TexMobject(
                "i_6", "=", "{v_4", "\\over", "100}"
            ),
            TexMobject(
                "i_7", "=", "{v_2", "-", "v_3", "\\over", "200}"
            ),
        )\
            .arrange(DOWN, aligned_edge=LEFT)
        VGroup(
            *[branch_currents[0][i] for i in (2, 4)],
            *[branch_currents[1][i] for i in (7, 9)],
            *[branch_currents[2][i] for i in (2, 4)],
            branch_currents[3][4],
            *[branch_currents[4][i] for i in (6, 8)],
            branch_currents[5][2],
            *[branch_currents[6][i] for i in (2, 4)],
        )\
            .set_color(self.voltage_color)
        VGroup(
            branch_currents[0][6],
            branch_currents[1][2],
            branch_currents[2][-1],
            branch_currents[3][2],
            branch_currents[4][0],
            branch_currents[5][-1],
            branch_currents[6][-1],
        ) \
            .set_color(self.unit_color)
        VGroup(
            branch_currents[0][0],
            branch_currents[1][0],
            branch_currents[2][0],
            branch_currents[3][0],
            branch_currents[4][2],
            branch_currents[5][0],
            branch_currents[6][0],
        )\
            .set_color(self.current_color)
        branch_currents = self.get_branch_currents()
        branch_currents_brace = Brace(branch_currents, direction=LEFT)
        branch_currents_text = branch_currents_brace.get_text("Branch Currents")
        bc_group = VGroup(
            branch_currents_text,
            branch_currents_brace,
            branch_currents,
        )

        return bc_group

    def get_KCLS(self):
        i_texts = VGroup(
            TexMobject(
                "0 = ", "i_1", "+", "i_2", "+", "i_3", "-", "i_4"
            ),
            TexMobject(
                "0 = ", "-", "i_7", "-", "i_3", "-", "i_5"
            ),
            TexMobject(
                "0 = ", "i_7", "-", "i_2"
            ),
            TexMobject(
                "0 = ", "i_5", "-", "i_6"
            )
        ) \
            .arrange(DOWN, aligned_edge=LEFT)
        VGroup(
            *[i_texts[0][i] for i in (1, 3, 5, 7)],
            *[i_texts[1][i] for i in (2, 4, 6)],
            *[i_texts[2][i] for i in (1, 3)],
            *[i_texts[3][i] for i in (1, 3)],
        ).set_color(self.current_color)

        KCLs = self.get_KCLS()
        KCLs_brace = Brace(KCLs, direction=LEFT)
        KCLs_text = KCLs_brace.get_text("KCLs")
        KCL_group = VGroup(
            KCLs_text,
            KCLs_brace,
            KCLs
        )

        return KCL_group

    def get_diff_eqs(self):
        diff_eq1 = TexMobject(
            "0 = ",
            "{1", "\\over", "150}", "v_0", " + ",
            "\\Bigg(-", "{1", "\\over", "150}", "-", "{1", "\\over", "100}", "\\Bigg)", "v_1", "+"
                                                                                               "{1", "\\over", "100}",
            "v_2", "-",
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

        # coloring
        unit_texs = VGroup(
            *[diff_eq1[i] for i in (3, 9, 13, 19, 18, 21, 27)],
            *[diff_eq2[i] for i in (3, 12, 16, 25, 33, 38)],
            *[diff_eq3[i] for i in (3, 8, 11, 17)],
            *[diff_eq4[i] for i in (2, 7, 12)],
        )
        unit_texs.set_color(self.unit_color)
        voltage_texs = VGroup(
            *[diff_eq1[i] for i in (4, 15, 19, 23, 29)],
            *[diff_eq2[i] for i in (5, 19, 27, 34, 39)],
            *[diff_eq3[i] for i in (4, 9, 13, 19)],
            *[diff_eq4[i] for i in (3, 8, 14)],
        )
        voltage_texs.set_color(self.voltage_color)
        diff_eqs = VGroup(diff_eq1, diff_eq2, diff_eq3, diff_eq4) \
            .arrange(DOWN, aligned_edge=LEFT)

        diff_eqs_brace = Brace(diff_eqs, direction=LEFT)
        diff_eqs_text = diff_eqs_brace.get_text("Differential Equations")
        diff_eqs_group = VGroup(
            diff_eqs_text,
            diff_eqs_brace,
            diff_eqs
        )

        return diff_eqs_group
