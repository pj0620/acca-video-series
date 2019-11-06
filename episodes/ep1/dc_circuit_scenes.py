from manimlib.imports import *
from manimlib.constants import *
from svg_objects import *

class SimpleDCCircuit(Scene):
    def construct(self):
        # # Fade in circuit
        # voltage_source, resistor, wires, vs_text, r_text = self.get_circuit()
        # kw = {
        #     "direction" : UP,
        #     "run_time" : 2,
        # }
        # self.play(
        #     FadeInFrom(voltage_source,**kw),
        #     FadeInFrom(resistor, **kw),
        #     FadeInFrom(wires, **kw),
        #     FadeInFrom(vs_text,**kw),
        #     FadeInFrom(r_text,**kw),
        # )
        # self.wait(0.5)
        #
        # # shake voltage source
        # self.play(WiggleOutThenIn(voltage_source,
        #                           rotation_angle=0.02 * TAU,
        #                           scale_value=1.17))
        # self.wait(0.5)
        #
        # # shake resistor
        # self.play(WiggleOutThenIn(resistor,
        #                           rotation_angle=0.02 * TAU,
        #                           scale_value=1.17))
        # self.wait(0.5)
        #
        # # expand voltage source
        # self.play(
        #     FadeOut(wires),
        #     FadeOut(vs_text),
        #     FadeOut(r_text),
        #     FadeOut(resistor),
        #     Succession(
        #         ApplyMethod(voltage_source.move_to, (FRAME_WIDTH/2 - voltage_source.get_width()/2 - 1.6)*LEFT),
        #         ApplyMethod(voltage_source.set_height, 6)
        #     )
        # )
        # # self.play(
        # #     ApplyMethod(voltage_source.set_height,5)
        # # )
        # self.wait(0.5)
        #
        # # Show "Voltage Source"
        # vs_label = self.get_vs_label()
        # self.play(
        #     Write(vs_label[0]),
        # )
        # self.wait(0.5)
        #
        # # Show "Independent Voltage Source"
        # self.play(
        #     Write(vs_label[1]),
        # )
        # self.wait(0.5)

        elem = VoltageSource(color=WHITE).scale(4)
        self.play(
            FadeIn(elem)
        )

        self.wait(10)

    def get_vs_volt_label(self,voltage_source):
        wire1 = self.get_wire(voltage_source.get_top(), voltage_source.get_top() + RIGHT)
        wire2 = self.get_wire(voltage_source.get_bottom(), voltage_source.get_bottom() + RIGHT)
        return VGroup(wire1,wire2)

    def get_vs_label(self):
        vs_label = TextMobject("\\underline{Voltage Source}", " / \\underline{Independent Voltage Source}")
        vs_label.scale(1.6)
        vs_label.to_edge(UP, buff=0.4)
        vs_label.shift(0.2*LEFT)
        return vs_label

    def get_circuit(self):
        voltage_source = ImageMobject("images/ep1/SimpleDCCircuit/white_comps/voltage_source.png")
        voltage_source.scale(1.25)
        voltage_source.to_corner(UL)
        voltage_source.shift(0.7*DOWN+1*RIGHT)
        vs_text = TextMobject("$12V$")
        vs_text.scale(1.75)
        vs_text.next_to(voltage_source,direction=LEFT,buff=-0.2)
        resistor = ImageMobject("images/ep1/SimpleDCCircuit/white_comps/resistor.png")
        resistor.scale(1.25)
        resistor.next_to(voltage_source,direction=RIGHT,buff=0.75)
        r_text = TextMobject("$2\Omega$")
        r_text.scale(1.75)
        r_text.next_to(resistor,direction=RIGHT,buff=-0.2)
        wires = []
        wires.append(self.get_wire(voltage_source.get_top(),
                              voltage_source.get_top() + 0.65*UP))
        wires[0].shift(0.01*LEFT)
        wires.append(self.get_wire(voltage_source.get_top() + 0.65*UP,
                              resistor.get_top() + 0.65*UP))
        wires.append(self.get_wire(resistor.get_top() + 0.65*UP,
                              resistor.get_top()))
        wires.append(self.get_wire(resistor.get_bottom(),
                              resistor.get_bottom() - 0.5*UP))
        wires.append(self.get_wire(resistor.get_bottom() - 0.5*UP,
                              voltage_source.get_bottom() - 0.5*UP))
        wires.append(self.get_wire(voltage_source.get_bottom() - 0.5*UP,
                              voltage_source.get_bottom()))
        return voltage_source, resistor, VGroup(*wires), vs_text, r_text

    def get_wire(self,start,end):
        return Line(start=start, end=end, stroke_width=7, color=WHITE)
