from manimlib.imports import *

class IntroduceACDC(Scene):
    CONFIG={
        "circuit_color": BLUE_C
    }
    def construct(self):
        # show ACCA
        acca_text = TextMobject(
            "AC", "Circuit", "Analysis",
            arg_separator=" ",
        )\
            .scale(2.5)\
            .to_edge(UP,buff=3)
        self.play(
            FadeInFrom(
                acca_text,
                direction=UP
            )
        )
        self.wait(3.57)

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
        self.wait(1.1)

        # indicate Circuit
        brace_Circuit = Brace(acca_text[0], color=self.circuit_color)
        text_Circuit = brace_Circuit.get_text("???").set_color(self.circuit_color)
        self.play(
            Write(
                VGroup(
                    brace_Circuit, text_Circuit
                )
            ),
            ApplyMethod(
                acca_text[0].set_color,
                self.circuit_color
            )
        )
        self.wait(1.67)

        # move to title
        self.play(
            ApplyMethod(
                acca_text[0].move_to,
                FRAME_HEIGHT*0.5*UP - acca_text[0].get_height()*0.5*UP - 0.3*UP
            ),
            FadeOutAndShift(
                acca_text[1],
                direction=RIGHT
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

        # underline Circuit
        underline = Line(LEFT, RIGHT, color=self.circuit_color)
        underline.match_width(acca_text[0])
        underline.scale(1.1)
        underline.next_to(acca_text[0], DOWN, SMALL_BUFF)
        self.play(
            Write(
                underline
            )
        )

        self.wait()