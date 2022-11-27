from manim import *

def generate_class_seperator_line(plane):
    return DashedLine((0.1,-0.1,0), (4.9,-4.9,0), stroke_color = YELLOW).align_to(plane, UP).align_to(plane, LEFT).shift(0.5 * RIGHT + 0.2 * DOWN)

def generate_class_seperator_label(class_seperator_line):
    return Tex("Entscheidungsgrenze", color = YELLOW, font_size = 30).align_to(class_seperator_line, RIGHT).shift(0.2 * RIGHT)