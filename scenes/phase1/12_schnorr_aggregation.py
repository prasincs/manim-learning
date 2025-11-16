"""
Module 1.12: Schnorr Math & Aggregation
Topics: Signature aggregation, MuSig, key aggregation, multi-signature scenarios
Duration: 5-10 minutes
"""

from manim import *
import sys
sys.path.append('/home/user/manim-learning')
from components import KeyPair

# Configure background
config.background_color = "#1e1e1e"


class AggregationIntroduction(Scene):
    """Introduction to signature aggregation"""

    def construct(self):
        # Title
        title = Text("Signature Aggregation", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Combining Multiple Signatures into One", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # The problem
        problem = VGroup(
            Text("The Problem:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Traditional multi-sig:", color=GRAY).scale(0.6),
            Text("• 3 signers → 3 separate signatures", color=RED).scale(0.5),
            Text("• Large transaction size", color=RED).scale(0.5),
            Text("• Privacy leak (reveals multi-sig)", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 0.8)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The solution
        solution = VGroup(
            Text("Schnorr Solution:", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• 3 signers → 1 aggregated signature", color=GREEN).scale(0.5),
            Text("• Same size as single signature!", color=GREEN).scale(0.5),
            Text("• Looks like normal signature (privacy)", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        solution.shift(DOWN * 1)

        self.play(FadeIn(solution), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(solution),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class NaiveAggregation(Scene):
    """Explain naive aggregation and why it fails"""

    def construct(self):
        # Title
        title = Text("Naive Aggregation (DON'T DO THIS)", color=RED).scale(0.95)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Naive approach
        naive = VGroup(
            Text("Naive Approach:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Just add everything:", color=BLUE).scale(0.6),
            MathTex("P_{agg} = P_1 + P_2 + P_3", color=BLUE).scale(0.6),
            MathTex("s_{agg} = s_1 + s_2 + s_3", color=BLUE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        naive.shift(UP * 1.2)

        for line in naive:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The attack
        attack = VGroup(
            Text("Rogue Key Attack:", color=RED).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Attacker Eve:", color=RED).scale(0.6),
            Text("1. Sees Alice's public key P₁", color=GRAY).scale(0.5),
            Text("2. Chooses P₂ = P_Eve - P₁", color=RED).scale(0.5),
            Text("3. Aggregated: P₁ + P₂ = P_Eve", color=RED).scale(0.5),
            Text("4. Eve can now sign alone!", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("BROKEN! ✗", color=RED).scale(0.8)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        attack.shift(DOWN * 0.5)

        self.play(FadeIn(attack), run_time=1)
        self.wait(3)

        # Warning
        warning = Text("Need a better approach!", color=YELLOW).scale(0.6)
        warning.to_edge(DOWN, buff=0.3)
        self.play(Write(warning), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(naive),
            FadeOut(attack),
            FadeOut(warning),
            FadeOut(title),
            run_time=1
        )


class MuSigProtocol(Scene):
    """Introduce MuSig protocol"""

    def construct(self):
        # Title
        title = Text("MuSig: Secure Aggregation", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is MuSig
        what_is_it = VGroup(
            Text("What is MuSig?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Multi-Signature protocol", color=GRAY).scale(0.5),
            Text("• Developed by Maxwell, Poelstra, Seurin, Wuille", color=GRAY).scale(0.5),
            Text("• Secure against rogue key attack", color=GREEN).scale(0.5),
            Text("• Creates single aggregated signature", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 1)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Key idea
        key_idea = VGroup(
            Text("Key Idea:", color=BLUE).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Use coefficients to prevent rogue keys:", color=BLUE).scale(0.6),
            MathTex("P_{agg} = a_1 P_1 + a_2 P_2 + a_3 P_3", color=BLUE).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("where a_i = hash(all public keys, P_i)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        key_idea.shift(DOWN * 0.8)

        self.play(FadeIn(key_idea), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(key_idea),
            FadeOut(title),
            run_time=1
        )


class MuSigKeyAggregation(Scene):
    """MuSig key aggregation process"""

    def construct(self):
        # Title
        title = Text("MuSig: Key Aggregation", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Key Aggregation Process:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Step 1: Collect all public keys", color=BLUE).scale(0.6),
            MathTex("\\{P_1, P_2, ..., P_n\\}", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 2: Compute key hash", color=GREEN).scale(0.6),
            MathTex("L = \\text{hash}(P_1 || P_2 || ... || P_n)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 3: Compute coefficients", color=ORANGE).scale(0.6),
            MathTex("a_i = \\text{hash}(L, P_i)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 4: Aggregate public key", color=PURPLE).scale(0.6),
            MathTex("P_{agg} = \\sum_{i=1}^{n} a_i \\cdot P_i", color=YELLOW).scale(0.6),
            Text("", color=GRAY).scale(0.1),

            Text("Result: Single aggregated public key", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        steps.scale(0.85).move_to(ORIGIN)

        for line in steps:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class MuSigSigning(Scene):
    """MuSig signing process"""

    def construct(self):
        # Title
        title = Text("MuSig: Signing Process", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Phases
        phases = VGroup(
            Text("Three-Round Protocol:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Round 1: Commitment", color=BLUE).scale(0.6),
            Text("• Each signer: Generate random r_i", color=GRAY).scale(0.5),
            Text("• Compute R_i = r_i * G", color=GRAY).scale(0.5),
            Text("• Send hash(R_i) to others (commitment)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Round 2: Nonce Reveal", color=GREEN).scale(0.6),
            Text("• Each signer: Reveal R_i", color=GRAY).scale(0.5),
            Text("• Verify commitments match", color=GRAY).scale(0.5),
            Text("• Compute R_agg = Σ R_i", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Round 3: Partial Signatures", color=ORANGE).scale(0.6),
            Text("• Each signer: Compute e = hash(R_agg || P_agg || m)", color=GRAY).scale(0.5),
            Text("• Compute s_i = r_i + e * a_i * d_i", color=GRAY).scale(0.5),
            Text("• Send s_i to others", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Final: Aggregate", color=PURPLE).scale(0.6),
            Text("• s_agg = Σ s_i", color=GRAY).scale(0.5),
            Text("• Signature = (R_agg, s_agg)", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        phases.scale(0.75).move_to(ORIGIN)

        for line in phases:
            self.play(FadeIn(line), run_time=0.4)
            self.wait(0.4)

        self.wait(3)

        # Clear
        self.play(FadeOut(phases), FadeOut(title), run_time=1)


class MuSigExample(Scene):
    """Example of MuSig with 2 signers"""

    def construct(self):
        # Title
        title = Text("MuSig Example: 2-of-2", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Alice and Bob
        participants = VGroup(
            Text("Alice", color=BLUE).scale(0.7),
            Text("d₁, P₁ = d₁·G", color=BLUE).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        participants.shift(LEFT * 5 + UP * 1.5)

        bob = VGroup(
            Text("Bob", color=GREEN).scale(0.7),
            Text("d₂, P₂ = d₂·G", color=GREEN).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        bob.shift(RIGHT * 5 + UP * 1.5)

        self.play(FadeIn(participants), FadeIn(bob), run_time=1)
        self.wait(1)

        # Process
        process = VGroup(
            Text("1. Key Aggregation:", color=YELLOW).scale(0.6),
            MathTex("a_1 = \\text{hash}(P_1 || P_2, P_1)", color=GRAY).scale(0.45),
            MathTex("a_2 = \\text{hash}(P_1 || P_2, P_2)", color=GRAY).scale(0.45),
            MathTex("P_{agg} = a_1 P_1 + a_2 P_2", color=BLUE).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("2. Signing:", color=YELLOW).scale(0.6),
            Text("Both generate R₁, R₂", color=GRAY).scale(0.45),
            MathTex("R_{agg} = R_1 + R_2", color=GRAY).scale(0.45),
            MathTex("e = \\text{hash}(R_{agg} || P_{agg} || m)", color=GRAY).scale(0.45),
            MathTex("s_1 = r_1 + e \\cdot a_1 \\cdot d_1", color=BLUE).scale(0.45),
            MathTex("s_2 = r_2 + e \\cdot a_2 \\cdot d_2", color=GREEN).scale(0.45),
            MathTex("s_{agg} = s_1 + s_2", color=PURPLE).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Result: (R_agg, s_agg)", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        process.scale(0.8).shift(DOWN * 0.3)

        for line in process:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(
            FadeOut(participants),
            FadeOut(bob),
            FadeOut(process),
            FadeOut(title),
            run_time=1
        )


class BatchVerification(Scene):
    """Batch verification with Schnorr"""

    def construct(self):
        # Title
        title = Text("Batch Verification", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The idea
        idea = VGroup(
            Text("Batch Verification:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Verify multiple signatures at once", color=BLUE).scale(0.6),
            Text("Faster than verifying individually", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        idea.shift(UP * 1.5)

        for line in idea:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # How it works
        how = VGroup(
            Text("How it works:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Instead of:", color=RED).scale(0.6),
            MathTex("s_1 G \\stackrel{?}{=} R_1 + e_1 P_1", color=RED).scale(0.5),
            MathTex("s_2 G \\stackrel{?}{=} R_2 + e_2 P_2", color=RED).scale(0.5),
            MathTex("...", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Verify once:", color=GREEN).scale(0.6),
            MathTex("(s_1 + s_2 + ...) G \\stackrel{?}{=} (R_1 + e_1 P_1) + (R_2 + e_2 P_2) + ...", color=GREEN).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("~2x faster for large batches!", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        how.shift(DOWN * 0.3)

        for line in how:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(
            FadeOut(idea),
            FadeOut(how),
            FadeOut(title),
            run_time=1
        )


class AggregationBenefits(Scene):
    """Benefits of signature aggregation"""

    def construct(self):
        # Title
        title = Text("Aggregation Benefits", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Benefits
        benefits = VGroup(
            Text("Benefits:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("1. Efficiency", color=GREEN).scale(0.6),
            Text("   • n signatures → 1 signature", color=GRAY).scale(0.5),
            Text("   • Smaller transactions", color=GRAY).scale(0.5),
            Text("   • Lower fees", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("2. Privacy", color=GREEN).scale(0.6),
            Text("   • Multi-sig looks like single-sig", color=GRAY).scale(0.5),
            Text("   • Can't tell how many signers", color=GRAY).scale(0.5),
            Text("   • Indistinguishable on chain", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("3. Scalability", color=GREEN).scale(0.6),
            Text("   • More signatures fit in a block", color=GRAY).scale(0.5),
            Text("   • Batch verification possible", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        benefits.scale(0.85).move_to(ORIGIN)

        for line in benefits:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(benefits), FadeOut(title), run_time=1)


class SchnorrAggregationSummary(Scene):
    """Summary of Schnorr aggregation"""

    def construct(self):
        # Title
        title = Text("Schnorr Aggregation: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Linearity enables aggregation", color=BLUE).scale(0.6),
            Text("✓ MuSig: Secure multi-signature protocol", color=GREEN).scale(0.6),
            Text("✓ Key aggregation: Σ aᵢPᵢ", color=YELLOW).scale(0.6),
            Text("✓ Signature aggregation: Σ sᵢ", color=ORANGE).scale(0.6),
            Text("✓ Benefits: Efficiency, privacy, scalability", color=PURPLE).scale(0.6),
            Text("✓ Batch verification: 2x faster", color=RED).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Digital signatures in practice",
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
