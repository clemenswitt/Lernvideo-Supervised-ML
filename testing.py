from manim import *
from manim.utils.color import Colors

def data_table():
    table = MathTable([['x', 'y', 'K'],
        [1, 1, 0],
        [2, 2.5, 0],
        [3, 4.5, 1],
        [2, 4.7, 1],
        [0.5, 2.9, 0],
        [2.5, 2.4, 0],
        [3, 3.1, 1],
        [5, 2.8, 1],
        [1.3, 1.9, 0],
        [1.2, 2.4, 0],
        [2.8, 1.2, 0],
        [4.2, 3.3, 1]],
        include_outer_lines = True
    )
    table.height = 6

    return table.move_to(ORIGIN)

def data_table_split():
    table_training = MathTable([['x', 'y', 'K'],
        [1, 1, 0],
        [2, 2.5, 0],
        [3, 4.5, 1],
        [2, 4.7, 1],
        [0.5, 2.9, 0],
        [2.5, 2.4, 0],
        [3, 3.1, 1],
        [5, 2.8, 1]],
        include_outer_lines = True
    )
    table_training.width = 2.5
    training_data_label = Tex(r'\textbf{Trainingsdaten}', font_size = 30).align_to(table_training, ORIGIN + UP).shift(0.4 * UP)
    training = VGroup(table_training, training_data_label)

    table_test = MathTable([['x', 'y', 'K'],
        [1.3, 1.9, 0],
        [1.2, 2.4, 0],
        [2.8, 1.2, 0],
        [4.2, 3.3, 1]],
        include_outer_lines = True
    )
    table_test.width = 2.5
    table_test.align_to(table_training, RIGHT + UP).shift(3.5 * RIGHT)

    test_data_label = Tex(r'\textbf{Testdaten}', font_size = 30).align_to(table_test, ORIGIN + UP).shift(3.5 * RIGHT + 0.4 * UP)
    test = VGroup(table_test, test_data_label)

    return VGroup(training, test).move_to(ORIGIN)

def validation():
    test_table = MathTable([['x', 'y', 'K'],
        [1.3, 1.9, 0],
        [1.2, 2.4, 0],
        [2.8, 1.2, 0],
        [4.2, 3.3, 1]],
        include_outer_lines = True
    )
    test_table.height = 3

    prediction_table = MathTable([['P'],
        [0], [0], [0], [0]],
        include_outer_lines = True
    )
    prediction_table.height = 3
    prediction_table.add_highlighted_cell((2,1), color = Colors.green_c.value)
    prediction_table.add_highlighted_cell((3,1), color = Colors.green_c.value)
    prediction_table.add_highlighted_cell((4,1), color = Colors.green_c.value)
    prediction_table.add_highlighted_cell((5,1), color = Colors.red_c.value)

    prediction_table.align_to(test_table, RIGHT + UP).shift(1.1 * RIGHT)

    return VGroup(test_table, prediction_table).move_to(ORIGIN)