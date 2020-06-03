from manimlib.imports import *

class SuccesionIssue(Scene):
    def construct(self):
        list = TextMobject(
            "cat\\\\",
            "dog\\\\",
            "fish\\\\",
        ).arrange(DOWN)
        self.play(
            Succession(
                Write(list[0]),
                Write(list[1]),
                Write(list[2]),
            )
        )

