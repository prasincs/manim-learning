"""
Stack visualization component for Bitcoin Script animations
"""
from manim import *


class StackElement(VGroup):
    """A single element in a stack with text and surrounding box"""

    def __init__(self, text, text_color=BLACK, box_color=YELLOW_B, is_opcode=False, **kwargs):
        super().__init__(**kwargs)

        # Set colors based on type
        if is_opcode or (isinstance(text, str) and text.startswith("OP_")):
            text_color = BLACK
            box_color = BLUE_E

        # Create text
        self.text = Text(text, color=text_color).scale(0.7)

        # Create box
        self.box = SurroundingRectangle(
            self.text,
            color=WHITE,
            fill_color=box_color,
            buff=0.15,
            fill_opacity=0.8
        )

        # Add to group
        self.add(self.box, self.text)


class Stack(VGroup):
    """A stack data structure visualization"""

    def __init__(self, position=DOWN*2.5, spacing=0.75, **kwargs):
        super().__init__(**kwargs)
        self.elements = []
        self.position = position
        self.spacing = spacing

    def push_element(self, element):
        """Add element to top of stack"""
        self.elements.insert(0, element)
        self._reposition()
        return element

    def pop_element(self):
        """Remove element from top of stack"""
        if self.elements:
            element = self.elements.pop(0)
            self._reposition()
            return element
        return None

    def _reposition(self):
        """Reposition all elements in stack"""
        self.remove(*self.submobjects)
        for i, element in enumerate(self.elements):
            element.move_to(self.position + UP * i * self.spacing)
            self.add(element)

    def get_top(self):
        """Get top element without removing"""
        return self.elements[0] if self.elements else None

    def get_all_elements(self):
        """Get all elements in stack"""
        return self.elements.copy()


class AnimatedStack(Stack):
    """Stack with built-in animations"""

    def animate_push(self, scene, text, text_color=BLACK, box_color=YELLOW_B, is_opcode=False):
        """Animate pushing an element onto the stack"""
        element = StackElement(text, text_color, box_color, is_opcode)

        # Start position (above the stack)
        start_pos = self.position + UP * (len(self.elements) + 2) * self.spacing
        element.move_to(start_pos)

        # Fade in at start position
        scene.play(FadeIn(element))

        # Push to stack
        self.push_element(element)

        # Animate all elements moving up if needed
        if len(self.elements) > 1:
            scene.play(
                *[elem.animate.shift(UP * self.spacing) for elem in self.elements[1:]],
                element.animate.move_to(self.position)
            )
        else:
            scene.play(element.animate.move_to(self.position))

        return element

    def animate_pop(self, scene):
        """Animate popping an element from the stack"""
        if not self.elements:
            return None

        element = self.get_top()

        # Fade out top element
        scene.play(FadeOut(element))

        # Remove from stack
        self.pop_element()

        # Move remaining elements down
        if self.elements:
            scene.play(
                *[elem.animate.shift(DOWN * self.spacing) for elem in self.elements]
            )

        return element

    def animate_operation(self, scene, operation_text, result_text):
        """
        Animate a stack operation:
        1. Pop required elements
        2. Show operation
        3. Push result
        """
        # Create operation display
        op = Text(operation_text, color=RED).scale(0.8)
        op.move_to(self.position + RIGHT * 3)

        scene.play(Write(op))
        scene.wait(1)

        # Push result
        self.animate_push(scene, result_text)

        # Fade out operation
        scene.play(FadeOut(op))


# Example usage scene
class StackExample(Scene):
    def construct(self):
        # Create animated stack
        stack = AnimatedStack()

        # Title
        title = Text("Bitcoin Script Stack").to_edge(UP)
        self.play(Write(title))

        # Push some elements
        stack.animate_push(self, "0x1234", box_color=YELLOW)
        self.wait(0.5)

        stack.animate_push(self, "OP_DUP", is_opcode=True)
        self.wait(0.5)

        stack.animate_push(self, "0x5678", box_color=YELLOW)
        self.wait(0.5)

        stack.animate_push(self, "OP_HASH160", is_opcode=True)
        self.wait(1)

        # Pop an element
        stack.animate_pop(self)
        self.wait(1)

        # Cleanup
        self.play(FadeOut(stack), FadeOut(title))
