from manim import *
import numpy as np
import axes, decision_boundary, points, class_labeling, perceptron_generator

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


        # Static test
        #self.add(title, plane, point_group, point_group_class_colored, class_labels, perceptron, sf)

        
        
        
        
        
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
        self.wait(1)

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
        self.wait(1)
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
        self.wait(1)

        # Learning rate
        for line in perceptron_learning_rate_description:
            self.play(Write(line))
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
        self.play(Circumscribe(classification_initial, buff = MED_SMALL_BUFF, color = GREEN))
        self.wait(2)
        self.play(Unwrite(point_highlight_initial), Unwrite(point_to_inputs_initial[0]), Unwrite(point_to_inputs_initial[1]), Unwrite(inputs_initial[0]), Unwrite(inputs_initial[1]), Unwrite(sum_initial), Unwrite(classification_initial), run_time = 0.5)
        self.wait(1)

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
        self.play(Circumscribe(classification_second, buff = MED_SMALL_BUFF, color = RED))
        self.wait(2)
        self.play(Unwrite(point_highlight_second), Unwrite(point_to_inputs_second[0]), Unwrite(point_to_inputs_second[1]), Unwrite(inputs_second[0]), Unwrite(inputs_second[1]), Unwrite(sum_second), Unwrite(classification_second), run_time = 0.5)
        self.wait(0.5)