"""
Module 1.14: Base58 & Bech32 Encoding
Topics: Bitcoin address formats, Base58Check, Bech32, QR code-friendly properties
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
sys.path.append('/home/user/manim-learning')
from components import DataBox

# Configure background
config.background_color = "#1e1e1e"


class EncodingIntroduction(Scene):
    """Introduction to encoding in Bitcoin"""

    def construct(self):
        # Title
        title = Text("Bitcoin Address Encoding", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The problem
        problem = VGroup(
            Text("The Problem:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Public key hash:", color=BLUE).scale(0.6),
            Text("0x1a2b3c4d5e6f7890abcdef...", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Issues:", color=RED).scale(0.6),
            Text("• Hard to read", color=RED).scale(0.5),
            Text("• Easy to mistype", color=RED).scale(0.5),
            Text("• No error detection", color=RED).scale(0.5),
            Text("• Not user-friendly", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 0.5)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The solution
        solution = VGroup(
            Text("Solution: Encoding Schemes", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Base58Check (legacy)", color=GREEN).scale(0.6),
            Text("• Bech32 (SegWit)", color=GREEN).scale(0.6),
            Text("• Human-readable", color=GREEN).scale(0.5),
            Text("• Error detection", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        solution.shift(DOWN * 1.5)

        self.play(FadeIn(solution), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(solution),
            FadeOut(title),
            run_time=1
        )


class Base58Introduction(Scene):
    """Introduction to Base58 encoding"""

    def construct(self):
        # Title
        title = Text("Base58 Encoding", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is it
        what_is_it = VGroup(
            Text("What is Base58?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Like Base64, but removes:", color=BLUE).scale(0.6),
            Text("• 0 (zero) - looks like O", color=RED).scale(0.5),
            Text("• O (capital O) - looks like 0", color=RED).scale(0.5),
            Text("• I (capital i) - looks like l", color=RED).scale(0.5),
            Text("• l (lowercase L) - looks like I", color=RED).scale(0.5),
            Text("• + and / - special characters", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 1)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Alphabet
        alphabet = VGroup(
            Text("Base58 Alphabet:", color=GREEN).scale(0.7),
            Text("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz", color=GREEN).scale(0.45)
        ).arrange(DOWN, buff=0.3)
        alphabet.shift(DOWN * 1.5)

        self.play(FadeIn(alphabet), run_time=1)
        self.wait(2)

        # Note
        note = Text("58 characters, no ambiguous ones", color=BLUE).scale(0.5)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(alphabet),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class Base58CheckEncoding(Scene):
    """Base58Check encoding process"""

    def construct(self):
        # Title
        title = Text("Base58Check Encoding", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Steps
        steps = VGroup(
            Text("Encoding Process:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Step 1: Add version byte", color=BLUE).scale(0.6),
            Text("version + payload", color=GRAY).scale(0.5),
            Text("(e.g., 0x00 for P2PKH mainnet)", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Step 2: Compute checksum", color=GREEN).scale(0.6),
            Text("checksum = SHA256(SHA256(version + payload))[0:4]", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Step 3: Concatenate", color=ORANGE).scale(0.6),
            Text("version + payload + checksum", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Step 4: Encode in Base58", color=PURPLE).scale(0.6),
            Text("Convert to Base58 string", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Result: Bitcoin address!", color=GREEN).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        steps.scale(0.85).move_to(ORIGIN)

        for line in steps:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(steps), FadeOut(title), run_time=1)


class Base58Example(Scene):
    """Example of Base58Check encoding"""

    def construct(self):
        # Title
        title = Text("Base58Check Example", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Example flow
        example = VGroup(
            Text("Example:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("1. Public key hash (160 bits):", color=BLUE).scale(0.6),
            Text("62e907b15cbf27d5425399ebf6f0fb50ebb88f18", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("2. Add version (0x00 for mainnet P2PKH):", color=GREEN).scale(0.6),
            Text("0062e907b15cbf27d5425399ebf6f0fb50ebb88f18", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("3. Compute checksum:", color=ORANGE).scale(0.6),
            Text("SHA256(SHA256(...)) = c3c901da...", color=GRAY).scale(0.45),
            Text("Checksum (first 4 bytes): c3c901da", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("4. Concatenate:", color=PURPLE).scale(0.6),
            Text("0062e907b15cbf27d5425399ebf6f0fb50ebb88f18c3c901da", color=GRAY).scale(0.4),
            Text("", color=GRAY).scale(0.1),

            Text("5. Base58 encode:", color=GREEN).scale(0.6),
            Text("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        example.scale(0.8).move_to(ORIGIN)

        for line in example:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Note
        note = Text("This is Satoshi's address!", color=YELLOW).scale(0.6)
        note.to_edge(DOWN, buff=0.3)
        self.play(Write(note), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(example),
            FadeOut(note),
            FadeOut(title),
            run_time=1
        )


class AddressTypes(Scene):
    """Different Bitcoin address types"""

    def construct(self):
        # Title
        title = Text("Bitcoin Address Types", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Types
        types = VGroup(
            Text("Legacy Addresses (Base58Check):", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("P2PKH (Pay to Public Key Hash):", color=BLUE).scale(0.6),
            Text("• Starts with '1'", color=GRAY).scale(0.5),
            Text("• Example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", color=GRAY).scale(0.4),
            Text("", color=GRAY).scale(0.1),

            Text("P2SH (Pay to Script Hash):", color=GREEN).scale(0.6),
            Text("• Starts with '3'", color=GRAY).scale(0.5),
            Text("• Example: 3J98t1WpEZ73CNmYviecrnyiWrnqRhWNLy", color=GRAY).scale(0.4),
            Text("• Used for multi-sig, SegWit", color=GRAY).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("SegWit Addresses (Bech32):", color=ORANGE).scale(0.6),
            Text("• Starts with 'bc1'", color=GRAY).scale(0.5),
            Text("• Example: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", color=GRAY).scale(0.4),
            Text("• Lowercase, error detection", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        types.scale(0.85).move_to(ORIGIN)

        for line in types:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(types), FadeOut(title), run_time=1)


class Bech32Introduction(Scene):
    """Introduction to Bech32 encoding"""

    def construct(self):
        # Title
        title = Text("Bech32: Next Generation Encoding", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What is it
        what_is_it = VGroup(
            Text("What is Bech32?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Developed for SegWit (BIP 173)", color=BLUE).scale(0.6),
            Text("• Better error detection than Base58", color=GREEN).scale(0.6),
            Text("• All lowercase (easier to type)", color=GREEN).scale(0.6),
            Text("• QR code friendly", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what_is_it.shift(UP * 1.2)

        for line in what_is_it:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Advantages
        advantages = VGroup(
            Text("Advantages over Base58Check:", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ Better error detection (up to 4 errors)", color=GREEN).scale(0.6),
            Text("✓ Case-insensitive", color=GREEN).scale(0.6),
            Text("✓ Shorter QR codes", color=GREEN).scale(0.6),
            Text("✓ Separator for human-readable part", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        advantages.shift(DOWN * 1)

        self.play(FadeIn(advantages), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(what_is_it),
            FadeOut(advantages),
            FadeOut(title),
            run_time=1
        )


class Bech32Format(Scene):
    """Bech32 address format"""

    def construct(self):
        # Title
        title = Text("Bech32 Format", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Format
        format_text = VGroup(
            Text("Format:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("[human-readable part] + [separator] + [data] + [checksum]", color=BLUE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        format_text.shift(UP * 2)

        self.play(FadeIn(format_text), run_time=1)
        self.wait(1.5)

        # Example breakdown
        example = Text("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", color=GREEN).scale(0.6)
        example.shift(UP * 0.8)

        self.play(Write(example), run_time=1)
        self.wait(1)

        # Parts
        hrp = VGroup(
            Text("bc", color=BLUE).scale(0.7),
            Text("Human-Readable Part", color=BLUE).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        hrp.shift(LEFT * 5 + DOWN * 0.3)

        separator = VGroup(
            Text("1", color=YELLOW).scale(0.7),
            Text("Separator", color=YELLOW).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        separator.shift(LEFT * 3 + DOWN * 0.3)

        witness_ver = VGroup(
            Text("q", color=ORANGE).scale(0.7),
            Text("Witness v0", color=ORANGE).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        witness_ver.shift(LEFT * 1 + DOWN * 0.3)

        data = VGroup(
            Text("w508d6qejxtdg4y5r3zarvary0c5xw7", color=GREEN).scale(0.5),
            Text("Data (32 bytes)", color=GREEN).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        data.shift(RIGHT * 2.2 + DOWN * 0.3)

        checksum = VGroup(
            Text("kv8f3t4", color=PURPLE).scale(0.6),
            Text("Checksum", color=PURPLE).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        checksum.shift(RIGHT * 5.5 + DOWN * 0.3)

        parts = [hrp, separator, witness_ver, data, checksum]
        for part in parts:
            self.play(FadeIn(part), run_time=0.8)
            self.wait(0.8)

        self.wait(3)

        # Explanation
        explanation = VGroup(
            Text("'bc' = Bitcoin mainnet", color=BLUE).scale(0.5),
            Text("'1' = Always the separator", color=YELLOW).scale(0.5),
            Text("'q' = Witness version 0 (SegWit v0)", color=ORANGE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(explanation), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(format_text),
            FadeOut(example),
            *[FadeOut(part) for part in parts],
            FadeOut(explanation),
            FadeOut(title),
            run_time=1
        )


class Bech32ErrorDetection(Scene):
    """Bech32 error detection capabilities"""

    def construct(self):
        # Title
        title = Text("Bech32 Error Detection", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Capabilities
        capabilities = VGroup(
            Text("Error Detection Capabilities:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Guaranteed Detection:", color=GREEN).scale(0.6),
            Text("• Any single character error", color=GREEN).scale(0.5),
            Text("• Any two character errors", color=GREEN).scale(0.5),
            Text("• Any insertion/deletion", color=GREEN).scale(0.5),
            Text("• Up to 4 consecutive errors", color=GREEN).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("Probability of Detection:", color=BLUE).scale(0.6),
            Text("• More errors: 99.9% detection", color=BLUE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        capabilities.shift(UP * 0.5)

        for line in capabilities:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Comparison
        comparison = VGroup(
            Text("vs Base58Check:", color=YELLOW).scale(0.7),
            Text("Base58: ~1 in 4 billion error detection", color=RED).scale(0.5),
            Text("Bech32: Guaranteed for common errors!", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        comparison.shift(DOWN * 1.8)

        self.play(FadeIn(comparison), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(capabilities),
            FadeOut(comparison),
            FadeOut(title),
            run_time=1
        )


class QRCodeFriendly(Scene):
    """Why Bech32 is QR code friendly"""

    def construct(self):
        # Title
        title = Text("QR Code Friendly", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Why it matters
        why = VGroup(
            Text("Why QR Codes Matter for Bitcoin:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• Mobile wallets scan addresses", color=GRAY).scale(0.6),
            Text("• Reduces typing errors", color=GRAY).scale(0.6),
            Text("• Faster payments", color=GRAY).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        why.shift(UP * 1.5)

        for line in why:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Bech32 advantages
        advantages = VGroup(
            Text("Bech32 QR Advantages:", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("✓ All lowercase → Alphanumeric mode", color=GREEN).scale(0.6),
            Text("✓ 45% smaller QR codes", color=GREEN).scale(0.6),
            Text("✓ Easier to scan", color=GREEN).scale(0.6),
            Text("✓ Less data = more reliable", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        advantages.shift(DOWN * 0.5)

        self.play(FadeIn(advantages), run_time=1)
        self.wait(3)

        # Comparison
        comparison = Text(
            "Mixed case (Base58) requires binary mode = larger QR code",
            color=RED
        ).scale(0.5)
        comparison.to_edge(DOWN, buff=0.3)
        self.play(Write(comparison), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(why),
            FadeOut(advantages),
            FadeOut(comparison),
            FadeOut(title),
            run_time=1
        )


class AddressComparison(Scene):
    """Side-by-side comparison of address formats"""

    def construct(self):
        # Title
        title = Text("Address Format Comparison", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Table header
        header = VGroup(
            Text("Feature", color=YELLOW).scale(0.6),
            Text("Base58Check", color=BLUE).scale(0.6),
            Text("Bech32", color=GREEN).scale(0.6)
        ).arrange(RIGHT, buff=2)
        header.shift(UP * 2)

        self.play(Write(header), run_time=1)
        self.wait(1)

        # Rows
        rows_data = [
            ("Error Detection", "Low", "High", RED, GREEN),
            ("Case Sensitive", "Yes", "No", RED, GREEN),
            ("QR Code Size", "Large", "45% smaller", RED, GREEN),
            ("SegWit Support", "Via P2SH", "Native", ORANGE, GREEN),
            ("Address Length", "~34 chars", "~42 chars", GREEN, ORANGE),
            ("Adoption", "Universal", "Growing", GREEN, ORANGE)
        ]

        rows = VGroup()
        y_pos = 0.8
        for feature, base58, bech32, color58, colorbech in rows_data:
            row = VGroup(
                Text(feature, color=WHITE).scale(0.5),
                Text(base58, color=color58).scale(0.5),
                Text(bech32, color=colorbech).scale(0.5)
            ).arrange(RIGHT, buff=2)
            row.shift(UP * y_pos)
            rows.add(row)
            y_pos -= 0.6

        for row in rows:
            self.play(FadeIn(row), run_time=0.7)
            self.wait(0.7)

        self.wait(3)

        # Recommendation
        recommendation = Text(
            "Recommendation: Use Bech32 (bc1...) for new addresses",
            color=GREEN
        ).scale(0.6)
        recommendation.to_edge(DOWN, buff=0.3)
        self.play(Write(recommendation), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(header),
            FadeOut(rows),
            FadeOut(recommendation),
            FadeOut(title),
            run_time=1
        )


class EncodingSummary(Scene):
    """Summary of Bitcoin encoding"""

    def construct(self):
        # Title
        title = Text("Encoding Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Base58: Removes ambiguous characters (0, O, I, l)", color=BLUE).scale(0.6),
            Text("✓ Base58Check: Adds version + checksum", color=GREEN).scale(0.6),
            Text("✓ Legacy addresses: Start with 1 (P2PKH) or 3 (P2SH)", color=YELLOW).scale(0.6),
            Text("✓ Bech32: Better error detection, lowercase", color=ORANGE).scale(0.6),
            Text("✓ SegWit addresses: Start with bc1", color=PURPLE).scale(0.6),
            Text("✓ Bech32 is superior: Use for new addresses", color=GREEN).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Congratulations
        congrats = Text(
            "Phase 1 Complete! You've mastered cryptography fundamentals.",
            color=GREEN
        ).scale(0.6)
        congrats.to_edge(DOWN, buff=0.3)
        self.play(Write(congrats), run_time=1)
        self.wait(3)

        # Final fade out
        self.play(
            FadeOut(summary),
            FadeOut(congrats),
            FadeOut(title),
            run_time=1
        )
        self.wait(1)
