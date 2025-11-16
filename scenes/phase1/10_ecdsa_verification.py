"""
Module 1.10: ECDSA Verification
Topics: How to verify an ECDSA signature, why it works mathematically, invalid signature detection
Duration: 5-10 minutes
"""

from manim import *
import sys
# Add repository root to path for components module
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components import VerificationProcess

# Configure background
config.background_color = "#1e1e1e"


class VerificationIntroduction(Scene):
    """Introduction to ECDSA verification"""

    def construct(self):
        # Title
        title = Text("ECDSA Signature Verification", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is verification
        what_is_it = VGroup(
            Text("What is Verification?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Checking if a signature is valid", color=GRAY).scale(0.5),
            Text("• Using only public information", color=GRAY).scale(0.5),
            Text("• Anyone can verify", color=GRAY).scale(0.5),
            Text("• No private key needed!", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 0.8)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Purpose
        purpose = VGroup(
            Text("Purpose:", color=BLUE).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Confirm signer has private key", color=GREEN).scale(0.5),
            Text("✓ Ensure message wasn't tampered with", color=GREEN).scale(0.5),
            Text("✓ Publicly verifiable proof", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        purpose.shift(DOWN * 1.2)

        self.play(FadeIn(purpose), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(purpose),
            FadeOut(title),
            run_time=1
        )


class VerificationInputs(Scene):
    """What you need to verify a signature"""

    def construct(self):
        # Title
        title = Text("Verification Inputs", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Public inputs
        inputs = VGroup(
            Text("Public Inputs (everyone has these):", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Message (m): Original data", color=BLUE).scale(0.5),
            Text("• Signature (r, s): The claimed signature", color=GREEN).scale(0.5),
            Text("• Public key (P): Signer's public key", color=PURPLE).scale(0.5),
            Text("• Curve parameters: G, n (known)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        inputs.shift(UP * 1)

        for line in inputs:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Output
        output = VGroup(
            Text("Output:", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Valid: Signature is authentic", color=GREEN).scale(0.6),
            Text("✗ Invalid: Signature is fake/tampered", color=RED).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        output.shift(DOWN * 1.2)

        self.play(FadeIn(output), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(inputs),
            FadeOut(output),
            FadeOut(title),
            run_time=1
        )


class VerificationAlgorithm(Scene):
    """Step-by-step verification algorithm"""

    def construct(self):
        # Title
        title = Text("ECDSA Verification Algorithm", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Step 1: Verify r and s are valid", color=BLUE).scale(0.6),
            MathTex("1 \\leq r, s < n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 2: Hash the message", color=GREEN).scale(0.6),
            MathTex("e = \\text{hash}(m)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 3: Calculate w", color=YELLOW).scale(0.6),
            MathTex("w = s^{-1} \\mod n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 4: Calculate u₁ and u₂", color=ORANGE).scale(0.6),
            MathTex("u_1 = e \\cdot w \\mod n", color=GRAY).scale(0.5),
            MathTex("u_2 = r \\cdot w \\mod n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 5: Calculate point R'", color=PURPLE).scale(0.6),
            MathTex("R' = u_1 \\cdot G + u_2 \\cdot P", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 6: Verify", color=RED).scale(0.6),
            MathTex("r \\stackrel{?}{=} x_{R'} \\mod n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Valid if r matches!", color=GREEN).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        steps.scale(0.85).move_to(ORIGIN)

        for step in steps:
            self.play(FadeIn(step), run_time=0.5)
            self.wait(0.6)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class VerificationVisualization(Scene):
    """Visual representation of verification process"""

    def construct(self):
        # Title
        title = Text("Verification: Visual Overview", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Show verification process component
        verification = VerificationProcess(
            message="Send 1 BTC to Bob",
            signature="(r, s)",
            public_key="P = d*G",
            is_valid=True,
            algorithm="ECDSA"
        )
        verification.scale(0.6).shift(DOWN * 0.3)

        # Animate step by step
        self.play(FadeIn(verification.message_box), run_time=0.8)
        self.wait(1)

        self.play(FadeIn(verification.signature_box), run_time=0.8)
        self.wait(1)

        self.play(FadeIn(verification.public_key_box), run_time=0.8)
        self.wait(1)

        self.play(
            FadeIn(verification.verify_machine),
            FadeIn(verification.verify_label),
            FadeIn(verification.verify_sublabel),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(verification.arrow1),
            Create(verification.arrow2),
            Create(verification.arrow3),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(verification.arrow4),
            FadeIn(verification.result_box),
            run_time=1
        )
        self.wait(2)

        # Note
        note = Text("No private key needed - anyone can verify!", color=YELLOW).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(verification),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class WhyItWorks(Scene):
    """Explain the mathematics of why verification works"""

    def construct(self):
        # Title
        title = Text("Why Does Verification Work?", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The math
        subtitle = Text("The Mathematical Magic:", color=YELLOW).scale(0.7)
        subtitle.shift(UP * 2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)

        # Signing equation
        signing = VGroup(
            Text("During Signing:", color=BLUE).scale(0.6),
            MathTex("s = k^{-1}(e + r \\cdot d)", color=BLUE).scale(0.6),
            MathTex("\\Rightarrow k = s^{-1}(e + r \\cdot d)", color=BLUE).scale(0.6),
            MathTex("\\Rightarrow k \\cdot G = s^{-1}(e + r \\cdot d) \\cdot G", color=BLUE).scale(0.6),
            MathTex("\\Rightarrow k \\cdot G = s^{-1} \\cdot e \\cdot G + s^{-1} \\cdot r \\cdot d \\cdot G", color=BLUE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        signing.shift(UP * 0.5)

        for line in signing:
            self.play(FadeIn(line), run_time=0.7)
            self.wait(0.7)

        self.wait(2)

        # Verification equation
        verification = VGroup(
            Text("During Verification:", color=GREEN).scale(0.6),
            MathTex("R' = u_1 \\cdot G + u_2 \\cdot P", color=GREEN).scale(0.6),
            MathTex("= (e \\cdot s^{-1}) \\cdot G + (r \\cdot s^{-1}) \\cdot P", color=GREEN).scale(0.6),
            MathTex("= s^{-1} \\cdot e \\cdot G + s^{-1} \\cdot r \\cdot (d \\cdot G)", color=GREEN).scale(0.6),
            MathTex("= s^{-1} \\cdot e \\cdot G + s^{-1} \\cdot r \\cdot d \\cdot G", color=GREEN).scale(0.6),
            MathTex("= k \\cdot G", color=YELLOW).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        verification.shift(DOWN * 1.5)

        for line in verification:
            self.play(FadeIn(line), run_time=0.7)
            self.wait(0.7)

        self.wait(3)

        # Clear
        self.play(
            FadeOut(signing),
            FadeOut(verification),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class WhyItWorksSimple(Scene):
    """Simplified explanation of why it works"""

    def construct(self):
        # Title
        title = Text("Why Verification Works (Simplified)", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Simple explanation
        explanation = VGroup(
            Text("The Key Insight:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Signing creates (r, s) using:", color=BLUE).scale(0.6),
            Text("• Random k", color=GRAY).scale(0.5),
            Text("• Private key d", color=GRAY).scale(0.5),
            Text("• Message hash e", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Verification reconstructs k*G using:", color=GREEN).scale(0.6),
            Text("• Signature (r, s)", color=GRAY).scale(0.5),
            Text("• Public key P = d*G", color=GRAY).scale(0.5),
            Text("• Message hash e", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("If they match → signature is valid!", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.scale(0.9).move_to(ORIGIN)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.6)
            self.wait(0.6)

        self.wait(3)

        # Clear
        self.play(FadeOut(explanation), FadeOut(title), run_time=1)


class InvalidSignatures(Scene):
    """What makes a signature invalid"""

    def construct(self):
        # Title
        title = Text("Invalid Signatures", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Reasons for invalidity
        reasons = VGroup(
            Text("Signature is INVALID if:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✗ Message was tampered with", color=RED).scale(0.6),
            Text("  → Different hash, verification fails", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✗ Signature (r, s) was altered", color=RED).scale(0.6),
            Text("  → Math doesn't work out", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✗ Wrong public key used", color=RED).scale(0.6),
            Text("  → P doesn't match d that created sig", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✗ Signature forged", color=RED).scale(0.6),
            Text("  → Impossible without private key", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        reasons.scale(0.9).move_to(ORIGIN)

        for line in reasons:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(reasons), FadeOut(title), run_time=1)


class InvalidSignatureDemo(Scene):
    """Demo of invalid signature verification"""

    def construct(self):
        # Title
        title = Text("Invalid Signature Example", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Show invalid verification
        verification = VerificationProcess(
            message="Send 1 BTC to Bob",
            signature="(r', s')",
            public_key="P = d*G",
            is_valid=False,
            algorithm="ECDSA"
        )
        verification.scale(0.6).shift(DOWN * 0.3)

        self.play(FadeIn(verification), run_time=1.5)
        self.wait(2)

        # Note about what went wrong
        note = Text("Tampered message → Verification fails!", color=RED).scale(0.6)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(verification),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class VerificationSecurity(Scene):
    """Security properties of ECDSA verification"""

    def construct(self):
        # Title
        title = Text("Security Properties", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Properties
        properties = VGroup(
            Text("ECDSA Verification is Secure because:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Requires private key to create valid signature", color=GREEN).scale(0.55),
            Text("  → Discrete log problem is hard", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Any tampering invalidates signature", color=GREEN).scale(0.55),
            Text("  → Hash function collision-resistant", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Unique signature for each message", color=GREEN).scale(0.55),
            Text("  → Can't replay signatures", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Non-repudiation", color=GREEN).scale(0.55),
            Text("  → Only private key holder could sign", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        properties.scale(0.9).move_to(ORIGIN)

        for line in properties:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(properties), FadeOut(title), run_time=1)


class ECDSAVerificationSummary(Scene):
    """Summary of ECDSA verification"""

    def construct(self):
        # Title
        title = Text("ECDSA Verification: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Inputs: Message + Signature (r, s) + Public key", color=BLUE).scale(0.6),
            Text("✓ Algorithm: Compute R' = u₁*G + u₂*P", color=GREEN).scale(0.6),
            Text("✓ Verify: r matches x-coordinate of R'", color=YELLOW).scale(0.6),
            Text("✓ Anyone can verify (public operation)", color=ORANGE).scale(0.6),
            Text("✓ Tampering → Invalid signature", color=RED).scale(0.6),
            Text("✓ Security: Based on discrete log problem", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Schnorr Signatures - a simpler alternative",
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
