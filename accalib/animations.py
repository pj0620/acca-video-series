from manim import *

class EllipsesFlash(AnimationGroup):
    def __init__(self,
                 point,
                 color="#FFFF00",
                 line_length=0.2,
                 num_lines=12,
                 flash_radius_x=0.3,
                 flash_radius_y=0.3,
                 line_stroke_width=3,
                 run_time=1,
                 **kwargs):
        self.point = point
        self.color = color
        self.line_length = line_length
        self.num_lines = num_lines
        self.flash_radius_x = flash_radius_x
        self.flash_radius_y = flash_radius_y
        self.line_stroke_width = line_stroke_width
        self.run_time = run_time
        self.lines = self.create_lines()
        animations = self.create_line_anims()
        super().__init__(
            *animations,
            group=self.lines,
            **kwargs,
        )

    def create_lines(self):
        lines = VGroup()
        for angle in np.arange(0, TAU, TAU / self.num_lines):
            line = Line(ORIGIN, self.line_length * RIGHT)
            radius = self.get_radius_ellipse(angle)
            line.shift((radius - self.line_length) * RIGHT)
            line.rotate(angle, about_point=ORIGIN)
            lines.add(line)
        lines.set_color(self.color)
        lines.set_stroke(width=3)
        lines.add_updater(lambda l: l.move_to(self.point))
        return lines

    def get_radius_ellipse(self,theta):
        b = self.flash_radius_x
        a = self.flash_radius_y

        return a*b/(((a*np.cos(theta))**2 + (b*np.sin(theta))**2)**0.5)

    def create_line_anims(self):
        return [
            ShowCreationThenDestruction(line)
            for line in self.lines
        ]