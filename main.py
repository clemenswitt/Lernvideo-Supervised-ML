from manim import *
import numpy as np
import axes, decision_boundary, points, class_labeling, perceptron_generator

class Training(Scene):
    def construct(self):
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

        # Create regular points grid with class coloring
        point_group = points.create_point_group(point_plane)

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
        sf, sf_sr = perceptron_generator.create_step_function(perceptron)

        # Classification hightlight-box + label
        classification_sr, perceptron_classification_label, perceptron_classification_description = perceptron_generator.create_classification_explaination(classification)


        #self.add(title, plane, class_seperator_line, class_seperator_label, point_group, class_labels, perceptron, sf, sf_sr)

        #Animationen
        self.play(Write(title))

        #Diagram
        self.play(Write(plane))

        #Class separator line + label
        self.play(Write(class_seperator_line), run_time = 0.5)
        self.play(Write(class_seperator_label))
        self.wait(1)
        self.play(Unwrite(class_seperator_label), run_time = 0.3)
        self.play(ShowIncreasingSubsets(point_group), run_time = 2.5)
        self.wait(1)

        #Class labels
        self.play(Write(class_labels))
        
        # Perceptron
        self.play(Write(perceptron))
        self.wait(1)

        # Perceptron hightlight-box + label
        self.play(Write(perceptron_sr), Write(perceptron_label))
        self.wait(1)
        self.play(Unwrite(perceptron_sr), Unwrite(perceptron_label))
        self.wait(1)

        # Perceptron inputs hightlight-box + label
        self.play(Write(in_x_sr), Write(in_y_sr), Write(perceptron_inputs_label))
        self.wait(1)
        self.play(Unwrite(in_x_sr), Unwrite(in_y_sr), Unwrite(perceptron_inputs_label))
        self.wait(1)

         # Perceptron weights hightlight-box + label
        self.play(Write(w_x_sr), Write(w_y_sr), Write(perceptron_weights_label))
        self.wait(1)
        self.play(Unwrite(w_x_sr), Unwrite(w_y_sr), Unwrite(perceptron_weights_label))
        self.wait(1)

        # Perceptron sum hightlight-box + label
        self.play(Write(sum_sr), Write(perceptron_sum_label))
        self.wait(1)
        self.play(Unwrite(sum_sr), Unwrite(perceptron_sum_label))
        self.wait(1) 

        # Perceptron activation-function hightlight-box + label
        self.play(Write(act_func_sr), Write(perceptron_act_func_label))
        self.wait(1)
        # Create space for step-function-image
        self.play(perceptron_act_func_label.animate.align_to(act_func_sr, LEFT + UP).shift(0.4 * LEFT + 0.5 * UP))

        # Step-function
        self.play(Write(sf), Write(sf_sr))
        self.wait(1)
        self.play(Unwrite(act_func_sr), Unwrite(perceptron_act_func_description), Unwrite(sf), Unwrite(sf_sr))
        self.wait(1)

        # Perceptron classification hightlight-box + label
        self.play(Write(classification_sr), Write(perceptron_classification_label))
        self.wait(1)
        self.play(Unwrite(classification_sr), Unwrite(perceptron_classification_label))
        self.wait(1) 