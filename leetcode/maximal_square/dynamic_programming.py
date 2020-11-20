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
        self.M = IntegerMatrix(
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
            FadeIn(self.M.get_entries())
        )
        self.wait(5.13)

        # show unfilled dp matrix
        self.dp = IntegerMatrix(
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
            .next_to(self.dp.get_entries(), direction=DOWN, buff=0.75)
        self.play(
            FadeIn(self.dp.get_entries())
        )
        self.wait(1.43)
        self.play(
            Write(dp_text)
        )
        self.wait(2.17)

        # show definition of dp(i,j)
        self.dp_def = TextMobject(
            "dp(", "i", ",", "j",
            ") = width of largest square in original matrix which \\\\has its bottom right corner at (", "i", ",", "j",
            ")",
            tex_to_color_map={
                "dp": YELLOW
            }
        ) \
            .scale(1.3) \
            .to_edge(UP, buff=0.5)
        self.dp_def[2].set_color(RED)
        self.dp_def[4].set_color(BLUE)
        self.dp_def[-4].set_color(RED)
        self.dp_def[-2].set_color(BLUE)
        self.play(Write(self.dp_def))
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
                        self.dp.mob_matrix[i][j].set_value, dp_vals[i][j]
                    )
                    for i, j in itertools.product(range(4), range(4))
                ],
                lag_ratio=0.1
            )
        )
        self.wait(1.39)

        # label example point in dp
        square = Rectangle(
            width=VGroup(*self.M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.5,
            height=VGroup(*self.M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(VGroup(*self.M.get_mob_matrix()[0:2, 0:2].flatten()).get_center())
        square_dp = Rectangle(
            width=self.dp.get_mob_matrix()[1][1].get_height() + 0.3,
            height=self.dp.get_mob_matrix()[1][1].get_height() + 0.3,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(self.dp.get_mob_matrix()[1][1].get_center())
        self.play(
            FadeIn(square_dp)
        )
        self.wait(6.87)
        self.play(
            FadeIn(square)
        )
        self.wait(3.26)

        del_x = self.M.get_mob_matrix()[0][1].get_x() - self.M.get_mob_matrix()[0][0].get_x()
        del_y = self.M.get_mob_matrix()[0][0].get_y() - self.M.get_mob_matrix()[1][0].get_y()

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
            width=VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.8,
            height=VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=YELLOW
        ) \
            .move_to(VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_center())
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
                self.dp.get_mob_matrix()[2, 2], largest_area_text[2]
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
        for mob in self.dp.get_entries():
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
        for mob in self.dp.get_entries():
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
        first_col_M_cp = VGroup(*self.M.get_mob_matrix()[:, 0].flatten()).copy()
        first_col_dp = VGroup(*self.dp.get_mob_matrix()[:, 0].flatten())
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
        first_row_M_cp = VGroup(*self.M.get_mob_matrix()[0, :].flatten()).copy()
        first_row_dp = VGroup(*self.dp.get_mob_matrix()[0, :].flatten())
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
            width=self.M.get_mob_matrix()[0, 0].get_height() + 0.5,
            height=self.M.get_mob_matrix()[0, 0].get_height() + 0.5,
            # stroke_width=2,
            color=GREEN
        ) \
            .move_to(self.M.get_mob_matrix()[0, 0].get_center()) \
            .shift(del_x * RIGHT)
        square_M_2 = Rectangle(
            width=VGroup(*self.M.get_mob_matrix()[:2, :2].flatten()).get_height() + 0.5,
            height=VGroup(*self.M.get_mob_matrix()[:2, :2].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*self.M.get_mob_matrix()[:2, :2].flatten()).get_center()) \
            .shift(del_y * UP + 2 * del_x * RIGHT)
        square_M_3 = Rectangle(
            width=VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.75,
            height=VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_height() + 0.5,
            # stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*self.M.get_mob_matrix()[:3, :3].flatten()).get_center()) \
            .shift(2 * del_y * UP + del_x * RIGHT)
        no_text = TextMobject(
            "No", color=RED
        ) \
            .scale(1.5) \
            .next_to(self.M, direction=DOWN) \
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
                    end_point=self.dp.get_mob_matrix()[0, 2].get_corner(UL) + 0.1 * UL,
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
                    end_point=self.dp.get_mob_matrix()[0, 3].get_corner(UL) + 0.1 * UL,
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
        first_col_M_cp = VGroup(*self.M.get_mob_matrix()[:, 0].flatten()).copy()
        first_col_dp = VGroup(*self.dp.get_mob_matrix()[:, 0].flatten())
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
        first_row_M_cp = VGroup(*self.M.get_mob_matrix()[0, :].flatten()).copy()
        first_row_dp = VGroup(*self.dp.get_mob_matrix()[0, :].flatten())
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
        for mob in self.dp.get_mob_matrix()[1:, 1:].flatten():
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
        self.wait(3.96)

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

        # note effect on yellow rectangle
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

        self.wait(8.13)

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

        # FadeIn Equation
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
        self.wait(1.61)
        self.play(
            AnimationGroup(
                *[
                    FadeIn(mob, run_time=0.46)
                    for mob in (equation[1], equation[3], equation[5])
                ],
                lag_ratio=1
            )
        )
        self.wait(2.92)
        self.play(
            FadeIn(equation[-1])
        )
        self.play(
            *[
                FadeIn(mob)
                for mob in (equation[0], equation[2], equation[4], equation[6])
            ]
        )
        self.wait(11.09)

        # increase A to 4x4
        new_A = Square(
            side_length=4,
            fill_color=self.colors[0],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        ) \
            .move_to(2 * UL)
        A_in_eq_original = equation[1].copy()
        new_A_in_eq = TexMobject(
            4,
            color=self.colors[0]
        ) \
            .scale(3)\
            .move_to(equation[1].get_center())
        self.play(
            Transform(
                squares[0], new_A
            ),
            ApplyMethod(
                corner_labels[0].set_value, 4
            ),
            Transform(
                equation[1], new_A_in_eq
            )
        )
        self.wait(2.09)

        # show that f(4,4,2) = f(3,4,2) = 3
        equation_other = TextMobject(
            "f(", "3", ",", "4", ",", "2", ")=",
        ) \
            .scale(3)
        equation_other[0].shift(1 * LEFT)
        equation_other[1].shift(0.8 * LEFT)
        equation_other[2].shift(0.6 * LEFT)
        equation_other[3].shift(0.4 * LEFT)
        equation_other[4].shift(0.2 * LEFT)
        equation_other[1].set_color(self.colors[0])
        equation_other[3].set_color(self.colors[1])
        equation_other[5].set_color(self.colors[2])
        self.play(
            ApplyMethod(
                equation.shift, 3.5*RIGHT
            )
        )
        equation_other.next_to(equation, direction=LEFT, buff=0.3)
        self.play(
            FadeIn(equation_other)
        )
        self.wait(5.91)

        # return back to original setup
        self.play(
            ApplyMethod(
                equation.shift, 3.5 * LEFT
            ),
            FadeOutAndShift(
                equation_other, direction=LEFT
            )
        )
        new_A = Square(
            side_length=3,
            fill_color=self.colors[0],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        ) \
            .move_to(1.5 * UL)
        self.play(
            Transform(
                equation[1], A_in_eq_original
            ),
            Transform(
                squares[0], new_A
            ),
            ApplyMethod(
                corner_labels[0].set_value, 3
            )
        )
        self.wait(1.39)

        # expand C to 3x3
        new_C = Square(
            side_length=3,
            fill_color=self.colors[2],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        ) \
            .move_to(0.5 * LEFT + 2.5 * UP)
        C_in_eq_original = equation[5].copy()
        new_C_in_eq = TexMobject(
            3,
            color=self.colors[2]
        ) \
            .scale(3) \
            .move_to(equation[5].get_center())
        self.play(
            Transform(
                squares[2], new_C
            ),
            ApplyMethod(
                corner_labels[2].set_value, 3
            ),
            Transform(
                equation[5], new_C_in_eq
            )
        )

        # expand yellow square to 4 by 4
        new_rhs = TextMobject(
            "4",
            color=YELLOW
        ) \
            .scale(3) \
            .move_to(equation[-1].get_center())
        orig_rhs = equation[-1].copy()
        self.play(
            Transform(
                new_square, new_square_4
            ),
            Transform(
                equation[-1], new_rhs
            )
        )
        self.wait(6.43)

        # reset setup
        new_C = Square(
            side_length=3,
            fill_color=self.colors[0],
            fill_opacity=self.square_fill_opacity,
            stroke_opacity=0,
            stroke_color=self.square_stroke_color
        ) \
            .move_to(1.5 * UL)
        self.play(
            Transform(
                equation[5], C_in_eq_original
            ),
            Transform(
                squares[2], original_C
            ),
            ApplyMethod(
                corner_labels[2].set_value, 2
            ),
            Transform(
                new_square, new_square_3
            )
        )
        self.wait(1.22)

        # replace rhs with question marks
        rhs_qms = TextMobject(
            "???",
            color=YELLOW
        ) \
            .scale(3) \
            .move_to(equation[-1].get_center()+0.5*RIGHT)
        self.play(
            Transform(
                equation[-1], rhs_qms
            )
        )
        self.wait(1.13)

        # replace f(3,4,2 with variables
        A_var_in_eq = TextMobject(
            "A",
            color=self.colors[0]
        ) \
            .scale(3) \
            .move_to(equation[1].get_center())
        B_var_in_eq = TextMobject(
            "B",
            color=self.colors[1]
        ) \
            .scale(3) \
            .move_to(equation[3].get_center())
        C_var_in_eq = TextMobject(
            "C",
            color=self.colors[2]
        ) \
            .scale(3) \
            .move_to(equation[5].get_center())
        self.play(
            AnimationGroup(
                Transform(
                    equation[1], A_var_in_eq,
                    run_time=0.42
                ),
                Transform(
                    equation[3], B_var_in_eq,
                    run_time=0.42
                ),
                Transform(
                    equation[5], C_var_in_eq,
                    run_time=0.42
                ),
                lag_ratio=1
            )
        )
        self.wait(4.04)

        # replace rhs with 1+min(A,B,C)
        self.play(
            ApplyMethod(
                equation.to_corner, LEFT
            )
        )
        rhs_qms = TextMobject(
            "1 + min(A,B,C)",
            tex_to_color_map={
                "A": self.colors[0],
                "B": self.colors[1],
                "C": self.colors[2],
            }
        ) \
            .scale(2.75) \
            .next_to(equation[:-1], direction=RIGHT, buff=0.4)
        self.play(
            Transform(
                equation[-1], rhs_qms
            )
        )
        self.wait(2.73)

        # create 1 by 1 square
        new_square_1 = Square(
            side_length=1,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(0.5 * UR)
        self.play(
            Transform(
                new_square, new_square_1
            )
        )
        self.play(
            FadeOut(
                new_corner_label
            )
        )

        # brace 1 length of yellow
        brace_1 = Brace(
            new_square, direction=RIGHT
        )
        brace_1_text = brace_1.get_text("1") \
            .scale(2)\
            .shift(0.5*RIGHT)
        self.play(
            AnimationGroup(
                Write(brace_1),
                Write(brace_1_text),
                lag_ratio=0.2
            )
        )

        # increase new square to 3 x 3
        self.play(
            Transform(
                new_square, new_square_3
            )
        )

        # brace min(A,B,C)
        brace_min = Brace(
            squares[2], direction=RIGHT
        )
        brace_min_text = brace_min.get_text("min(", "A", ",", "B", ",", "C", ")")\
            .scale(2)\
            .shift(1.5*RIGHT)\
            .add_background_rectangle(opacity=1)
        brace_min_text[2].set_color(self.colors[0])
        brace_min_text[4].set_color(self.colors[1])
        brace_min_text[6].set_color(self.colors[2])
        self.play(
            AnimationGroup(
                Write(brace_min),
                Write(brace_min_text),
                lag_ratio=0.2
            )
        )
        self.wait(4.09)

        # try to expand to 2+min(A,B,C)
        self.play(
            Transform(
                new_square, new_square_4
            )
        )
        self.wait()

        # show rectangle outside of three squares
        outside_square = Square(
            side_length=1,
            fill_opacity=1,
            fill_color="#FF0000",
            stroke_opacity=0,
            stroke_color="#FF0000"
        ) \
            .move_to(0.5 * RIGHT + 3.5 * UP)
        self.play(
            FadeIn(outside_square)
        )
        self.wait()
        self.play(
            FadeOut(outside_square)
        )
        self.wait()
        self.play(
            Transform(
                new_square, new_square_3
            )
        )
        self.wait(6.83)


class ThreeSquareProof2(Scene):
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
                .move_to(self.final_corner + self.unit_length * LEFT + 0.5 * square_widths[0] * UL),
            Square(
                side_length=square_widths[1],
                fill_color=self.colors[1],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length * UL + 0.5 * square_widths[1] * UL),
            Square(
                side_length=square_widths[2],
                fill_color=self.colors[2],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length * UP + 0.5 * square_widths[2] * UL),
        )
        self.add(squares)
        self.wait()

        zeros = VGroup()
        ones = VGroup()
        corner_one = TexMobject("1") \
            .set_color(YELLOW) \
            .scale(1.75) \
            .move_to(0.5 * UR)
        rects_corners = [(-3, 0), (-4, 1), (-1, 1)]
        for x in range(-9,10):
            for y in range(-5,6):
                # put one at (0,0)
                if x == y == 0:
                    continue
                in_square = False
                # one inside square
                for i, corner in enumerate(rects_corners):
                    if corner[0] <= x < corner[0]+square_widths[i] and \
                       corner[1] <= y < corner[1]+square_widths[i]:
                        ones.add(
                            TexMobject("1")
                            .set_color(GREY)
                            .scale(1.75)
                            .move_to(0.5*UR + x*RIGHT + y*UP)
                        )
                        in_square = True
                        break
                # zero outside square
                if not in_square:
                    zeros.add(
                        TexMobject("0")
                        .set_color(GREY)
                        .scale(1.75)
                        .move_to(0.5*UR + x*RIGHT + y*UP)
                    )
        self.play(
            LaggedStartMap(
                FadeIn, VGroup(ones)
            )
        )
        self.play(
            LaggedStartMap(
                FadeIn, zeros
            )
        )
        self.wait(6.7)

        square_labels = VGroup(
            TextMobject("A", color="#FF0000").scale(3.1).next_to(squares[0], direction=DOWN).shift(
                0.1 * UP).add_background_rectangle(opacity=0.9),
            TextMobject("B", color="#00FF00").scale(3.1).next_to(squares[1], direction=LEFT).shift(
                0.1 * UP).add_background_rectangle(opacity=0.9),
            TextMobject("C", color="#0000FF").scale(3.1).next_to(squares[2], direction=UR)
                .add_background_rectangle(opacity=0.9),
        )
        self.play(
            LaggedStartMap(
                FadeIn, square_labels,lag_ratio=0.8
            )
        )
        self.wait(2.21)

        # add 1 at (0,0), show yellow square
        new_square_3 = Square(
            side_length=3,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(1.5 * UP + 0.5 * LEFT)
        self.play(
            FadeIn(corner_one)
        )
        self.wait(3.87)
        self.play(
            FadeIn(new_square_3)
        )
        self.wait(4.96)

        # add dp values
        corner_labels = VGroup(
            Integer(square_widths[0]).set_color(self.colors[0]).scale(1.75).move_to(0.5 * UL),
            Integer(square_widths[1]).set_color(self.colors[1]).scale(1.75).move_to(0.5 * LEFT + 1.5 * UP),
            Integer(square_widths[2]).set_color(self.colors[2]).scale(1.75).move_to(0.5 * RIGHT + 1.5 * UP)
        )
        new_corner_label = Integer(3).set_color(YELLOW).scale(1.75).move_to(0.5 * UR)
        self.play(
            Transform(
                ones[14], corner_labels[0]
            )
        )
        self.wait(4.7)
        self.play(
            Transform(
                ones[15], corner_labels[1]
            )
        )
        self.play(
            Transform(
                ones[19], corner_labels[2]
            )
        )
        self.wait(4.22)
        self.play(
            Transform(
                corner_one, new_corner_label
            )
        )
        self.wait()

        # fadein equation
        eq_rect = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT * 0.3,
            stroke_opacity=0,
            fill_opacity=1,
            fill_color=BLACK
        ) \
            .to_edge(DOWN, buff=0)
        equation = TextMobject(
            "f(", "3", ",", "4", ",", "2", ")=", "3",
        ) \
            .scale(3) \
            .to_edge(DOWN, buff=1)
        equation[0].shift(1 * LEFT)
        equation[1].shift(0.8 * LEFT)
        equation[2].shift(0.6 * LEFT)
        equation[3].shift(0.4 * LEFT)
        equation[4].shift(0.2 * LEFT)
        equation[-1].shift(0.2 * RIGHT)
        equation[1].set_color(self.colors[0])
        equation[3].set_color(self.colors[1])
        equation[5].set_color(self.colors[2])
        equation[-1].set_color(YELLOW)
        self.play(
            AnimationGroup(
                FadeIn(eq_rect),
                FadeIn(equation),
                lag_ratio=0.8
            )
        )
        self.wait(14.87)

        # plug in dp values
        self.play(
            ApplyMethod(
                equation[0].shift, 4*LEFT
            ),
            ApplyMethod(
                equation[1].shift, 3*LEFT
            ),
            ApplyMethod(
                equation[2].shift, 2.25 * LEFT
            ),
            ApplyMethod(
                equation[3].shift, 1.5 * LEFT
            ),
            # ApplyMethod(
            #     equation[4].shift, 0 * LEFT
            # ),
            ApplyMethod(
                equation[6].shift, 1.5 * RIGHT
            ),
            ApplyMethod(
                equation[7].shift, 2.25 * RIGHT
            )
        )
        dp_n10 = TexMobject(
            "dp(-1,0)"
        )\
            .scale(1.5)\
            .set_color(self.colors[0])\
            .move_to(equation[1].get_center()+0.1*DOWN+0.25*LEFT)
        self.play(
            Transform(
                equation[1], dp_n10
            )
        )
        self.wait(2.26)
        dp_n11 = TexMobject(
            "dp(-1,1)"
        ) \
            .scale(1.5) \
            .set_color(self.colors[1]) \
            .move_to(equation[3].get_center() + 0.1 * DOWN + 0.25 * RIGHT)
        self.play(
            Transform(
                equation[3], dp_n11
            )
        )
        self.wait(1.74)
        dp_01 = TexMobject(
            "dp(0,1)"
        ) \
            .scale(1.5) \
            .set_color(self.colors[2]) \
            .move_to(equation[5].get_center() + 0.1 * DOWN + 0.75 * RIGHT)
        self.play(
            Transform(
                equation[5], dp_01
            )
        )
        self.wait(3.48)
        dp_00 = TexMobject(
            "dp(0,0)"
        ) \
            .scale(1.5) \
            .set_color(YELLOW) \
            .move_to(equation[7].get_center()+ 0.1 * DOWN )
        self.play(
            Transform(
                equation[7], dp_00
            )
        )
        self.wait(22.57)

        # black out everything
        block_rect2 = Rectangle(
            width=FRAME_WIDTH*1.1,
            height=0.75*FRAME_HEIGHT,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_opacity=0
        )\
            .to_edge(UP, buff=0)
        self.play(
            FadeIn(
                block_rect2
            )
        )
        self.wait(9.57)

        # show translation invariants
        new_equation = TexMobject(
            "dp(i,j)", "=", "f(", "dp(i-1,j)", ",", "dp(i-1,j+1)", ",", "dp(i,j+1)", ")"
        )\
            .scale(1.5)\
            .to_edge(UP, buff=1)
        new_equation[0].set_color(YELLOW)
        new_equation[3].set_color(self.colors[0])
        new_equation[5].set_color(self.colors[1])
        new_equation[7].set_color(self.colors[2])
        self.play(
            AnimationGroup(
                TransformFromCopy(dp_00, new_equation[0]),
                FadeIn(new_equation[1]),
                FadeIn(new_equation[2]),
                TransformFromCopy(dp_n10, new_equation[3]),
                FadeIn(new_equation[4]),
                TransformFromCopy(dp_n11, new_equation[5]),
                FadeIn(new_equation[6]),
                TransformFromCopy(dp_01, new_equation[7]),
                FadeIn(new_equation[8]),
                lag_ratio=1
            )
        )

        # note that equal when i = j = 0
        arrow_same = DoubleArrow(
            new_equation[1].get_bottom() + 0.5 * DOWN,
            new_equation[1].get_bottom() + 6 * DOWN
        )
        text_same = TextMobject(
            "Same when \\textit{i} = \\textit{j} = 0"
        )\
            .scale(1.5)\
            .next_to(arrow_same, direction=RIGHT)
        self.play(
            AnimationGroup(
                ShowCreation(arrow_same),
                Write(text_same),
                lag_ratio=0.5
            )
        )
        self.wait(2.4)
        self.play(
            FadeOut(arrow_same),
            FadeOut(text_same),
            *[
                FadeOut(mob)
                for mob in (dp_00, dp_01, dp_n10, dp_n10, equation)
            ]
        )
        self.wait()

        # show f(A,B,C)
        f_def = TexMobject(
            "f(A,B,C) = 1+min(A,B,C)",
            tex_to_color_map={
                "A": self.colors[0],
                "B": self.colors[1],
                "C": self.colors[2],
            }
        ) \
            .scale(1.5) \
            .to_edge(DOWN, buff=1)
        self.play(
            FadeInFrom(f_def, direction=DOWN)
        )
        self.wait(4.3)

        # f plugged in
        new_equation_1 = TexMobject(
            "dp(i,j)", "=", "1+min(", "dp(i-1,j)", ",", "dp(i-1,j+1)", ",", "dp(i,j+1)", ")"
        ) \
            .scale(1.35) \
            .to_edge(UP, buff=3)
        new_equation_1[0].set_color(YELLOW)
        new_equation_1[3].set_color(self.colors[0])
        new_equation_1[5].set_color(self.colors[1])
        new_equation_1[7].set_color(self.colors[2])
        self.play(
            TransformFromCopy(
                new_equation, new_equation_1
            )
        )
        self.wait(17.83)


class NotCorrectFormulaForDP(ThreeSquareProof):
    def construct(self):
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
                .move_to(self.final_corner + self.unit_length * LEFT + 0.5 * square_widths[0] * UL),
            Square(
                side_length=square_widths[1],
                fill_color=self.colors[1],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length * UL + 0.5 * square_widths[1] * UL),
            Square(
                side_length=square_widths[2],
                fill_color=self.colors[2],
                fill_opacity=self.square_fill_opacity,
                stroke_opacity=0,
                stroke_color=self.square_stroke_color
            )
                .move_to(self.final_corner + self.unit_length * UP + 0.5 * square_widths[2] * UL),
        )
        self.add(squares)

        zeros = VGroup()
        ones = VGroup()
        corner_one = TexMobject("1") \
            .set_color(GREY) \
            .scale(1.75) \
            .move_to(0.5 * UR)
        corner_zero = TexMobject("0") \
            .set_color(GREY) \
            .scale(1.75) \
            .move_to(0.5 * UR)
        rects_corners = [(-3, 0), (-4, 1), (-1, 1)]
        for x in range(-9, 10):
            for y in range(-5, 6):
                # put one at (0,0)
                if x == y == 0:
                    continue
                in_square = False
                # one inside square
                for i, corner in enumerate(rects_corners):
                    if corner[0] <= x < corner[0] + square_widths[i] and \
                            corner[1] <= y < corner[1] + square_widths[i]:
                        ones.add(
                            TexMobject("1")
                                .set_color(GREY)
                                .scale(1.75)
                                .move_to(0.5 * UR + x * RIGHT + y * UP)
                        )
                        in_square = True
                        break
                # zero outside square
                if not in_square:
                    zeros.add(
                        TexMobject("0")
                            .set_color(GREY)
                            .scale(1.75)
                            .move_to(0.5 * UR + x * RIGHT + y * UP)
                    )
        self.add(ones,zeros)
        self.wait(6.52)

        square_labels = VGroup(
            TextMobject("A", color="#FF0000").scale(3.1).next_to(squares[0], direction=DOWN).shift(
                0.1 * UP).add_background_rectangle(opacity=0.9),
            TextMobject("B", color="#00FF00").scale(3.1).next_to(squares[1], direction=LEFT).shift(
                0.1 * UP).add_background_rectangle(opacity=0.9),
            TextMobject("C", color="#0000FF").scale(3.1).next_to(squares[2], direction=UR)
                .add_background_rectangle(opacity=0.9),
        )
        self.play(
            LaggedStartMap(
                FadeIn, square_labels, lag_ratio=0.8
            )
        )
        self.wait()

        # add 1 at (0,0), show yellow square
        new_square_3 = Square(
            side_length=3,
            fill_opacity=0,
            stroke_opacity=1,
            stroke_color=YELLOW
        ) \
            .move_to(1.5 * UP + 0.5 * LEFT)
        self.play(
            FadeIn(corner_one)
        )
        self.wait()
        self.play(
            FadeIn(new_square_3)
        )
        self.wait()

        # note that this is only true when M(0,0) = 1
        one_needed_text = TextMobject(
            "1", " at M(0,0)",
            color=YELLOW
        )\
            .scale(1.75)\
            .next_to(corner_one, direction=RIGHT, buff=3)\
            .add_background_rectangle(opacity=1, buff=0.13)
        one_needed_arrow = Arrow(
            one_needed_text.get_left(),
            one_needed_text.get_left() + 3*LEFT,
            color=YELLOW
        )
        self.play(
            AnimationGroup(
                ShowCreation(one_needed_arrow),
                Write(one_needed_text)
            )
        )
        self.wait(4.35)

        # change M[0,0] to 0
        zero_in_label = TextMobject(
            "0",
            color=YELLOW
        )\
            .scale(1.75)\
            .move_to(one_needed_text[1].get_center())
        one_in_label = one_needed_text[1].copy()
        self.play(
            Transform(
                corner_one, corner_zero
            ),
            Transform(
                one_needed_text[1], zero_in_label
            )
        )
        self.play(
            ApplyMethod(
                new_square_3.set_color, RED
            )
        )
        self.play(
            FadeOut(
                new_square_3
            )
        )
        self.wait(6)

        # # add dp values
        # corner_labels = VGroup(
        #     Integer(square_widths[0]).set_color(self.colors[0]).scale(1.75).move_to(0.5 * UL),
        #     Integer(square_widths[1]).set_color(self.colors[1]).scale(1.75).move_to(0.5 * LEFT + 1.5 * UP),
        #     Integer(square_widths[2]).set_color(self.colors[2]).scale(1.75).move_to(0.5 * RIGHT + 1.5 * UP)
        # )
        # # new_corner_label = Integer(3).set_color(YELLOW).scale(1.75).move_to(0.5 * UR)
        # self.play(
        #     Transform(
        #         ones[14], corner_labels[0]
        #     )
        # )
        # self.wait()
        # self.play(
        #     Transform(
        #         ones[15], corner_labels[1]
        #     )
        # )
        # self.play(
        #     Transform(
        #         ones[19], corner_labels[2]
        #     )
        # )
        # self.wait()

        # fadein equation
        eq_rect = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT * 0.3,
            stroke_opacity=0,
            fill_opacity=1,
            fill_color=BLACK
        ) \
            .to_edge(DOWN, buff=0)
        equation = TextMobject(
            "\\begin{align*}"
                "dp(0,0)& = "
                "\\begin{cases}"
                   "0 ,&  M(0,0) = 0\\\\"
                   "1+min(dp(-1,0),dp(-1,1),dp(0,1)),& M(0,0) = 1"
                "\\end{cases}"
            "\\end{align*}"
        ) \
            .scale(1.05) \
            .to_edge(DOWN, buff=1)
        # old coloring
        # VGroup(*equation.submobjects[0][0:7]).set_color(YELLOW)
        # equation.submobjects[0][18].set_color(GREY)
        # VGroup(*equation.submobjects[0][25:34]).set_color(self.colors[0])
        # VGroup(*equation.submobjects[0][35:46]).set_color(self.colors[1])
        # VGroup(*equation.submobjects[0][47:56]).set_color(self.colors[2])
        # equation.submobjects[0][65].set_color(GREY)

        # new coloring
        VGroup(*equation.submobjects[0][0:7]).set_color(YELLOW)
        equation.submobjects[0][18].set_color(GREY)
        VGroup(*equation.submobjects[0][25:33]).set_color(self.colors[0])
        VGroup(*equation.submobjects[0][34:42]).set_color(self.colors[1])
        VGroup(*equation.submobjects[0][43:50]).set_color(self.colors[2])
        equation.submobjects[0][-1].set_color(GREY)
        self.play(
            FadeIn(eq_rect),
            FadeIn(VGroup(equation[0][0:7])),
        )
        self.wait(3.57)
        self.play(
            FadeIn(VGroup(equation[0][7:9]), run_time=0.52),
        )
        self.play(
            FadeIn(VGroup(equation[0][9:11])),
        )
        self.play(
            FadeIn(VGroup(equation[0][11:19])),
        )
        self.wait(18)
        corner_one_new = TexMobject("1") \
            .set_color(GREY) \
            .scale(1.75) \
            .move_to(0.5 * UR)
        new_square_3.set_color(YELLOW)
        self.play(
            FadeIn(VGroup(equation[0][52:])),
            Transform(
                corner_one, corner_one_new
            ),
            ShowCreation(new_square_3),
            Transform(
                one_needed_text[1], one_in_label
            )
        )
        self.play(
            FadeIn(VGroup(equation[0][19:52])),
        )
        self.wait(2)


class FinalFormulaForDP(ThreeSquareProof):
    def construct(self):
        equation = TextMobject(
            "\\begin{align*}"
            "dp(0,0)& = "
            "\\begin{cases}"
            "0 ,&  M(0,0) = 0\\\\"
            "1+min(dp(-1,0),dp(-1,1),dp(0,1)),& M(0,0) = 1"
            "\\end{cases}"
            "\\end{align*}"
        ) \
            .scale(1.05) \
            .to_edge(UP, buff=1)
        VGroup(*equation.submobjects[0][0:7]).set_color(YELLOW)
        equation.submobjects[0][18].set_color(GREY)
        VGroup(*equation.submobjects[0][25:33]).set_color(self.colors[0])
        VGroup(*equation.submobjects[0][34:42]).set_color(self.colors[1])
        VGroup(*equation.submobjects[0][43:50]).set_color(self.colors[2])
        equation.submobjects[0][-1].set_color(GREY)
        self.add(equation)
        self.wait(2.7)

        equation_gen = TextMobject(
            "\\begin{align*}"
            "dp(i,j)& = "
            "\\begin{cases}"
            "0 ,&  M(i,j) = 0\\\\"
            "1+min(dp(i-1,j),dp(i-1,j+1),dp(i,j+1)),& M(i,j) = 1"
            "\\end{cases}"
            "\\end{align*}"
        ) \
            .scale(1.05) \
            .to_edge(DOWN, buff=1)
        VGroup(*equation_gen.submobjects[0][0:7]).set_color(YELLOW)
        equation_gen.submobjects[0][18].set_color(GREY)
        VGroup(*equation_gen.submobjects[0][25:34]).set_color(self.colors[0])
        VGroup(*equation_gen.submobjects[0][35:46]).set_color(self.colors[1])
        VGroup(*equation_gen.submobjects[0][47:56]).set_color(self.colors[2])
        equation_gen.submobjects[0][65].set_color(GREY)
        self.play(
            TransformFromCopy(
                equation, equation_gen
            )
        )
        self.wait()

        # note that equal when i = j = 0
        arrow_same = DoubleArrow(
            equation.get_bottom() + 0.5 * DOWN + 2*LEFT,
            equation.get_bottom() + 4.5 * DOWN + 2*LEFT
        )
        text_same = TextMobject(
            "Same when \\textit{i} = \\textit{j} = 0"
        ) \
            .scale(1.5) \
            .next_to(arrow_same, direction=RIGHT)
        self.play(
            AnimationGroup(
                ShowCreation(arrow_same),
                Write(text_same),
                lag_ratio=0.5
            )
        )
        self.wait(2.4)
        self.play(
            FadeOut(arrow_same),
            FadeOut(text_same),
        )

        self.play(
            FadeOutAndShift(
                equation, direction=UP
            ),
            ApplyMethod(
                equation_gen.to_edge, UP
            )
        )
        self.wait()

        self.play(
            ShowCreation(
                SurroundingRectangle(
                    equation_gen,
                    color=PURPLE
                )
            )
        )
        self.wait()

class ComputingDP(ThreeSquareProof):
    def construct(self):
        # show original matrix
        self.M = IntegerMatrix(
            [[1, 1, 1, 0],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 0, 1]],
            v_buff=1.0
        ) \
            .scale(1.3) \
            .to_edge(LEFT, buff=0.2) \
            .shift(1 * DOWN + 1.25 * RIGHT)
        self.add(self.M.get_entries())

        # show unfilled dp matrix
        self.dp = IntegerMatrix(
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
            .next_to(self.dp.get_entries(), direction=DOWN, buff=0.75)
        self.add(
            self.dp.get_entries(), dp_text
        )

        # show definition of dp(i,j)
        self.dp_def = TextMobject(
            "dp(", "i", ",", "j",
            ") = width of largest square in original matrix which \\\\has its bottom right corner at (", "i", ",", "j",
            ")",
            tex_to_color_map={
                "dp": YELLOW
            }
        ) \
            .scale(1.3) \
            .to_edge(UP, buff=0.5)
        self.dp_def[2].set_color(RED)
        self.dp_def[4].set_color(BLUE)
        self.dp_def[-4].set_color(RED)
        self.dp_def[-2].set_color(BLUE)
        self.add(self.dp_def)

        # copy first column
        first_col_M_cp = VGroup(*self.M.get_mob_matrix()[:, 0].flatten()).copy()
        first_col_dp = VGroup(*self.dp.get_mob_matrix()[:, 0].flatten())
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
        first_row_M_cp = VGroup(*self.M.get_mob_matrix()[0, :].flatten()).copy()
        first_row_dp = VGroup(*self.dp.get_mob_matrix()[0, :].flatten())
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
        self.wait()

        new_dp = VGroup(
            first_row_M_cp,
            first_col_M_cp,
            *self.dp.get_mob_matrix()[1:,1:].flatten()
        )

        # fade out everything and focus on dp
        self.play(
            FadeOut(self.M.get_entries()),
            FadeOut(self.dp_def),
            ApplyMethod(
                VGroup(new_dp, dp_text).move_to, 1.5*UP,
                buff=1
            )
        )

        # replace all elements not in first row/column with question mark
        qm_anims = []
        for mob in self.dp.get_mob_matrix()[1:, 1:].flatten():
            qm = TextMobject("?").scale(1.3).move_to(mob.get_center())
            qm_anims.append(Transform(mob, qm))
        self.play(
            AnimationGroup(
                *qm_anims,
                lag_ratio=0.1
            )
        )

        del_x = self.dp.get_mob_matrix()[0][1].get_x() - self.dp.get_mob_matrix()[0][0].get_x()
        del_y = self.dp.get_mob_matrix()[0][0].get_y() - self.dp.get_mob_matrix()[1][0].get_y()

        sq_kw = {
            "width": 1,
            "height": 1,
            "fill_opacity": 0.3,
            "stroke_opacity": 0
        }
        A = Rectangle(
            fill_color=self.colors[0],
            **sq_kw
        ) \
            .move_to(first_col_M_cp[1].get_center())
        B = Rectangle(
            fill_color=self.colors[1],
            **sq_kw
        ) \
            .move_to(A.get_center() + del_y*UP)
        C = Rectangle(
            fill_color=self.colors[2],
            **sq_kw
        ) \
            .move_to(B.get_center() + del_x*RIGHT)
        D = Rectangle(
            fill_color=YELLOW,
            **sq_kw
        ) \
            .move_to(C.get_center() + del_y*DOWN)
        self.add(A, B, C, D)
        self.wait()
