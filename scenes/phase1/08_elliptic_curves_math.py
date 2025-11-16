"""
Module 1.8: Elliptic Curves Math
Topics: Scalar multiplication, generator point, discrete log problem
Duration: 5-10 minutes
"""

from manim import *
import sys
# Add repository root to path for components module
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components import EllipticCurve

# Configure background
config.background_color = "#1e1e1e"


class ScalarMultiplicationIntro(Scene):
    """Introduction to scalar multiplication"""

    def construct(self):
        # Title
        title = Text("Scalar Multiplication", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Multiplying Points by Numbers", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Definition
        definition = VGroup(
            Text("What is k * P?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Adding P to itself k times", color=BLUE).scale(0.6)
        ).arrange(DOWN, buff=0.3)
        definition.shift(UP * 1)

        self.play(FadeIn(definition), run_time=1)
        self.wait(2)

        # Examples
        examples = VGroup(
            Text("Examples:", color=GREEN).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("2*P = P + P", color=GRAY).scale(0.5),
            Text("3*P = P + P + P", color=GRAY).scale(0.5),
            Text("4*P = P + P + P + P", color=GRAY).scale(0.5),
            Text("...", color=GRAY).scale(0.5),
            Text("k*P = P + P + ... + P (k times)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        examples.shift(DOWN * 0.8)

        self.play(FadeIn(examples), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(definition),
            FadeOut(examples),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class VisualizingScalarMultiplication(Scene):
    """Visualize scalar multiplication on the curve"""

    def construct(self):
        # Title
        title = Text("Visualizing k * G", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create curve
        curve = EllipticCurve(a=0, b=7, x_range=(-3, 3), y_range=(-4, 4))
        curve.scale(0.6).shift(DOWN * 0.5)

        self.play(Create(curve.axes), run_time=0.8)
        self.play(
            Create(curve.curve_positive),
            Create(curve.curve_negative),
            run_time=1.2
        )
        self.wait(1)

        # Generator point G
        g_x, g_y = 1, (1**3 + 7)**0.5
        g_dot = Dot(curve.axes.c2p(g_x, g_y), color=BLUE)
        g_label = Text("G", color=BLUE).scale(0.7)
        g_label.next_to(g_dot, UP, buff=0.2)

        g_caption = Text("G = Generator Point", color=BLUE).scale(0.5)
        g_caption.to_edge(DOWN, buff=0.3)

        self.play(Create(g_dot), Write(g_label), Write(g_caption), run_time=1)
        self.wait(2)

        # Show 2G
        self.play(FadeOut(g_caption), run_time=0.5)

        two_g_caption = Text("2G = G + G", color=GREEN).scale(0.5)
        two_g_caption.to_edge(DOWN, buff=0.3)

        # Approximate position for 2G (using simplified calculation)
        two_g_x, two_g_y = -0.5, ((-0.5)**3 + 7)**0.5
        two_g_dot = Dot(curve.axes.c2p(two_g_x, two_g_y), color=GREEN)
        two_g_label = Text("2G", color=GREEN).scale(0.7)
        two_g_label.next_to(two_g_dot, UP + LEFT, buff=0.2)

        self.play(
            Create(two_g_dot),
            Write(two_g_label),
            Write(two_g_caption),
            run_time=1
        )
        self.wait(2)

        # Show 3G
        self.play(FadeOut(two_g_caption), run_time=0.5)

        three_g_caption = Text("3G = 2G + G", color=YELLOW).scale(0.5)
        three_g_caption.to_edge(DOWN, buff=0.3)

        three_g_x, three_g_y = 2, -(2**3 + 7)**0.5
        three_g_dot = Dot(curve.axes.c2p(three_g_x, three_g_y), color=YELLOW)
        three_g_label = Text("3G", color=YELLOW).scale(0.7)
        three_g_label.next_to(three_g_dot, DOWN, buff=0.2)

        self.play(
            Create(three_g_dot),
            Write(three_g_label),
            Write(three_g_caption),
            run_time=1
        )
        self.wait(2)

        # Continue pattern
        self.play(FadeOut(three_g_caption), run_time=0.5)

        continue_note = Text("Pattern continues: 4G, 5G, 6G, ...", color=ORANGE).scale(0.5)
        continue_note.to_edge(DOWN, buff=0.3)

        self.play(Write(continue_note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(curve),
            FadeOut(g_dot), FadeOut(g_label),
            FadeOut(two_g_dot), FadeOut(two_g_label),
            FadeOut(three_g_dot), FadeOut(three_g_label),
            FadeOut(continue_note),
            FadeOut(title),
            run_time=1
        )


class GeneratorPoint(Scene):
    """Explain the generator point"""

    def construct(self):
        # Title
        title = Text("The Generator Point (G)", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is it
        what_is_it = VGroup(
            Text("What is a Generator Point?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• A special point on the curve", color=GRAY).scale(0.5),
            Text("• Everyone agrees on the same G", color=GRAY).scale(0.5),
            Text("• Part of the curve parameters", color=GRAY).scale(0.5),
            Text("• Used to generate all other points", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 1)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Properties
        properties = VGroup(
            Text("Properties of G:", color=BLUE).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Has large prime order n", color=GRAY).scale(0.5),
            Text("• n * G = O (point at infinity)", color=GRAY).scale(0.5),
            Text("• Can generate ~2²⁵⁶ different points", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        properties.shift(DOWN * 1)

        self.play(FadeIn(properties), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(properties),
            FadeOut(title),
            run_time=1
        )


class PublicKeyGeneration(Scene):
    """How private keys become public keys"""

    def construct(self):
        # Title
        title = Text("Generating Public Keys", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The formula
        formula = MathTex("P = d \\times G", color=YELLOW).scale(1.5)
        formula.shift(UP * 1.5)

        self.play(Write(formula), run_time=1)
        self.wait(1)

        # Explanation
        explanation = VGroup(
            Text("Where:", color=BLUE).scale(0.6),
            Text("d = Private key (random number)", color=RED).scale(0.5),
            Text("G = Generator point (known)", color=GREEN).scale(0.5),
            Text("P = Public key (point on curve)", color=BLUE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.shift(DOWN * 0.3)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Example
        example = VGroup(
            Text("Example:", color=YELLOW).scale(0.6),
            Text("d = 7 (private key)", color=RED).scale(0.5),
            Text("P = 7 * G = G+G+G+G+G+G+G", color=BLUE).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        example.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(example), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(example),
            FadeOut(title),
            run_time=1
        )


class DiscreteLogProblem(Scene):
    """Explain the discrete logarithm problem"""

    def construct(self):
        # Title
        title = Text("The Discrete Logarithm Problem", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The problem
        problem = VGroup(
            Text("The Security Foundation:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Given: P = d * G", color=BLUE).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("Easy: d → P (multiply)", color=GREEN).scale(0.55),
            Text("Hard: P → d (find discrete log)", color=RED).scale(0.55)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 1)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Computational complexity
        complexity = VGroup(
            Text("Why is it hard?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• No known efficient algorithm", color=GRAY).scale(0.5),
            Text("• Only option: Try all d values (brute force)", color=GRAY).scale(0.5),
            Text("• With 256-bit keys: 2²⁵⁶ possibilities", color=GRAY).scale(0.5),
            Text("• Would take billions of years!", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        complexity.shift(DOWN * 0.8)

        self.play(FadeIn(complexity), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(complexity),
            FadeOut(title),
            run_time=1
        )


class ForwardVsReverse(Scene):
    """Visual comparison of forward vs reverse"""

    def construct(self):
        # Title
        title = Text("One-Way Function", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Forward (easy)
        forward = VGroup(
            Text("Forward: EASY", color=GREEN).scale(0.8),
            Text("", color=GRAY).scale(0.1),
            Text("d = 12345...", color=RED).scale(0.5),
            Arrow(ORIGIN, DOWN * 0.8, color=GREEN),
            Text("Scalar Multiplication", color=YELLOW).scale(0.4),
            Arrow(ORIGIN, DOWN * 0.8, color=GREEN),
            Text("P = 12345 * G", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Time: milliseconds ✓", color=GREEN).scale(0.45)
        ).arrange(DOWN, buff=0.2)
        forward.shift(LEFT * 3.5)

        # Reverse (hard)
        reverse = VGroup(
            Text("Reverse: HARD", color=RED).scale(0.8),
            Text("", color=GRAY).scale(0.1),
            Text("P = known point", color=BLUE).scale(0.5),
            Arrow(ORIGIN, DOWN * 0.8, color=RED),
            Text("Discrete Log Problem", color=YELLOW).scale(0.4),
            Arrow(ORIGIN, DOWN * 0.8, color=RED),
            Text("d = ???", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Time: billions of years ✗", color=RED).scale(0.45)
        ).arrange(DOWN, buff=0.2)
        reverse.shift(RIGHT * 3.5)

        self.play(FadeIn(forward), run_time=1.5)
        self.wait(2)
        self.play(FadeIn(reverse), run_time=1.5)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(forward),
            FadeOut(reverse),
            FadeOut(title),
            run_time=1
        )


class DoubleAndAddAlgorithm(Scene):
    """Explain the double-and-add algorithm for efficient scalar multiplication"""

    def construct(self):
        # Title
        title = Text("Efficient Scalar Multiplication", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The naive way
        naive = VGroup(
            Text("Naive Approach:", color=RED).scale(0.7),
            Text("To compute 100 * G:", color=GRAY).scale(0.5),
            Text("G + G + G + ... + G (100 times)", color=GRAY).scale(0.5),
            Text("→ 99 additions", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        naive.shift(UP * 1.5)

        for line in naive:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1.5)

        # The smart way
        smart = VGroup(
            Text("Double-and-Add:", color=GREEN).scale(0.7),
            Text("100 in binary: 1100100", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Start with G", color=GRAY).scale(0.45),
            Text("Double: 2G, 4G, 8G, 16G, 32G, 64G", color=GRAY).scale(0.45),
            Text("Add where bit is 1: 64G + 32G + 4G", color=GRAY).scale(0.45),
            Text("→ Only 7 operations!", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        smart.shift(DOWN * 0.5)

        self.play(FadeIn(smart), run_time=1)
        self.wait(3)

        # Efficiency note
        efficiency = Text(
            "For 256-bit keys: ~512 ops vs 2²⁵⁶ ops!",
            color=YELLOW
        ).scale(0.6)
        efficiency.to_edge(DOWN, buff=0.3)
        self.play(Write(efficiency), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(naive),
            FadeOut(smart),
            FadeOut(efficiency),
            FadeOut(title),
            run_time=1
        )


class EllipticCurveMathSummary(Scene):
    """Summary of elliptic curve mathematics"""

    def construct(self):
        # Title
        title = Text("Elliptic Curve Math: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Scalar multiplication: k * P = P + P + ... (k times)", color=BLUE).scale(0.55),
            Text("✓ Generator point G: Known, agreed-upon starting point", color=GREEN).scale(0.55),
            Text("✓ Public key = Private key * G: P = d * G", color=YELLOW).scale(0.55),
            Text("✓ Easy: d → P (forward direction)", color=ORANGE).scale(0.55),
            Text("✓ Hard: P → d (discrete log problem)", color=RED).scale(0.55),
            Text("✓ Double-and-add: Efficient computation", color=PURPLE).scale(0.55)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: ECDSA - How to create digital signatures",
            color=GRAY
        ).scale(0.5)
        next_topic.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(next_topic), run_time=1)
        self.wait(2)

        # Final fade out
        self.play(
            FadeOut(summary),
            FadeOut(next_topic),
            FadeOut(title),
            run_time=1
        )
        self.wait(1)
