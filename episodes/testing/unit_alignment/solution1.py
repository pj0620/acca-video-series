from manimlib.imports import *

class Problem(Scene):
    def construct(self):
        num = DecimalNumber(
            12,
            unit="Amps"
        )
        num.add_updater(
            lambda x:
            VGroup(
                VGroup(*x.submobjects[:-1]),
                x.submobjects[-1]
            ).arrange(RIGHT,center=True)
        )
        self.add(num)
        self.wait()
        self.play(
            ApplyMethod(
                num.set_value,
                0
            )
        )
        self.wait()