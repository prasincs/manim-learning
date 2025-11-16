"""
Module 1.11: Schnorr Signatures Introduction
Topics: Schnorr vs ECDSA, advantages, linearity property
Duration: 5-10 minutes
"""

from manim import *
import sys
sys.path.append('/home/user/manim-learning')
from components import SignatureProcess, VerificationProcess

# Configure background
config.background_color = "#1e1e1e"


class SchnorrIntroduction(Scene):
    """Introduction to Schnorr signatures"""

    def construct(self):
        # Title
        title = Text("Schnorr Signatures", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("A Simpler, More Elegant Alternative to ECDSA", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # What is it
        what_is_it = VGroup(
            Text("What is Schnorr?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Digital signature scheme", color=GRAY).scale(0.5),
            Text("• Invented by Claus Schnorr (1989)", color=GRAY).scale(0.5),
            Text("• Simpler math than ECDSA", color=GRAY).scale(0.5),
            Text("• Added to Bitcoin in 2021 (Taproot)", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.move_to(ORIGIN)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class ECDSAvsSchnorr(Scene):
    """Compare ECDSA and Schnorr"""

    def construct(self):
        # Title
        title = Text("ECDSA vs Schnorr", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # ECDSA (left side)
        ecdsa = VGroup(
            Text("ECDSA", color=BLUE).scale(0.8),
            Text("", color=GRAY).scale(0.1),
            Text("Signature:", color=GRAY).scale(0.5),
            Text("s = k⁻¹(e + rd)", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Verification:", color=GRAY).scale(0.5),
            Text("R = u₁G + u₂P", color=BLUE).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("Properties:", color=GRAY).scale(0.5),
            Text("• Complex formula", color=RED).scale(0.45),
            Text("• Non-linear", color=RED).scale(0.45),
            Text("• 71-73 bytes", color=ORANGE).scale(0.45),
            Text("• No aggregation", color=RED).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ecdsa.shift(LEFT * 3.5)

        # Schnorr (right side)
        schnorr = VGroup(
            Text("Schnorr", color=GREEN).scale(0.8),
            Text("", color=GRAY).scale(0.1),
            Text("Signature:", color=GRAY).scale(0.5),
            Text("s = k + e·d", color=GREEN).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Verification:", color=GRAY).scale(0.5),
            Text("sG = R + eP", color=GREEN).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("Properties:", color=GRAY).scale(0.5),
            Text("• Simple formula", color=GREEN).scale(0.45),
            Text("• Linear!", color=GREEN).scale(0.45),
            Text("• 64 bytes", color=GREEN).scale(0.45),
            Text("• Aggregation!", color=GREEN).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        schnorr.shift(RIGHT * 3.5)

        self.play(FadeIn(ecdsa), run_time=1.5)
        self.wait(2)
        self.play(FadeIn(schnorr), run_time=1.5)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(ecdsa),
            FadeOut(schnorr),
            FadeOut(title),
            run_time=1
        )


class SchnorrAdvantages(Scene):
    """Advantages of Schnorr signatures"""

    def construct(self):
        # Title
        title = Text("Schnorr Advantages", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Advantages
        advantages = VGroup(
            Text("Why Schnorr is Better:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("1. Simplicity", color=GREEN).scale(0.6),
            Text("   • Simpler math (linear equation)", color=GRAY).scale(0.5),
            Text("   • Easier to understand and implement", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("2. Smaller Signatures", color=GREEN).scale(0.6),
            Text("   • 64 bytes vs 71-73 bytes (ECDSA)", color=GRAY).scale(0.5),
            Text("   • ~12% smaller", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("3. Linearity", color=GREEN).scale(0.6),
            Text("   • Signatures can be combined", color=GRAY).scale(0.5),
            Text("   • Enables key and signature aggregation", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("4. Provable Security", color=GREEN).scale(0.6),
            Text("   • Strong security proofs", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        advantages.scale(0.85).move_to(ORIGIN)

        for line in advantages:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(advantages), FadeOut(title), run_time=1)


class SchnorrSigning(Scene):
    """Schnorr signing algorithm"""

    def construct(self):
        # Title
        title = Text("Schnorr Signing", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Signing Algorithm:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Input:", color=BLUE).scale(0.6),
            Text("• Message m", color=GRAY).scale(0.5),
            Text("• Private key d", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 1: Generate random k", color=GREEN).scale(0.6),
            MathTex("k \\in [1, n-1]", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 2: Compute R = k·G", color=GREEN).scale(0.6),
            MathTex("R = k \\times G", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 3: Compute challenge e", color=GREEN).scale(0.6),
            MathTex("e = \\text{hash}(R || P || m)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 4: Compute s", color=GREEN).scale(0.6),
            MathTex("s = k + e \\cdot d", color=YELLOW).scale(0.6),
            Text("", color=GRAY).scale(0.1),

            Text("Signature = (R, s)", color=GREEN).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        steps.scale(0.85).move_to(ORIGIN)

        for line in steps:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class SchnorrVerification(Scene):
    """Schnorr verification algorithm"""

    def construct(self):
        # Title
        title = Text("Schnorr Verification", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Verification Algorithm:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Input:", color=BLUE).scale(0.6),
            Text("• Message m", color=GRAY).scale(0.5),
            Text("• Signature (R, s)", color=GRAY).scale(0.5),
            Text("• Public key P", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 1: Compute challenge e", color=GREEN).scale(0.6),
            MathTex("e = \\text{hash}(R || P || m)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 2: Verify equation", color=GREEN).scale(0.6),
            MathTex("s \\cdot G \\stackrel{?}{=} R + e \\cdot P", color=YELLOW).scale(0.6),
            Text("", color=GRAY).scale(0.1),

            Text("If equal → Valid signature!", color=GREEN).scale(0.7),
            Text("If not equal → Invalid!", color=RED).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.scale(0.9).move_to(ORIGIN)

        for line in steps:
            self.play(FadeIn(line), run_time=0.6)
            self.wait(0.6)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class WhyVerificationWorks(Scene):
    """Why Schnorr verification works"""

    def construct(self):
        # Title
        title = Text("Why Does Schnorr Verification Work?", color=WHITE).scale(0.95)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The proof
        proof = VGroup(
            Text("The Math:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("During Signing:", color=BLUE).scale(0.6),
            MathTex("s = k + e \\cdot d", color=BLUE).scale(0.6),
            Text("", color=GRAY).scale(0.1),

            Text("Multiply both sides by G:", color=GREEN).scale(0.6),
            MathTex("s \\cdot G = (k + e \\cdot d) \\cdot G", color=GREEN).scale(0.6),
            MathTex("s \\cdot G = k \\cdot G + e \\cdot d \\cdot G", color=GREEN).scale(0.6),
            Text("", color=GRAY).scale(0.1),

            Text("Substitute R = k·G and P = d·G:", color=ORANGE).scale(0.6),
            MathTex("s \\cdot G = R + e \\cdot P", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("This is exactly the verification equation!", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        proof.scale(0.9).move_to(ORIGIN)

        for line in proof:
            self.play(FadeIn(line), run_time=0.6)
            self.wait(0.6)

        self.wait(3)

        # Insight
        insight = Text("Much simpler than ECDSA!", color=GREEN).scale(0.6)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(proof),
            FadeOut(insight),
            FadeOut(title),
            run_time=1
        )


class LinearityProperty(Scene):
    """Explain the linearity property"""

    def construct(self):
        # Title
        title = Text("Linearity: The Secret Sauce", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is linearity
        what_is_it = VGroup(
            Text("What is Linearity?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Schnorr signatures are additive:", color=BLUE).scale(0.6),
            MathTex("\\text{sig}(m, d_1 + d_2) = \\text{sig}_1 + \\text{sig}_2", color=BLUE).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("You can add:", color=GREEN).scale(0.6),
            Text("• Public keys: P₁ + P₂", color=GREEN).scale(0.5),
            Text("• Signatures: s₁ + s₂", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 0.8)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Why it matters
        why_matters = VGroup(
            Text("Why Does This Matter?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Multi-signature wallets", color=GREEN).scale(0.6),
            Text("✓ Signature aggregation", color=GREEN).scale(0.6),
            Text("✓ Key aggregation", color=GREEN).scale(0.6),
            Text("✓ Privacy improvements", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        why_matters.shift(DOWN * 1.2)

        self.play(FadeIn(why_matters), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(why_matters),
            FadeOut(title),
            run_time=1
        )


class BitcoinSchnorr(Scene):
    """Schnorr in Bitcoin"""

    def construct(self):
        # Title
        title = Text("Schnorr in Bitcoin", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # History
        history = VGroup(
            Text("History:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• 2008: Bitcoin launched with ECDSA", color=GRAY).scale(0.5),
            Text("• 2015: Pieter Wuille proposes Schnorr for Bitcoin", color=GRAY).scale(0.5),
            Text("• 2021: Taproot upgrade adds Schnorr", color=GREEN).scale(0.5),
            Text("• Now: Both ECDSA and Schnorr supported", color=BLUE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        history.shift(UP * 1.2)

        for line in history:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # BIP 340
        bip340 = VGroup(
            Text("BIP 340: Schnorr for Bitcoin", color=BLUE).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Specifications:", color=YELLOW).scale(0.6),
            Text("• Uses secp256k1 curve", color=GRAY).scale(0.5),
            Text("• 64-byte signatures", color=GRAY).scale(0.5),
            Text("• Deterministic nonces (like RFC 6979)", color=GRAY).scale(0.5),
            Text("• Batch verification support", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        bip340.shift(DOWN * 0.8)

        self.play(FadeIn(bip340), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(history),
            FadeOut(bip340),
            FadeOut(title),
            run_time=1
        )


class SchnorrSummary(Scene):
    """Summary of Schnorr signatures"""

    def construct(self):
        # Title
        title = Text("Schnorr Signatures: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Simpler than ECDSA: s = k + e·d", color=BLUE).scale(0.6),
            Text("✓ Smaller: 64 bytes vs 71-73 bytes", color=GREEN).scale(0.6),
            Text("✓ Linear: Enables aggregation", color=YELLOW).scale(0.6),
            Text("✓ Verification: sG = R + eP", color=ORANGE).scale(0.6),
            Text("✓ Bitcoin: Added in Taproot (2021)", color=PURPLE).scale(0.6),
            Text("✓ Provably secure", color=RED).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Schnorr aggregation and multi-signatures",
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
