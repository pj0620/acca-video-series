from manimlib.imports import *

class Problem(Scene):
    def construct(self):
        num = DecimalNumber(
            12,
            unit="Amps"
        ).scale(3)

        def alignment_updater(x):
            x.unit_sign[0].next_to(VGroup(*x.submobjects[:-1]), direction=RIGHT, buff=x.digit_to_digit_buff)
            for i in range(1, len(x.unit_sign)):
                x.unit_sign[i].next_to(x.unit_sign[i - 1], direction=RIGHT, buff=x.digit_to_digit_buff,
                                         aligned_edge=DOWN)
            x.unit_sign[2].next_to(x.unit_sign[3], direction=LEFT, aligned_edge=UP, buff=x.digit_to_digit_buff)

        num.clear_updaters()
        num.add_updater(alignment_updater)
        self.add(num)
        self.wait()
        self.play(
            ApplyMethod(
                num.set_value,
                0
            )
        )
        self.wait()