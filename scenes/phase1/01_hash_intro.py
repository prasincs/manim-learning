"""
Module 1.1: Hash Functions Basics
Topics: What is a hash? Properties (deterministic, one-way, collision-resistant)
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
sys.path.append('/home/user/manim-learning')
from components import HashMachine, DataBox, HashVisualization, AvalancheEffect

# Configure background
config.background_color = "#1e1e1e"


class HashIntroduction(Scene):
    """Introduction to hash functions"""

    def construct(self):
        # Title
        title = Text("What is a Hash Function?", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Simple explanation
        explanation = Text(
            "A function that converts data of any size into a fixed-size output",
            color=GRAY
        ).scale(0.6)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(2)

        # Clear explanation
        self.play(FadeOut(explanation), run_time=0.5)

        # Show hash visualization
        hash_viz = HashVisualization(
            input_data="Hello, World!",
            hash_function="SHA-256",
            compute_hash=True
        )
        hash_viz.scale(0.8)

        self.play(FadeIn(hash_viz.input_box), run_time=0.5)
        self.wait(0.5)

        self.play(
            Create(hash_viz.input_arrow),
            FadeIn(hash_viz.machine),
            run_time=1
        )
        self.wait(0.5)

        self.play(
            Create(hash_viz.output_arrow),
            FadeIn(hash_viz.output_box),
            run_time=1
        )
        self.wait(2)

        # Caption
        caption = Text(
            "Same input always produces the same output",
            color=YELLOW
        ).scale(0.5)
        caption.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(hash_viz),
            FadeOut(caption),
            FadeOut(title),
            run_time=1
        )


class HashProperties(Scene):
    """Three key properties of hash functions"""

    def construct(self):
        # Title
        title = Text("Hash Function Properties", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # List of properties
        properties = VGroup()

        prop1 = VGroup(
            Text("1. Deterministic", color=BLUE).scale(0.7),
            Text("Same input → Same output (always)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        prop2 = VGroup(
            Text("2. One-Way", color=GREEN).scale(0.7),
            Text("Easy to compute, impossible to reverse", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        prop3 = VGroup(
            Text("3. Collision-Resistant", color=YELLOW).scale(0.7),
            Text("Hard to find two inputs with same output", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        properties.add(prop1, prop2, prop3)
        properties.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        properties.move_to(ORIGIN)

        # Animate properties one by one
        for prop in properties:
            self.play(FadeIn(prop), run_time=1)
            self.wait(1.5)

        self.wait(2)

        # Clear
        self.play(FadeOut(properties), FadeOut(title), run_time=1)


class DeterministicProperty(Scene):
    """Demonstrate deterministic property"""

    def construct(self):
        # Title
        title = Text("Property 1: Deterministic", color=BLUE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Same input, same output
        input_text = "Bitcoin"

        # First hash
        hash_viz1 = HashVisualization(
            input_data=input_text,
            hash_function="SHA-256",
            compute_hash=True
        )
        hash_viz1.scale(0.7).shift(UP * 1.5)

        # Second hash (same input)
        hash_viz2 = HashVisualization(
            input_data=input_text,
            hash_function="SHA-256",
            compute_hash=True
        )
        hash_viz2.scale(0.7).shift(DOWN * 1.5)

        # Show first hash
        self.play(FadeIn(hash_viz1), run_time=1)
        self.wait(1)

        # Show second hash
        self.play(FadeIn(hash_viz2), run_time=1)
        self.wait(1)

        # Highlight that outputs are identical
        highlight1 = SurroundingRectangle(hash_viz1.output_box, color=YELLOW, buff=0.1)
        highlight2 = SurroundingRectangle(hash_viz2.output_box, color=YELLOW, buff=0.1)

        self.play(Create(highlight1), Create(highlight2), run_time=0.5)

        caption = Text("Identical outputs!", color=YELLOW).scale(0.6)
        caption.to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(hash_viz1),
            FadeOut(hash_viz2),
            FadeOut(highlight1),
            FadeOut(highlight2),
            FadeOut(caption),
            FadeOut(title),
            run_time=1
        )


class OneWayProperty(Scene):
    """Demonstrate one-way property"""

    def construct(self):
        # Title
        title = Text("Property 2: One-Way Function", color=GREEN).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Hash visualization
        hash_viz = HashVisualization(
            input_data="Secret Message",
            hash_function="SHA-256",
            compute_hash=True
        )
        hash_viz.scale(0.8)

        # Forward direction (easy)
        forward_label = Text("Forward: EASY ✓", color=GREEN).scale(0.6)
        forward_label.next_to(hash_viz, UP, buff=0.5)

        self.play(Write(forward_label), run_time=0.5)
        self.play(FadeIn(hash_viz), run_time=1)
        self.wait(2)

        # Clear
        self.play(FadeOut(forward_label), run_time=0.5)

        # Reverse direction (impossible)
        reverse_label = Text("Reverse: IMPOSSIBLE ✗", color=RED).scale(0.6)
        reverse_label.next_to(hash_viz, DOWN, buff=0.5)

        # Flip arrows to show reverse direction
        reverse_arrow1 = Arrow(
            hash_viz.machine.get_input_pos(),
            hash_viz.input_box.get_connection_point("right"),
            buff=0.1,
            color=RED
        )

        reverse_arrow2 = Arrow(
            hash_viz.output_box.get_connection_point("left"),
            hash_viz.machine.get_output_pos(),
            buff=0.1,
            color=RED
        )

        # Question mark on input
        question = Text("???", color=RED).scale(0.8)
        question.move_to(hash_viz.input_box.get_center())

        self.play(Write(reverse_label), run_time=0.5)
        self.play(
            Create(reverse_arrow1),
            Create(reverse_arrow2),
            run_time=1
        )
        self.play(Transform(hash_viz.input_box[1], question), run_time=0.5)
        self.wait(2)

        caption = Text(
            "Cannot find input from hash alone",
            color=GRAY
        ).scale(0.5)
        caption.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(hash_viz),
            FadeOut(reverse_label),
            FadeOut(reverse_arrow1),
            FadeOut(reverse_arrow2),
            FadeOut(caption),
            FadeOut(title),
            run_time=1
        )


class CollisionResistance(Scene):
    """Demonstrate collision resistance"""

    def construct(self):
        # Title
        title = Text("Property 3: Collision-Resistant", color=YELLOW).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Explanation
        explanation = Text(
            "Finding two different inputs with the same hash is extremely difficult",
            color=GRAY
        ).scale(0.5)
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(2)

        # Two different inputs
        input1 = "Message A"
        input2 = "Message B"

        hash1 = hashlib.sha256(input1.encode()).hexdigest()[:16] + "..."
        hash2 = hashlib.sha256(input2.encode()).hexdigest()[:16] + "..."

        # Create boxes
        box1 = VGroup(
            Text("Input 1:", color=BLUE).scale(0.5),
            Text(input1, color=WHITE).scale(0.4),
            Text("Hash:", color=GRAY).scale(0.4),
            Text(hash1, color=GREEN).scale(0.35)
        ).arrange(DOWN, buff=0.2)
        box1.shift(LEFT * 3)

        box2 = VGroup(
            Text("Input 2:", color=BLUE).scale(0.5),
            Text(input2, color=WHITE).scale(0.4),
            Text("Hash:", color=GRAY).scale(0.4),
            Text(hash2, color=GREEN).scale(0.35)
        ).arrange(DOWN, buff=0.2)
        box2.shift(RIGHT * 3)

        not_equal = Text("≠", color=RED).scale(1.5)
        not_equal.move_to(ORIGIN)

        self.play(FadeIn(box1), run_time=1)
        self.play(FadeIn(box2), run_time=1)
        self.wait(1)

        self.play(Write(not_equal), run_time=0.5)
        self.wait(1)

        # Caption
        caption = Text(
            "Different inputs → Different hashes",
            color=YELLOW
        ).scale(0.6)
        caption.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(box1),
            FadeOut(box2),
            FadeOut(not_equal),
            FadeOut(caption),
            FadeOut(explanation),
            FadeOut(title),
            run_time=1
        )


class AvalancheEffectDemo(Scene):
    """Demonstrate avalanche effect"""

    def construct(self):
        # Title
        title = Text("Avalanche Effect", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text(
            "Small change in input → Large change in output",
            color=GRAY
        ).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Two similar inputs
        input1 = "Bitcoin"
        input2 = "bitcoin"  # Just one character different (capital B)

        hash1 = hashlib.sha256(input1.encode()).hexdigest()
        hash2 = hashlib.sha256(input2.encode()).hexdigest()

        # Create visualizations
        viz1 = VGroup(
            Text(f'"{input1}"', color=BLUE).scale(0.5),
            Text(hash1[:32], color=GREEN).scale(0.35),
            Text(hash1[32:], color=GREEN).scale(0.35)
        ).arrange(DOWN, buff=0.2)
        viz1.shift(UP * 0.5)

        viz2 = VGroup(
            Text(f'"{input2}"', color=BLUE).scale(0.5),
            Text(hash2[:32], color=YELLOW).scale(0.35),
            Text(hash2[32:], color=YELLOW).scale(0.35)
        ).arrange(DOWN, buff=0.2)
        viz2.shift(DOWN * 1.5)

        # Highlight the difference in input
        diff_label = Text("Only 1 character different!", color=RED).scale(0.5)
        diff_label.next_to(viz1, LEFT, buff=0.5)

        self.play(FadeIn(viz1), run_time=1)
        self.play(FadeIn(viz2), run_time=1)
        self.wait(1)

        self.play(Write(diff_label), run_time=0.5)
        self.wait(2)

        # Highlight that hashes are completely different
        hash_diff_label = Text("Completely different hashes!", color=RED).scale(0.5)
        hash_diff_label.next_to(viz2, RIGHT, buff=0.5)
        self.play(Write(hash_diff_label), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(viz1),
            FadeOut(viz2),
            FadeOut(diff_label),
            FadeOut(hash_diff_label),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class HashSizeComparison(Scene):
    """Compare hash output sizes for different inputs"""

    def construct(self):
        # Title
        title = Text("Fixed Output Size", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text(
            "No matter the input size, output is always the same length",
            color=GRAY
        ).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Different input sizes
        inputs = [
            ("A", "Short input"),
            ("Hello, Bitcoin!", "Medium input"),
            ("This is a much longer input to demonstrate that SHA-256 always produces 256-bit output", "Long input")
        ]

        # Create hash displays
        hash_displays = VGroup()

        for input_data, label in inputs:
            hash_value = hashlib.sha256(input_data.encode()).hexdigest()

            display = VGroup(
                Text(label, color=BLUE).scale(0.4),
                Text(f'Input: "{input_data[:30]}..."', color=GRAY).scale(0.3),
                Text(f"Hash: {hash_value[:32]}...", color=GREEN).scale(0.35)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

            hash_displays.add(display)

        hash_displays.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        hash_displays.shift(DOWN * 0.5)

        # Show one by one
        for display in hash_displays:
            self.play(FadeIn(display), run_time=0.8)
            self.wait(1)

        # Highlight that all outputs are same length
        caption = Text(
            "All outputs are 256 bits (64 hex characters)",
            color=YELLOW
        ).scale(0.6)
        caption.to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(hash_displays),
            FadeOut(caption),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class HashSummary(Scene):
    """Summary of hash functions"""

    def construct(self):
        # Title
        title = Text("Hash Functions: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Deterministic: Same input → Same output", color=BLUE).scale(0.6),
            Text("✓ One-Way: Easy to compute, hard to reverse", color=GREEN).scale(0.6),
            Text("✓ Collision-Resistant: Hard to find duplicates", color=YELLOW).scale(0.6),
            Text("✓ Avalanche Effect: Small change → Big difference", color=ORANGE).scale(0.6),
            Text("✓ Fixed Size: Any input → Fixed output length", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        # Show summary points
        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Use cases caption
        use_cases = Text(
            "Used in: Blockchain, Passwords, Data Integrity, Digital Signatures",
            color=GRAY
        ).scale(0.5)
        use_cases.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(use_cases), run_time=1)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(summary),
            FadeOut(use_cases),
            FadeOut(title),
            run_time=1
        )
        self.wait(1)


# Combined scene for full video
class HashFunctionsBasicsComplete(Scene):
    """Complete module combining all scenes"""

    def construct(self):
        # Run all subscenes in sequence
        scenes = [
            HashIntroduction,
            HashProperties,
            DeterministicProperty,
            OneWayProperty,
            CollisionResistance,
            AvalancheEffectDemo,
            HashSizeComparison,
            HashSummary
        ]

        for scene_class in scenes:
            scene = scene_class()
            scene.construct()
