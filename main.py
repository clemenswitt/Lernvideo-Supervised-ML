from manim import *
from manim.utils.color import Colors
import ml_process, supervised_ml, axes, decision_boundary, points, class_labeling, perceptron_generator

class MLDefinition(Scene):
    def construct(self):
        #Elements
        title = Tex("Was ist Machine Learning?", font_size = 70).to_edge(UP).to_edge(LEFT)

        definition = Tex(r'Machine Learning beschreibt die künstliche \\ Generierung von Wissen aus Erfahrung.', font_size = 40)
        definition_easy = Tex(r'Machine Learning beschreibt das ', r'Nutzen von Daten ', r'\\zur ', r'Beantwortung von Fragen.', font_size = 40).set_color_by_tex('Nutzen von Daten', Colors.green_c.value).set_color_by_tex('Beantwortung von Fragen.', RED)
        
        using_data = Tex('Nutzen von Daten', font_size = 45).set_color(Colors.green_c.value).to_corner(LEFT + UP).shift(2 * DOWN)
        answer_questions = Tex('Beantwortung von Fragen', font_size = 45).set_color(Colors.red_c.value).to_corner(RIGHT + UP).shift(2 * DOWN)

        using_data_answer_questions = VGroup(using_data, answer_questions)

        down_arrow_training = Tex(r'$\downarrow$', font_size = 45).move_to(using_data.get_center()).shift(0.75 * DOWN)
        training = Tex('Training', font_size = 45).move_to(down_arrow_training.get_center()).shift(0.75 * DOWN)
        training_group = VGroup(down_arrow_training, training)
        down_arrow_prediction = Tex(r'$\downarrow$', font_size = 45).move_to(answer_questions.get_center()).shift(0.75 * DOWN)
        prediction = Tex('Vorhersage', font_size = 45).move_to(down_arrow_prediction.get_center()).shift(0.75 * DOWN)
        prediction_group = VGroup(down_arrow_prediction, prediction)
        training_prediction_group = VGroup(training_group, prediction_group)

        model_creation = ml_process.model_creation()

        prediction = ml_process.prediction()

        # Static test
        #self.add(title, prediction)

        #Animations
        self.play(Write(title))
        self.play(Write(definition_easy))
        self.play(ReplacementTransform(definition_easy, using_data_answer_questions))
        self.play(Write(training_prediction_group))
        self.play(FadeOut(using_data_answer_questions), FadeOut(training_prediction_group))
        self.play(FadeIn(model_creation[0]))
        self.play(FadeIn(model_creation[1]), FadeIn(model_creation[2]))
        self.play(FadeIn(model_creation[3]), FadeIn(model_creation[4]))
        self.play(FadeOut(model_creation))
        self.play(FadeIn(prediction[0]))
        self.play(FadeIn(prediction[1]), FadeIn(prediction[2]))
        self.play(FadeIn(prediction[3]), FadeIn(prediction[4]))
        self.play(FadeOut(prediction))

class SupervisedML(Scene):
    def construct(self):
        #Elements
        title = Tex(r'Was ist ', r'Supervised ' , r'Machine Learning?', font_size = 70).to_edge(UP).to_edge(LEFT)
        title[1].set_color(Colors.green_c.value)

        line1 = Tex(r'$\rightarrow$ ', r'Trainingsdaten sind beschriftet', r' -- \textit{gelabelt}', font_size = 40).to_edge(LEFT).shift(2 * UP)
        line1[2].set_color(Colors.red_c.value)
        line2 = Tex(r'$\rightarrow$ ', r'Ziel der Vorhersage: ', r'Labels ', r'unbeschrifteter Daten ', r'vorhersagen', font_size = 40).align_to(line1, DOWN).to_edge(LEFT).shift(0.75 * DOWN)
        line2[3].set_color(Colors.green_c.value)

        regression_learning_graphics = supervised_ml.regression_learning().to_edge(LEFT).shift(0.8 * DOWN)
        regression_learning_label = Tex(r'Regressionsprobleme', font_size = 35).move_to(regression_learning_graphics.get_center()).shift(1.5 * DOWN)
        regression_learning = Group(regression_learning_graphics, regression_learning_label)

        classification_learning_graphics = supervised_ml.classification_learning().to_edge(RIGHT)
        classification_learning_label = Tex(r'Klassifikationsprobleme', font_size = 35).move_to(classification_learning_graphics.get_center()).shift(1.3 * DOWN)
        classification_learning = Group(classification_learning_graphics, classification_learning_label).align_to(regression_learning, DOWN)

        #Static test
        #self.add(title, line1, line2, regression_learning, classification_learning)

        #Animations
        self.play(Write(title))
        self.play(Write(line1[0]), Write(line1[1]))
        self.play(Write(line1[2]))
        self.play(Write(line2))
        self.play(FadeIn(regression_learning[0][0]))
        self.play(FadeIn(regression_learning[0][1]))
        self.play(FadeIn(regression_learning[0][2]))
        self.play(FadeIn(regression_learning[1]))
        self.play(FadeIn(classification_learning[0][0]))
        self.play(FadeIn(classification_learning[0][1]), FadeIn(classification_learning[0][2]))
        self.play(FadeIn(classification_learning[0][3]), FadeIn(classification_learning[0][4]))
        self.play(FadeIn(classification_learning[1]))




