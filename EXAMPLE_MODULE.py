"""
Example Module: Hash Functions Introduction (Phase 1, Module 1.1)

This demonstrates all best practices from CLAUDE.md:
- Tufte's visualization principles
- Clean, purposeful animations
- Integrated text and graphics
- Accessible color choices
- Proper timing
"""

from manim import *
import hashlib

# Configuration
config.background_color = "#1e1e1e"

class BaseEducationalScene(Scene):
    """Base class with Tufte principles and consistent styling"""

    def setup(self):
        self.colors = {
            "primary": BLUE,
            "secondary": GREEN,
            "accent": YELLOW,
            "danger": RED,
            "neutral": GRAY,
        }

        self.title_scale = 1.2
        self.heading_scale = 0.9
        self.body_scale = 0.7
        self.caption_scale = 0.5

    def create_title(self, text, color=WHITE):
        title = Text(text, color=color).scale(self.title_scale)
        title.to_edge(UP, buff=0.5)
        return title

    def create_caption(self, text):
        caption = Text(text, color=GRAY).scale(self.caption_scale)
        caption.to_edge(DOWN, buff=0.3)
        return caption

    def create_labeled_box(self, content, label, box_color=BLUE):
        if isinstance(content, str):
            content_obj = Text(content, color=WHITE, font="Fira Code").scale(0.6)
        else:
            content_obj = content

        box = SurroundingRectangle(
            content_obj,
            color=WHITE,
            fill_color=box_color,
            fill_opacity=0.3,
            buff=0.3
        )

        label_text = Text(label, color=WHITE).scale(0.5)
        label_text.next_to(box.get_corner(UL), DR, buff=0.1)

        return VGroup(box, content_obj, label_text)


