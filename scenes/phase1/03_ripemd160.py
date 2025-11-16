"""
Module 1.3: RIPEMD-160
Topics: RIPEMD-160 and its use in Bitcoin addresses
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
# Add repository root to path for components module
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components import HashMachine, DataBox, HashVisualization

# Configure background
config.background_color = "#1e1e1e"


class RIPEMD160Introduction(Scene):
    """Introduction to RIPEMD-160"""

    def construct(self):
        # Title
        title = Text("RIPEMD-160", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("RACE Integrity Primitives Evaluation Message Digest", color=GRAY).scale(0.5)
        subtitle.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Key facts
        facts = VGroup(
            Text("• Produces 160-bit (20-byte) hash", color=BLUE).scale(0.6),
            Text("• Shorter than SHA-256 (saves space)", color=GREEN).scale(0.6),
            Text("• Used in Bitcoin for address generation", color=YELLOW).scale(0.6),
            Text("• Part of Hash160 function", color=ORANGE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        facts.move_to(ORIGIN)

        for fact in facts:
            self.play(FadeIn(fact), run_time=0.8)
            self.wait(1)

        self.wait(2)

        # Clear
        self.play(FadeOut(facts), FadeOut(subtitle), FadeOut(title), run_time=1)


class Hash160Explanation(Scene):
    """Explain Hash160 = RIPEMD160(SHA256(data))"""

    def construct(self):
        # Title
        title = Text("Hash160 Function", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Formula
        formula = Text("Hash160(x) = RIPEMD160(SHA256(x))", color=YELLOW).scale(0.8)
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula), run_time=1)
        self.wait(2)

        # Explanation
        explanation = VGroup(
            Text("Two-step hashing process:", color=GRAY).scale(0.6),
            Text("1. First apply SHA-256", color=BLUE).scale(0.5),
            Text("2. Then apply RIPEMD-160 to result", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.shift(UP * 0.5)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(1)

        self.wait(1)

        # Why?
        why = VGroup(
            Text("Why two hash functions?", color=YELLOW).scale(0.6),
            Text("• Defense in depth (if one breaks, other still secure)", color=GRAY).scale(0.5),
            Text("• Shorter addresses (160 bits vs 256 bits)", color=GRAY).scale(0.5),
            Text("• Industry standard for Bitcoin addresses", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        why.shift(DOWN * 1.2)

        self.play(FadeIn(why), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(explanation),
            FadeOut(why),
            FadeOut(formula),
            FadeOut(title),
            run_time=1
        )


class Hash160Visualization(Scene):
    """Visualize Hash160 process"""

    def construct(self):
        # Title
        title = Text("Hash160 Process", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Input (public key)
        input_data = "Public Key (33 or 65 bytes)"
        input_box = DataBox(input_data, color=BLUE)
        input_box.shift(LEFT * 5)

        # Step 1: SHA-256
        sha256_machine = HashMachine(label="SHA-256", machine_color=BLUE_D)
        sha256_machine.scale(0.8).shift(LEFT * 1.5)

        # Intermediate result
        intermediate = DataBox("256-bit hash", color=PURPLE)
        intermediate.scale(0.8).shift(RIGHT * 1.5)

        # Step 2: RIPEMD-160
        ripemd_machine = HashMachine(label="RIPEMD-160", machine_color=GREEN_D)
        ripemd_machine.scale(0.8).shift(RIGHT * 1.5 + DOWN * 2.5)

        # Final output
        output_box = DataBox("160-bit Hash160", color=GREEN)
        output_box.shift(RIGHT * 5 + DOWN * 2.5)

        # Arrows
        arrow1 = Arrow(input_box.get_right(), sha256_machine.get_input_pos(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(sha256_machine.get_output_pos(), intermediate.get_left(), buff=0.1, color=YELLOW)
        arrow3 = Arrow(intermediate.get_bottom(), ripemd_machine.get_input_pos(), buff=0.1, color=YELLOW)
        arrow4 = Arrow(ripemd_machine.get_output_pos(), output_box.get_left(), buff=0.1, color=YELLOW)

        # Animate
        self.play(FadeIn(input_box), run_time=0.5)
        self.wait(0.5)

        self.play(Create(arrow1), FadeIn(sha256_machine), run_time=1)
        self.wait(0.5)

        self.play(Create(arrow2), FadeIn(intermediate), run_time=1)
        self.wait(1)

        self.play(Create(arrow3), FadeIn(ripemd_machine), run_time=1)
        self.wait(0.5)

        self.play(Create(arrow4), FadeIn(output_box), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(input_box),
            FadeOut(sha256_machine),
            FadeOut(intermediate),
            FadeOut(ripemd_machine),
            FadeOut(output_box),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(title),
            run_time=1
        )


class BitcoinAddressGeneration(Scene):
    """Show Bitcoin address generation flow"""

    def construct(self):
        # Title
        title = Text("Bitcoin Address Generation", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup()

        step1 = VGroup(
            Text("1. Start with Public Key", color=BLUE).scale(0.6),
            Text("(from ECDSA key pair)", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        step2 = VGroup(
            Text("2. Apply SHA-256", color=GREEN).scale(0.6),
            Text("→ 256-bit hash", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        step3 = VGroup(
            Text("3. Apply RIPEMD-160", color=YELLOW).scale(0.6),
            Text("→ 160-bit Hash160", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        step4 = VGroup(
            Text("4. Add Version Byte", color=ORANGE).scale(0.6),
            Text("(0x00 for mainnet P2PKH)", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        step5 = VGroup(
            Text("5. Add Checksum", color=PURPLE).scale(0.6),
            Text("(first 4 bytes of double SHA-256)", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        step6 = VGroup(
            Text("6. Encode with Base58", color=RED).scale(0.6),
            Text("→ Bitcoin Address", color=GRAY).scale(0.4)
        ).arrange(DOWN, buff=0.1)

        steps.add(step1, step2, step3, step4, step5, step6)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.shift(DOWN * 0.2)

        # Animate steps
        for step in steps:
            self.play(FadeIn(step), run_time=0.8)
            self.wait(1)

        self.wait(2)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class AddressExample(Scene):
    """Show example Bitcoin address"""

    def construct(self):
        # Title
        title = Text("Example Bitcoin Address", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Example address
        example = VGroup(
            Text("Public Key:", color=BLUE).scale(0.5),
            Text("0279BE667EF9DCBBAC55A06295CE870B...", color=GRAY).scale(0.4),
            Text("↓", color=YELLOW).scale(0.6),
            Text("Hash160:", color=GREEN).scale(0.5),
            Text("751e76e8199196d454941c45d1b3a323f1433bd6", color=GRAY).scale(0.4),
            Text("↓", color=YELLOW).scale(0.6),
            Text("Bitcoin Address (P2PKH):", color=ORANGE).scale(0.5),
            Text("1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH", color=WHITE).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        example.move_to(ORIGIN)

        # Show components
        for component in example:
            self.play(FadeIn(component), run_time=0.6)
            self.wait(0.5)

        self.wait(2)

        # Note
        note = Text(
            "Address format: Human-readable, error-checking (checksum)",
            color=YELLOW
        ).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(FadeOut(example), FadeOut(note), FadeOut(title), run_time=1)


class RIPEMD160Summary(Scene):
    """Summary of RIPEMD-160"""

    def construct(self):
        # Title
        title = Text("RIPEMD-160: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ 160-bit hash function (20 bytes)", color=BLUE).scale(0.6),
            Text("✓ Combined with SHA-256 in Hash160", color=GREEN).scale(0.6),
            Text("✓ Core component of Bitcoin addresses", color=YELLOW).scale(0.6),
            Text("✓ Provides shorter addresses than SHA-256 alone", color=ORANGE).scale(0.6),
            Text("✓ Part of defense-in-depth security", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Note
        note = Text(
            "Next: Merkle Trees - organizing transactions in blocks",
            color=GRAY
        ).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=1)
        self.wait(2)

        # Final fade out
        self.play(
            FadeOut(summary),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )
        self.wait(1)
