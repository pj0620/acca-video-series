from manimlib.imports import *


class ProblemSetup(Scene):
    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=YELLOW
            )
        )

        # add matrix
        M = IntegerMatrix(
            [[1, 0, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 0, 0, 1, 1]]
        )\
            .scale(2)
        self.play(
            Write(M.get_entries())
        )
        self.wait(2.23)

        # largest square
        rect = SurroundingRectangle(
            VGroup(*M.mob_matrix[0:3, 2:5].flatten()),
            buff=0.2
        )
        self.play(
            Write(rect)
        )
        self.wait(2.37)

        # label area
        area_label = TextMobject(
            "largest area = 9",
            color=YELLOW
        )\
            .scale(1.5) \
            .next_to(rect, direction=UP)
        self.play(
            Write(area_label)
        )

        self.wait(1.56)

class AnotherExample(Scene):
    def construct(self):
        # add matrix
        M = IntegerMatrix(
            [[1, 0, 0, 1, 1],
             [0, 1, 1, 1, 1],
             [1, 1, 0, 1, 0]]
        )\
            .scale(2)
        self.play(
            Write(M.get_entries())
        )
        self.wait(2.84)

        # largest square
        rect = SurroundingRectangle(
            VGroup(*M.mob_matrix[0:2, 3:].flatten()),
            buff=0.2
        )
        self.play(
            Write(rect)
        )
        self.wait(0.25)

        # label area
        area_label = TextMobject(
            "largest area = 4",
            color=YELLOW
        )\
            .scale(1.5) \
            .next_to(rect, direction=UP)
        self.play(
            Write(area_label)
        )

        self.wait(1.56)

class SolutionTimeComplexity(Scene):
    def construct(self):
        self.add(
            Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=YELLOW
            )
        )

        M = IntegerMatrix(
            [[1, 0, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 0, 0, 1, 1]]
        ) \
            .scale(1.25)\
            .to_edge(LEFT, buff=2)
        self.play(
            Write(M.get_entries())
        )

        # label time complexity
        time_complexity = TexMobject(
            "O(", "N", "M", ")",
            tex_to_color_map={
                "N": BLUE_C,
                "M": RED_C
            }
        ) \
            .scale(3) \
            .to_edge(RIGHT, buff=1.2)
        self.play(
            AnimationGroup(
                Write(time_complexity),
                Write(SurroundingRectangle(time_complexity, color=PURPLE_B, buff=0.3)),
                lag_ratio=0.1
            )
        )
        self.wait(0.77)

        # label height
        M_arrow = DoubleArrow(
            start=M.get_entries().get_corner(UL) + 1*LEFT,
            end=M.get_entries().get_corner(DL) + 1*LEFT,
            buff=0,
            color=RED_C
        )
        M_text = TexMobject(
            "M",
            color=RED_C
        )\
            .scale(1.5)\
            .next_to(M_arrow, direction=LEFT)

        # label length
        N_arrow = DoubleArrow(
            start=M.get_entries().get_corner(UL) + 1 * UP,
            end=M.get_entries().get_corner(UR) + 1 * UP,
            buff=0,
            color=BLUE_C
        )
        N_text = TexMobject(
            "N",
            color=BLUE_C
        ) \
            .scale(1.5) \
            .next_to(N_arrow, direction=UP)
        self.play(
            ShowCreation(N_arrow),
            Write(N_text),
            ShowCreation(M_arrow),
            Write(M_text)
        )

        self.wait(3.43)