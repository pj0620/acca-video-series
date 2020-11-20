from manimlib.imports import *


# not finished
class Table(VGroup):
    CONFIG = {
        "col_widths_array": None,
        "first_row_height": None,
        "row_height": None,
        "col_alignment_array": None,
        "first_row_alignment_array": None,

        # line settings for table
        "first_col_kw": {},
        "first_row_kw": {},
        "first_row_divide_line_kw": {},
        "col_kw": {},
        "row_kw": {},
    }

    def __init__(self, entries, **kwargs):
        VGroup.__init__(self)
        self.entries = entries
        self.build_params()
        self.build_table(entries)

    def build_table(self):
        pass

    def build_params(self):
        if self.col_widths_array is None:
            self.col_widths_array = [mob.get_width()*1.1 for mob in self.entries[1]]
