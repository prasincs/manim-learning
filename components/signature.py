"""
Digital signature visualization components for ECDSA, Schnorr, etc.
"""
from manim import *
import hashlib


class KeyPair(VGroup):
    """Visual representation of a public/private key pair"""

    def __init__(
        self,
        private_key="Private Key",
        public_key="Public Key",
        show_connection=True,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Private key (lock icon representation)
        self.private_box = self._create_key_box(
            private_key,
            "Private",
            RED,
            lock_icon=True
        )

        # Public key (unlocked icon representation)
        self.public_box = self._create_key_box(
            public_key,
            "Public",
            GREEN,
            lock_icon=False
        )

        # Position side by side
        self.private_box.shift(LEFT * 2.5)
        self.public_box.shift(RIGHT * 2.5)

        # Connection arrow
        if show_connection:
            self.arrow = Arrow(
                self.private_box.get_right(),
                self.public_box.get_left(),
                buff=0.2,
                color=YELLOW
            )
            self.arrow_label = Text("derives", color=YELLOW).scale(0.4)
            self.arrow_label.next_to(self.arrow, UP, buff=0.1)
            self.add(self.private_box, self.public_box, self.arrow, self.arrow_label)
        else:
            self.add(self.private_box, self.public_box)

    def _create_key_box(self, key_text, label, color, lock_icon=True):
        """Create a box for a key"""
        # Label
        label_text = Text(label, color=color).scale(0.5)

        # Key value
        display_key = key_text if len(key_text) <= 12 else key_text[:9] + "..."
        key_value = Text(display_key, color=WHITE).scale(0.4)

        # Lock icon (simple representation)
        if lock_icon:
            lock = Text("🔒", color=color).scale(0.6)
        else:
            lock = Text("🔓", color=color).scale(0.6)

        # Arrange
        content = VGroup(lock, label_text, key_value).arrange(DOWN, buff=0.2)

        # Box
        box = SurroundingRectangle(
            content,
            color=WHITE,
            fill_color=color,
            fill_opacity=0.2,
            buff=0.3
        )

        return VGroup(box, content)


class SignatureProcess(VGroup):
    """Visualization of signing process: message + private key -> signature"""

    def __init__(
        self,
        message="Message",
        private_key="Private Key",
        signature="Signature",
        algorithm="ECDSA",
        **kwargs
    ):
        super().__init__(**kwargs)

        # Message box
        self.message_box = self._create_box(message, "Message", BLUE)
        self.message_box.shift(LEFT * 3 + UP * 1)

        # Private key box
        self.private_key_box = self._create_box(private_key, "Private Key", RED)
        self.private_key_box.shift(LEFT * 3 + DOWN * 1)

        # Signing machine
        self.sign_machine = RoundedRectangle(
            width=2.5,
            height=2.5,
            corner_radius=0.2,
            color=GRAY,
            fill_opacity=0.8
        )
        self.sign_machine.move_to(ORIGIN)

        self.sign_label = Text(algorithm, color=WHITE).scale(0.6)
        self.sign_label.move_to(self.sign_machine.get_center() + UP * 0.3)

        self.sign_sublabel = Text("Sign", color=YELLOW).scale(0.5)
        self.sign_sublabel.move_to(self.sign_machine.get_center() + DOWN * 0.3)

        # Signature output
        self.signature_box = self._create_box(signature, "Signature", GREEN)
        self.signature_box.shift(RIGHT * 3.5)

        # Arrows
        self.arrow1 = Arrow(
            self.message_box.get_right(),
            self.sign_machine.get_left() + UP * 0.5,
            buff=0.1,
            color=YELLOW
        )

        self.arrow2 = Arrow(
            self.private_key_box.get_right(),
            self.sign_machine.get_left() + DOWN * 0.5,
            buff=0.1,
            color=YELLOW
        )

        self.arrow3 = Arrow(
            self.sign_machine.get_right(),
            self.signature_box.get_left(),
            buff=0.1,
            color=YELLOW
        )

        # Add all
        self.add(
            self.message_box,
            self.private_key_box,
            self.sign_machine,
            self.sign_label,
            self.sign_sublabel,
            self.signature_box,
            self.arrow1,
            self.arrow2,
            self.arrow3
        )

    def _create_box(self, text, label, color):
        """Create a labeled box"""
        label_text = Text(label, color=color).scale(0.4)
        value_text = Text(text if len(text) <= 10 else text[:7] + "...", color=WHITE).scale(0.4)

        content = VGroup(label_text, value_text).arrange(DOWN, buff=0.1)

        box = SurroundingRectangle(
            content,
            color=WHITE,
            fill_color=color,
            fill_opacity=0.2,
            buff=0.2
        )

        return VGroup(box, content)


class VerificationProcess(VGroup):
    """Visualization of verification process: message + signature + public key -> valid/invalid"""

    def __init__(
        self,
        message="Message",
        signature="Signature",
        public_key="Public Key",
        is_valid=True,
        algorithm="ECDSA",
        **kwargs
    ):
        super().__init__(**kwargs)

        # Message box
        self.message_box = self._create_box(message, "Message", BLUE)
        self.message_box.shift(LEFT * 3.5 + UP * 1.2)

        # Signature box
        self.signature_box = self._create_box(signature, "Signature", GREEN)
        self.signature_box.shift(LEFT * 3.5)

        # Public key box
        self.public_key_box = self._create_box(public_key, "Public Key", GREEN)
        self.public_key_box.shift(LEFT * 3.5 + DOWN * 1.2)

        # Verification machine
        self.verify_machine = RoundedRectangle(
            width=2.5,
            height=3,
            corner_radius=0.2,
            color=GRAY,
            fill_opacity=0.8
        )
        self.verify_machine.move_to(ORIGIN)

        self.verify_label = Text(algorithm, color=WHITE).scale(0.6)
        self.verify_label.move_to(self.verify_machine.get_center() + UP * 0.5)

        self.verify_sublabel = Text("Verify", color=YELLOW).scale(0.5)
        self.verify_sublabel.move_to(self.verify_machine.get_center() + DOWN * 0.3)

        # Result
        result_text = "✓ Valid" if is_valid else "✗ Invalid"
        result_color = GREEN if is_valid else RED

        self.result_box = self._create_box(result_text, "Result", result_color)
        self.result_box.shift(RIGHT * 3.5)

        # Arrows
        self.arrow1 = Arrow(
            self.message_box.get_right(),
            self.verify_machine.get_left() + UP * 0.8,
            buff=0.1,
            color=YELLOW
        )

        self.arrow2 = Arrow(
            self.signature_box.get_right(),
            self.verify_machine.get_left(),
            buff=0.1,
            color=YELLOW
        )

        self.arrow3 = Arrow(
            self.public_key_box.get_right(),
            self.verify_machine.get_left() + DOWN * 0.8,
            buff=0.1,
            color=YELLOW
        )

        self.arrow4 = Arrow(
            self.verify_machine.get_right(),
            self.result_box.get_left(),
            buff=0.1,
            color=YELLOW
        )

        # Add all
        self.add(
            self.message_box,
            self.signature_box,
            self.public_key_box,
            self.verify_machine,
            self.verify_label,
            self.verify_sublabel,
            self.result_box,
            self.arrow1,
            self.arrow2,
            self.arrow3,
            self.arrow4
        )

    def _create_box(self, text, label, color):
        """Create a labeled box"""
        label_text = Text(label, color=color).scale(0.4)
        value_text = Text(text if len(text) <= 10 else text[:7] + "...", color=WHITE).scale(0.4)

        content = VGroup(label_text, value_text).arrange(DOWN, buff=0.1)

        box = SurroundingRectangle(
            content,
            color=WHITE,
            fill_color=color,
            fill_opacity=0.2,
            buff=0.2
        )

        return VGroup(box, content)


class EllipticCurve(VGroup):
    """Visual representation of an elliptic curve y² = x³ + ax + b"""

    def __init__(
        self,
        a=0,
        b=7,
        x_range=(-3, 3),
        y_range=(-3, 3),
        **kwargs
    ):
        super().__init__(**kwargs)

        # Create axes
        self.axes = Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=6,
            y_length=6,
            axis_config={"color": GRAY},
        )

        # Equation label
        equation_text = f"y² = x³ + {a}x + {b}" if a != 0 else f"y² = x³ + {b}"
        self.equation = MathTex(equation_text, color=WHITE).scale(0.7)
        self.equation.to_corner(UL)

        # Plot curve (for secp256k1: y² = x³ + 7)
        # We'll plot the positive and negative branches
        self.curve_positive = self.axes.plot(
            lambda x: (x**3 + a*x + b)**0.5 if x**3 + a*x + b >= 0 else 0,
            x_range=[max(x_range[0], -(b/1)**(1/3)), x_range[1]],
            color=BLUE
        )

        self.curve_negative = self.axes.plot(
            lambda x: -(x**3 + a*x + b)**0.5 if x**3 + a*x + b >= 0 else 0,
            x_range=[max(x_range[0], -(b/1)**(1/3)), x_range[1]],
            color=BLUE
        )

        self.add(self.axes, self.curve_positive, self.curve_negative, self.equation)


