from manimlib.imports import *
import itertools


class TimeComplexityComparison(Scene):
    def construct(self):
        time_complexity_dp = TexMobject(
            "O(", "N", "M", ")",
            tex_to_color_map={
                "N": BLUE_C,
                "M": RED_C
            }
        ) \
            .scale(2.5) \
            .to_edge(RIGHT, buff=1.2)
        title_dp = TextMobject(
            "\\underline{Dynamic Programming}",
            color=YELLOW
        ) \
            .scale(1.25) \
            .next_to(time_complexity_dp, direction=UP, buff=0.5)
        self.play(
            FadeInFrom(
                time_complexity_dp, direction=RIGHT
            ),
        )
        self.wait(0.96)

        time_complexity_new = TexMobject(
            "O((", "N", "M", ")^2)",
            tex_to_color_map={
                "N": BLUE_C,
                "M": RED_C
            }
        ) \
            .scale(2.5) \
            .to_edge(LEFT, buff=1.2)
        title_new = TextMobject(
            "\\underline{Old Algorithm}",
            color=YELLOW
        ) \
            .scale(1.25) \
            .next_to(time_complexity_new, direction=UP, buff=0.5)
        self.play(
            FadeInFrom(
                time_complexity_new, direction=LEFT
            ),
            FadeInFrom(
                title_new, direction=LEFT
            ),
        )

        # label "much faster"
        arrow = CurvedArrow(
            start_point=time_complexity_new.get_corner(DR) + DOWN * 0.2 + 0.3 * RIGHT,
            end_point=time_complexity_dp.get_corner(DL) + DOWN * 0.2 + 0.3 * LEFT,
            angle=TAU / 4,
            color=PURPLE_D
        )
        faster_text = TextMobject(
            "much faster",
            color=PURPLE_D
        ) \
            .next_to(arrow, direction=DOWN)
        self.play(
            ShowCreation(arrow),
            FadeIn(faster_text)
        )
        self.wait(4.7)

        self.play(
            FadeInFrom(title_dp, direction=RIGHT)
        )

        self.wait(4.78)


