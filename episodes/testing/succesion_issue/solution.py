from manimlib.imports import *

class SuccesionIssue(Scene):
    def construct(self):
        list = TextMobject(
            "cat\\\\", "dog\\\\","fish\\\\",
        ).arrange(DOWN)
        self.play(
            AnimationGroup(
                Write(list[0]),
                Write(list[1]),
                Write(list[2]),
                lag_ratio=1,
            )
        )