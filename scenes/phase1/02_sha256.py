"""
Module 1.2: SHA-256 Deep Dive
Topics: SHA-256 algorithm internals, block diagram, compression function, message scheduling
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
sys.path.append('/home/user/manim-learning')
from components import HashMachine, DataBox

# Configure background
config.background_color = "#1e1e1e"


class SHA256Introduction(Scene):
    """Introduction to SHA-256"""

    def construct(self):
        # Title
        title = Text("SHA-256: Secure Hash Algorithm", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key facts
        facts = VGroup(
            Text("• Part of SHA-2 family (designed by NSA)", color=GRAY).scale(0.6),
            Text("• Produces 256-bit (32-byte) hash", color=BLUE).scale(0.6),
            Text("• Used in Bitcoin for mining and addresses", color=GREEN).scale(0.6),
            Text("• Considered cryptographically secure", color=YELLOW).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        facts.move_to(ORIGIN)

        for fact in facts:
            self.play(FadeIn(fact), run_time=0.8)
            self.wait(1)

        self.wait(2)

        # Clear
        self.play(FadeOut(facts), FadeOut(title), run_time=1)


class SHA256Overview(Scene):
    """High-level overview of SHA-256 process"""

    def construct(self):
        # Title
        title = Text("SHA-256 Process Overview", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup()

        step1 = VGroup(
            Text("1. Preprocessing", color=BLUE).scale(0.7),
            Text("• Pad message to multiple of 512 bits", color=GRAY).scale(0.5),
            Text("• Append length of original message", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        step2 = VGroup(
            Text("2. Initialize Hash Values", color=GREEN).scale(0.7),
            Text("• 8 initial hash values (H0-H7)", color=GRAY).scale(0.5),
            Text("• Derived from square roots of primes", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        step3 = VGroup(
            Text("3. Process Each 512-bit Block", color=YELLOW).scale(0.7),
            Text("• 64 rounds of compression function", color=GRAY).scale(0.5),
            Text("• Uses message schedule (W0-W63)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        step4 = VGroup(
            Text("4. Produce Final Hash", color=ORANGE).scale(0.7),
            Text("• Concatenate final hash values", color=GRAY).scale(0.5),
            Text("• Result: 256-bit hash", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        steps.add(step1, step2, step3, step4)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        steps.shift(DOWN * 0.5)

        # Show steps
        for step in steps:
            self.play(FadeIn(step), run_time=1)
            self.wait(1.5)

        self.wait(2)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class MessagePadding(Scene):
    """Demonstrate message padding"""

    def construct(self):
        # Title
        title = Text("Step 1: Message Padding", color=BLUE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Original message
        message = "Hello"
        message_bits = len(message) * 8  # 40 bits

        original = VGroup(
            Text("Original Message:", color=GRAY).scale(0.6),
            Text(f'"{message}" ({message_bits} bits)', color=WHITE).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        original.shift(UP * 2)

        self.play(FadeIn(original), run_time=1)
        self.wait(1)

        # Padding explanation
        padding_steps = VGroup(
            Text("1. Append bit '1'", color=YELLOW).scale(0.5),
            Text("2. Append zeros until length ≡ 448 (mod 512)", color=YELLOW).scale(0.5),
            Text("3. Append 64-bit message length", color=YELLOW).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        padding_steps.move_to(ORIGIN)

        for step in padding_steps:
            self.play(FadeIn(step), run_time=0.8)
            self.wait(1)

        self.wait(1)

        # Result
        result = VGroup(
            Text("Padded Message:", color=GRAY).scale(0.6),
            Text("512 bits (one block)", color=GREEN).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        result.shift(DOWN * 2)

        self.play(FadeIn(result), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(original),
            FadeOut(padding_steps),
            FadeOut(result),
            FadeOut(title),
            run_time=1
        )


class InitialHashValues(Scene):
    """Show initial hash values"""

    def construct(self):
        # Title
        title = Text("Step 2: Initial Hash Values", color=GREEN).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Explanation
        explanation = Text(
            "8 initial values derived from fractional parts of square roots of first 8 primes",
            color=GRAY
        ).scale(0.5)
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(2)

        # Initial values (actual SHA-256 constants)
        initial_values = VGroup(
            Text("H0 = 0x6a09e667", color=BLUE).scale(0.5),
            Text("H1 = 0xbb67ae85", color=BLUE).scale(0.5),
            Text("H2 = 0x3c6ef372", color=BLUE).scale(0.5),
            Text("H3 = 0xa54ff53a", color=BLUE).scale(0.5),
            Text("H4 = 0x510e527f", color=BLUE).scale(0.5),
            Text("H5 = 0x9b05688c", color=BLUE).scale(0.5),
            Text("H6 = 0x1f83d9ab", color=BLUE).scale(0.5),
            Text("H7 = 0x5be0cd19", color=BLUE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        initial_values.shift(DOWN * 0.3)

        # Show in two columns
        col1 = VGroup(initial_values[0], initial_values[1], initial_values[2], initial_values[3])
        col2 = VGroup(initial_values[4], initial_values[5], initial_values[6], initial_values[7])

        col1.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(LEFT * 2)
        col2.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(RIGHT * 2)

        self.play(FadeIn(col1), FadeIn(col2), run_time=1)
        self.wait(2)

        # Note
        note = Text(
            "These values are constant for all SHA-256 computations",
            color=YELLOW
        ).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(col1),
            FadeOut(col2),
            FadeOut(note),
            FadeOut(explanation),
            FadeOut(title),
            run_time=1
        )


class CompressionFunction(Scene):
    """Visualize compression function"""

    def construct(self):
        # Title
        title = Text("Step 3: Compression Function", color=YELLOW).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("64 rounds of processing per 512-bit block", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)

        # Working variables
        var_label = Text("Working Variables (32-bit each):", color=BLUE).scale(0.6)
        var_label.shift(UP * 1.5)

        variables = VGroup(
            Text("a, b, c, d, e, f, g, h", color=WHITE).scale(0.7)
        )
        variables.next_to(var_label, DOWN, buff=0.3)

        self.play(FadeIn(var_label), FadeIn(variables), run_time=1)
        self.wait(1)

        # Round function description
        round_desc = VGroup(
            Text("Each round:", color=GREEN).scale(0.6),
            Text("• Calculate T1 = h + Σ1(e) + Ch(e,f,g) + K[t] + W[t]", color=GRAY).scale(0.45),
            Text("• Calculate T2 = Σ0(a) + Maj(a,b,c)", color=GRAY).scale(0.45),
            Text("• Update variables: h=g, g=f, f=e, e=d+T1", color=GRAY).scale(0.45),
            Text("                    d=c, c=b, b=a, a=T1+T2", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        round_desc.shift(DOWN * 0.5)

        self.play(FadeIn(round_desc), run_time=1)
        self.wait(3)

        # Note about functions
        note = Text(
            "Σ0, Σ1: Bitwise rotation and XOR operations",
            color=YELLOW
        ).scale(0.5)
        note.to_edge(DOWN, buff=0.5)

        note2 = Text(
            "Ch, Maj: Bitwise choice and majority functions",
            color=YELLOW
        ).scale(0.5)
        note2.next_to(note, UP, buff=0.2)

        self.play(FadeIn(note2), FadeIn(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(var_label),
            FadeOut(variables),
            FadeOut(round_desc),
            FadeOut(note),
            FadeOut(note2),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class MessageSchedule(Scene):
    """Visualize message schedule"""

    def construct(self):
        # Title
        title = Text("Message Schedule", color=ORANGE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Explanation
        explanation = Text(
            "Expands 512-bit block into 64 words (W0-W63) of 32 bits each",
            color=GRAY
        ).scale(0.6)
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(2)

        # First 16 words
        first_16 = VGroup(
            Text("W[0] to W[15]:", color=BLUE).scale(0.6),
            Text("Directly from the 512-bit message block", color=WHITE).scale(0.5),
            Text("(16 words × 32 bits = 512 bits)", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        first_16.shift(UP * 1)

        self.play(FadeIn(first_16), run_time=1)
        self.wait(2)

        # Remaining words
        remaining = VGroup(
            Text("W[16] to W[63]:", color=GREEN).scale(0.6),
            Text("Calculated using formula:", color=WHITE).scale(0.5),
            Text("W[t] = σ1(W[t-2]) + W[t-7] + σ0(W[t-15]) + W[t-16]", color=YELLOW).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        remaining.shift(DOWN * 0.5)

        self.play(FadeIn(remaining), run_time=1)
        self.wait(2)

        # Note about sigma functions
        note = Text(
            "σ0, σ1: Bitwise rotation and XOR operations (different from Σ)",
            color=ORANGE
        ).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(first_16),
            FadeOut(remaining),
            FadeOut(note),
            FadeOut(explanation),
            FadeOut(title),
            run_time=1
        )


class FinalHash(Scene):
    """Show final hash production"""

    def construct(self):
        # Title
        title = Text("Step 4: Produce Final Hash", color=PURPLE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Process
        process = VGroup(
            Text("After processing all blocks:", color=GRAY).scale(0.6),
            Text("• Add final working variables to hash values", color=WHITE).scale(0.5),
            Text("• H0 = H0 + a", color=BLUE).scale(0.45),
            Text("• H1 = H1 + b", color=BLUE).scale(0.45),
            Text("• ... (H2 through H7)", color=BLUE).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        process.shift(UP * 1)

        self.play(FadeIn(process), run_time=1)
        self.wait(2)

        # Final concatenation
        concat = VGroup(
            Text("Concatenate all hash values:", color=GREEN).scale(0.6),
            Text("Hash = H0 || H1 || H2 || H3 || H4 || H5 || H6 || H7", color=YELLOW).scale(0.5)
        ).arrange(DOWN, buff=0.2)
        concat.shift(DOWN * 0.5)

        self.play(FadeIn(concat), run_time=1)
        self.wait(2)

        # Result
        result = VGroup(
            Text("Result:", color=WHITE).scale(0.6),
            Text("256-bit (32-byte) hash value", color=GREEN).scale(0.5),
            Text("Typically displayed as 64 hexadecimal characters", color=GRAY).scale(0.45)
        ).arrange(DOWN, buff=0.2)
        result.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(result), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(process),
            FadeOut(concat),
            FadeOut(result),
            FadeOut(title),
            run_time=1
        )


class SHA256BlockDiagram(Scene):
    """Simple block diagram of SHA-256"""

    def construct(self):
        # Title
        title = Text("SHA-256 Block Diagram", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create simple flow diagram
        # Input
        input_box = Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.3)
        input_label = Text("Message", color=WHITE).scale(0.5)
        input_label.move_to(input_box.get_center())
        input_group = VGroup(input_box, input_label)
        input_group.shift(LEFT * 4 + UP * 1.5)

        # Padding
        pad_box = Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.3)
        pad_label = Text("Padding", color=WHITE).scale(0.5)
        pad_label.move_to(pad_box.get_center())
        pad_group = VGroup(pad_box, pad_label)
        pad_group.shift(LEFT * 4 + DOWN * 0.5)

        # 512-bit blocks
        blocks_box = Rectangle(width=2, height=1, color=YELLOW, fill_opacity=0.3)
        blocks_label = Text("512-bit\nBlocks", color=BLACK).scale(0.4)
        blocks_label.move_to(blocks_box.get_center())
        blocks_group = VGroup(blocks_box, blocks_label)
        blocks_group.shift(LEFT * 1)

        # Compression
        comp_box = Rectangle(width=2.5, height=2, color=ORANGE, fill_opacity=0.3)
        comp_label = Text("64 Rounds\nCompression", color=WHITE).scale(0.5)
        comp_label.move_to(comp_box.get_center())
        comp_group = VGroup(comp_box, comp_label)
        comp_group.shift(RIGHT * 2)

        # Output
        output_box = Rectangle(width=2, height=1, color=PURPLE, fill_opacity=0.3)
        output_label = Text("256-bit\nHash", color=WHITE).scale(0.5)
        output_label.move_to(output_box.get_center())
        output_group = VGroup(output_box, output_label)
        output_group.shift(RIGHT * 5)

        # Arrows
        arrow1 = Arrow(input_group.get_bottom(), pad_group.get_top(), buff=0.1, color=GRAY)
        arrow2 = Arrow(pad_group.get_right(), blocks_group.get_left(), buff=0.1, color=GRAY)
        arrow3 = Arrow(blocks_group.get_right(), comp_group.get_left(), buff=0.1, color=GRAY)
        arrow4 = Arrow(comp_group.get_right(), output_group.get_left(), buff=0.1, color=GRAY)

        # Animate construction
        self.play(FadeIn(input_group), run_time=0.8)
        self.wait(0.5)
        self.play(Create(arrow1), FadeIn(pad_group), run_time=0.8)
        self.wait(0.5)
        self.play(Create(arrow2), FadeIn(blocks_group), run_time=0.8)
        self.wait(0.5)
        self.play(Create(arrow3), FadeIn(comp_group), run_time=0.8)
        self.wait(0.5)
        self.play(Create(arrow4), FadeIn(output_group), run_time=0.8)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(input_group),
            FadeOut(pad_group),
            FadeOut(blocks_group),
            FadeOut(comp_group),
            FadeOut(output_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(title),
            run_time=1
        )


class SHA256Summary(Scene):
    """Summary of SHA-256"""

    def construct(self):
        # Title
        title = Text("SHA-256: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Industry-standard cryptographic hash", color=BLUE).scale(0.6),
            Text("✓ Always produces 256-bit output", color=GREEN).scale(0.6),
            Text("✓ Uses 64 rounds of compression per block", color=YELLOW).scale(0.6),
            Text("✓ Relies on bitwise operations (fast & secure)", color=ORANGE).scale(0.6),
            Text("✓ Foundation of Bitcoin's security", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Use case
        use_case = Text(
            "Used in Bitcoin for: Mining (PoW), Address Generation, Merkle Trees",
            color=GRAY
        ).scale(0.5)
        use_case.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(use_case), run_time=1)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(summary),
            FadeOut(use_case),
            FadeOut(title),
            run_time=1
        )
        self.wait(1)