class SimpleExample(Scene):
    def construct(self):
        # show original matrix
        M = IntegerMatrix(
            [[1, 1, 1, 0],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 0, 1]],
            v_buff=1.0
        ) \
            .scale(1.3) \
            .to_edge(LEFT, buff=0.2) \
            .shift(1 * DOWN + 1.25 * RIGHT)
        self.play(
            FadeIn(M.get_entries())
        )
        self.wait(5.13)

        # show unfilled dp matrix
        dp = IntegerMatrix(
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],
            v_buff=1.0
        ) \
            .scale(1.3) \
            .to_edge(RIGHT, buff=0.2) \
            .shift(1 * DOWN + 1.25 * LEFT)
        dp_text = TextMobject(
            "dp", color=YELLOW_C
        ) \
            .scale(1.5) \
            .next_to(dp.get_entries(), direction=DOWN, buff=0.75)
        self.play(
            FadeIn(dp.get_entries())
        )
        self.wait(1.43)
        self.play(
            Write(dp_text)
        )
        self.wait(2.17)

        # show definition of dp(i,j)
        dp_def = TextMobject(
            "dp(", "i", ",", "j",
            ") = width of largest square in original matrix which \\\\has its bottom right corner at (", "i", ",", "j",
            ")",
            tex_to_color_map={
                "dp": YELLOW
            }
        ) \
            .scale(1.3) \
            .to_edge(UP, buff=0.5)
        dp_def[2].set_color(RED)
        dp_def[4].set_color(BLUE)
        dp_def[-4].set_color(RED)
        dp_def[-2].set_color(BLUE)
        self.play(Write(dp_def))
        self.wait(7.61)

        # fill out dp
        dp_vals = [
            [1, 1, 1, 0],
            [1, 2, 2, 1],
            [1, 2, 3, 1],
            [1, 1, 0, 1]
        ]
        self.play(
            AnimationGroup(
                *[
                    ApplyMethod(
                        dp.mob_matrix[i][j].set_value, dp_vals[i][j]
                    )
                    for i, j in itertools.product(range(4), range(4))
                ],
                lag_ratio=0.1
            )
        )
        self.wait(1.39)

        # label example point in dp
        square = Rectangle(
            width=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.5,
            height=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_center())
        square_dp = Rectangle(
            width=dp.get_mob_matrix()[1][1].get_height() + 0.3,
            height=dp.get_mob_matrix()[1][1].get_height() + 0.3,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(dp.get_mob_matrix()[1][1].get_center())
        self.play(
            FadeIn(square_dp)
        )
        self.wait(6.87)
        self.play(
            FadeIn(square)
        )
        self.wait(3.26)

        del_x = M.get_mob_matrix()[0][1].get_x() - M.get_mob_matrix()[0][0].get_x()
        del_y = M.get_mob_matrix()[0][0].get_y() - M.get_mob_matrix()[1][0].get_y()

        # shift right
        self.play(
            ApplyMethod(
                square.shift, del_x * RIGHT
            ),
            ApplyMethod(
                square_dp.shift, del_x * RIGHT
            )
        )
        self.wait(11.39)

        # move to 3 by 3 square
        square_new = Rectangle(
            width=VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.8,
            height=VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_center())
        self.play(
            Transform(
                square, square_new
            ),
            ApplyMethod(
                square_dp.shift, del_y * DOWN
            )
        )
        self.wait(10.61)
        self.play(
            FadeOut(square),
            FadeOut(square_dp)
        )
        self.wait(6.91)

        # label solution
        square_dp.set_color(GREEN)
        square.set_color(GREEN)
        self.play(
            FadeIn(square),
            FadeIn(square_dp)
        )

        # copy result into largest_area, and calculate
        largest_area_text = TexMobject(
            "\\text{largest\\_area} =", "(", "3", ")^2",
            color=GREEN
        ) \
            .scale(1.35) \
            .to_edge(DOWN)
        res = TexMobject("9", color=GREEN) \
            .scale(1.35) \
            .move_to(VGroup(*largest_area_text[1:]).get_center())
        self.play(
            FadeIn(largest_area_text[0]),
        )
        self.play(
            TransformFromCopy(
                dp.get_mob_matrix()[2, 2], largest_area_text[2]
            )
        )
        self.play(
            FadeIn(largest_area_text[1]),
            FadeIn(largest_area_text[3]),
        )
        self.play(
            ReplacementTransform(
                VGroup(*largest_area_text[1:]), res
            )
        )
        res_rect = SurroundingRectangle(
            largest_area_text,
            color=PURPLE,
            buff=0.3
        )
        self.play(
            ShowCreation(res_rect)
        )
        self.wait(7.91)

        # FadeOut results
        self.play(
            FadeOut(largest_area_text),
            FadeOut(res),
            FadeOut(square),
            FadeOut(square_dp),
            FadeOut(res_rect)
        )
        self.wait(1)

        # fill dp with question marks
        qm_anims = []
        for mob in dp.get_entries():
            qm = TextMobject("?").scale(1.3).move_to(mob.get_center())
            qm_anims.append(Transform(mob, qm))
        self.play(
            AnimationGroup(
                *qm_anims,
                lag_ratio=0.1
            )
        )
        self.wait(4.48)

        # fill dp with 0s
        qm_anims = []
        for mob in dp.get_entries():
            qm = TextMobject("0").scale(1.3).move_to(mob.get_center())
            qm_anims.append(Transform(mob, qm))
        self.play(
            AnimationGroup(
                *qm_anims,
                lag_ratio=0.1
            )
        )
        self.wait(0.48)

        # copy first column
        first_col_M_cp = VGroup(*M.get_mob_matrix()[:, 0].flatten()).copy()
        first_col_dp = VGroup(*dp.get_mob_matrix()[:, 0].flatten())
        col_rect = SurroundingRectangle(
            first_col_M_cp,
            color=RED,
            buff=0.3
        ) \
            .move_to(first_col_M_cp.get_center())
        self.play(
            Write(col_rect)
        )
        self.play(
            ApplyMethod(
                col_rect.move_to,
                first_col_dp.get_center()
            ),
            ApplyMethod(
                first_col_M_cp.move_to,
                first_col_dp.get_center()
            ),
            FadeOut(
                first_col_dp
            )
        )
        self.play(
            FadeOut(col_rect)
        )

        # copy first row
        first_row_M_cp = VGroup(*M.get_mob_matrix()[0, :].flatten()).copy()
        first_row_dp = VGroup(*dp.get_mob_matrix()[0, :].flatten())
        row_rect = SurroundingRectangle(
            first_row_M_cp,
            color=RED,
            buff=0.3
        ) \
            .move_to(first_row_M_cp.get_center())
        self.play(
            Write(row_rect)
        )
        self.play(
            ApplyMethod(
                row_rect.move_to,
                first_row_dp.get_center()
            ),
            ApplyMethod(
                first_row_M_cp.move_to,
                first_row_dp.get_center()
            ),
            FadeOut(
                VGroup(*first_row_dp[1:])
            ),
        )
        self.play(
            FadeOut(row_rect)
        )
        self.wait(16.56)

        # shows only squares < 2 possible in first row/column
        square_M_1 = Rectangle(
            width=M.get_mob_matrix()[0, 0].get_height() + 0.5,
            height=M.get_mob_matrix()[0, 0].get_height() + 0.5,
            # stroke_width=2,
            color=GREEN
        ) \
            .move_to(M.get_mob_matrix()[0, 0].get_center()) \
            .shift(del_x * RIGHT)
        square_M_2 = Rectangle(
            width=VGroup(*M.get_mob_matrix()[:2, :2].flatten()).get_height() + 0.5,
            height=VGroup(*M.get_mob_matrix()[:2, :2].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[:2, :2].flatten()).get_center()) \
            .shift(del_y * UP + 2 * del_x * RIGHT)
        square_M_3 = Rectangle(
            width=VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.75,
            height=VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[:3, :3].flatten()).get_center()) \
            .shift(2 * del_y * UP + del_x * RIGHT)
        no_text = TextMobject(
            "No", color=RED
        ) \
            .scale(1.5) \
            .next_to(M, direction=DOWN) \
            .shift(0.5 * DOWN)
        yes_text = TextMobject(
            "Yes", color=GREEN
        ) \
            .scale(1.5) \
            .move_to(no_text.get_center())
        cur_text = yes_text.copy()

        # show 1 in first row case
        self.play(
            FadeIn(square_M_1),
            FadeIn(cur_text)
        )
        self.wait(1.96)
        self.play(
            ShowCreationThenFadeOut(
                CurvedArrow(
                    start_point=square_M_1.get_corner(UR) + 0.1 * UR,
                    end_point=dp.get_mob_matrix()[0, 2].get_corner(UL) + 0.1 * UL,
                    angle=-TAU / 8,
                    color=PURPLE
                )
            )
        )
        self.wait(0.74)

        # show 0 in first row
        self.play(
            ApplyMethod(
                square_M_1.shift, 2 * del_x * RIGHT
            ),
            Transform(
                cur_text, no_text
            )
        )
        square_M_1.set_color(RED)
        self.wait(4.43)
        self.play(
            ShowCreationThenFadeOut(
                CurvedArrow(
                    start_point=square_M_1.get_corner(UR) + 0.1 * UR,
                    end_point=dp.get_mob_matrix()[0, 3].get_corner(UL) + 0.1 * UL,
                    angle=-TAU / 8,
                    color=PURPLE
                )
            )
        )

        self.play(
            ReplacementTransform(
                square_M_1, square_M_2
            ),
            Transform(
                cur_text, no_text
            )
        )

        # move around 2 by 2 square
        for _ in range(3):
            self.play(ApplyMethod(square_M_2.shift, del_x * LEFT))
        for _ in range(3):
            self.play(ApplyMethod(square_M_2.shift, del_y * DOWN))

        # convert 2 by 2 to 3 by 3
        self.play(
            ReplacementTransform(
                square_M_2, square_M_3
            ),
        )

        # move around 3 by 3 square
        for _ in range(3):
            self.play(ApplyMethod(square_M_3.shift, del_x * LEFT))
        for _ in range(3):
            self.play(ApplyMethod(square_M_3.shift, del_y * DOWN))

        # fade out square
        self.play(
            FadeOut(square_M_3),
            FadeOut(cur_text)
        )

        # show copying first row and column again
        # copy first column
        first_col_M_cp = VGroup(*M.get_mob_matrix()[:, 0].flatten()).copy()
        first_col_dp = VGroup(*dp.get_mob_matrix()[:, 0].flatten())
        col_rect = SurroundingRectangle(
            first_col_M_cp,
            color=RED,
            buff=0.3
        ) \
            .move_to(first_col_M_cp.get_center())
        self.play(
            Write(col_rect)
        )
        self.play(
            ApplyMethod(
                col_rect.move_to,
                first_col_dp.get_center()
            ),
            ApplyMethod(
                first_col_M_cp.move_to,
                first_col_dp.get_center()
            ),
            # FadeOut(
            #     first_col_dp
            # )
        )
        self.play(
            FadeOut(col_rect)
        )

        # copy first row
        first_row_M_cp = VGroup(*M.get_mob_matrix()[0, :].flatten()).copy()
        first_row_dp = VGroup(*dp.get_mob_matrix()[0, :].flatten())
        row_rect = SurroundingRectangle(
            first_row_M_cp,
            color=RED,
            buff=0.3
        ) \
            .move_to(first_row_M_cp.get_center())
        self.play(
            Write(row_rect)
        )
        self.play(
            ApplyMethod(
                row_rect.move_to,
                first_row_dp.get_center()
            ),
            ApplyMethod(
                first_row_M_cp.move_to,
                first_row_dp.get_center()
            ),
            # FadeOut(
            #     VGroup(*first_row_dp[1:])
            # ),
        )
        self.play(
            FadeOut(row_rect)
        )

        # replace all elements not in first row/column with question mark
        qm_anims = []
        for mob in dp.get_mob_matrix()[1:, 1:].flatten():
            qm = TextMobject("?").scale(1.3).move_to(mob.get_center())
            qm_anims.append(Transform(mob, qm))
        self.play(
            AnimationGroup(
                *qm_anims,
                lag_ratio=0.1
            )
        )

        self.wait(5)


