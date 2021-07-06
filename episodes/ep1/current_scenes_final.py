from manimlib.imports import *
from accalib.electrical_circuits import BatteryLampCircuit
from accalib.particles import Electron

class IntroCurrentPart(Scene):
    def construct(self):
        section_label = TextMobject(
            "Part 2: \\\\",
            "Current"
        ).scale(1.5)
        self.play(
            Write(section_label[0]),
        )
        self.wait()
        self.play(
            Write(section_label[1])
        )
        self.wait()


class CurrentOverview(Scene):
    CONFIG = {
        "current_color": GREEN_D,  # GREEN_C
        "voltage_color": RED_D,  # RED_A,RED_B,
        "resistance_color": ORANGE,
        "electron_freq_0": 0.11,
        "electron_freq_1": 0.5
    }
    def construct(self):
        # add circuit
        circuit = BatteryLampCircuit(
            electron_freq=self.electron_freq_0
        ) \
            .shift(UP)
        self.add(circuit)
        self.wait(2.09)

        # label elements
        elements_label = VGroup()
        elements_label.add(
            SurroundingRectangle(
                circuit.outer_rect
            ),
            SurroundingRectangle(
                VGroup(
                    circuit.base_big,
                    circuit.base_small,
                    circuit.light_bulb
                )
            )
        )
        self.play(
            AnimationGroup(
                *[
                    Write(mob)
                    for mob in elements_label
                ],
                lag_ratio=1
            )
        )
        self.play(
            FadeOut(elements_label),
        )

        # add electrons
        circuit.setup_electrons()
        self.add(*circuit.electrons)
        self.add(circuit.battery, circuit.block_rect, circuit.base_big, circuit.base_small)
        self.play(
            circuit.get_electron_anim(2.43)
        )

        arrow = CurvedArrow(
            circuit.outer_rect.get_bottom() + 1.0 * RIGHT + 0 * DOWN,
            circuit.outer_rect.get_top() + 1.0 * RIGHT + 0 * UP,
            color=GREEN,
            angle=np.pi * 0.8
        )
        self.play(
            ShowCreationThenFadeOut(
                arrow,
                run_time=5
            ),
            circuit.get_electron_anim(5)
        )
        self.play(
            circuit.get_electron_anim(1.48)
        )

        # fade in current label
        point1 = circuit.electron_vect_inter.interpolate(0.55)
        point2 = circuit.electron_vect_inter.interpolate(0.5)
        angle = np.arccos((point2[0] - point1[0]) / np.linalg.norm(point2 - point1))
        current_arrow = ArrowTip(
            start_angle=-1 * angle,
            color=self.current_color
        ) \
            .scale(2.5) \
            .move_to(point1 + 0.05 * UR)
        current_text = TextMobject(
            "current", "=",
            color=self.current_color) \
            .next_to(current_arrow, direction=UR) \
            .shift(0.5 * RIGHT) \
            .scale(1.5)
        current_value = DecimalNumber(
            1,
            unit="A",
            color=self.current_color,
            num_decimal_places=2
        ) \
            .scale(1.5) \
            .next_to(current_text, direction=RIGHT, buff=0.3)
        current_tracker = ValueTracker(1)
        self.play(
            FadeInFrom(current_arrow, direction=UP),
            FadeInFrom(current_text, direction=UP),
            FadeInFrom(current_value, direction=UP),
            circuit.get_electron_anim()
        )
        self.play(
            circuit.get_electron_anim(5.66)
        )

        # draw square around amp /
        self.play(
            ShowCreationThenDestructionAround(
                current_value.submobjects[-1],
                surrounding_rectangle_config={"stroke_width": 7},
                run_time=1
            ),
            circuit.get_electron_anim(1)
        )

        current_value.add_updater(
            lambda x:
            x.set_value(current_tracker.get_value())
        )
        
        # label equivalent electrons per second
        current_1 = DecimalNumber(
            1,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT,
            unit="A"
        ) \
            .scale(1.5) \
            .to_corner(DL, buff=1.7)\
            .shift(1.9*RIGHT)\
            .add_updater(lambda x: x.set_value(current_tracker.get_value()))
        current_1_eq = TexMobject(
            "=",
            color=self.current_color
        ) \
            .scale(1.5) \
            .next_to(current_1, direction=RIGHT, buff=0.2)
        elec_per_sec = DecimalNumber(
            6246000000000000,
            num_decimal_places=0,
            color=self.current_color,
            edge_to_fix=RIGHT
        ) \
            .scale(1.5) \
            .next_to(current_1_eq, direction=RIGHT, buff=1)
        elec_per_sec.add_updater(
            lambda x: x.set_value(6242000000000000*current_tracker.get_value()),
            call_updater=True
        )
        elec_per_sec_unit_tex = TexMobject(
            "{1", "\\over", "\\text{second}}"
        ) \
            .scale(1.15) \
            .next_to(elec_per_sec, direction=RIGHT)
        elec_per_sec_unit_elec = Electron() \
            .scale(0.3) \
            .move_to(elec_per_sec_unit_tex[0])
        elec_per_sec_unit = VGroup(
            elec_per_sec_unit_tex, elec_per_sec_unit_elec
        )
        self.play(
            FadeInFrom(
                VGroup(current_1, current_1_eq, elec_per_sec),
                direction=DOWN
            ),
            FadeInFrom(
                elec_per_sec_unit,
                direction=DOWN
            ),
            circuit.get_electron_anim(5.31)
        )

        # set current to 2 A
        self.play(
            ApplyMethod(
                current_tracker.set_value, 2
            ),
            circuit.get_electron_acceleration_anim(self.electron_freq_0 * 3)
        )
        self.play(
            circuit.get_electron_anim(7.53)
        )

        # set current to 40 A
        self.play(
            ApplyMethod(
                current_tracker.set_value, 40
            ),
            circuit.get_electron_acceleration_anim(self.electron_freq_0 * 10)
        )
        self.play(
            circuit.get_electron_anim(7.8)
        )

        # remove battery
        circuit.electrons_flowing = False
        circuit.set_light_bulb_state(False)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons + circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(0)
        # stop electrons
        circuit.set_electron_freq(0)
        self.play(
            FadeOutAndShift(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            ApplyMethod(
                current_tracker.set_value, 0
            ),
            circuit.get_electron_anim(13.65)
        )

        circuit.electrons_flowing = True
        circuit.set_light_bulb_state(True)
        circuit.set_electron_freq(self.electron_freq_0)
        for i in range(len(circuit.electrons)):
            cur = (circuit.electron_loc.get_value() + i / circuit.num_of_electrons +
                   circuit.electron_disps[i]) % 1
            if 0.755 < cur < 1:
                circuit.electrons[i].set_opacity(1)
                circuit.electrons[i].set_stroke(BLUE, opacity=0)
        definition = TextMobject(
            "current - measure of flow of electrons in a circuit",
            color=YELLOW
        ) \
            .scale(1) \
            .to_corner(DOWN)
        self.play(
            FadeInFrom(
                circuit.battery,
                direction=LEFT,
                run_time=1
            ),
            ApplyMethod(
                current_tracker.set_value, 1
            ),
            Write(
                definition,
                run_time=2
            ),
            circuit.get_electron_anim(2.15)
        )

        # wait for scene to end
        self.play(
            circuit.get_electron_anim(14.7)
        )