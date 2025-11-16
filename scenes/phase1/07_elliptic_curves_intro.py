"""
Module 1.7: Elliptic Curves Basics
Topics: What is an elliptic curve? Point addition, geometric visualization
Duration: 5-10 minutes
"""

from manim import *
import numpy as np
import sys
sys.path.append('/home/user/manim-learning')
from components import EllipticCurve, PointAddition

# Configure background
config.background_color = "#1e1e1e"


class EllipticCurveIntroduction(Scene):
    """Introduction to elliptic curves"""

    def construct(self):
        # Title
        title = Text("Elliptic Curves", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("The Math Behind Bitcoin Keys", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # What is it?
        explanation = VGroup(
            Text("What is an Elliptic Curve?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• A curve defined by an equation", color=GRAY).scale(0.5),
            Text("• Shape: y² = x³ + ax + b", color=BLUE).scale(0.5),
            Text("• Special mathematical properties", color=GRAY).scale(0.5),
            Text("• Used for cryptography", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.move_to(ORIGIN)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Clear
        self.play(
            FadeOut(explanation),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class EllipticCurveEquation(Scene):
    """Show the elliptic curve equation"""

    def construct(self):
        # Title
        title = Text("The Elliptic Curve Equation", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # General form
        general_eq = MathTex("y^2 = x^3 + ax + b", color=BLUE).scale(1.2)
        general_eq.shift(UP * 1.5)

        general_label = Text("General form", color=GRAY).scale(0.5)
        general_label.next_to(general_eq, DOWN, buff=0.3)

        self.play(Write(general_eq), run_time=1)
        self.play(FadeIn(general_label), run_time=0.5)
        self.wait(2)

        # Bitcoin's curve: secp256k1
        self.play(FadeOut(general_label), run_time=0.5)

        bitcoin_label = Text("Bitcoin uses: secp256k1", color=YELLOW).scale(0.7)
        bitcoin_label.shift(DOWN * 0.3)
        self.play(Write(bitcoin_label), run_time=1)
        self.wait(1)

        # Specific equation
        secp256k1_eq = MathTex("y^2 = x^3 + 7", color=GREEN).scale(1.2)
        secp256k1_eq.shift(DOWN * 1.2)

        secp_note = Text("(a = 0, b = 7)", color=GRAY).scale(0.5)
        secp_note.next_to(secp256k1_eq, DOWN, buff=0.3)

        self.play(Write(secp256k1_eq), run_time=1)
        self.play(FadeIn(secp_note), run_time=0.5)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(general_eq),
            FadeOut(bitcoin_label),
            FadeOut(secp256k1_eq),
            FadeOut(secp_note),
            FadeOut(title),
            run_time=1
        )


class VisualizingTheCurve(Scene):
    """Visualize the elliptic curve y² = x³ + 7"""

    def construct(self):
        # Title
        title = Text("Visualizing y² = x³ + 7", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create and show the curve
        curve = EllipticCurve(a=0, b=7, x_range=(-3, 3), y_range=(-4, 4))
        curve.scale(0.7).shift(DOWN * 0.3)

        self.play(Create(curve.axes), run_time=1)
        self.wait(0.5)

        self.play(
            Create(curve.curve_positive),
            Create(curve.curve_negative),
            run_time=2
        )
        self.wait(2)

        # Add note
        note = Text("This curve has special symmetry", color=YELLOW).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(curve),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class CurveSymmetry(Scene):
    """Demonstrate the symmetry property"""

    def construct(self):
        # Title
        title = Text("Elliptic Curve Symmetry", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create curve
        curve = EllipticCurve(a=0, b=7, x_range=(-3, 3), y_range=(-4, 4))
        curve.scale(0.65).shift(DOWN * 0.5)

        self.play(Create(curve.axes), run_time=0.8)
        self.play(
            Create(curve.curve_positive),
            Create(curve.curve_negative),
            run_time=1.5
        )
        self.wait(1)

        # Show symmetry around x-axis
        symmetry_line = DashedLine(
            curve.axes.c2p(-3, 0),
            curve.axes.c2p(3, 0),
            color=YELLOW,
            stroke_width=3
        )

        symmetry_label = Text("Symmetric around x-axis", color=YELLOW).scale(0.6)
        symmetry_label.next_to(curve, RIGHT, buff=0.5)

        self.play(Create(symmetry_line), run_time=1)
        self.play(Write(symmetry_label), run_time=1)
        self.wait(1)

        # Show mirror points
        point_x = 1.5
        point_y = (point_x**3 + 7)**0.5

        dot_top = Dot(curve.axes.c2p(point_x, point_y), color=GREEN)
        dot_bottom = Dot(curve.axes.c2p(point_x, -point_y), color=GREEN)

        mirror_line = DashedLine(
            curve.axes.c2p(point_x, point_y),
            curve.axes.c2p(point_x, -point_y),
            color=GREEN,
            stroke_width=2
        )

        self.play(
            Create(dot_top),
            Create(dot_bottom),
            Create(mirror_line),
            run_time=1
        )
        self.wait(2)

        # Clear
        self.play(
            FadeOut(curve),
            FadeOut(symmetry_line),
            FadeOut(symmetry_label),
            FadeOut(dot_top),
            FadeOut(dot_bottom),
            FadeOut(mirror_line),
            FadeOut(title),
            run_time=1
        )


class PointAdditionIntro(Scene):
    """Introduction to point addition on elliptic curves"""

    def construct(self):
        # Title
        title = Text("Point Addition on Elliptic Curves", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The magic
        explanation = VGroup(
            Text("The Magic of Elliptic Curves:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• You can 'add' points on the curve", color=GRAY).scale(0.5),
            Text("• Result is also on the curve", color=GRAY).scale(0.5),
            Text("• This operation has special properties", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.shift(UP * 1)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The rule
        rule = VGroup(
            Text("The Rule:", color=BLUE).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("1. Draw line through P and Q", color=GRAY).scale(0.5),
            Text("2. Find where it crosses curve (third point)", color=GRAY).scale(0.5),
            Text("3. Reflect across x-axis", color=GRAY).scale(0.5),
            Text("4. That's P + Q!", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        rule.shift(DOWN * 0.8)

        self.play(FadeIn(rule), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(explanation),
            FadeOut(rule),
            FadeOut(title),
            run_time=1
        )


class PointAdditionVisualization(Scene):
    """Visualize point addition geometrically"""

    def construct(self):
        # Title
        title = Text("Point Addition: P + Q = R", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create curve
        curve = EllipticCurve(a=0, b=7, x_range=(-3, 3), y_range=(-4, 4))
        curve.scale(0.65).shift(DOWN * 0.5)

        self.play(Create(curve.axes), run_time=0.8)
        self.play(
            Create(curve.curve_positive),
            Create(curve.curve_negative),
            run_time=1.2
        )
        self.wait(1)

        # Choose two points
        p_x, p_y = 0.5, (0.5**3 + 7)**0.5
        q_x, q_y = 2, (2**3 + 7)**0.5

        # Show point P
        p_dot = Dot(curve.axes.c2p(p_x, p_y), color=RED)
        p_label = Text("P", color=RED).scale(0.6)
        p_label.next_to(p_dot, UP, buff=0.2)

        self.play(Create(p_dot), Write(p_label), run_time=0.8)
        self.wait(0.5)

        # Show point Q
        q_dot = Dot(curve.axes.c2p(q_x, q_y), color=GREEN)
        q_label = Text("Q", color=GREEN).scale(0.6)
        q_label.next_to(q_dot, UP, buff=0.2)

        self.play(Create(q_dot), Write(q_label), run_time=0.8)
        self.wait(1)

        # Draw line through P and Q
        slope = (q_y - p_y) / (q_x - p_x)
        # Find third intersection (simplified for visualization)
        # For y² = x³ + 7, this requires solving cubic equation
        # Using approximate third point for visualization
        r_x = 1.8
        r_y_temp = (r_x**3 + 7)**0.5  # Point on curve before reflection

        line = Line(
            curve.axes.c2p(p_x - 0.5, p_y - 0.5 * slope),
            curve.axes.c2p(r_x + 0.3, r_y_temp + 0.3 * slope),
            color=YELLOW,
            stroke_width=2
        )

        step1 = Text("Step 1: Draw line through P and Q", color=YELLOW).scale(0.5)
        step1.to_edge(DOWN, buff=0.3)

        self.play(Create(line), Write(step1), run_time=1)
        self.wait(2)

        # Show third intersection
        r_temp_dot = Dot(curve.axes.c2p(r_x, r_y_temp), color=ORANGE)
        r_temp_label = Text("R'", color=ORANGE).scale(0.6)
        r_temp_label.next_to(r_temp_dot, UP, buff=0.2)

        self.play(FadeOut(step1), run_time=0.3)
        step2 = Text("Step 2: Find third intersection", color=YELLOW).scale(0.5)
        step2.to_edge(DOWN, buff=0.3)

        self.play(Create(r_temp_dot), Write(r_temp_label), Write(step2), run_time=1)
        self.wait(2)

        # Reflect across x-axis
        r_y = -r_y_temp
        r_dot = Dot(curve.axes.c2p(r_x, r_y), color=BLUE)
        r_label = Text("R = P + Q", color=BLUE).scale(0.6)
        r_label.next_to(r_dot, DOWN, buff=0.2)

        reflection_line = DashedLine(
            curve.axes.c2p(r_x, r_y_temp),
            curve.axes.c2p(r_x, r_y),
            color=PURPLE,
            stroke_width=2
        )

        self.play(FadeOut(step2), run_time=0.3)
        step3 = Text("Step 3: Reflect across x-axis", color=YELLOW).scale(0.5)
        step3.to_edge(DOWN, buff=0.3)

        self.play(
            Create(reflection_line),
            Create(r_dot),
            Write(r_label),
            Write(step3),
            run_time=1
        )
        self.wait(3)

        # Clear
        self.play(
            FadeOut(curve),
            FadeOut(p_dot), FadeOut(p_label),
            FadeOut(q_dot), FadeOut(q_label),
            FadeOut(r_dot), FadeOut(r_label),
            FadeOut(r_temp_dot), FadeOut(r_temp_label),
            FadeOut(line),
            FadeOut(reflection_line),
            FadeOut(step3),
            FadeOut(title),
            run_time=1
        )


class PointDoubling(Scene):
    """Explain point doubling (P + P = 2P)"""

    def construct(self):
        # Title
        title = Text("Point Doubling: P + P = 2P", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Explanation
        explanation = VGroup(
            Text("What if we add a point to itself?", color=YELLOW).scale(0.6),
            Text("P + P = 2P", color=BLUE).scale(0.7)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(UP * 2)

        self.play(FadeIn(explanation), run_time=1)
        self.wait(1.5)

        # Create curve
        curve = EllipticCurve(a=0, b=7, x_range=(-3, 3), y_range=(-4, 4))
        curve.scale(0.6).shift(DOWN * 0.8)

        self.play(Create(curve.axes), run_time=0.8)
        self.play(
            Create(curve.curve_positive),
            Create(curve.curve_negative),
            run_time=1.2
        )
        self.wait(1)

        # Show point P
        p_x, p_y = 1.5, (1.5**3 + 7)**0.5
        p_dot = Dot(curve.axes.c2p(p_x, p_y), color=RED)
        p_label = Text("P", color=RED).scale(0.6)
        p_label.next_to(p_dot, UP + RIGHT, buff=0.2)

        self.play(Create(p_dot), Write(p_label), run_time=0.8)
        self.wait(1)

        # Draw tangent line
        # Slope of tangent: dy/dx = (3x²)/(2y) for y² = x³ + 7
        slope = (3 * p_x**2) / (2 * p_y)

        tangent = Line(
            curve.axes.c2p(p_x - 1.5, p_y - 1.5 * slope),
            curve.axes.c2p(p_x + 1.5, p_y + 1.5 * slope),
            color=YELLOW,
            stroke_width=2
        )

        tangent_label = Text("Tangent line at P", color=YELLOW).scale(0.5)
        tangent_label.next_to(curve, RIGHT, buff=0.3)

        self.play(Create(tangent), Write(tangent_label), run_time=1)
        self.wait(2)

        # Show result (simplified visualization)
        result_note = Text("Follow same reflection rule", color=GREEN).scale(0.5)
        result_note.to_edge(DOWN, buff=0.3)
        self.play(Write(result_note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(curve),
            FadeOut(p_dot), FadeOut(p_label),
            FadeOut(tangent), FadeOut(tangent_label),
            FadeOut(explanation),
            FadeOut(result_note),
            FadeOut(title),
            run_time=1
        )


class PointAdditionProperties(Scene):
    """Properties of point addition"""

    def construct(self):
        # Title
        title = Text("Point Addition Properties", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Properties
        properties = VGroup(
            Text("Point addition forms a group:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("1. Closure: P + Q is on the curve", color=BLUE).scale(0.55),
            Text("2. Associative: (P + Q) + R = P + (Q + R)", color=GREEN).scale(0.55),
            Text("3. Identity: Point at infinity (O)", color=ORANGE).scale(0.55),
            Text("4. Inverse: -P is P reflected over x-axis", color=PURPLE).scale(0.55),
            Text("5. Commutative: P + Q = Q + P", color=RED).scale(0.55)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        properties.move_to(ORIGIN)

        for prop in properties:
            self.play(FadeIn(prop), run_time=0.8)
            self.wait(1)

        self.wait(2)

        # Key insight
        insight = Text(
            "These properties make elliptic curves perfect for cryptography!",
            color=YELLOW
        ).scale(0.6)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(properties),
            FadeOut(insight),
            FadeOut(title),
            run_time=1
        )


class EllipticCurveSummary(Scene):
    """Summary of elliptic curves basics"""

    def construct(self):
        # Title
        title = Text("Elliptic Curves: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Equation: y² = x³ + ax + b", color=BLUE).scale(0.6),
            Text("✓ Bitcoin uses: y² = x³ + 7 (secp256k1)", color=GREEN).scale(0.6),
            Text("✓ Symmetric around x-axis", color=YELLOW).scale(0.6),
            Text("✓ Point addition: Draw line, find intersection, reflect", color=ORANGE).scale(0.6),
            Text("✓ Forms a mathematical group", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Scalar multiplication and the discrete log problem",
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
