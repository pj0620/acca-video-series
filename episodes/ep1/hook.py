from manimlib.imports import *
from accalib.animations import EllipsesFlash
from accalib.electrical_circuits import SimpleCircuitFreqDomain

class ComplexNumbersTitle(Scene):
    def construct(self):
        complex_number = TextMobject(
            "Complex Numbers",
            color=WHITE
        )\
            .scale(2.5)

        self.add(
            complex_number
        )
        self.play(
            EllipsesFlash(
                complex_number,
                flash_radius_x=7,
                flash_radius_y=4,
                line_length=1.7,
                num_lines=16,
                run_time=1
                # line_stroke_width=5,
            )
        )
        self.wait()


class ApplicationsOfComplexNumbers(Scene):
    def construct(self):
        title = Title(
            "Applications of Complex Numbers",
            scale_factor=1.25
        )
        self.add(
            title
        )

        i_text = TexMobject(
            "i", "&=\\sqrt{-1}",
            substrings_to_isolate=["$i$"]
        )\
            .scale(1.4)\
            .next_to(title, direction=DOWN, aligned_edge=RIGHT)\
            .shift(0.75*DL)
        i_text.get_part_by_tex("i").set_color(YELLOW)
        i_rect = SurroundingRectangle(
            i_text,
            buff=0.5,
            color=PURPLE
        )
        self.play(
            Write(i_text),
            Write(i_rect)
        )
        self.wait(2.5)

        qm_text = TextMobject(
            "Quantum Mechanics:"
        )\
            .scale(1.35)\
            .next_to(title, direction=DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(
            Write(
                qm_text,
                run_time=0.75
            )
        )

        schrodinger_eq = TexMobject(
            "i", "\\hbar {\\partial \\Psi \\over \\partial t}","=",
            "\\hat{H} \\Psi",
            substrings_to_isolate=["$i$"]
        )\
            .scale(1.5)\
            .next_to(qm_text, direction=DR)\
            .shift(2*LEFT)
        schrodinger_eq.get_part_by_tex("i").set_color(YELLOW)
        self.play(Write(schrodinger_eq))

        ft_text = TextMobject(
            "Fourier Analysis:"
        )\
            .scale(1.35)\
            .next_to(qm_text, direction=DOWN, aligned_edge=LEFT, buff=2.5)
        self.play(
            Write(
                ft_text,
                run_time=1
            )
        )
        ft_equation = TexMobject(
            "G(f) = ",
            "\\int_{-\\infty}^{\\infty} g(t)",
            "e^{-", "i", "2\\pi f t}dt",
            substrings_to_isolate=["$i$"]
        )\
            .scale(1.5)\
            .next_to(ft_text, direction=DR)\
            .shift(2*LEFT)
        ft_equation[3].set_color(YELLOW)
        self.play(
            Write(
                ft_equation,
                run_time=1
            )
        )

        many_more = TextMobject(
            "many more ..."
        )\
            .scale(1.35)\
            .next_to(ft_text, direction=DOWN, aligned_edge=LEFT, buff=2.5)
        self.play(Write(many_more))

        self.wait(7.6)


class EEApplication(Scene):
    CONFIG = {
        "axes_config": {
            "number_line_config": {
                "include_tip": False,
            },
            "x_axis_config": {
                # "tick_frequency": 1,
                # "unit_size": 4,
            },
            "x_min": 0,
            "x_max": 5,
            "y_min": 0,
            "y_max": 5,
            "center_point": 3*DOWN+0*LEFT,
        },
        "current_color": GREEN_C,
        "voltage_color": RED_C,
        "inductor_color": ORANGE,
        "resistor_color": BLUE_C,
        "impedence_color": "#A4A88E",
        "I_phase": 50,
        "IM": 2,
        "R": 2.2,
        "L": 0.6,
        "w": 2
    }
    def construct(self):
        title = Title(
            "Electrical Engineering",
            scale_factor=1.25
        )
        self.play(
            Write(title, run_time=1.4)
        )

        circuit = SimpleCircuitFreqDomain()\
            .scale(0.75)\
            .to_edge(LEFT)
        self.play(
            FadeInFrom(
                circuit,
                direction=LEFT,
                run_time=0.95
            )
        )

        axes = Axes(**self.axes_config)
        axes_origin = self.axes_config["center_point"]
        im_label = axes.get_y_axis_label("\\text{Imaginary}").shift(0.8*UP+0.4*LEFT)
        re_label = axes.get_x_axis_label("\\text{Real}")
        self.play(
            FadeIn(
                VGroup(axes, im_label, re_label),
                run_time=0.95
            )
        )
        deg_to_rad = 2*PI/365
        unit_vec = lambda t: np.cos(deg_to_rad*t)*RIGHT + np.sin(deg_to_rad*t)*UP

        # setup current phasor
        I_line = Arrow(
            buff=0,
            start=axes_origin,
            end=axes_origin+self.IM*unit_vec(self.I_phase),
            color=self.current_color
        )
        I_label = TexMobject(
            "I", " &= ", "I_M", "e^{", "j", "\\varphi", "}",
            color=WHITE,
            substrings_to_isolate=["j", "I", "\\varphi"]
        )\
            .next_to(I_line.get_end(), direction=RIGHT)\
            .shift(0.4*UP+0.3*LEFT)
        I_label.get_part_by_tex("j").set_color(YELLOW)
        I_label.get_part_by_tex("I").set_color(self.current_color)
        I_label[2].set_color(self.current_color)
        I_label[3].set_color(self.current_color)
        I_label.get_part_by_tex("\\varphi").set_color(self.current_color)
        I_phase_arc = Arc(
            angle=deg_to_rad * self.I_phase,
            arc_center=axes_origin,
            color=self.current_color
        )
        I_phase_label = TexMobject(
            "\\varphi",
            color=self.current_color
        )\
            .move_to(axes_origin+1.25*unit_vec(self.I_phase*0.75))
        self.play(
            TransformFromCopy(
                circuit.vs_text,
                VGroup(I_line, I_label, I_phase_arc, I_phase_label),
                run_time=0.95
            )
        )

        # impedence vector
        Z_phase = np.arctan((self.w*self.L)/self.R)/deg_to_rad
        Z_ampl = ((self.w*self.L)**2+self.R**2)**0.5
        # print(f"({self.R},{self.w*self.L}): {Z_phase} -> {Z_ampl}")
        Z_line = Arrow(
            buff=0,
            start=axes_origin,
            end=axes_origin + Z_ampl * unit_vec(Z_phase),
            color=self.impedence_color
        )
        Z_label = TexMobject(
            "Z", " &= ", "R", "+", "j", "\\omega", "L",
            substrings_to_isolate=["Z", "R", "j", "L", "\\omega"],
            color=WHITE
        ) \
            .next_to(Z_line.get_end(), direction=RIGHT)\
            .shift(0.2*DOWN+0.1*LEFT)
        Z_label.get_part_by_tex("Z").set_color(self.impedence_color)
        Z_label.get_part_by_tex("R").set_color(self.resistor_color)
        Z_label.get_part_by_tex("j").set_color(YELLOW)
        Z_label.get_part_by_tex("L").set_color(self.inductor_color)
        Z_label.get_part_by_tex("\\omega").set_color(self.current_color)
        Z_phase_arc = Arc(
            angle=deg_to_rad * Z_phase,
            arc_center=axes_origin,
            color=self.impedence_color,
            radius=1.5
        )
        Z_phase_label = TexMobject(
            "\\theta",
            color=self.impedence_color
        ) \
            .move_to(axes_origin + 1.75 * unit_vec(Z_phase / 2))
        self.play(
            TransformFromCopy(
                VGroup(circuit.L_text, circuit.R_text),
                VGroup(Z_line, Z_label, Z_phase_arc, Z_phase_label),
                run_time=0.95
            )
        )

        V_line = Arrow(
            buff=0,
            start=axes_origin,
            end=axes_origin + Z_ampl * unit_vec(Z_phase),
            color=self.impedence_color
        )
        V_arc2 = Z_phase_arc.copy()
        V_ang_label2 = Z_phase_label.copy()
        self.add(V_line, V_arc2, V_ang_label2)
        print(V_line.get_start())
        self.play(
            Rotate(
                VGroup(V_line, V_arc2, V_ang_label2),
                angle=self.I_phase*deg_to_rad,
                about_point=axes_origin,
                run_time=0.95
            )
        )
        self.play(
            ApplyMethod(
                V_line.scale_about_point,
                self.IM, axes_origin,
                run_time=0.95
            ),
        )
        self.play(
            ApplyMethod(
                V_line.set_color,
                self.voltage_color,
                run_time=0.95
            )
        )

        V_label = TexMobject(
            "V", "= ", "I", "Z", "=|", "Z", "|", "I_M", "e^{", "j", "(", "\\varphi", "+", "\\theta", ")}",
            substrings_to_isolate=["V","|Z|", "j", "I_M", "\\varphi", "\\theta", "I", "Z"],
            color=WHITE
        ) \
            .next_to(V_line.get_end(), direction=RIGHT)\
            .shift(0.3*DOWN)
        V_label.get_part_by_tex("I").set_color(self.current_color)
        V_label.get_parts_by_tex("Z").set_color(self.impedence_color)
        V_label.get_part_by_tex("V").set_color(self.voltage_color)
        V_label.get_part_by_tex("j").set_color(YELLOW)
        V_label[7].set_color(self.current_color)
        V_label[8].set_color(self.current_color)
        V_label.get_part_by_tex("\\varphi").set_color(self.current_color)
        V_label.get_part_by_tex("\\theta").set_color(self.impedence_color)
        self.play(
            FadeIn(V_label),
            run_time=0.95
        )

        self.wait(4.87)

class ComplexQuantitiesPaper(Scene):
    def construct(self):
        # create charles stienmitz photo
        cs_image = self.get_stienmitz_image()
        self.play(
            FadeIn(
                cs_image,
                run_time=0.77
            )
        )

        # add pages to screen
        pages = self.get_paper(cs_image, n_pages=7)
        self.play(
            *[
                FadeIn(page)
                for page in pages
            ]
        )

        # scroll pages
        rect=Rectangle(width=8, height=4, color=BLACK, fill_opacity=1)\
            .next_to(pages[0],direction=UP)\
            .shift(2.6*DOWN)
        title_text = TextMobject("\\textbf{Complex Quantities and their}\\\\"
                                 "\\textbf{use in Electrical Engineering}")\
            .scale(1.3)\
            .move_to(rect.get_center())\
            .shift(1*DOWN)
        page_speed = 3.2 #Munit/s
        self.play(
            ApplyMethod(
                pages.shift, 2.23 * page_speed * UP,
                run_time=2.23,
                rate_func=linear,
            ),
        )
        self.play(
            ApplyMethod(
                pages.shift, 10 * page_speed * UP,
                run_time=10,
                rate_func=linear,
            ),
            AnimationGroup(
                FadeIn(
                    rect
                ),
                Write(
                    title_text
                ),
                lag_ratio=0.01
            )
        )


    def get_paper(self, cs_image, n_pages=20, img_scale=5):
        pages = Group(
            *[
                ImageMobject("images/ep1/ComplexQuantitiesPaper/paper/img-{:02d}.png".format(i))
                .scale(img_scale)
                for i in range(1,n_pages+1)
            ]
        )
        pages\
            .arrange(DOWN, buff=0.1) \
            .next_to(cs_image, direction=RIGHT, buff=2, aligned_edge=UP)

        return pages

    def get_stienmitz_image(self):
        cs_image=ImageMobject("images/ep1/ComplexQuantitiesPaper/portrait_cs_2.jpg")
        cs_image.to_edge(LEFT, buff=1)
        cs_image.scale(4)
        return cs_image

class PoleZeroPlot(Scene):
    CONFIG = {
        "time_axes_config": {
            "number_line_config": {
                "include_tip": False,
            },
            "x_axis_config": {
                "color": BLUE_C,
            },
            "y_axis_config": {
                "color": BLUE_C,
            },
            "x_min": 0,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "center_point": RIGHT_SIDE+7*LEFT+0.5*UP,
        },
        "pole_zero_axes_config": {
            "number_line_config": {
                "include_tip": True,
            },
            "x_axis_config": {
                "color": RED_C,
            },
            "y_axis_config": {
                "color": RED_C,
            },
            "x_min": -3,
            "x_max": 3,
            "y_min": -3,
            "y_max": 3,
            "center_point": LEFT_SIDE+5*RIGHT+0.5*UP,
        }
    }
    def construct(self):
        time_axes = Axes(**self.time_axes_config)
        y_label = time_axes.get_y_axis_label("\\text{h(t)}").shift(0.5*UP)
        time_label = time_axes.get_x_axis_label("\\text{time}").set_color(BLUE_C)
        self.add(time_axes, time_label, y_label)

        pole_zero_axes = Axes(**self.pole_zero_axes_config)
        pole_zero_origin = self.pole_zero_axes_config["center_point"]
        re_label = pole_zero_axes.get_x_axis_label("\\text{Real}").set_color(RED_C)
        im_label = pole_zero_axes.get_y_axis_label("\\text{Imaginary}").set_color(RED_C)
        self.add(pole_zero_axes, re_label, im_label)

        vals = self.get_vals()
        # print(f"vals = {vals}")
        zero_label = Circle(color=WHITE)\
            .scale(0.1)\
            .move_to(pole_zero_origin)
        pole_labels = VGroup(
            self.get_pole_marker()
                .move_to(pole_zero_origin),
            self.get_pole_marker()
                .move_to(pole_zero_origin),
        )

        # initialize pole zero plot to (0,0,0)
        time_graph = time_axes.get_graph(self.get_time_graph(0, 0, 0))
        self.add(zero_label, pole_labels,  time_graph)

        self.add(
            Title("Pole-Zero Plot")
        )

        system_diagram = self.get_system_diagram()\
            .to_corner(DR)
        self.add(
            system_diagram
        )

        run_time = 0.06
        for s, w, z in vals:
            # print(f"({s}, {w}, {z})")
            self.play(
                ApplyMethod(
                    zero_label.move_to,
                    pole_zero_origin + RIGHT * z,
                    run_time=run_time
                ),
                ApplyMethod(
                    pole_labels[0].move_to,
                    pole_zero_origin + RIGHT * s + UP * w,
                    run_time=run_time
                ),
                ApplyMethod(
                    pole_labels[1].move_to,
                    pole_zero_origin + RIGHT * s - UP * w,
                    run_time=run_time
                ),
                Transform(
                    time_graph,
                    time_axes.get_graph(self.get_time_graph(s, w, z)),
                    run_time=run_time
                )
            )
            # self.wait()

        self.wait(3.79)

    def get_vals(self):
        vals = []

        def triangle(n, xmin, xmax, num_points):
            l = int((xmin/(xmin+xmax))*num_points)
            q = num_points - l
            m1 = (2*xmin)/l
            if q > 0:
                m2 = (2*xmax)/q
            else:
                m2 = 0
            # print(f"m1 = {m1}, m2 = {m2}, l = {l}, q = {q}")
            if n <= l/2:
                return -m1*n
            if l/2 < n <= l:
                return -xmin + m1*(n-l/2)
            if l < n <= l + q/2:
                return (n - l)*m2
            else:
                return xmax - (n - l - q/2)*m2

        # move left then right
        num_points_lr = 100
        xmin = 2
        xmax = 1
        for n in range(num_points_lr):
            s = triangle(n, xmin, xmax, num_points_lr)
            # z = triangle(n//2, zmin, zmax, num_points_lr)
            vals += [(s, 0, 0)]
        vals += [(0, 0, 0)]

        # move up then down
        num_points_ud = 100
        ymin = 2.5
        ymax = 0
        for n in range(num_points_ud):
            # w = triangle(n, ymin, ymax, num_points_ud)
            w = n * (ymin/num_points_ud)
            # z = triangle(n//2, zmin, zmax, num_points_ud)
            vals += [(0, w, 0)]
        vals += [(0, ymin, 0)]

        # circular point
        num_points = 50
        radius_x = 1
        radius_y = 2.5
        for theta in np.append(np.linspace(PI/2, 0, num_points//2),
                               np.linspace(0, int(0.95*PI), int(0.95*num_points))):
            s = radius_x*np.cos(theta)
            w = radius_y*np.sin(theta)
            vals += [(s, w, 0)]

        last_s = vals[-1][0]
        last_w = vals[-1][1]
        num_points_z = 50
        zmin = 3
        zmax = 3
        for n in range(num_points_z):
            z = triangle(n, zmin, zmax, num_points_z)
            vals += [(last_s, last_w, z)]

        return vals

    def get_system_diagram(self):
        rect = Rectangle().scale(0.75)
        tf = TexMobject("h(t)").move_to(rect.get_center())
        arrow_in = Arrow(
            start=rect.get_left()+LEFT,
            end=rect.get_left(),
            buff=0
        )
        arrow_out = Arrow(
            start=rect.get_right(),
            end=rect.get_right() + RIGHT,
            buff=0
        )
        in_func = TexMobject("x(t)")\
            .next_to(arrow_in, direction=LEFT)
        out_func = TexMobject("y(t)") \
            .next_to(arrow_out, direction=RIGHT)
        return VGroup(rect, tf, arrow_in, arrow_out, in_func, out_func)

    def get_pole_marker(self):
        return VGroup(
            Line(
                start=DL, end=UR
            ),
            Line(
                start=UL, end=DR
            )
        )\
            .scale(0.1)

    # get impulse response
    def get_time_graph(self, s, w, z, freq_mult=3):
        ''' multiply w by freq_mult to increase frequency '''
        # zero frequency case
        if w == 0:
            return lambda t: 2*np.exp(s*t)*(s*t-z*t+1)

        return lambda t: \
            2*(((s-z)/(freq_mult*w))*np.sin((freq_mult*w)*t) + np.cos((freq_mult*w)*t))*np.exp(s*t)

class CompareToClassroom(Scene):
    def construct(self):
        # add line dividing screen
        dividing_line = DashedLine(
            start=FRAME_HEIGHT*0.5*DOWN,
            end=FRAME_HEIGHT*0.5*UP,
            dash_length=0.25
        )
        self.play(
            ShowCreation(dividing_line)
        )

        # my video title
        my_video = TextMobject("\\underline{This Video}")
        my_video.move_to(FRAME_WIDTH*0.25*LEFT + FRAME_HEIGHT*0.5*UP + my_video.get_height()*0.5*DOWN + 0.2*DOWN)
        self.play(
            Write(my_video)
        )

        # add animations later
        todo = TextMobject("Insert\\\\Visuals\\\\Later")\
            .move_to(FRAME_WIDTH*0.25*LEFT)
        self.play(
            Write(todo),
            Write(SurroundingRectangle(todo, buff=2))
        )
        self.wait(2.4)

        # add college classroom title
        classroom = TextMobject("\\underline{Circuits Class}")
        classroom.move_to(
            FRAME_WIDTH * 0.25 * RIGHT + FRAME_HEIGHT * 0.5 * UP + classroom.get_height() * 0.5 * DOWN + 0.2 * DOWN)
        self.play(
            Write(classroom)
        )

        # add math
        # kw = {
        #     "substrings_to_isolate": ["v"]
        # }
        kw ={}
        eqs = VGroup(
            TexMobject("v", " = V_M cos(\\omega t + \\varphi)", **kw),
            TexMobject("{d", "v", "\\over", "dt}", " = -V_M \\omega sin(\\omega t + \\varphi)", **kw),
            TexMobject("{d", "v", "\\over dt} = V_M \\omega cos(\\omega t + \\varphi + 90^\\circ)", **kw),
            TexMobject("{d", "v", "\\over dt} = \\Re(\\omega V_M e^{j \\omega t} e^{j \\varphi} e^{j 90^\\circ})", **kw),
            TexMobject("{d", "v", "\\over dt} = \\Re(j \\omega V_M e^{j \\omega t} e^{j \\varphi})", **kw),
        ) \
            .arrange(DOWN, aligned_edge=LEFT) \
            .move_to(FRAME_WIDTH*0.25*RIGHT)
        self.play(
            Write(eqs)
        )

        self.wait(1.53)

class NoPrerequisites(Scene):
    def construct(self):
        # show list
        list = BulletedList(
            "Calculus",
            "Physics",
            "Circuits I"
        )\
            .scale(1.25)
        preq_title = TextMobject("\\underline{Background Knowledge}")\
            .next_to(list, direction=UP, buff=0.5) \
            .scale(1.5)
        self.play(
            Write(preq_title)
        )
        self.wait(2.67)
        self.play(
            AnimationGroup(
                *[
                    Write(item)
                    for item in list
                ],
                lag_ratio=1
            )
        )

        # cross out
        list_group = VGroup(preq_title, list)
        x_height = max(list_group.get_width(), list_group.get_height()) + 0.1
        x_center = list_group.get_center()
        x = VGroup(
            Line(
                start=x_center+UR*0.5*x_height,
                end=x_center+DL*0.5*x_height,
                stroke_width=30,
                color=RED
            ),
            Line(
                start=x_center + UL * 0.5 * x_height,
                end=x_center + DR * 0.5 * x_height,
                stroke_width=30,
                color=RED
            )
        )
        self.play(
            Write(x)
        )
        self.wait(1.6)
