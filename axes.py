from manim import *

# Koordinatensystem
def generate_axes():
    axis = Axes(
        x_range=[0, 5],
        y_range=[0, 5],
        x_length=5,
        y_length=5,
        axis_config={
            "include_ticks": False,
            "include_numbers": False,
            "tip_width": 0.1,
            "tip_height": 0.1,
            "label_direction": UP
        },
        tips=True,
    )
    y_label = axis.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.1)
    x_label = axis.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.1)
    return VGroup(axis, y_label, x_label).to_edge(LEFT).shift(0.5 * DOWN)