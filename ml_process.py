from manim import *
from manim.utils.color import Colors

def model_creation():
    data_image = ImageMobject("assets/images/data.png").scale(0.2)
    data_label = Tex('Daten', font_size = 40).move_to(data_image.get_center()).shift(1.4 * DOWN)
    data = Group(data_image, data_label)

    arrow_1 = get_arrow().move_to(data_image.get_center()).shift(2 * RIGHT)

    training_image = ImageMobject("assets/images/training.png").scale(0.2).move_to(arrow_1.get_center()).shift(2 * RIGHT)
    training_label = Tex('Training', font_size = 40).move_to(training_image.get_center()).shift(1.4 * DOWN)
    training = Group(training_image, training_label)

    arrow_2 = get_arrow().move_to(training_image.get_center()).shift(2 * RIGHT)

    model_image = ImageMobject("assets/images/model.png").scale(0.2).move_to(arrow_2.get_center()).shift(2 * RIGHT)
    model_label = Tex('KI-Modell', font_size = 40).move_to(model_image.get_center()).shift(1.4 * DOWN)
    model = Group(model_image, model_label)

    return Group(data, arrow_1, training, arrow_2, model).move_to(ORIGIN)

def get_arrow():
    return Tex(r'$\rightarrow$', font_size = 100)

def prediction():
    sample_image = ImageMobject("assets/images/sample.png").scale(0.2)
    sample_label = Tex('Daten', font_size = 40).move_to(sample_image.get_center()).shift(1.4 * DOWN)
    sample = Group(sample_image, sample_label)

    arrow_1 = get_arrow().move_to(sample_image.get_center()).shift(2 * RIGHT)

    model_image = ImageMobject("assets/images/model.png").scale(0.2).move_to(arrow_1.get_center()).shift(2 * RIGHT)
    model_label = Tex('KI-Modell', font_size = 40).move_to(model_image.get_center()).shift(1.4 * DOWN)
    model = Group(model_image, model_label)

    arrow_2 = get_arrow().move_to(model_image.get_center()).shift(2 * RIGHT)

    prediction_image = ImageMobject("assets/images/prediction.png").scale(0.2).move_to(arrow_2.get_center()).shift(2 * RIGHT)
    prediction_label = Tex('Vorhersage', font_size = 40).move_to(prediction_image.get_center()).shift(1.4 * DOWN)
    prediction = Group(prediction_image, prediction_label)

    return Group(sample, arrow_1, model, arrow_2, prediction).move_to(ORIGIN)
