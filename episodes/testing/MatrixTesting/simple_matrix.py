from manimlib.imports import *

class SimpleMatrix(Scene):
    def construct(self):
        array = Matrix([2, 1, 3]).scale(2)
        x, y, z = array.get_mob_matrix().flatten()
        brackets = array.get_brackets()
        x.set_color(X_COLOR)
        y.set_color(Y_COLOR)
        z.set_color(Z_COLOR)

        self.add(brackets)
        for mob in x, y, z:
            self.play(Write(mob), run_time=2)
        self.wait()