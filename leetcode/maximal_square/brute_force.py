from manimlib.imports import *
import random

class BruteForceExample(Scene):
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
            [[0, 0, 0, 1],
             [1, 0, 1, 1],
             [1, 1, 1, 1]],
            v_buff=1.0
        ) \
            .scale(1.5) \
            .to_edge(LEFT, buff=2)
        self.play(
            Write(M.get_entries())
        )
        self.wait(6.96)

        # add rectangle
        square = Rectangle(
            width=M.get_entries()[0][0].get_height() + 0.3,
            height=M.get_entries()[0][0].get_height() + 0.3,
            color=YELLOW
        )\
            .move_to(M.get_entries()[0][0].get_center())
        self.play(
            Write(square)
        )
        self.wait(2.52)

        largest_area = TextMobject(
            "largest\\_area = ",
            color=YELLOW
        )\
            .scale(1.5)\
            .next_to(M.get_entries(), direction=RIGHT, buff=1.7)
        largest_area_val = Integer(
            0,
            color=YELLOW
        )\
            .scale(1.5)\
            .next_to(largest_area, direction=RIGHT, buff=0.3)
        self.play(
            FadeInFrom(
                largest_area, direction=RIGHT
            ),
            FadeInFrom(
                largest_area_val, direction=RIGHT
            )
        )
        self.wait(5.9)

        # label as no ones in square
        no_text = TextMobject(
            "Nope", color=RED
        )\
            .scale(1.5)\
            .next_to(M.get_entries(), direction=UP, buff=1)
        yes_text = TextMobject(
            "Yes", color=GREEN
        )\
            .scale(1.5)\
            .move_to(no_text.get_center())
        q_text = TextMobject(
            "???", color=YELLOW
        ) \
            .scale(1.5) \
            .move_to(no_text.get_center())
        cur_text = no_text.copy()
        self.play(
            ApplyMethod(
                square.set_color,
                RED
            ),
            Write(cur_text)
        )
        self.wait(1.52)

        # shift until 1 is found
        del_x = M.get_mob_matrix()[0][1].get_x() - M.get_mob_matrix()[0][0].get_x()
        del_y = M.get_mob_matrix()[0][0].get_y() - M.get_mob_matrix()[1][0].get_y()
        for i in range(3):
            self.play(
                ApplyMethod(
                    square.shift, del_x*RIGHT
                )
            )
            if i != 2:
                self.wait(1)

        # change to yes
        self.play(
            ApplyMethod(
                square.set_color,
                GREEN
            ),
            Transform(
                cur_text, yes_text
            )
        )
        self.wait(2.22)
        self.play(
            ApplyMethod(
                largest_area_val.set_value, 1
            ),
        )
        self.wait(0.53)

        # reset 2 by 2 square
        new_square = Rectangle(
            width=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.7,
            height=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.7,
            color=YELLOW
        )\
            .move_to(VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_center())
        self.play(
            Transform(
                square, new_square
            ),
            Transform(
                cur_text, q_text
            )
        )
        self.wait(7.65)

        # change to no
        self.play(
            ApplyMethod(
                square.set_color,
                RED
            ),
            Transform(
                cur_text, no_text
            )
        )

        # move around until end of matrix
        for _ in range(2):
            self.play(
                ApplyMethod(
                    square.shift, del_x*RIGHT
                )
            )
            self.wait(1)
        self.play(
            ApplyMethod(
                square.shift, 2*del_x * LEFT + del_y * DOWN
            )
        )
        self.wait(1)
        self.play(
            ApplyMethod(
                square.shift, del_x * RIGHT
            )
        )
        self.wait(1)
        self.play(
            ApplyMethod(
                square.shift, del_x * RIGHT
            )
        )
        self.play(
            ApplyMethod(
                square.set_color,
                GREEN
            ),
            Transform(
                cur_text, yes_text
            )
        )
        self.wait(3.91)

        self.play(
            ApplyMethod(
                largest_area_val.set_value,
                4
            )
        )
        self.wait(2.04)

        # reset 3 by 3 square
        new_square_2 = Rectangle(
            width=VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_height() + 1,
            height=VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_height() + 1,
            color=YELLOW
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_center())
        self.play(
            Transform(
                square, new_square_2
            ),
            Transform(
                cur_text, q_text
            )
        )
        self.wait(1.09)

        self.play(
            ApplyMethod(
                square.set_color,
                RED
            ),
            Transform(
                cur_text, no_text
            )
        )
        self.play(
            ApplyMethod(
                square.shift, del_x * RIGHT
            )
        )
        self.wait(9.78)

        final_rect = Rectangle(
            width=VGroup(*M.get_mob_matrix()[1:, 2:].flatten()).get_height() + 1,
            height=VGroup(*M.get_mob_matrix()[1:, 2:].flatten()).get_height() + 1,
            color=GREEN
        )\
            .move_to(VGroup(*M.get_mob_matrix()[1:, 2:].flatten()).get_center())
        self.play(
            ShowCreation(
                SurroundingRectangle(
                    VGroup(largest_area, largest_area_val),
                    color=PURPLE_C,
                    buff=0.3
                )
            ),
            Transform(
                square, final_rect
            ),
            Transform(cur_text, yes_text)
        )

        self.wait(7.65)


