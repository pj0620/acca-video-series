from manimlib.imports import *

class Problem(Scene):
    def construct(self):
        num = DecimalNumber(
            12,
            unit="Amps"
        )
        self.add(num)
        self.wait()