from manim import *

def generate_class_labels(point_plane):
    class_0 = Tex("Klasse 0", font_size = 30, color = BLACK, fill_color = BLACK).add_background_rectangle(color = WHITE, opacity = 1, buff = SMALL_BUFF).align_to(point_plane, DOWN).shift(3.75 * LEFT + 0.2 * DOWN)
    class_1 = Tex("Klasse 1", font_size = 30, color = BLACK, fill_color = BLACK).add_background_rectangle(color = WHITE, opacity = 1, buff = SMALL_BUFF).align_to(class_0, LEFT + UP).shift(5 * UP)
    return VGroup(class_0, class_1)