from manimlib.imports import *

class Problem(Scene):
    def construct(self):
        equation_R = TexMobject("R(x)", " = ", "{f(x)", "\\over", "g(x)}")
        equation_R.set_color_by_tex("R(x)", PURPLE)
        equation_R.set_color_by_tex("f(x)", RED)
        equation_R.set_color_by_tex("g(x)", BLUE)

        equation_f = TexMobject("f(x)", "=", "x^3 + 4x^2 - 11x - 30")
        equation_f.set_color_by_tex("f(x)", RED)
        equation_f.shift(0.5 * UP)

        equation_g = TexMobject("g(x)", "=", "x^3 - 4x^2 + 5x - 2")
        equation_g.set_color_by_tex("g(x)", BLUE)
        equation_g.shift(0.5 * DOWN)

        self.play(Write(equation_R))
        self.wait(3)
        self.play(Transform(equation_R, target_mobject=equation_R),
                  ApplyMethod(equation_R.move_to, equation_R.get_center() + 3 * UP + 5 * LEFT))

        self.wait(3)

        self.play(Write(equation_f))
        self.wait()
        self.play(Write(equation_g))
        self.wait()

        grouped_equation = VGroup(equation_f, equation_g)

        self.play(ApplyMethod(grouped_equation.scale, 0.65))
        self.play(ApplyMethod(grouped_equation.move_to, grouped_equation.get_center() + 4 * LEFT))

        self.play(ReplacementTransform(equation_R[2], equation_f[2]))

        self.wait()

class Solution(Scene):
    def construct(self):
        equation_R = TexMobject("R(x)", " = ", "{f(x)", "\\over", "g(x)}")
        equation_R.set_color_by_tex("R(x)", PURPLE)
        equation_R.set_color_by_tex("f(x)", RED)
        equation_R.set_color_by_tex("g(x)", BLUE)

        equation_f = TexMobject("f(x)", "=", "x^3 + 4x^2 - 11x - 30")
        equation_f.set_color_by_tex("f(x)", RED)
        equation_f.shift(0.5 * UP)

        equation_g = TexMobject("g(x)", "=", "x^3 - 4x^2 + 5x - 2")
        equation_g.set_color_by_tex("g(x)", BLUE)
        equation_g.shift(0.5 * DOWN)

        self.play(Write(equation_R))
        self.wait(3)
        self.play(
            ApplyMethod(
                equation_R.move_to, equation_R.get_center() + 3 * UP + 5 * LEFT
            )
        )

        self.wait(3)

        self.play(Write(equation_f))
        self.wait()
        self.play(Write(equation_g))
        self.wait()

        grouped_equation = VGroup(equation_f, equation_g)

        # self.play(ApplyMethod(grouped_equation.scale, 0.65))
        self.play(ApplyMethod(grouped_equation.move_to, grouped_equation.get_center() + 4 * LEFT))

        scale_factor = 5
        left_point = equation_R[3].get_left()
        transform_matrix = np.array(
            [[scale_factor, 0, 0],
             [0,            1, 0],
             [0,            0, 1]]
        )
        def fun(p):
            return left_point + transform_matrix.dot(p-left_point)

        new_mid_x = equation_R[3].get_width() * scale_factor * 0.5 + equation_R[3].get_left()[0]
        self.play(
            ApplyPointwiseFunction(
                fun, equation_R[3],
                rate_func=linear,
                run_time=0.5
            ),
            ApplyMethod(
                equation_R[2].set_x, new_mid_x,
                rate_func=linear,
                run_time=0.5
            ),
            ApplyMethod(
                equation_R[4].set_x, new_mid_x,
                rate_func=linear,
                run_time=0.5
            )
        )
        self.play(
            ApplyMethod(
                equation_f[2].copy().move_to, equation_R[2].get_center()
            ),
            FadeOut(
                equation_R[2]
            )
        )
        self.play(
            ApplyMethod(
                equation_g[2].copy().move_to, equation_R[4].get_center()
            ),
            FadeOut(
                equation_R[4]
            )
        )

        self.wait()