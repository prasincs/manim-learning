"""
Module 1.13: Digital Signatures in Practice
Topics: Common pitfalls, nonce reuse attack, best practices, real-world examples
Duration: 5-10 minutes
"""

from manim import *
import sys
sys.path.append('/home/user/manim-learning')
from components import SignatureProcess, VerificationProcess

# Configure background
config.background_color = "#1e1e1e"


class PracticalSignaturesIntro(Scene):
    """Introduction to signatures in practice"""

    def construct(self):
        # Title
        title = Text("Digital Signatures in Practice", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Common Pitfalls and Best Practices", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Overview
        overview = VGroup(
            Text("We've learned the theory...", color=BLUE).scale(0.7),
            Text("Now let's see what can go wrong", color=RED).scale(0.7),
            Text("And how to do it right", color=GREEN).scale(0.7)
        ).arrange(DOWN, buff=0.4)
        overview.move_to(ORIGIN)

        for line in overview:
            self.play(FadeIn(line), run_time=1)
            self.wait(1)

        self.wait(2)

        # Clear
        self.play(
            FadeOut(overview),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class NonceReuseDeepDive(Scene):
    """Deep dive into nonce reuse attack"""

    def construct(self):
        # Title
        title = Text("Nonce Reuse Attack: Deep Dive", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The setup
        setup = VGroup(
            Text("The Setup:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Alice signs two messages with same k:", color=BLUE).scale(0.6),
            MathTex("s_1 = k^{-1}(e_1 + r \\cdot d)", color=GRAY).scale(0.5),
            MathTex("s_2 = k^{-1}(e_2 + r \\cdot d)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Note: Same k → Same r", color=ORANGE).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        setup.shift(UP * 1.3)

        for line in setup:
            self.play(FadeIn(line), run_time=0.7)
            self.wait(0.7)

        self.wait(1)

        # The attack
        attack = VGroup(
            Text("The Attack:", color=RED).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Step 1: Subtract signatures", color=RED).scale(0.6),
            MathTex("s_1 - s_2 = k^{-1}(e_1 - e_2)", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Step 2: Solve for k", color=RED).scale(0.6),
            MathTex("k = (e_1 - e_2)(s_1 - s_2)^{-1}", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Step 3: Recover private key d", color=RED).scale(0.6),
            MathTex("d = r^{-1}(s \\cdot k - e)", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        attack.shift(DOWN * 0.5)

        self.play(FadeIn(attack), run_time=1.5)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(setup),
            FadeOut(attack),
            FadeOut(title),
            run_time=1
        )


class RealWorldNonceFailure(Scene):
    """Real-world example of nonce reuse (PlayStation 3)"""

    def construct(self):
        # Title
        title = Text("Real-World Disaster: PlayStation 3", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The story
        story = VGroup(
            Text("The Incident (2010):", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("• PlayStation 3 used ECDSA for code signing", color=GRAY).scale(0.5),
            Text("• Sony's signing tool had a bug", color=RED).scale(0.5),
            Text("• Used SAME k for different messages", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("The Result:", color=YELLOW).scale(0.7),
            Text("• Hackers recovered Sony's private key", color=RED).scale(0.5),
            Text("• Could sign any code as Sony", color=RED).scale(0.5),
            Text("• PS3 security completely broken", color=RED).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("All because of k reuse!", color=RED).scale(0.8)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        story.scale(0.9).move_to(ORIGIN)

        for line in story:
            self.play(FadeIn(line), run_time=0.6)
            self.wait(0.6)

        self.wait(3)

        # Lesson
        lesson = Text("Lesson: NEVER reuse nonces!", color=RED).scale(0.7)
        lesson.to_edge(DOWN, buff=0.3)
        self.play(Write(lesson), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(story),
            FadeOut(lesson),
            FadeOut(title),
            run_time=1
        )


class BiasedNonces(Scene):
    """Danger of biased or predictable nonces"""

    def construct(self):
        # Title
        title = Text("Predictable Nonces", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The problem
        problem = VGroup(
            Text("Even if k is unique, it must be RANDOM", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Bad examples:", color=RED).scale(0.6),
            Text("• k = 1, 2, 3, 4... (sequential)", color=RED).scale(0.5),
            Text("• k derived from timestamp", color=RED).scale(0.5),
            Text("• k with known bias (some bits zero)", color=RED).scale(0.5),
            Text("• k from weak RNG", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 1)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The attack
        attack = VGroup(
            Text("Attack:", color=RED).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("With partial k knowledge:", color=BLUE).scale(0.6),
            Text("• Lattice attacks can recover d", color=RED).scale(0.5),
            Text("• Can work with just a few bits of bias", color=RED).scale(0.5),
            Text("• Multiple signatures make it easier", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        attack.shift(DOWN * 1.2)

        self.play(FadeIn(attack), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(attack),
            FadeOut(title),
            run_time=1
        )


class WeakRandomness(Scene):
    """Problems with weak random number generation"""

    def construct(self):
        # Title
        title = Text("Weak Random Number Generation", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # The problem
        problem = VGroup(
            Text("RNG Quality Matters!", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Bad sources of randomness:", color=RED).scale(0.6),
            Text("• Current time/timestamp", color=RED).scale(0.5),
            Text("• Process ID", color=RED).scale(0.5),
            Text("• Unseeded PRNG", color=RED).scale(0.5),
            Text("• Predictable system state", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem.shift(UP * 1.2)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Good sources
        good = VGroup(
            Text("Good sources of randomness:", color=GREEN).scale(0.6),
            Text("• /dev/urandom (Linux)", color=GREEN).scale(0.5),
            Text("• CryptGenRandom (Windows)", color=GREEN).scale(0.5),
            Text("• Hardware RNG", color=GREEN).scale(0.5),
            Text("• RFC 6979 (deterministic nonces)", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        good.shift(DOWN * 1)

        self.play(FadeIn(good), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problem),
            FadeOut(good),
            FadeOut(title),
            run_time=1
        )


class SideChannelAttacks(Scene):
    """Side-channel attacks on signature implementations"""

    def construct(self):
        # Title
        title = Text("Side-Channel Attacks", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # What are they
        what = VGroup(
            Text("What are Side-Channels?", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("Information leaked through:", color=BLUE).scale(0.6),
            Text("• Timing (how long operations take)", color=GRAY).scale(0.5),
            Text("• Power consumption", color=GRAY).scale(0.5),
            Text("• Electromagnetic radiation", color=GRAY).scale(0.5),
            Text("• Cache timing", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        what.shift(UP * 1.2)

        for line in what:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # Example
        example = VGroup(
            Text("Example: Timing Attack", color=RED).scale(0.7),
            Text("", color=GRAY).scale(0.1),
            Text("If multiplication time depends on bit value:", color=GRAY).scale(0.5),
            Text("• Measure time for k*G", color=RED).scale(0.5),
            Text("• Infer bits of k", color=RED).scale(0.5),
            Text("• Recover private key", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        example.shift(DOWN * 0.8)

        self.play(FadeIn(example), run_time=1)
        self.wait(3)

        # Mitigation
        mitigation = Text("Mitigation: Constant-time implementations", color=GREEN).scale(0.6)
        mitigation.to_edge(DOWN, buff=0.3)
        self.play(Write(mitigation), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(what),
            FadeOut(example),
            FadeOut(mitigation),
            FadeOut(title),
            run_time=1
        )


class BestPractices(Scene):
    """Best practices for using digital signatures"""

    def construct(self):
        # Title
        title = Text("Best Practices", color=GREEN).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Practices
        practices = VGroup(
            Text("1. Nonce Generation", color=YELLOW).scale(0.6),
            Text("   ✓ Use RFC 6979 (deterministic)", color=GREEN).scale(0.5),
            Text("   ✓ Or use cryptographically secure RNG", color=GREEN).scale(0.5),
            Text("   ✗ Never reuse nonces", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("2. Implementation", color=YELLOW).scale(0.6),
            Text("   ✓ Use well-tested libraries", color=GREEN).scale(0.5),
            Text("   ✓ Constant-time operations", color=GREEN).scale(0.5),
            Text("   ✓ Protect private key in memory", color=GREEN).scale(0.5),
            Text("   ✗ Don't roll your own crypto", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("3. Key Management", color=YELLOW).scale(0.6),
            Text("   ✓ Hardware wallets for Bitcoin", color=GREEN).scale(0.5),
            Text("   ✓ Backup private keys securely", color=GREEN).scale(0.5),
            Text("   ✓ Use multi-sig when possible", color=GREEN).scale(0.5),
            Text("   ✗ Never share private keys", color=RED).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("4. Testing", color=YELLOW).scale(0.6),
            Text("   ✓ Test with known test vectors", color=GREEN).scale(0.5),
            Text("   ✓ Verify signatures after signing", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        practices.scale(0.8).move_to(ORIGIN)

        for line in practices:
            self.play(FadeIn(line), run_time=0.4)
            self.wait(0.4)

        self.wait(3)

        # Clear
        self.play(FadeOut(practices), FadeOut(title), run_time=1)


class LibraryRecommendations(Scene):
    """Recommended libraries for signatures"""

    def construct(self):
        # Title
        title = Text("Recommended Libraries", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Libraries
        libraries = VGroup(
            Text("Use These (Trusted & Audited):", color=GREEN).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("Python:", color=BLUE).scale(0.6),
            Text("• python-bitcoinlib", color=GRAY).scale(0.5),
            Text("• ecdsa (with caution)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("JavaScript:", color=BLUE).scale(0.6),
            Text("• bitcoinjs-lib", color=GRAY).scale(0.5),
            Text("• secp256k1 (noble)", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("C/C++:", color=BLUE).scale(0.6),
            Text("• libsecp256k1 (Bitcoin Core)", color=GREEN).scale(0.5),
            Text("  → The gold standard", color=GREEN).scale(0.45),
            Text("", color=GRAY).scale(0.1),

            Text("Rust:", color=BLUE).scale(0.6),
            Text("• rust-secp256k1", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        libraries.scale(0.9).move_to(ORIGIN)

        for line in libraries:
            self.play(FadeIn(line), run_time=0.5)
            self.wait(0.5)

        self.wait(3)

        # Clear
        self.play(FadeOut(libraries), FadeOut(title), run_time=1)


class CommonMistakes(Scene):
    """Common mistakes to avoid"""

    def construct(self):
        # Title
        title = Text("Common Mistakes to Avoid", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Mistakes
        mistakes = VGroup(
            Text("Don't make these mistakes:", color=YELLOW).scale(0.7),
            Text("", color=GRAY).scale(0.1),

            Text("✗ Signing without verifying", color=RED).scale(0.6),
            Text("  → Always verify your own signatures", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("✗ Trusting signature without checking public key", color=RED).scale(0.6),
            Text("  → Verify the signer is who you expect", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("✗ Not checking signature validity", color=RED).scale(0.6),
            Text("  → Verify r and s are in valid range", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("✗ Reusing addresses in Bitcoin", color=RED).scale(0.6),
            Text("  → Reduces privacy, can leak info", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),

            Text("✗ Storing private keys in plain text", color=RED).scale(0.6),
            Text("  → Always encrypt at rest", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        mistakes.scale(0.85).move_to(ORIGIN)

        for line in mistakes:
            self.play(FadeIn(line), run_time=0.4)
            self.wait(0.4)

        self.wait(3)

        # Clear
        self.play(FadeOut(mistakes), FadeOut(title), run_time=1)


class SignaturesPracticeSummary(Scene):
    """Summary of signatures in practice"""

    def construct(self):
        # Title
        title = Text("Digital Signatures: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Nonce reuse is FATAL", color=RED).scale(0.6),
            Text("✓ Use RFC 6979 or secure RNG", color=GREEN).scale(0.6),
            Text("✓ Beware of side-channel attacks", color=ORANGE).scale(0.6),
            Text("✓ Use trusted, audited libraries", color=BLUE).scale(0.6),
            Text("✓ Constant-time implementations", color=YELLOW).scale(0.6),
            Text("✓ Protect private keys at all costs", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Address encoding - Base58 and Bech32",
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
