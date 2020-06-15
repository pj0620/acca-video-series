from datetime import datetime

from manimlib.imports import *
from phasorlib.cobject import *
from phasorlib.constants import *


class Stienmitz(Scene):
    def construct(self):
        # show inventors
        inventors=self.get_inventor_images()
        for inventor in inventors:
            self.play(
                FadeIn(inventor, run_time=1.5)
            )
        self.wait(1)

        # reduce height, move up inventors
        kw={
            "rate_func": lambda alpha: interpolate(
                0,
                2.6,
                alpha
            )
        }
        path=ParametricFunction(
            lambda t: t * UP + ORIGIN,
            t_min=0,
            t_max=2.6,
        )
        self.play(
            *[ApplyMethod(inventor.set_height, 2.9, run_time=1.7)
              for inventor in inventors],
        )
        self.play(
            MoveAlongPath(inventors[0], path, **kw, run_time=1.7),
        )

        # add steinmitz/einstien photo
        ae_cs_image = self.get_einstien_steinmitz_image()
        ae_cs_image.to_edge(DOWN)
        self.play(FadeInFrom(ae_cs_image,direction=DOWN))

        # label early architects
        architects_label = TextMobject("\\underline{Early Innovators}")
        architects_label.next_to(inventors[0],direction=UP)
        self.play(FadeInFrom(architects_label,direction=DOWN))

        # circle stienmitz
        R = 0.32
        cs_circ = Circle(radius=R,stroke_width=4,color=WHITE)
        cs_circ.shift(ae_cs_image.get_center() - 0.05*RIGHT + 0.7*UP)
        cs_arrow = Arrow(stroke_width=1000,color=WHITE)
        circ_point = cs_circ.get_center() + R*self.unit_vec(-1*PI/8)
        dir_vec = 0.7*self.unit_vec(-0.15*PI)
        cs_arrow.put_start_and_end_on(circ_point+dir_vec, circ_point)
        cs_text=TextMobject("Charles\\\\Stienmitz")
        cs_text.scale(1.14)
        cs_text.next_to(circ_point+dir_vec,direction=DR)
        cs_text.shift(0.28*UP + 0.4*LEFT)
        self.play(
            GrowArrow(cs_arrow),
            ShowCreation(cs_circ),
            Write(cs_text)
        )

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


        self.wait(10)
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
            FadeIn(cs_image)
        )

        # add pages to screen
        pages = self.get_paper(cs_image,n_pages=8)
        self.play(
            *[FadeIn(page) for page in pages]
        )
        self.wait(0.2)

        # scroll pages
        nil_dot = Dot()
        nil_dot.move_to(100*RIGHT)
        nil_text=TextMobject("kdkdkd")
        nil_text.move_to(100 * RIGHT)
        rect=Rectangle(width=8, height=4, color=BLACK, fill_opacity=1)
        rect.next_to(pages[0],direction=UP)
        rect.shift(2.6*DOWN)
        title_text = TextMobject("\\textbf{Complex Quantities and their}\\\\ "
                                 "\\textbf{use in Electrical Engineering}")
        title_text.scale(1.3)
        title_text.move_to(rect.get_center())
        title_text.shift(1*DOWN)
        self.play(
            ApplyMethod(
               pages[0].shift, 50 * UP,
               run_time=30,
               # pages[0].shift, 5 * UP,
               # run_time=3,
               rate_func=linear,
            ),
            LaggedStartMap(
                FadeIn,[nil_dot,rect],
                lag_ratio=0.9,run_time=4,
            ),
            LaggedStartMap(
                Write, [nil_text, title_text],
                lag_ratio=0.99999, run_time=5,
            )
        )

        self.wait(10)


    def get_paper(self,cs_image,n_pages=20,img_scale=5):
        pages = [ImageMobject("images/ep1/ComplexQuantitiesPaper/paper/img-01.png")]
        pages[0].scale(img_scale)
        pages[0].next_to(cs_image,direction=RIGHT,buff=2)
        for i in range(2, n_pages+1):
            page = ImageMobject("images/ep1/ComplexQuantitiesPaper/paper/img-{:02d}.png".format(i))
            page.scale(img_scale)
            page.add_updater(lambda x, i=i: x.next_to(pages[i - 2], direction=DOWN, buff=0.1))
            pages.append(page)

        return pages

    def get_stienmitz_image(self):
        cs_image=ImageMobject("images/ep1/ComplexQuantitiesPaper/portrait_cs_2.jpg")
        cs_image.to_edge(LEFT, buff=1)
        cs_image.scale(4)
        return cs_image

