from manim import *
from manim.utils.color import Colors

def regression_learning():
    house_small_image = ImageMobject('assets/images/house_small.png').scale(0.5)
    house_small_label = Tex(r'200.000 €', font_size = 30).move_to(house_small_image.get_center()).shift(0.8 * DOWN)
    house_small = Group(house_small_image, house_small_label)

    house_medium_image = ImageMobject('assets/images/house_medium.png').scale(0.5).align_to(house_small, ORIGIN).shift(2 * RIGHT)
    house_medium_label = Tex(r'250.000 €', font_size = 30).move_to(house_medium_image.get_center()).shift(0.8 * DOWN)
    house_medium = Group(house_medium_image, house_medium_label)

    house_big_image = ImageMobject('assets/images/house_big.png').scale(0.5).align_to(house_medium_image, ORIGIN).shift(4 * RIGHT + 0.2 * UP)
    house_big_label = Tex(r'??? €', font_size = 30).move_to(house_big_image.get_center()).shift(1 * DOWN)
    house_big = Group(house_big_image, house_big_label)

    return Group(house_small, house_medium, house_big).move_to(ORIGIN)

def classification_learning():
    apple_image = ImageMobject('assets/images/apple.png').scale(0.4)
    arrow_1 = get_arrow().move_to(apple_image.get_center()).shift(RIGHT)
    model_image = ImageMobject('assets/images/model.png').scale(0.1).move_to(arrow_1.get_center()).shift(RIGHT)
    arrow_2 = get_arrow().move_to(model_image.get_center()).shift(RIGHT)
    prediction = Tex(r'Apfel: ', r'99\%', font_size = 32).move_to(arrow_2.get_center()).shift(1.4 * RIGHT)
    
    return Group(apple_image, arrow_1, model_image, arrow_2, prediction).move_to(ORIGIN)

def get_arrow():
    return Tex(r'$\rightarrow$', font_size = 50)