class ThreeSquareProof(Scene):
    CONFIG = {
        "colors": ["#FF0000", "#00FF00", "#0000FF"],
        "square_fill_opacity": 0.3333,
        "square_stroke_color": WHITE,
        "final_corner": RIGHT,
        "unit_length": 1,
        "axes_config": {
            "axis_config": {
                "stroke_color": WHITE,
                "stroke_width": 2,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "number_scale_val": 0.5,
            },
            "y_axis_config": {
                "label_direction": DR,
            },
            "background_line_style": {
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 1,
            },
            # Defaults to a faded version of line_config
            "faded_line_style": None,
            "x_line_frequency": 1,
            "y_line_frequency": 1,
            "faded_line_ratio": 0,
            "make_smooth_after_applying_functions": True,
        }
    }

    def construct(self):
        # self.add(
        #     Rectangle(
        #         width=FRAME_WIDTH,
        #         height=FRAME_HEIGHT,
        #         color=YELLOW
        #     )
        # )

        grid = NumberPlane(**self.axes_config)
        self.add(grid)

        # add squares
        square_widths = [3, 4, 2]
        squares = VGroup(
            Square(
                side_length=square_widths[0],
                fill_color=self.colors[0],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length*LEFT + 0.5*square_widths[0]*UL),
            Square(
                side_length=square_widths[1],
                fill_color=self.colors[1],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length*UL + 0.5*square_widths[1]*UL),
            Square(
                side_length=square_widths[2],
                fill_color=self.colors[2],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length * UP + 0.5 * square_widths[2] * UL),
        )
        square_labels = VGroup(
            TextMobject("A", color="#FF0000").scale(3.1).next_to(squares[0], direction=DOWN).shift(0.1*UP).add_background_rectangle(),
            TextMobject("B", color="#00FF00").scale(3.1).next_to(squares[1], direction=LEFT).shift(0.1*UP).add_background_rectangle(),
            TextMobject("C", color="#0000FF").scale(3.1).next_to(squares[2], direction=UR).add_background_rectangle(),
        )
        self.wait(1.52)
        self.play(
            AnimationGroup(
                *[
                    AnimationGroup(
                        FadeIn(squares[i], 0.35),
                        FadeIn(square_labels[i], 0.35),
                        lag_ratio=0.8
                    )
                    for i in range(3)
                ],
                lag_ratio=0.5
            )
        )
        self.wait(1.26)

        # label corners
        corner_dots = VGroup(
            Dot().move_to(ORIGIN),
            Dot().move_to(UP),
            Dot().move_to(UR)
        )
        corner_labels = VGroup(
            TextMobject("(0,0)").scale(1.3).next_to(corner_dots[0], direction=UL, buff=0),
            TextMobject("(0,1)").scale(1.3).next_to(corner_dots[1], direction=UL, buff=0),
            TextMobject("(1,1)").scale(1.3).next_to(corner_dots[2], direction=UP, buff=0.15).shift(0.1*LEFT)
        )
        # corner_labels.set_color(YELLOW)
        corner_dots.set_color(YELLOW)
        self.play(
            AnimationGroup(
                *[
                    AnimationGroup(
                        FadeIn(corner_dots[i]),
                        FadeIn(corner_labels[i]),
                        lag_ratio=0.5
                    )
                    for i in range(3)
                ],
                lag_ratio=0.8
            )
        )

        # fadeout corner labels
        self.play(
            FadeOut(corner_dots),
            FadeOut(corner_labels)
        )
        self.wait(0.96)

        # create inital square
        new_dot = Dot().move_to(RIGHT).set_color(YELLOW)
        new_corner_label = TextMobject("(1,0)").scale(1.3).next_to(new_dot, direction=UR, buff=0).shift(0.1*RIGHT).add_background_rectangle()
        new_square = Square(
            side_length=1,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        )\
            .move_to(0.5*UR)
        self.play(
            FadeIn(new_square)
        )
        self.wait(1.04)
        self.play(
            AnimationGroup(
                FadeIn(new_dot),
                FadeIn(new_corner_label),
                lag_ratio=0.9
            )
        )

        # fade out corner label
        self.play(
            FadeOut(new_corner_label),
            FadeOut(new_dot)
        )
        self.wait(4.39)

        # indicate each square
        for i in range(3):
            squares[i].set_fill(self.colors[i], opacity=1)
            self.wait(0.3)
            squares[i].set_fill(self.colors[i], opacity=self.square_fill_opacity)
            self.wait(0.3)
        self.wait(2.26)

        # expand to 2 by 2
        new_square_2 = Square(
            side_length=2,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(UP)
        self.play(
            Transform(
                new_square, new_square_2
            )
        )
        self.wait(6.65)

        # expand to 3 by 3
        new_square_3 = Square(
            side_length=3,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(1.5*UP+0.5*LEFT)
        self.play(
            Transform(
                new_square, new_square_3
            )
        )
        self.wait(2.26)

        # expand to 4 by 4
        new_square_4 = Square(
            side_length=4,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(2 * UP + 1 * LEFT)
        self.play(
            Transform(
                new_square, new_square_4
            )
        )
        self.wait(2.96)

        # show rectangle outside of three squares
        outside_square = Square(
            side_length=1,
            fill_opacity=1,
            fill_color="#FF0000",
            stroke_opacity=0,
            stroke_color="#FF0000"
        ) \
            .move_to(0.5*RIGHT+3.5*UP)
        self.play(
            FadeIn(outside_square)
        )
        self.wait(2)
        self.play(
            FadeOut(outside_square)
        )
        self.wait(1.21)

        # transform back to 3 by 3
        self.play(
            Transform(
                new_square, new_square_3
            )
        )

        # re fade in new corner
        self.play(
            AnimationGroup(
                FadeIn(new_dot),
                FadeIn(new_corner_label),
                lag_ratio=0.9
            )
        )

        # fade out corner label
        self.play(
            FadeOut(new_corner_label),
            FadeOut(new_dot)
        )
        self.wait(6.09)

        # add square lengths in bottom right corners
        corner_labels=VGroup(
            Integer(square_widths[0]).set_color(self.colors[0]).scale(1.75).move_to(0.5*UL),
            Integer(square_widths[1]).set_color(self.colors[1]).scale(1.75).move_to(0.5*LEFT+1.5*UP),
            Integer(square_widths[2]).set_color(self.colors[2]).scale(1.75).move_to(0.5*RIGHT+1.5*UP)
        )
        # corner_labels.set_stroke(WHITE, opacity=1, width=1)
        self.play(
            AnimationGroup(
                *[
                    FadeIn(mob, run_time=0.6)
                    for mob in corner_labels
                ],
                lag_ratio=0.8
            )
        )
        self.wait(4.26)

        # re fade in new corner
        self.play(
            AnimationGroup(
                FadeIn(new_dot),
                FadeIn(new_corner_label),
                lag_ratio=0.9
            )
        )
        self.wait(12.3)

        # expand A to 4 by 4
        new_A = Square(
            side_length=4,
            fill_color=self.colors[0],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        )\
            .move_to(2*UL)
        self.play(
            Transform(
                squares[0], new_A
            ),
            ApplyMethod(
                corner_labels[0].set_value, 4
            )
        )
        self.add(squares[1], squares[2], corner_labels, new_square)
        square_widths[0] = 4
        self.wait(1.91)

        # note no effect on yellow rectangle
        no_effect_text = TextMobject(
            "No Effect", color=YELLOW
        )\
            .scale(1.5)\
            .next_to(new_square, direction=RIGHT, buff=3)\
            .add_background_rectangle()
        no_effect_arrow = Arrow(
            start=no_effect_text.get_edge_center(LEFT) + 0.1*LEFT,
            end=new_square.get_edge_center(RIGHT) + 0.1*RIGHT,
            color=YELLOW
        )
        self.play(
            Write(no_effect_text),
            ShowCreation(no_effect_arrow)
        )
        self.wait()
        self.play(
            FadeOut(no_effect_text),
            FadeOut(no_effect_arrow)
        )

        # expand to 4 by 4
        self.play(
            Transform(
                new_square, new_square_4
            )
        )
        self.wait(2.96)

        # show rectangle outside of three squares
        self.play(
            FadeIn(outside_square)
        )
        self.wait(2)
        self.play(
            FadeOut(outside_square)
        )
        self.wait(1.21)

        # transform back to 3 by 3
        self.play(
            Transform(
                new_square, new_square_3
            )
        )

        # convert A back to 3 by 3
        square_widths[0] = 3
        new_first_square = Square(
            side_length=square_widths[0],
            fill_color=self.colors[0],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        )\
            .move_to(self.final_corner + self.unit_length * LEFT + 0.5 * square_widths[0] * UL)
        self.play(
            Transform(
                squares[0], new_first_square
            ),
            ApplyMethod(
                corner_labels[0].set_value, 3
            )
        )

        # expand C to 3 by 3
        new_C = Square(
            side_length=3,
            fill_color=self.colors[2],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        ) \
            .move_to(0.5*LEFT + 2.5*UP)
        self.play(
            Transform(
                squares[2], new_C
            ),
            ApplyMethod(
                corner_labels[2].set_value, 3
            )
        )
        self.add(corner_labels, new_square)
        square_widths[2] = 3
        self.wait(1.91)

        self.play(
            Transform(
                new_square, new_square_4
            )
        )
        self.wait(2.96)

        # note no effect on yellow rectangle
        inc_text = TextMobject(
            "Increases to 4x4", color=YELLOW
        ) \
            .scale(1.5) \
            .next_to(new_square, direction=RIGHT, buff=2.25) \
            .add_background_rectangle()
        inc_arrow = Arrow(
            start=inc_text.get_edge_center(LEFT) + 0.1 * LEFT,
            end=new_square.get_edge_center(RIGHT) + 0.1 * RIGHT,
            color=YELLOW
        )
        self.play(
            Write(inc_text),
            ShowCreation(inc_arrow)
        )
        self.wait()
        self.play(
            FadeOut(inc_text),
            FadeOut(inc_arrow)
        )

        # reset everything before showing equation
        square_widths[2] = 2
        original_C = Square(
            side_length=square_widths[2],
            fill_color=self.colors[2],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        )\
            .move_to(self.final_corner + self.unit_length * UP + 0.5 * square_widths[2] * UL)
        self.play(
            Transform(
                new_square, new_square_3
            ),
            Transform(
                squares[2], original_C
            ),
            ApplyMethod(
                corner_labels[2].set_value, 2
            )

        )
        self.wait(2.96)

        eq_rect = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT*0.3,
            stroke_opacity=0,
            fill_opacity=1,
            fill_color=BLACK
        )\
            .to_edge(DOWN, buff=0)
        equation = TextMobject(
            "f(", "3", ",", "4", ",", "2", ")=", "3",
        ) \
            .scale(3)\
            .to_edge(DOWN, buff=1)
        equation[0].shift(1*LEFT)
        equation[1].shift(0.8*LEFT)
        equation[2].shift(0.6*LEFT)
        equation[3].shift(0.4*LEFT)
        equation[4].shift(0.2*LEFT)
        equation[-1].shift(0.2*RIGHT)
        equation[1].set_color(self.colors[0])
        equation[3].set_color(self.colors[1])
        equation[5].set_color(self.colors[2])
        equation[-1].set_color(YELLOW)
        self.play(
            FadeIn(eq_rect)
        )
        self.play(
            AnimationGroup(
                *[
                    FadeIn(mob)
                    for mob in (equation[1], equation[3], equation[5])
                ],
                lag_ratio=1
            )
        )
        self.play(
            FadeIn(equation[-1])
        )
        self.play(
            *[
                FadeIn(mob)
                for mob in (equation[0], equation[2], equation[4], equation[6])
            ]
        )
