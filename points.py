from manim import *
import numpy as np

def generate_point_plane(plane):
    return  Rectangle(width = 5, height = 5).align_to(plane, DOWN + LEFT).shift(0.45 * RIGHT + 0.1 * UP)

def create_point_group(point_plane):
    point_list = []
    for i in np.arange(0, 5, 0.5):
        for j in np.arange(0, 5, 0.5):
            c = Circle(radius = 0.1, fill_opacity = 1).align_to(point_plane, UP + LEFT).shift((i + 0.15) * RIGHT + (j + 0.15) * DOWN)
            if i <= j:
                c.color = RED
            else: c.color = GREEN
            point_list.append(c)

    # Remove every third point and convert list into VGroup
    del point_list[::3]
    return VGroup(*point_list)