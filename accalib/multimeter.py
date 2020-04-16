from manimlib.imports import *
from enum import Enum

class Measurement(Enum):
    V=0
    R=1
    I=2

class Multimeter():
    def __init__(self,width=3.2,height=4.8,corner_radius=0.15,
                        screen_width=2.3, screen_height=0.8,
                        perc_screen_offset=0.08,
                        outer_radius=0.95,inner_radius=0.85,
                        perc_circ_offset=0.62,color=WHITE,
                        bar_width=0.3,initial_state=Measurement.V):
        self.state = initial_state
        self.reading = ValueTracker(0)
        self.color = color
        self.width = width
        self.height = height
        self.deg_to_rad=(2. * math.pi) / 360.
        self.angle=90
        self.submobjects = []
        kw = {
            "color": WHITE
        }
        self.border = Rectangle(width=width,
                                height=height,**kw)
        self.border.round_corners(corner_radius)

        self.screen_border = Rectangle(width=screen_width,
                                       height=screen_height,**kw)
        self.screen_border.move_to(self.border.get_top()
                                   + DOWN*self.screen_border.get_height()/2
                                   + DOWN*height*perc_screen_offset)

        self.circ_center = self.border.get_top() + DOWN*perc_circ_offset*height
        self.outer_circle = Circle(radius=inner_radius,stroke_width=3, **kw)
        self.outer_circle.move_to(self.circ_center)
        self.inner_circle = Circle(radius=outer_radius,stroke_width=3, **kw)
        self.inner_circle.move_to(self.circ_center)

        bar_length = ((4*(inner_radius**2) - bar_width**2)**0.5)
        self.bar = VGroup(Line(start=(bar_width/2)*LEFT  + (bar_length/2)*UP   + self.circ_center,
                                 end=(bar_width/2)*LEFT  + (bar_length/2)*DOWN + self.circ_center),
                          Line(start=(bar_width/2)*RIGHT + (bar_length/2)*UP   + self.circ_center,
                                 end=(bar_width/2)*RIGHT + (bar_length/2)*DOWN + self.circ_center)
                          )

        self.units_displayed = False

        self.setup_settings_labels(outer_radius,initial_state)

        self.arrow = Triangle(color=color,fill_color=WHITE,fill_opacity=1)
        self.arrow.scale(0.115)
        self.arrow.move_to(self.circ_center+inner_radius*UP+self.arrow.get_height()*0.8*DOWN)

        self.setup_connectors()

        self.setup_display()

        self.submobjects.extend([self.border, self.screen_border, self.inner_circle, self.outer_circle, self.bar,
                                 *self.labels, self.arrow, self.gnd_connect, self.vr_connect, self.i_connect,
                                 self.vr_label, self.i_label, *self.lines, self.text])
        self.submobjects.extend(list(self.unit_labels.values()))



    def setup_connectors(self):
        self.gnd_connect=Circle(radius=0.095, color=self.color)
        self.gnd_connect.move_to(self.border.get_bottom() + 0.07 * self.height * UP)
        self.vr_connect=Circle(radius=0.095, color=self.color)
        self.vr_connect.move_to(self.border.get_bottom() + 0.07 * self.height * UP + 0.3 * self.width * LEFT)
        self.i_connect=Circle(radius=0.095, color=self.color)
        self.i_connect.move_to(self.border.get_bottom() + 0.07 * self.height * UP + 0.3 * self.width * RIGHT)

        self.vr_label=TextMobject("\\textbf{V}\hspace{0mm}/\hspace{0.1mm}R").scale(0.5).next_to(self.vr_connect,
                                                                                                direction=UP, buff=0.1)
        self.i_label=TextMobject("\\textbf{I}").scale(0.57).next_to(self.i_connect, direction=UP, buff=0.12)

        self.lines=[]
        p1=self.gnd_connect.get_top() + 0.25 * UP
        p2=p1 + LEFT * 0.35
        p3=p2 + DOWN * 0.22
        p4=p3 + DOWN * 0.07
        p5=p4 + DOWN * 0.07
        self.lines.append(Line(start=self.gnd_connect.get_top(), end=p1))
        self.lines.append(Line(start=p1, end=p2))
        self.lines.append(Line(start=p2, end=p3))
        self.lines.append(Line(start=p3 + 0.16 * RIGHT, end=p3 + 0.16 * LEFT))
        self.lines.append(Line(start=p4 + 0.11 * RIGHT, end=p4 + 0.11 * LEFT))
        self.lines.append(Line(start=p5 + 0.06 * RIGHT, end=p5 + 0.06 * LEFT))

    def setup_display(self):
        self.unit_labels={}
        self.unit_labels[Measurement.V]= \
            TextMobject("V") \
                .scale(1.45) \
                .next_to(self.screen_border.get_right(), direction=LEFT, buff=0.15)
        self.unit_labels[Measurement.R]= \
            TextMobject("$\Omega$") \
                .scale(1.45) \
                .next_to(self.screen_border.get_right(), direction=LEFT, buff=0.15)
        self.unit_labels[Measurement.I]= \
            TextMobject("A") \
                .scale(1.45) \
                .next_to(self.screen_border.get_right(), direction=LEFT, buff=0.15)

        for unit_label in self.unit_labels.values():
            unit_label.save_state()

        self.value = DecimalNumber(self.reading.get_value(),num_decimal_places=1)\
                              .add_updater(lambda v: v.set_value(self.reading.get_value()))
        self.text = self.value.scale(1.5)\
                              .next_to(self.screen_border.get_left(),direction=RIGHT,buff=0.15)

    def set_value(self,scene,new_reading,run_time=0.7):
        scene.play(
            self.reading.set_value, new_reading,
            rate_func=linear,
            run_time=run_time
        )

    def setup_settings_labels(self,outer_radius,initial_state):
        unit_scale=1.01
        unit_radius=outer_radius * 1.35
        labels_text=["\\textbf{I}",
                     "\\textbf{R}",
                     "\\textbf{V}"]
        self.labels=[]
        for i in range(3):
            loc=self.circ_center + unit_radius * self.get_rect(45 + 45 * i)
            label=TextMobject(labels_text[i]).move_to(loc).scale(unit_scale)
            self.labels.append(label)

        self.initialize_state(initial_state)

    def initialize_state(self,initial_state):
        angles = {
            Measurement.I: 42,
            Measurement.R: 90,
            Measurement.V: 135,
        }
        del_angle = (angles[initial_state] - self.angle) % 360
        del_2_angle = 360 - del_angle
        if del_2_angle < del_angle:
            self.bar.rotate(-1.*del_2_angle*self.deg_to_rad, about_point=self.circ_center)
        else:
            self.bar.rotate(del_angle*self.deg_to_rad,about_point=self.circ_center)

    def set_state(self,scene,new_state,run_time=0.7):
        angles = {
            Measurement.I: 42,
            Measurement.R: 90,
            Measurement.V: 135,
        }
        kw = {
            'run_time': run_time
        }
        del_angle = (angles[new_state] - self.angle) % 360
        del_2_angle = 360 - del_angle
        if del_2_angle < del_angle:
            del_angle = -1. * del_2_angle
        self.angle += del_angle
        scene.play(
            Rotate(
                self.bar,
                del_angle * self.deg_to_rad,
                about_point=self.circ_center,
                **kw
            ),
            Rotate(
                self.arrow,
                del_angle * self.deg_to_rad,
                about_point=self.circ_center,
                **kw
            )
        )

        if self.units_displayed:
            scene.play(
                ReplacementTransform(
                    self.unit_labels[self.state],
                    self.unit_labels[new_state],
                    run_time=0.7
                )
            )
        else:
            scene.play(
                FadeIn(
                    self.unit_labels[new_state]
                ),
                FadeIn(
                    self.text
                )
            )
        self.units_displayed = True
        self.unit_labels[self.state].restore()
        self.state = new_state

    def get_rect(self,theta):
        return math.cos(self.deg_to_rad*theta)*RIGHT + \
               math.sin(self.deg_to_rad*theta)*UP

    def draw(self, scene, draw_method=FadeIn):
        animations = []
        for submobject in self.submobjects:
            if submobject in self.unit_labels.values() or \
               submobject == self.text:
                continue
            animations.append(
                draw_method(submobject)
            )
        scene.play(*animations)