class PointAddition(VGroup):
    """Visualization of point addition on elliptic curve"""

    def __init__(self, point_p, point_q, point_r, axes, **kwargs):
        super().__init__(**kwargs)

        # Points
        self.p_dot = Dot(axes.c2p(*point_p), color=RED)
        self.q_dot = Dot(axes.c2p(*point_q), color=GREEN)
        self.r_dot = Dot(axes.c2p(point_r[0], -point_r[1]), color=YELLOW)  # Reflected

        # Labels
        self.p_label = Text("P", color=RED).scale(0.5).next_to(self.p_dot, UP)
        self.q_label = Text("Q", color=GREEN).scale(0.5).next_to(self.q_dot, UP)
        self.r_label = Text("R=P+Q", color=YELLOW).scale(0.5).next_to(self.r_dot, DOWN)

        # Line through P and Q
        self.line = Line(
            axes.c2p(point_p[0] - 2, point_p[1] - 2 * (point_q[1] - point_p[1]) / (point_q[0] - point_p[0])),
            axes.c2p(point_q[0] + 2, point_q[1] + 2 * (point_q[1] - point_p[1]) / (point_q[0] - point_p[0])),
            color=YELLOW,
            stroke_width=2
        )

        # Vertical line for reflection
        self.reflection = DashedLine(
            axes.c2p(point_r[0], point_r[1]),
            axes.c2p(point_r[0], -point_r[1]),
            color=ORANGE,
            stroke_width=2
        )

        self.add(
            self.p_dot,
            self.q_dot,
            self.r_dot,
            self.p_label,
            self.q_label,
            self.r_label,
            self.line,
            self.reflection
        )


