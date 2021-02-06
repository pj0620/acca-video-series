from manimlib.imports import *

class DottedLine(Line):
    CONFIG = {
        "dot_config": {
            "radius": 0.05
        },
        # wll used fixed spacing if not None otherwise num_points used
        "fixed_spacing": None,
        "num_dots": 10
    }

    def __init__(self, *args, **kwargs):
        Line.__init__(self, *args, **kwargs)
        self.clear_points()
        self.add_dots()

    def add_dots(self):
        self.start_dot = Dot(**self.dot_config).move_to(self.start)
        self.end_dot = Dot(**self.dot_config).move_to(self.end)
        self.add(self.start_dot,self.end_dot)

        if self.fixed_spacing is None:
            length = np.linalg.norm(self.start - self.end)
            spacing = length/(self.num_dots-1)
            dir_vec = (self.end - self.start)/length
            print("length = " + str(length))
            print("spacing = " + str(spacing))
            print("dir_vec = " + str(dir_vec))
            self.add(
                *[
                    Dot(**self.dot_config).move_to(self.start + dir_vec * spacing * i)
                    for i in range(1, self.num_dots-1)
                ]
            )

    def get_start(self):
        if len(self.submobjects) > 0:
            return self.start_dot.get_start()
        else:
            return Line.get_start(self)

    def get_end(self):
        if len(self.submobjects) > 0:
            return self.end_dot.get_end()
        else:
            return Line.get_end(self)