class HashFunctionIntro(BaseEducationalScene):
    """
    Phase 1, Module 1.1: Hash Functions Basics

    Topics covered:
    - What is a hash function?
    - Deterministic property
    - Avalanche effect
    - Fixed output size

    Duration: ~5 minutes
    """

    def construct(self):
        # 1. Title and introduction
        title = self.create_title("Hash Functions: The Basics")
        self.play(FadeIn(title), run_time=0.5)
        self.wait(1)

        # 2. What is a hash function?
        self.explain_hash_concept()
        self.wait(1)

        # 3. Demonstrate deterministic property
        self.demonstrate_deterministic()
        self.wait(1)

        # 4. Show avalanche effect
        self.demonstrate_avalanche_effect()
        self.wait(1)

        # 5. Fixed output size
        self.demonstrate_fixed_output()
        self.wait(1)

        # 6. Summary
        self.show_summary()
        self.wait(2)

        # Clean exit
        self.play(FadeOut(*self.mobjects))

    def explain_hash_concept(self):
        """Introduce the hash function concept"""

        # Simple metaphor: input -> machine -> output
        input_box = self.create_labeled_box("Any Data", "Input", self.colors["primary"])
        input_box.shift(LEFT * 3.5)

        # Hash "machine"
        machine = RoundedRectangle(
            width=2.5,
            height=1.5,
            corner_radius=0.2,
            color=WHITE,
            fill_color=GRAY,
            fill_opacity=0.5
        )
        machine_label = Text("SHA-256", color=WHITE).scale(0.7)
        machine_label.move_to(machine)
        hash_machine = VGroup(machine, machine_label)

        output_box = self.create_labeled_box("Fixed-Size Hash", "Output", self.colors["secondary"])
        output_box.shift(RIGHT * 3.5)

        # Arrows
        arrow1 = Arrow(
            input_box.get_right(),
            machine.get_left(),
            buff=0.2,
            color=self.colors["accent"]
        )
        arrow2 = Arrow(
            machine.get_right(),
            output_box.get_left(),
            buff=0.2,
            color=self.colors["accent"]
        )

        # Caption
        caption = self.create_caption("A hash function transforms any input into a fixed-size output")

        # Animate (clean, simple)
        self.play(FadeIn(input_box), run_time=0.5)
        self.wait(0.5)
        self.play(
            Create(arrow1),
            FadeIn(hash_machine),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(
            Create(arrow2),
            FadeIn(output_box),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(input_box),
            FadeOut(hash_machine),
            FadeOut(output_box),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(caption),
            run_time=0.5
        )

    def demonstrate_deterministic(self):
        """Show that same input always produces same output"""

        heading = Text("Property 1: Deterministic", color=self.colors["accent"]).scale(0.8)
        heading.to_edge(UP, buff=1.5)
        self.play(FadeIn(heading), run_time=0.5)

        # Compute actual hash
        input_text = "Hello, Bitcoin!"
        hash_value = hashlib.sha256(input_text.encode()).hexdigest()

        # Show input and output multiple times
        input_display = Text(f'"{input_text}"', color=self.colors["primary"]).scale(0.6)
        input_display.shift(UP * 1.5 + LEFT * 3)

        arrow = Arrow(LEFT, RIGHT, color=self.colors["accent"]).scale(0.5)
        arrow.next_to(input_display, RIGHT, buff=0.5)

        output_display = Text(hash_value[:16] + "...", font="Fira Code", color=self.colors["secondary"]).scale(0.5)
        output_display.next_to(arrow, RIGHT, buff=0.5)

        # First time
        self.play(
            FadeIn(input_display),
            Create(arrow),
            FadeIn(output_display),
            run_time=0.8
        )
        self.wait(1)

        # Show it again (same result)
        input_display2 = input_display.copy().shift(DOWN * 1.2)
        arrow2 = arrow.copy().shift(DOWN * 1.2)
        output_display2 = output_display.copy().shift(DOWN * 1.2)

        self.play(
            FadeIn(input_display2),
            Create(arrow2),
            FadeIn(output_display2),
            run_time=0.8
        )
        self.wait(0.5)

        # And again (emphasize consistency)
        input_display3 = input_display.copy().shift(DOWN * 2.4)
        arrow3 = arrow.copy().shift(DOWN * 2.4)
        output_display3 = output_display.copy().shift(DOWN * 2.4)

        self.play(
            FadeIn(input_display3),
            Create(arrow3),
            FadeIn(output_display3),
            run_time=0.8
        )

        caption = self.create_caption("Same input ALWAYS produces the same output")
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clean up
        self.play(FadeOut(*self.mobjects[1:]), run_time=0.5)  # Keep title

    def demonstrate_avalanche_effect(self):
        """Show that tiny input change = huge output change"""

        heading = Text("Property 2: Avalanche Effect", color=self.colors["accent"]).scale(0.8)
        heading.to_edge(UP, buff=1.5)
        self.play(FadeIn(heading), run_time=0.5)

        # Two very similar inputs
        input1 = "Bitcoin"
        input2 = "bitcoin"  # Only one character different

        hash1 = hashlib.sha256(input1.encode()).hexdigest()
        hash2 = hashlib.sha256(input2.encode()).hexdigest()

        # Display side by side (Tufte: small multiples)
        # Left side
        input1_text = Text(f'"{input1}"', color=self.colors["primary"]).scale(0.6)
        input1_text.shift(UP * 1 + LEFT * 3)

        hash1_text = Text(hash1[:24] + "...", font="Fira Code", color=self.colors["secondary"]).scale(0.4)
        hash1_text.next_to(input1_text, DOWN, buff=0.5)

        left_group = VGroup(input1_text, hash1_text)

        # Right side
        input2_text = Text(f'"{input2}"', color=self.colors["primary"]).scale(0.6)
        input2_text.shift(UP * 1 + RIGHT * 3)

        hash2_text = Text(hash2[:24] + "...", font="Fira Code", color=self.colors["secondary"]).scale(0.4)
        hash2_text.next_to(input2_text, DOWN, buff=0.5)

        right_group = VGroup(input2_text, hash2_text)

        # Show both
        self.play(FadeIn(left_group), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(right_group), run_time=0.5)
        self.wait(1)

        # Highlight the difference in inputs
        diff_label = Text("One letter different", color=self.colors["danger"]).scale(0.5)
        diff_label.move_to(UP * 2)
        self.play(FadeIn(diff_label), run_time=0.5)
        self.wait(1)

        # Highlight completely different outputs
        hash_diff_label = Text("Completely different hashes!", color=self.colors["accent"]).scale(0.5)
        hash_diff_label.move_to(DOWN * 1.5)
        self.play(FadeIn(hash_diff_label), run_time=0.5)

        caption = self.create_caption("Small input change → drastically different output")
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clean up
        self.play(FadeOut(*self.mobjects[1:]), run_time=0.5)

    def demonstrate_fixed_output(self):
        """Show that output is always the same size"""

        heading = Text("Property 3: Fixed Output Size", color=self.colors["accent"]).scale(0.8)
        heading.to_edge(UP, buff=1.5)
        self.play(FadeIn(heading), run_time=0.5)

        # Different sized inputs, same sized outputs
        inputs = [
            "Hi",
            "Hello, World!",
            "This is a much longer input string with many more characters"
        ]

        input_displays = VGroup()
        output_displays = VGroup()

        for i, input_str in enumerate(inputs):
            hash_value = hashlib.sha256(input_str.encode()).hexdigest()

            # Input (variable length)
            input_text = Text(f'"{input_str[:20]}..."' if len(input_str) > 20 else f'"{input_str}"',
                            color=self.colors["primary"]).scale(0.5)
            input_text.shift(UP * (1.5 - i * 1.2) + LEFT * 3)

            # Output (always 256 bits = 64 hex chars)
            output_text = Text(hash_value[:16] + "...", font="Fira Code",
                             color=self.colors["secondary"]).scale(0.4)
            output_text.next_to(input_text, RIGHT, buff=1.5)

            input_displays.add(input_text)
            output_displays.add(output_text)

        # Animate inputs
        self.play(FadeIn(input_displays), run_time=1)
        self.wait(0.5)

        # Animate outputs
        self.play(FadeIn(output_displays), run_time=1)
        self.wait(1)

        # Highlight that all outputs are the same length
        brace = Brace(output_displays, RIGHT, color=self.colors["accent"])
        brace_text = Text("All 256 bits", color=self.colors["accent"]).scale(0.5)
        brace_text.next_to(brace, RIGHT)

        self.play(Create(brace), FadeIn(brace_text), run_time=0.5)

        caption = self.create_caption("SHA-256 always produces a 256-bit (64 hex character) output")
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clean up
        self.play(FadeOut(*self.mobjects[1:]), run_time=0.5)

    def show_summary(self):
        """Final summary of key properties"""

        heading = Text("Key Properties of Hash Functions", color=self.colors["accent"]).scale(0.9)
        heading.to_edge(UP, buff=1)
        self.play(FadeIn(heading), run_time=0.5)

        # Summary points
        points = VGroup(
            Text("1. Deterministic: Same input → Same output", color=WHITE).scale(0.6),
            Text("2. Avalanche Effect: Tiny change → Big difference", color=WHITE).scale(0.6),
            Text("3. Fixed Size: Always 256 bits (for SHA-256)", color=WHITE).scale(0.6),
            Text("4. One-Way: Can't reverse the process", color=WHITE).scale(0.6),
            Text("5. Collision Resistant: Hard to find two inputs with same output", color=WHITE).scale(0.6),
        )

        points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.move_to(ORIGIN + DOWN * 0.3)

        # Animate each point
        for i, point in enumerate(points):
            self.play(FadeIn(point), run_time=0.3)
            self.wait(0.5)

        self.wait(2)

        # Use cases caption
        caption = self.create_caption("Used in: Bitcoin mining, digital signatures, data integrity, and more!")
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)


# Quick test render
# Run with: manim -pql EXAMPLE_MODULE.py HashFunctionIntro
