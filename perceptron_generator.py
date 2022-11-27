from manim import *

def generate_perceptron():
    perceptron_structure = SVGMobject("assets/images/perceptron.svg")
    label_x = Tex("X", font_size = 40, color = BLACK).align_to(perceptron_structure, LEFT).shift(0.15 * RIGHT + 0.7 * UP)
    label_y = Tex("Y", font_size = 40, color = BLACK).align_to(label_x, LEFT).shift(0.7 * DOWN)
    w_x = Tex(r'$w_x$', font_size = 30, color = WHITE).align_to(label_x, RIGHT).shift(0.75 * RIGHT + 0.85 * UP)
    w_y = Tex(r'$w_y$', font_size = 30, color = WHITE).align_to(w_x, LEFT).shift(0.9 * DOWN)
    sum = Tex(r'$\sum$', font_size = 40, color = BLACK).shift(0.6 * LEFT)
    act_func = Tex(r'$f_a$', font_size = 40, color = BLACK).align_to(sum, RIGHT).shift(0.97 * RIGHT)
    classification = Tex(r'$0 \vee 1$', font_size = 40, color = BLACK).align_to(act_func, RIGHT).scale(0.8).shift(1.55 * RIGHT)
    return VGroup(perceptron_structure, label_x, w_x, label_y, w_y, sum, act_func, classification).scale(1.3).to_edge(RIGHT).to_edge(DOWN).shift(0.6 * LEFT + 0.3 * UP), label_x, label_y, w_x, w_y, sum, act_func, classification

def create_perceptron_explaination(perceptron):
    perceptron_sr = SurroundingRectangle(perceptron, buff = MED_SMALL_BUFF, color = YELLOW)
    perceptron_label = Tex("Perzeptron", font_size = 40, color = YELLOW).align_to(perceptron_sr, LEFT + UP).shift(0.5 * UP)
    perceptron_description = VGroup(perceptron_sr, perceptron_label)
    return perceptron_sr, perceptron_label, perceptron_description

def create_inputs_explaination(label_x, label_y):
    in_x_sr = SurroundingRectangle(label_x, buff = MED_SMALL_BUFF, color = YELLOW)
    in_y_sr = SurroundingRectangle(label_y, buff = MED_SMALL_BUFF, color = YELLOW)
    perceptron_inputs_label = Tex("Eingabewerte", font_size = 40, color = YELLOW).align_to(in_x_sr, LEFT + UP).shift(0.5 * UP + 0.75 * LEFT)
    perceptron_inputs_description = VGroup(in_x_sr, in_y_sr, perceptron_inputs_label)
    return in_x_sr, in_y_sr, perceptron_inputs_label, perceptron_inputs_description

def create_weights_explaination(w_x, w_y):
    w_x_sr = SurroundingRectangle(w_x, buff = SMALL_BUFF, color = YELLOW)
    w_y_sr = SurroundingRectangle(w_y, buff = SMALL_BUFF, color = YELLOW)
    perceptron_weights_label = Tex("Gewichte", font_size = 40, color = YELLOW).align_to(w_x_sr, LEFT + UP).shift(0.5 * UP + 0.52 * LEFT)
    perceptron_weights_description = VGroup(w_x_sr, w_y_sr, perceptron_weights_label)
    return w_x_sr, w_y_sr, perceptron_weights_label, perceptron_weights_description

def create_sum_explaination(sum):
    sum_sr = SurroundingRectangle(sum, buff = MED_SMALL_BUFF, color = YELLOW)
    perceptron_sum_label = Tex("Gewichtete Summe", font_size = 40, color = YELLOW).align_to(sum_sr, LEFT + UP).shift(1.3 * UP + 1.2 * LEFT)
    perceptron_sum_description = VGroup(sum_sr, perceptron_sum_label)
    return sum_sr, perceptron_sum_label, perceptron_sum_description

def create_activation_function_explaination(act_func):
    act_func_sr = SurroundingRectangle(act_func, buff = MED_SMALL_BUFF, color = YELLOW)
    perceptron_act_func_label = Tex("Aktivierungsfunktion", font_size = 40, color = YELLOW).align_to(act_func_sr, LEFT + UP).shift(1.3 * UP + 1.4 * LEFT)
    perceptron_act_func_description = VGroup(act_func_sr, perceptron_act_func_label)
    return act_func_sr, perceptron_act_func_label, perceptron_act_func_description

def create_classification_explaination(classification):
    classification_sr = SurroundingRectangle(classification, buff = MED_SMALL_BUFF + 0.1, color = YELLOW)
    perceptron_classification_label = Tex("Vorhersage", font_size = 40, color = YELLOW).align_to(classification_sr, LEFT + UP).shift(0.5 * UP + 0.25 * LEFT)
    perceptron_classification_description = VGroup(classification_sr, perceptron_classification_label)
    return classification_sr, perceptron_classification_label, perceptron_classification_description

def create_step_function(perceptron):
    # Step-function
        # SF-Axes + Labels
        sf_axis = Axes(
            x_range = [-2, 2],
            y_range = [0, 1.2],
            x_length = 4,
            y_length = 1.2,
            axis_config = {
                "include_ticks": True,
                "include_numbers": True,
                "tip_width": 0.1,
                "tip_height": 0.1,
                "label_direction": UP,
            },
            tips = True,
        )
        sf_y_label = sf_axis.get_y_axis_label("y").shift(0.3 * LEFT + 0.1 * UP)
        sf_x_label = sf_axis.get_x_axis_label("x").shift(0.1 * RIGHT + 0.7 * DOWN)
        
        # SF-Plot
        sf_graph = sf_axis.plot(lambda x: 1 if x >= 0 else 0, discontinuities = [0], color = RED, use_smoothing = False)

        # SF-Group
        sf = VGroup(sf_axis, sf_x_label, sf_y_label, sf_graph).align_to(perceptron, LEFT + UP).shift(0.4 * RIGHT + 2.5 * UP).scale(0.9)

        # SF-Surrounding-Box
        sf_sr = SurroundingRectangle(sf, color = WHITE, buff = MED_SMALL_BUFF)

        return sf, sf_sr