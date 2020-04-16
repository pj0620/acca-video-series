from manimlib.imports import *

class CompareACDC(Scene):
    def construct(self):
        self.show_titles()
        self.show_dc_examples()
        self.show_ac_examples()

        self.wait(2)

    def show_titles(self):
        # SS6.1
        self.DC_title = TextMobject("\\underline{DC}")\
            .scale(2.5)\
            .to_edge(UP)\
            .shift(FRAME_WIDTH*0.25*LEFT)
        self.play(
            Write(
                self.DC_title
            )
        )

        # SS6.2
        self.AC_title = TextMobject("\\underline{AC}")\
            .scale(2.5)\
            .to_edge(UP)\
            .shift(FRAME_WIDTH*0.25*RIGHT)
        self.play(
            Write(
                self.AC_title
            )
        )

    def show_dc_examples(self):
        # SS6.3
        phone_image=ImageMobject("images/ep1/CompareACDC/cell-phone.png") \
            .scale(2.5) \
            .next_to(self.DC_title, direction=DOWN, buff=0.5) \
            .shift(3 * LEFT)
        self.play(
            FadeInFrom(
                phone_image,
                direction=LEFT
            )
        )

        # SS6.4
        computer=ImageMobject("images/ep1/CompareACDC/computer.jpeg") \
            .scale(2) \
            .next_to(phone_image, direction=RIGHT, buff=0) \
            .shift(1.2 * LEFT)
        self.play(
            FadeIn(
                computer
            )
        )

    def show_ac_examples(self):
        outlet_US = ImageMobject("images/ep1/CompareACDC/outlet-US.jpg")\
            .scale(1.8)\
            .next_to(self.AC_title,direction=DOWN,buff=0.3)\
            .shift(1*LEFT)
        self.play(
            FadeInFrom(
                outlet_US,
                direction=RIGHT
            )
        )

        outlet_EU = ImageMobject("images/ep1/CompareACDC/outlet-EU.jpg")\
            .scale(1.7)\
            .next_to(outlet_US,direction=RIGHT,buff=0.1)
        self.play(
            FadeInFrom(
                outlet_EU,
                direction=RIGHT
            )
        )

        utility_pole = ImageMobject("images/ep1/CompareACDC/utility_pole.jpg")\
            .scale(2)\
            .next_to(self.AC_title,direction=DOWN,buff=4.25)
        self.play(
            FadeInFrom(
                utility_pole,
                direction=RIGHT
            )
        )