class Training(Scene):
    def construct(self):
        # Elements

        #Titel
        title = Tex("Wie laufen Trainingsprozesse ab?", font_size = 70).to_edge(UP).to_edge(LEFT)

        #Koordinatensystem
        plane = axes.generate_axes()

        # Entscheidungsgrenze
        class_seperator_line = decision_boundary.generate_class_seperator_line(plane)
        class_seperator_label = decision_boundary.generate_class_seperator_label(class_seperator_line)



        # Points
        # Helper rectangle for points arrangement
        point_plane = points.generate_point_plane(plane)

        # Create two point-grids -> white + with class coloring
        point_group = points.create_point_group(point_plane, "w")
        point_group_class_colored = points.create_point_group(point_plane, "c")

        # Class-Labels
        class_labels = class_labeling.generate_class_labels(point_plane)


        # Perceptron
        perceptron, label_x, label_y, w_x, w_y, sum, act_func, classification = perceptron_generator.generate_perceptron()
        
        # Perceptron highlight-box + label
        perceptron_sr, perceptron_label, perceptron_act_func_description = perceptron_generator.create_perceptron_explaination(perceptron)


        # Inputs highlight-box + label
        in_x_sr, in_y_sr, perceptron_inputs_label, perceptron_inputs_description = perceptron_generator.create_inputs_explaination(label_x, label_y)


        # Weights highlight-box + label
        w_x_sr, w_y_sr, perceptron_weights_label, perceptron_weights_description = perceptron_generator.create_weights_explaination(w_x, w_y)

       
        # Sum hightlight-box + label
        sum_sr, perceptron_sum_label, perceptron_sum_description = perceptron_generator.create_sum_explaination(sum)


        # Activation-function hightlight-box + label
        act_func_sr, perceptron_act_func_label, perceptron_act_func_description = perceptron_generator.create_activation_function_explaination(act_func)

        # Step-function + surrounding-box
        sf = perceptron_generator.create_step_function(perceptron)

        # Classification hightlight-box + label
        classification_sr, perceptron_classification_label, perceptron_classification_description = perceptron_generator.create_classification_explaination(classification)

        # Perception learning rule
        perceptron_learning_rule = perceptron_generator.create_perceptron_learning_rule(perceptron)

        # Learning rate description
        perceptron_learning_rate_description = perceptron_generator.create_learning_rate_description(perceptron)

        # First point
        # Initialise weights 
        weights_initial = perceptron_generator.override_weights(w_x, w_y, 0.31, 0.45)
        # Initialise Inputs
        inputs_initial = perceptron_generator.override_inputs(label_x, label_y, 2.37, 4.06)
        # Highlight point
        point_highlight_initial = perceptron_generator.highlight_point(point_group, 21)
        # Point connection 
        point_to_inputs_initial = perceptron_generator.connect_point_to_inputs(point_highlight_initial, inputs_initial)
        # Initial sum
        sum_initial = perceptron_generator.override_sum(sum, 2.56)
        # Initial classification
        classification_initial = perceptron_generator.override_classification(classification, 1)

        # Second point (weights unchanged)
        # Initialise Inputs
        inputs_second = perceptron_generator.override_inputs(label_x, label_y, 2.77, 3.18)
        # Highlight point
        point_highlight_second = perceptron_generator.highlight_point(point_group, 29)
        # Point connection 
        point_to_inputs_second = perceptron_generator.connect_point_to_inputs(point_highlight_second, inputs_second)
        # Initial sum
        sum_second = perceptron_generator.override_sum(sum, 2.29)
        # Initial classification
        classification_second = perceptron_generator.override_classification(classification, 1)

        # Weight update
        decrease_weights = perceptron_generator.decrease_weights(perceptron)
        weights_calculated = perceptron_generator.override_weights(w_x, w_y, 0.03, 0.13)

        # Third point (weights already updated)
        # Initialise Inputs
        inputs_third = perceptron_generator.override_inputs(label_x, label_y, 3.27, 2.68)
        # Highlight point
        point_highlight_third = perceptron_generator.highlight_point(point_group, 36)
        # Point connection 
        point_to_inputs_third = perceptron_generator.connect_point_to_inputs(point_highlight_third, inputs_third)
        # Initial sum
        sum_third = perceptron_generator.override_sum(sum, 0.45)
        # Initial classification
        classification_third = perceptron_generator.override_classification(classification, 0)



        # Static test
        #self.add(title, plane, point_group, point_group_class_colored, class_labels, perceptron, decrease_weights)

        #Animations
        self.play(Write(title))

        #Diagram
        self.play(Write(plane))

        #Class separator line + label
        self.play(Write(class_seperator_line), run_time = 0.5)
        self.play(Write(class_seperator_label))
        self.wait(1)
        self.play(FadeOut(class_seperator_label), run_time = 0.3)

        #Point-group
        self.play(ShowIncreasingSubsets(point_group), run_time = 2.5)
        self.wait(1)
        self.play(Write(point_group_class_colored))
        self.wait(1)

        #Class labels
        self.play(Write(class_labels))
        
        # Perceptron
        self.play(Write(perceptron))
        self.wait(2)
        
        # Perceptron hightlight-box + label
        self.play(Write(perceptron_sr), Write(perceptron_label))
        self.wait(1)
        self.play(FadeOut(perceptron_sr), FadeOut(perceptron_label), run_time = 0.5)
        self.wait(1)

        # Perceptron inputs hightlight-box + label
        self.play(Write(in_x_sr), Write(in_y_sr), Write(perceptron_inputs_label))
        self.wait(1)
        self.play(FadeOut(in_x_sr), FadeOut(in_y_sr), FadeOut(perceptron_inputs_label), run_time = 0.5)
        self.wait(1)

         # Perceptron weights hightlight-box + label
        self.play(Write(w_x_sr), Write(w_y_sr), Write(perceptron_weights_label))
        self.wait(1)
        self.play(FadeOut(w_x_sr), FadeOut(w_y_sr), FadeOut(perceptron_weights_label), run_time = 0.5)
        self.wait(1)

        # Perceptron sum hightlight-box + label
        self.play(Write(sum_sr), Write(perceptron_sum_label))
        self.wait(1)
        self.play(FadeOut(sum_sr), FadeOut(perceptron_sum_label), run_time = 0.5)
        self.wait(1) 

        # Perceptron activation-function hightlight-box + label
        self.play(Write(act_func_sr), Write(perceptron_act_func_label))
        self.wait(1)
        # Create space for step-function-image
        self.play(perceptron_act_func_label.animate.align_to(act_func_sr, LEFT + UP).shift(0.4 * LEFT + 0.5 * UP))

        # Step-function
        self.play(Write(sf[0]), Write(sf[1]), Write(sf[2]))
        self.wait(3)
        self.play(FadeOut(act_func_sr), FadeOut(perceptron_act_func_label), FadeOut(sf[0]), FadeOut(sf[1]), FadeOut(sf[2]), run_time = 0.5)
        self.wait(1)

        # Perceptron classification hightlight-box + label
        self.play(Write(classification_sr), Write(perceptron_classification_label))
        self.wait(1)
        self.play(FadeOut(classification_sr), FadeOut(perceptron_classification_label), run_time = 0.5)
        self.wait(1)

        # Perceptron learning rule
        for line in perceptron_learning_rule:
            self.play(Write(line))
            self.wait(1)
        self.play(FadeOut(perceptron_learning_rule[0]), FadeOut(perceptron_learning_rule[1]), FadeOut(perceptron_learning_rule[2]), FadeOut(perceptron_learning_rule[3]), run_time = 0.5)
        self.wait(2)

        # Learning rate
        for line in perceptron_learning_rate_description:
            self.play(Write(line))
            self.wait(2)
        self.play(FadeOut(perceptron_learning_rate_description[0]), FadeOut(perceptron_learning_rate_description[1]))

        # Show perceptron learning rule again
        self.play(FadeIn(perceptron_learning_rule[0]), FadeIn(perceptron_learning_rule[1]), FadeIn(perceptron_learning_rule[2]), FadeIn(perceptron_learning_rule[3]))
        self.wait(1)

        # Initialise weights
        self.play(Write(weights_initial))
        self.wait(1)

        # Highlight initial point + conncect point to inputs + initial sum + initial prediction
        self.play(Write(point_highlight_initial))
        self.wait(0.5)
        self.play(Write(point_to_inputs_initial[0]), Write(point_to_inputs_initial[1]), run_time = 0.5)
        self.play(Write(inputs_initial[0]), Write(inputs_initial[1]))
        self.wait(0.5)
        self.play(Write(sum_initial))
        self.wait(0.5)
        self.play(Circumscribe(act_func, buff = MED_SMALL_BUFF))
        self.wait(0.5)
        self.play(Write(classification_initial))
        self.wait(1)
        self.play(Circumscribe(classification_initial, buff = SMALL_BUFF, color = GREEN))
        self.wait(2)
        self.play(Unwrite(point_highlight_initial), Unwrite(point_to_inputs_initial[0]), Unwrite(point_to_inputs_initial[1]), Unwrite(inputs_initial[0]), Unwrite(inputs_initial[1]), Unwrite(sum_initial), Unwrite(classification_initial), run_time = 0.5)
        self.wait(2)
        

        # Highlight second point + conncect point to inputs + second sum + second prediction
        self.play(Write(point_highlight_second))
        self.wait(0.5)
        self.play(Write(point_to_inputs_second[0]), Write(point_to_inputs_second[1]), run_time = 0.5)
        self.play(Write(inputs_second[0]), Write(inputs_second[1]))
        self.wait(0.5)
        self.play(Write(sum_second))
        self.wait(0.5)
        self.play(Circumscribe(act_func, buff = MED_SMALL_BUFF))
        self.wait(0.5)
        self.play(Write(classification_second))
        self.wait(1)
        self.play(Circumscribe(classification_second, buff = SMALL_BUFF, color = RED))
        self.wait(2)
        self.play(Unwrite(point_highlight_second), Unwrite(point_to_inputs_second[0]), Unwrite(point_to_inputs_second[1]), Unwrite(sum_second), Unwrite(classification_second), run_time = 0.5)
        self.wait(0.5)

        # Show weight decrease formulas
        self.play(FadeOut(perceptron_learning_rule[0]), FadeOut(perceptron_learning_rule[1]), FadeOut(perceptron_learning_rule[2]), FadeOut(perceptron_learning_rule[3]), run_time = 0.5)
        self.play(Write(decrease_weights[0]), Write(decrease_weights[1]), Write(decrease_weights[2]))
        self.wait(2)

        # Move current weights into decrease_weights formula
        self.bring_to_front(weights_initial) # Avoid overlapping in formula
        self.play(weights_initial[0].animate.move_to(decrease_weights[1][2].get_center()), weights_initial[1].animate.move_to(decrease_weights[2][2].get_center()))
        self.wait(2)
        self.remove(inputs_initial) # initial inputs have not been removed previously
        
        # Transform circular inputs into rectangular shapes & move them into decrease_weights formula
        transformed_inputs = perceptron_generator.inputs_to_rectangle_merge_into_formula(inputs_second, decrease_weights)
        self.play(ReplacementTransform(inputs_second, transformed_inputs))
        self.wait(2)

        # Show learning rate in formula
        learning_rate_labels = perceptron_generator.show_learning_rate_in_formula(0.1, decrease_weights)
        self.play(Write(learning_rate_labels[0]), Write(learning_rate_labels[1]))
        self.wait(2)

        # Show new calculated weights in formula
        for i in range(len(weights_calculated)):
            weights_calculated[i].move_to(decrease_weights[i + 1][0].get_center())
        self.play(Write(weights_calculated[0]), Write(weights_calculated[1]))
        self.wait(1)
        self.play(FadeOut(weights_initial[0]), FadeOut(weights_initial[1]), FadeOut(transformed_inputs[0]), FadeOut(transformed_inputs[1]), FadeOut(learning_rate_labels[0]), FadeOut(learning_rate_labels[1]))
        self.wait(1)

        # Move new weights to perceptron 
        self.play(weights_calculated[0].animate.move_to(w_x.get_center()), weights_calculated[1].animate.move_to(w_y.get_center()))
        self.wait(2)


        # Highlight third point + conncect point to inputs + third sum + third prediction
        self.play(Write(point_highlight_third))
        self.wait(0.5)
        self.play(Write(point_to_inputs_third[0]), Write(point_to_inputs_third[1]), run_time = 0.5)
        self.play(Write(inputs_third[0]), Write(inputs_third[1]))
        self.wait(0.5)
        self.play(Write(sum_third))
        self.wait(0.5)
        self.play(Circumscribe(act_func, buff = MED_SMALL_BUFF))
        self.wait(0.5)
        self.play(Write(classification_third))
        self.wait(1)
        self.play(Circumscribe(classification_third, buff = SMALL_BUFF, color = GREEN))
        self.wait(2)
        #self.play(Unwrite(point_highlight_third), Unwrite(point_to_inputs_third[0]), Unwrite(point_to_inputs_third[1]), Unwrite(sum_third), Unwrite(classification_third), run_time = 0.5)
        #self.wait(0.5)