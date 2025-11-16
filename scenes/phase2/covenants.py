from manim import *


class IntroduceCheckSigFromStack(Scene):
    def construct(self):
        # Create a list of elements to represent the stack
        stack_elements = ["bytes", "OP_CAT", "OP_CHECKSIGFROMSTACK", "OP_EQUAL"]
        
        # Initialize an empty list to hold the TextMobjects
        stack_mobjects = []
        
        # Position for the bottom of the stack
        position = DOWN * 3

         # Create TextMobjects for each element and position them in a stack
        for element in stack_elements:
            text_color = BLACK
            box_color = YELLOW_B
           
           
            # Check if the element starts with "OP_" and set color to dark blue if it does
            if element.startswith("OP_"):
                text_color = BLACK
                box_color = BLUE_E

            # Create a TextMobject for the current element
            text_object = Text(element, color=text_color).move_to(position)

            # Create a SurroundingRectangle for the Text object
            rectangle = SurroundingRectangle(text_object, color=WHITE, fill_color=box_color, buff=0.1, fill_opacity=0.5)
            
            # Group the Text object and its SurroundingRectangle
            text_with_box = VGroup(text_object, rectangle)
            
            # Animate the appearance of the Text object and its SurroundingRectangle
            self.play(FadeIn(text_with_box))
            
            # Add the new element (Text object and its SurroundingRectangle) to the list of stack mobjects
            stack_mobjects.insert(0, text_with_box)  # Insert at the beginning to maintain the stack order

            # Move up all elements in the stack to make space for the new element
            if len(stack_mobjects) > 1:  # If there are other elements, move them up
                self.play(*[ApplyMethod(mob.shift, UP * 0.75) for mob in stack_mobjects[1:]])    


        self.wait()