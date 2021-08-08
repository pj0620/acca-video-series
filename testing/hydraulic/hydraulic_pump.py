from manimlib.imports import *
from accalib.hydraulic import HydraulicCircuit

class HydraulicCircuitTest(Scene):
    CONFIG = {
        "pump_ang_freq": 0.5 * PI,
        "A": 3.125  # (r^4)(\\Delta P)/Q [m^4 kPa s / L] from Hagen–Poiseuille equation
    }
    def construct(self):
        self.hydraulic_circuit = HydraulicCircuit(
            include_water_source=False,
            ang_freq=PI * 0.2
        )
        self.add(self.hydraulic_circuit)
        self.v_value = ValueTracker(12)
        self.setup_vector_fields()

        self.wait(5)

        # self.play(
        #     self.hydraulic_circuit.get_rotate_anim(5)
        # )

    def vector_field_st(self, p):
        # viscosity = 8.90E-4
        # R = abs(self.vf_x_max - self.vf_x_min) / 2.
        # r = p[0] - (self.vf_x_min + self.vf_x_max) / 2.
        # scale_factor = 0.6E-2
        # dPdx = self.voltage_to_pressure(self.v_value.get_value()) / (self.hydraulic_circuit.body.small_tube[0].get_height())

        # in small tube
        if self.vf_x_min+0 < p[0] < self.vf_x_max-0:
            if self.vf_y_min < p[1] < self.vf_y_max:
                # print(f"{p[0]} -> {scale_factor*(1/(4*viscosity))*dPdx*(R**2-r**2)*DOWN}")
                # print(f"r = {r}, R = {R}")
                # return scale_factor * (1 / (4 * viscosity)) * dPdx * (R ** 2 - r ** 2) * DOWN
                return 2 * DOWN

        return 0 * UP

    def vector_field(self, p):
        large_tube = self.hydraulic_circuit.body.large_tube
        small_tube = self.hydraulic_circuit.body.small_tube
        PUM_circle = self.hydraulic_circuit.pump_circle

        # return 1 for any non-zero pressure
        mag = int(bool(self.voltage_to_pressure(self.v_value.get_value())))

        # in pump
        if np.linalg.norm(p - self.hydraulic_circuit.body.circle.get_center()) < \
                (self.hydraulic_circuit.body.circle.get_width() / 2) * 0.8:
            return -self.pump_ang_freq * mag * self.rot_matrix.dot(p - self.hydraulic_circuit.body.circle.get_center())

        # region 1
        if large_tube[1].get_left()[0] < p[0] < \
                large_tube[0].get_left()[0]:
            if large_tube[1].get_bottom()[1] < p[1] < \
                    large_tube[0].get_top()[1] + 0.1:
                r = abs(p[0] - (large_tube[1].get_left()[0] + large_tube[0].get_left()[0]) / 2.)
                R = abs(large_tube[1].get_left()[0] - large_tube[0].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 2
        if large_tube[0].get_left()[0] < p[0] < \
                large_tube[0].get_right()[0] - 0.3:
            if large_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r = abs(p[1] - (large_tube[0].get_top()[1] + large_tube[1].get_top()[1]) / 2.)
                R = abs(large_tube[0].get_top()[1] - large_tube[1].get_top()[1]) / 2.
                return mag * RIGHT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 3
        if large_tube[0].get_right()[0] - 0.27 < p[0] < \
                large_tube[1].get_right()[0]:
            if small_tube[0].get_top()[1] < p[1] < \
                    large_tube[1].get_top()[1]:
                r = abs(p[0] - (large_tube[0].get_right()[0] - 0.27 + large_tube[1].get_right()[0]) / 2.)
                R = abs(large_tube[0].get_right()[0] - 0.27 - large_tube[1].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 4
        if large_tube[2].get_right()[0] - 0.3 < p[0] < \
                large_tube[3].get_right()[0]:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[3].get_top()[1]:
                r = abs(p[0] - (large_tube[2].get_right()[0] - 0.3 + large_tube[3].get_right()[0]) / 2.)
                R = abs(large_tube[2].get_right()[0] - 0.3 - large_tube[3].get_right()[0]) / 2.
                return mag * DOWN * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 5
        if large_tube[2].get_left()[0] < p[0] < \
                large_tube[2].get_right()[0] - 0.3:
            if large_tube[3].get_bottom()[1] < p[1] < \
                    large_tube[2].get_bottom()[1]:
                r = abs(p[1] - (large_tube[3].get_bottom()[1] + large_tube[2].get_bottom()[1]) / 2.)
                R = abs(large_tube[3].get_bottom()[1] - large_tube[2].get_bottom()[1]) / 2.
                return mag * LEFT * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        # region 6
        if large_tube[3].get_left()[0] < p[0] < \
                large_tube[2].get_left()[0]:
            if large_tube[2].get_bottom()[1] < p[1] < \
                    large_tube[2].get_top()[1]:
                r = abs(p[0] - (large_tube[3].get_left()[0] + large_tube[2].get_left()[0]) / 2.)
                R = abs(large_tube[3].get_left()[0] - large_tube[2].get_left()[0]) / 2.
                return mag * UP * (1 / (R ** 2)) * (R ** 2 - r ** 2)

        return 0 * RIGHT

    def setup_vector_fields(self):
        self.vf_x_min = self.hydraulic_circuit.body.small_tube[1].get_center()[0] - 0.01
        self.vf_x_max = self.hydraulic_circuit.body.small_tube[0].get_center()[0] + 0.01
        self.vf_y_min = self.hydraulic_circuit.body.small_tube[1].get_bottom()[1]
        self.vf_y_max = self.hydraulic_circuit.body.small_tube[1].get_top()[1] + 0.2

        # add_hguide(self, large_tube[3].get_left()[0], color=GREEN)
        # add_hguide(self, large_tube[2].get_left()[0], color=RED)
        # add_vguide(self, large_tube[2].get_bottom()[1], color=GREEN)
        # add_vguide(self, large_tube[2].get_top()[1], color=RED)

        self.rot_matrix = np.array([[0, -1, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])

        # # setup vector field in small tube
        # self.stream_lines_yellow_st = StreamLines(
        #     self.vector_field_st,
        #     delta_x=0.015,
        #     delta_y=0.1,
        #     # bad: 0.1, 0.5
        #     # good: 0.3, 0.4
        #     colors=["#FFFF00"],
        #     x_min=self.vf_x_min,
        #     x_max=self.vf_x_max,
        #     y_min=self.vf_y_max - 0.2,
        #     y_max=self.vf_y_max,
        #     dt=0.16
        #     # min_magnitude=4
        # )
        # self.stream_lines_st = StreamLines(
        #     self.vector_field_st,
        #     delta_x=0.015,
        #     delta_y=0.1,
        #     # bad: 0.1, 0.5
        #     # good: 0.3, 0.4
        #     colors=[WHITE],
        #     x_min=self.vf_x_min,
        #     x_max=self.vf_x_max,
        #     y_min=self.vf_y_max - 0.2,
        #     y_max=self.vf_y_max,
        #     dt=0.16
        #     # min_magnitude=4
        # )
        # self.animated_stream_lines_st = AnimatedStreamLines(
        #     self.stream_lines_st,
        #     line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        # )
        # self.add(self.animated_stream_lines_st)

        # setup vector field for pump
        stream_lines = StreamLines(
            self.vector_field,
            delta_x=0.2,
            delta_y=0.2,
            # dt=0.1,
            # virtual_time=1.8,
            colors=[WHITE],
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3
            # min_magnitude=4
        )
        class MyAnim(ShowPassingFlashWithThinningStrokeWidth):
            def __init__(self, vmobject, **kwargs):
                super().__init__(vmobject, **kwargs, remover=False)

        self.animated_stream_lines = AnimatedStreamLines(
            stream_lines,
            x_min=self.hydraulic_circuit.body.circle.get_left()[0],
            x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
            y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
            y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3,
            line_anim_class=MyAnim,
            # line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        )
        self.add(self.animated_stream_lines)

        # stream_lines_2 = StreamLines(
        #     self.vector_field,
        #     delta_x=0.1,
        #     delta_y=0.1,
        #     # dt=0.1,
        #     # virtual_time=1.8,
        #     colors=[WHITE],
        #     x_min=self.hydraulic_circuit.body.circle.get_left()[0],
        #     x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
        #     y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
        #     y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3
        #     # min_magnitude=4
        # )
        # self.animated_stream_lines_2 = AnimatedStreamLines(
        #     stream_lines_2,
        #     x_min=self.hydraulic_circuit.body.circle.get_left()[0],
        #     x_max=self.hydraulic_circuit.body.large_tube[1].get_right()[0],
        #     y_min=self.hydraulic_circuit.body.large_tube[3].get_bottom()[1],
        #     y_max=self.hydraulic_circuit.body.large_tube[1].get_top()[1] - 0.3,
        #     line_anim_class=MyAnim,
        #     line_anim_config={
        #         "run_time": 2,
        #         "rate_func": linear,
        #         "time_width": 0.3,
        #     },
        #     # line_anim_class=ShowPassingFlashWithThinningStrokeWidth,
        # )

    def voltage_to_pressure(self, voltage):
        return 100 + 40 * voltage
