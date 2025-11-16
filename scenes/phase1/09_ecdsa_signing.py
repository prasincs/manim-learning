"""
Module 1.9: ECDSA Signing
Topics: How ECDSA signatures are created, nonce importance, r and s values
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
# Add repository root to path for components module
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components import SignatureProcess

# Configure background
config.background_color = "#1e1e1e"


class ECDSAIntroduction(Scene):
    """Introduction to ECDSA"""

    def construct(self):
        # Title
        title = Text("ECDSA: Elliptic Curve Digital Signature Algorithm", color=WHITE).scale(0.9)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is it
        what_is_it = VGroup(
            Text("What is ECDSA?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Digital signature algorithm", color=GRAY).scale(0.5),
            Text("• Based on elliptic curve cryptography", color=GRAY).scale(0.5),
            Text("• Used in Bitcoin (and many other systems)", color=GRAY).scale(0.5),
            Text("• Proves ownership without revealing private key", color=GRAY).scale(0.5)
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
            Text("✓ Prove you own the private key", color=GREEN).scale(0.5),
            Text("✓ Authenticate a message", color=GREEN).scale(0.5),
            Text("✓ Non-repudiation (can't deny signing)", color=GREEN).scale(0.5)
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


class SignatureComponents(Scene):
    """Explain the components of an ECDSA signature"""

    def construct(self):
        # Title
        title = Text("ECDSA Signature Components", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Inputs
        inputs = VGroup(
            Text("Inputs (What you need to sign):", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Message (m): Data to sign", color=BLUE).scale(0.5),
            Text("• Private key (d): Your secret key", color=RED).scale(0.5),
            Text("• Nonce (k): Random number (critical!)", color=ORANGE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        inputs.shift(UP * 1.3)

        for line in inputs:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Output
        output = VGroup(
            Text("Output (The signature):", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• (r, s): Two numbers", color=GREEN).scale(0.5),
            Text("• r: x-coordinate of k*G", color=GREEN).scale(0.5),
            Text("• s: Computed from message and private key", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        output.shift(DOWN * 0.8)

        self.play(FadeIn(output), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(inputs),
            FadeOut(output),
            FadeOut(title),
            run_time=1
        )


class SigningProcess(Scene):
    """Step-by-step signing process"""

    def construct(self):
        # Title
        title = Text("ECDSA Signing Algorithm", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Step 1: Hash the message", color=BLUE).scale(0.6),
            MathTex("e = \\text{hash}(m)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 2: Generate random nonce k", color=GREEN).scale(0.6),
            MathTex("k = \\text{random}(1, n-1)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 3: Calculate point R = k * G", color=YELLOW).scale(0.6),
            MathTex("R = k \\times G = (x, y)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 4: Calculate r", color=ORANGE).scale(0.6),
            MathTex("r = x \\mod n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Step 5: Calculate s", color=PURPLE).scale(0.6),
            MathTex("s = k^{-1}(e + r \\cdot d) \\mod n", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.15),

            Text("Signature = (r, s)", color=GREEN).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        steps.scale(0.9).move_to(ORIGIN)

        for step in steps:
            self.play(FadeIn(step), run_time=0.6)
            self.wait(0.7)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class SigningVisualization(Scene):
    """Visual representation of signing process"""

    def construct(self):
        # Title
        title = Text("Signing: Visual Overview", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Show signing process component
        signing = SignatureProcess(
            message="Send 1 BTC to Bob",
            private_key="d (secret)",
            signature="(r, s)",
            algorithm="ECDSA"
        )
        signing.scale(0.65).shift(DOWN * 0.3)

        # Animate step by step
        self.play(FadeIn(signing.message_box), run_time=0.8)
        self.wait(1)

        self.play(FadeIn(signing.private_key_box), run_time=0.8)
        self.wait(1)

        self.play(
            FadeIn(signing.sign_machine),
            FadeIn(signing.sign_label),
            FadeIn(signing.sign_sublabel),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(signing.arrow1),
            Create(signing.arrow2),
            run_time=1
        )
        self.wait(1)

        self.play(
            Create(signing.arrow3),
            FadeIn(signing.signature_box),
            run_time=1
        )
        self.wait(2)

        # Note
        note = Text("Signature proves ownership without revealing private key!", color=YELLOW).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(signing),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class NonceImportance(Scene):
    """Explain the critical importance of the nonce"""

    def construct(self):
        # Title
        title = Text("The Critical Importance of Nonce (k)", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is it
        what_is_nonce = VGroup(
            Text("What is the nonce (k)?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Random number used in signing", color=GRAY).scale(0.5),
            Text("• Must be unpredictable", color=GRAY).scale(0.5),
            Text("• Must be unique for each signature", color=GRAY).scale(0.5),
            Text("• Never revealed", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_nonce.shift(UP * 1)

        for line in what_is_nonce:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Critical rules
        rules = VGroup(
            Text("CRITICAL RULES:", color=RED).scale(0.8),
            Text("", color=GRAY).scale(0.1),
            Text("✗ NEVER reuse k", color=RED).scale(0.6),
            Text("✗ NEVER use predictable k", color=RED).scale(0.6),
            Text("✗ NEVER reveal k", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("If k is compromised → private key exposed!", color=RED).scale(0.55)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        rules.shift(DOWN * 0.8)

        self.play(FadeIn(rules), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_nonce),
            FadeOut(rules),
            FadeOut(title),
            run_time=1
        )


class NonceReuseAttack(Scene):
    """Demonstrate what happens if nonce is reused"""

    def construct(self):
        # Title
        title = Text("Nonce Reuse Attack", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The scenario
        scenario = VGroup(
            Text("Scenario: Same k used twice", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Message 1: m₁, signature (r₁, s₁)", color=BLUE).scale(0.5),
            Text("Message 2: m₂, signature (r₂, s₂)", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Same k → Same r (r₁ = r₂)", color=ORANGE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        scenario.shift(UP * 1.3)

        for line in scenario:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The attack
        attack = VGroup(
            Text("Attacker can compute:", color=RED).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            MathTex("k = (e_1 - e_2) \\cdot (s_1 - s_2)^{-1}", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("Then recover private key:", color=RED).scale(0.6),
            MathTex("d = (s \\cdot k - e) \\cdot r^{-1}", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("GAME OVER!", color=RED).scale(0.8)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        attack.shift(DOWN * 0.5)

        self.play(FadeIn(attack), run_time=1)
        self.wait(3)

        # Warning
        warning = Text("NEVER reuse nonces in ECDSA!", color=RED).scale(0.6)
        warning.to_edge(DOWN, buff=0.3)
        self.play(Write(warning), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(scenario),
            FadeOut(attack),
            FadeOut(warning),
            FadeOut(title),
            run_time=1
        )


class DeterministicNonces(Scene):
    """Explain RFC 6979 deterministic nonces"""

    def construct(self):
        # Title
        title = Text("Solution: Deterministic Nonces (RFC 6979)", color=WHITE).scale(0.9)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The problem with random
        problem = VGroup(
            Text("Problem with Random Nonces:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Bad RNG = Predictable k", color=RED).scale(0.5),
            Text("• Accidental reuse = Disaster", color=RED).scale(0.5),
            Text("• Hard to test/verify", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 1.3)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The solution
        solution = VGroup(
            Text("RFC 6979 Solution:", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Derive k deterministically:", color=BLUE).scale(0.6),
            MathTex("k = \\text{HMAC}(\\text{private key}, \\text{message})", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Benefits:", color=GREEN).scale(0.6),
            Text("✓ Same inputs → Same k (reproducible)", color=GREEN).scale(0.5),
            Text("✓ Different messages → Different k", color=GREEN).scale(0.5),
            Text("✓ Still unpredictable to attackers", color=GREEN).scale(0.5),
            Text("✓ No need for RNG", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        solution.shift(DOWN * 0.2)

        self.play(FadeIn(solution), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(solution),
            FadeOut(title),
            run_time=1
        )


class SignatureExample(Scene):
    """Concrete example of ECDSA signing"""

    def construct(self):
        # Title
        title = Text("ECDSA Example", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Example data
        example = VGroup(
            Text("Example:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Message:", color=BLUE).scale(0.6),
            Text('"Send 1 BTC to Bob"', color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Private key (d):", color=RED).scale(0.6),
            Text("123456789abcdef... (256 bits)", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Message hash (e):", color=GREEN).scale(0.6),
            Text("a1b2c3d4e5f6... (256 bits)", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Nonce (k):", color=ORANGE).scale(0.6),
            Text("fedcba987654... (random/deterministic)", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Signature (r, s):", color=PURPLE).scale(0.6),
            Text("r = 9f8e7d6c5b...", color=GRAY).scale(0.45),
            Text("s = 1a2b3c4d5e...", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        example.scale(0.85).move_to(ORIGIN)

        for line in example:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(example), FadeOut(title), run_time=1)


class ECDSASigningSummary(Scene):
    """Summary of ECDSA signing"""

    def construct(self):
        # Title
        title = Text("ECDSA Signing: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Inputs: Message + Private key + Nonce", color=BLUE).scale(0.6),
            Text("✓ Output: Signature (r, s)", color=GREEN).scale(0.6),
            Text("✓ r: x-coordinate of k*G", color=YELLOW).scale(0.6),
            Text("✓ s: Combines message hash and private key", color=ORANGE).scale(0.6),
            Text("✓ Nonce MUST be unique and unpredictable", color=RED).scale(0.6),
            Text("✓ RFC 6979: Deterministic nonce generation", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: ECDSA Verification - how to verify a signature",
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
