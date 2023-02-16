from manim import *
from manim.utils.color import Colors

def create_bullet_point_list(arguments):
    bullet_point_list = VGroup()
    for i in range(len(arguments)):
        dot = LabeledDot(Tex(i + 1, font_size = 40).set_color(BLACK)).to_edge(LEFT).shift(i * DOWN)
        text = Tex(arguments[i], font_size = 35).next_to(dot, RIGHT)
        bullet_point_list.add(VGroup(dot, text))
    
    return bullet_point_list.move_to(ORIGIN)