# Example usage scene
class SignatureExample(Scene):
    def construct(self):
        # Title
        title = Text("Digital Signature Process").to_edge(UP)
        self.play(Write(title))

        # Show signing
        signing = SignatureProcess(
            message="Hello, Bitcoin!",
            private_key="d=secret",
            signature="(r, s)",
            algorithm="ECDSA"
        )
        signing.scale(0.7)

        self.play(FadeIn(signing))
        self.wait(2)

        # Clear
        self.play(FadeOut(signing))

        # Show verification
        verification = VerificationProcess(
            message="Hello, Bitcoin!",
            signature="(r, s)",
            public_key="P=d*G",
            is_valid=True,
            algorithm="ECDSA"
        )
        verification.scale(0.7)

        self.play(FadeIn(verification))
        self.wait(3)

        self.play(FadeOut(verification), FadeOut(title))


class EllipticCurveExample(Scene):
    def construct(self):
        # Title
        title = Text("Elliptic Curve: y² = x³ + 7").to_edge(UP)
        self.play(Write(title))

        # Create curve
        curve = EllipticCurve(a=0, b=7)
        curve.scale(0.8).shift(DOWN * 0.5)

        self.play(Create(curve.axes))
        self.play(Create(curve.curve_positive), Create(curve.curve_negative))
        self.wait(2)

        # Show point addition (example points)
        # Note: These are illustrative, not actual secp256k1 points
        point_addition = PointAddition(
            point_p=(1, 2.5),
            point_q=(2, 3),
            point_r=(0.5, 2),
            axes=curve.axes
        )

        self.play(FadeIn(point_addition))
        self.wait(3)

        self.play(FadeOut(curve), FadeOut(point_addition), FadeOut(title))