class NotBestSolution(Scene):
    def construct(self):
        self.wait(4.43)

        rand_vals = [
                [random.choice([0, 1]) for _ in range(12)]
                for __ in range(16)
            ]
        rand_vals[0][0] = 0
        rand_vals[0][1] = 0
        rand_vals[0][2] = 0
        rand_vals[0][3] = 0
        M = IntegerMatrix(rand_vals) \
            .scale(0.6)\
            .to_corner(LEFT, buff=0)\
            .shift(DOWN)
        block_rect = Rectangle(
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            color=BLACK,
            fill_color=BLACK,
            fill_opacity=1
        )
        no_text = TextMobject(
            "No", color=RED
        )\
            .next_to(M, direction=UP)
        yes_text = TextMobject(
            "Yes", color=GREEN
        )\
            .move_to(no_text.get_center())
        cur_text = no_text.copy()
        square = Rectangle(
            width=M.get_entries()[0][0].get_height() + 0.1,
            height=M.get_entries()[0][0].get_height() + 0.1,
            stroke_width=2,
            color=RED
        )\
            .move_to(M.get_entries()[0][0].get_center())
        self.add(M.get_entries(), cur_text, square, block_rect)
        time_complexity = TexMobject(
            "O((", "N", "M", ")^2)",
            tex_to_color_map={
                "N": BLUE_C,
                "M": RED_C
            }
        ) \
            .scale(3) \
            .to_corner(UR, buff=1.2)
        time_complexity.add_background_rectangle(opacity=1)
        self.play(
            Write(time_complexity)
        )
        self.wait(6.96)

        self.play(
            FadeOut(block_rect)
        )

        # largest_area = TextMobject(
        #     "largest\\_area = ",
        #     color=YELLOW
        # ) \
        #     .scale(1.5) \
        #     .next_to(M.get_entries(), direction=RIGHT, buff=1.7)
        # largest_area_val = Integer(
        #     0,
        #     color=YELLOW
        # ) \
        #     .scale(1.5) \
        #     .next_to(largest_area, direction=RIGHT, buff=0.3)

        # check 1 by 1
        del_x = M.get_mob_matrix()[0][1].get_x() - M.get_mob_matrix()[0][0].get_x()
        del_y = M.get_mob_matrix()[0][0].get_y() - M.get_mob_matrix()[1][0].get_y()
        loc = [0, 0]
        while rand_vals[loc[0]][loc[1]] == 0:
            self.wait(0.75)
            self.play(
                square.shift, del_x*RIGHT
            )
            loc[1] += 1
        self.play(
            Transform(cur_text, yes_text),
            ApplyMethod(
                square.set_color, GREEN
            )
        )
        self.wait(0.75)

        # 2 by 2
        new_square = Rectangle(
            width=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.5,
            height=VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_height() + 0.3,
            stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[0:2, 0:2].flatten()).get_center())
        self.play(
            Transform(
                square, new_square
            ),
            Transform(
                cur_text, no_text
            )
        )
        l = [0, 0]
        while not (rand_vals[l[0]][l[1]] == rand_vals[l[0]+1][l[1]] ==
                   rand_vals[l[0]][l[1]+1] == rand_vals[l[0]+1][l[1]+1] == 1):
            self.wait(0.75)
            self.play(
                square.shift, del_x*RIGHT
            )
            l[1] += 1
        self.play(
            Transform(cur_text, yes_text),
            ApplyMethod(
                square.set_color, GREEN
            )
        )

        # 3 by 3 check
        # will never find a 3x3 square due to math
        # probability = (1/2)^9 ~= 2%
        new_square = Rectangle(
            width=VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_height() + 0.8,
            height=VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_height() + 0.3,
            stroke_width=2,
            color=RED
        ) \
            .move_to(VGroup(*M.get_mob_matrix()[0:3, 0:3].flatten()).get_center())
        self.play(
            Transform(
                square, new_square
            ),
            Transform(
                cur_text, no_text
            )
        )
        l = [0, 0]
        finished = False
        # for i in range(16):
        for i in range(2):
            for j in range(9):
                self.wait(0.75)
                self.play(
                    square.shift, del_x * RIGHT
                )
            self.wait(0.75)
            self.play(
                square.shift, del_y * DOWN + 9 * LEFT * del_x
            )

        self.wait()
