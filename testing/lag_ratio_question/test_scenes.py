from manimlib.imports import *


class EmVe(Scene):
    def construct(self):
        text = TextMobject("Text")
        text1=TextMobject("meh")
        text1.move_to(UP+RIGHT)
        text.move_to(DOWN+LEFT)
        self.wait(0.3)
        self.play(
            AnimationGroup(
                Write(text1),
                Write(text),
                lag_ratio=1
            )
        )
        self.wait()