"""
Module 1.6: Public Key Cryptography Introduction
Topics: Asymmetric encryption concept, key pairs, Alice & Bob scenario
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
sys.path.append('/home/user/manim-learning')
from components import KeyPair, SignatureProcess, VerificationProcess

# Configure background
config.background_color = "#1e1e1e"


class PublicKeyIntroduction(Scene):
    """Introduction to public key cryptography"""

    def construct(self):
        # Title
        title = Text("Public Key Cryptography", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Asymmetric Encryption", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # The problem
        problem = VGroup(
            Text("The Problem:", color=YELLOW).scale(0.7),
            Text("• How do strangers communicate securely?", color=GRAY).scale(0.5),
            Text("• No shared secret in advance", color=GRAY).scale(0.5),
            Text("• Communication is public (internet)", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problem.shift(UP * 0.5)

        for line in problem:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The solution
        solution = VGroup(
            Text("The Solution: Two Keys", color=GREEN).scale(0.7),
            Text("• Public key: Anyone can have it", color=GRAY).scale(0.5),
            Text("• Private key: Only you have it", color=GRAY).scale(0.5),
            Text("• Mathematically linked", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        solution.shift(DOWN * 1.2)

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


class SymmetricVsAsymmetric(Scene):
    """Compare symmetric vs asymmetric encryption"""

    def construct(self):
        # Title
        title = Text("Symmetric vs Asymmetric", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Symmetric (left side)
        symmetric = VGroup(
            Text("Symmetric", color=BLUE).scale(0.7),
            Text("Same key for both", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Encrypt: key", color=GREEN).scale(0.45),
            Text("Decrypt: key", color=GREEN).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("Problem:", color=RED).scale(0.45),
            Text("Key distribution", color=RED).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        symmetric.shift(LEFT * 3.5)

        # Asymmetric (right side)
        asymmetric = VGroup(
            Text("Asymmetric", color=GREEN).scale(0.7),
            Text("Different keys", color=GRAY).scale(0.5),
            Text("", color=GRAY).scale(0.1),
            Text("Encrypt: public key", color=BLUE).scale(0.45),
            Text("Decrypt: private key", color=RED).scale(0.45),
            Text("", color=GRAY).scale(0.1),
            Text("Advantage:", color=GREEN).scale(0.45),
            Text("No key exchange!", color=GREEN).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        asymmetric.shift(RIGHT * 3)

        # Show both
        self.play(FadeIn(symmetric), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(asymmetric), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(symmetric),
            FadeOut(asymmetric),
            FadeOut(title),
            run_time=1
        )


class KeyPairConcept(Scene):
    """Explain key pair concept"""

    def construct(self):
        # Title
        title = Text("The Key Pair", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Show key pair
        keypair = KeyPair(
            private_key="d = secret",
            public_key="P = d * G",
            show_connection=True
        )
        keypair.scale(0.8).shift(UP * 0.3)

        self.play(FadeIn(keypair.private_box), run_time=1)
        self.wait(1)

        self.play(
            Create(keypair.arrow),
            FadeIn(keypair.arrow_label),
            run_time=1
        )
        self.wait(0.5)

        self.play(FadeIn(keypair.public_box), run_time=1)
        self.wait(2)

        # Properties
        properties = VGroup(
            Text("Properties:", color=YELLOW).scale(0.6),
            Text("• Private key → Public key (one-way)", color=GRAY).scale(0.5),
            Text("• Public key → Private key (impossible)", color=GRAY).scale(0.5),
            Text("• Private key: Keep secret!", color=RED).scale(0.5),
            Text("• Public key: Share freely", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        properties.shift(DOWN * 1.8)

        self.play(FadeIn(properties), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(keypair),
            FadeOut(properties),
            FadeOut(title),
            run_time=1
        )


class LockAndKeyMetaphor(Scene):
    """Lock and key metaphor for public/private keys"""

    def construct(self):
        # Title
        title = Text("Lock and Key Metaphor", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Public key = Lock
        lock_section = VGroup(
            Text("Public Key = Lock", color=GREEN).scale(0.7),
            Text("🔓", color=GREEN).scale(1.5),
            Text("• Anyone can use it to lock", color=GRAY).scale(0.5),
            Text("• Share it publicly", color=GRAY).scale(0.5)
        ).arrange(DOWN, buff=0.3)
        lock_section.shift(LEFT * 3.5 + UP * 0.3)

        # Private key = Key
        key_section = VGroup(
            Text("Private Key = Key", color=RED).scale(0.7),
            Text("🔑", color=RED).scale(1.5),
            Text("• Only you can unlock", color=GRAY).scale(0.5),
            Text("• Keep it secret!", color=GRAY).scale(0.5)
        ).arrange(DOWN, buff=0.3)
        key_section.shift(RIGHT * 3.5 + UP * 0.3)

        self.play(FadeIn(lock_section), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(key_section), run_time=1)
        self.wait(2)

        # Example scenario
        scenario = VGroup(
            Text("Example:", color=YELLOW).scale(0.6),
            Text("1. Alice publishes her lock (public key)", color=GRAY).scale(0.45),
            Text("2. Bob locks message with Alice's lock", color=GRAY).scale(0.45),
            Text("3. Only Alice's key (private key) can unlock it", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        scenario.shift(DOWN * 1.5)

        self.play(FadeIn(scenario), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(lock_section),
            FadeOut(key_section),
            FadeOut(scenario),
            FadeOut(title),
            run_time=1
        )


class AliceAndBobScenario(Scene):
    """Classic Alice and Bob secure communication scenario"""

    def construct(self):
        # Title
        title = Text("Alice and Bob: Secure Communication", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Alice and Bob
        alice = VGroup(
            Text("Alice", color=BLUE).scale(0.7),
            Text("👩", color=BLUE).scale(1.2)
        ).arrange(DOWN, buff=0.2)
        alice.shift(LEFT * 5 + UP * 1.5)

        bob = VGroup(
            Text("Bob", color=GREEN).scale(0.7),
            Text("👨", color=GREEN).scale(1.2)
        ).arrange(DOWN, buff=0.2)
        bob.shift(RIGHT * 5 + UP * 1.5)

        self.play(FadeIn(alice), FadeIn(bob), run_time=1)
        self.wait(1)

        # Step 1: Alice generates key pair
        step1 = Text("Step 1: Alice generates key pair", color=YELLOW).scale(0.5)
        step1.shift(UP * 0.3)
        self.play(Write(step1), run_time=0.8)
        self.wait(1)

        alice_keys = VGroup(
            Text("Private: secret", color=RED).scale(0.4),
            Text("Public: <share>", color=GREEN).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        alice_keys.next_to(alice, DOWN, buff=0.3)

        self.play(FadeIn(alice_keys), run_time=1)
        self.wait(1.5)

        # Step 2: Alice shares public key
        self.play(FadeOut(step1), run_time=0.5)
        step2 = Text("Step 2: Alice shares public key with Bob", color=YELLOW).scale(0.5)
        step2.shift(UP * 0.3)
        self.play(Write(step2), run_time=0.8)
        self.wait(1)

        public_key_copy = alice_keys[1].copy()
        self.play(
            public_key_copy.animate.move_to(bob.get_center() + DOWN * 1.2),
            run_time=1.5
        )
        self.wait(1)

        # Step 3: Bob encrypts message
        self.play(FadeOut(step2), run_time=0.5)
        step3 = Text("Step 3: Bob encrypts message with Alice's public key", color=YELLOW).scale(0.5)
        step3.shift(UP * 0.3)
        self.play(Write(step3), run_time=0.8)
        self.wait(1)

        encrypted_msg = VGroup(
            Text("Encrypted:", color=ORANGE).scale(0.4),
            Text("🔒 message", color=ORANGE).scale(0.4)
        ).arrange(DOWN, buff=0.1)
        encrypted_msg.next_to(bob, DOWN, buff=0.8)

        self.play(FadeIn(encrypted_msg), run_time=1)
        self.wait(1.5)

        # Step 4: Bob sends encrypted message
        self.play(FadeOut(step3), run_time=0.5)
        step4 = Text("Step 4: Bob sends encrypted message", color=YELLOW).scale(0.5)
        step4.shift(UP * 0.3)
        self.play(Write(step4), run_time=0.8)
        self.wait(1)

        encrypted_copy = encrypted_msg.copy()
        self.play(
            encrypted_copy.animate.move_to(alice.get_center() + DOWN * 1.8),
            run_time=1.5
        )
        self.wait(1)

        # Step 5: Alice decrypts
        self.play(FadeOut(step4), run_time=0.5)
        step5 = Text("Step 5: Alice decrypts with her private key", color=YELLOW).scale(0.5)
        step5.shift(UP * 0.3)
        self.play(Write(step5), run_time=0.8)
        self.wait(1)

        decrypted = Text("✓ Read message", color=GREEN).scale(0.4)
        decrypted.next_to(alice, DOWN, buff=2.2)

        self.play(
            Transform(encrypted_copy, decrypted),
            run_time=1
        )
        self.wait(2)

        # Clear
        self.play(
            FadeOut(alice),
            FadeOut(bob),
            FadeOut(alice_keys),
            FadeOut(public_key_copy),
            FadeOut(encrypted_msg),
            FadeOut(encrypted_copy),
            FadeOut(step5),
            FadeOut(title),
            run_time=1
        )


class PublicKeyUseCases(Scene):
    """Different use cases for public key cryptography"""

    def construct(self):
        # Title
        title = Text("Public Key Cryptography: Use Cases", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Use case 1: Encryption
        encryption = VGroup(
            Text("1. Encryption", color=BLUE).scale(0.7),
            Text("• Encrypt with public key", color=GRAY).scale(0.5),
            Text("• Decrypt with private key", color=GRAY).scale(0.5),
            Text("• Use: Secure messaging, email", color=GREEN).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        encryption.shift(UP * 1.5)

        self.play(FadeIn(encryption), run_time=1)
        self.wait(2)

        # Use case 2: Digital Signatures
        signatures = VGroup(
            Text("2. Digital Signatures", color=YELLOW).scale(0.7),
            Text("• Sign with private key", color=GRAY).scale(0.5),
            Text("• Verify with public key", color=GRAY).scale(0.5),
            Text("• Use: Bitcoin, authentication, documents", color=GREEN).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        signatures.shift(DOWN * 0.2)

        self.play(FadeIn(signatures), run_time=1)
        self.wait(2)

        # Use case 3: Key Exchange
        key_exchange = VGroup(
            Text("3. Key Exchange", color=ORANGE).scale(0.7),
            Text("• Establish shared secret", color=GRAY).scale(0.5),
            Text("• No prior communication needed", color=GRAY).scale(0.5),
            Text("• Use: TLS/SSL, VPNs", color=GREEN).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        key_exchange.shift(DOWN * 2)

        self.play(FadeIn(key_exchange), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(encryption),
            FadeOut(signatures),
            FadeOut(key_exchange),
            FadeOut(title),
            run_time=1
        )


class BitcoinFocus(Scene):
    """Focus on Bitcoin's use of public key cryptography"""

    def construct(self):
        # Title
        title = Text("Public Keys in Bitcoin", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Main use
        main_use = VGroup(
            Text("Primary Use: Digital Signatures", color=YELLOW).scale(0.7),
            Text("Not for encryption!", color=RED).scale(0.5)
        ).arrange(DOWN, buff=0.3)
        main_use.shift(UP * 1.5)

        self.play(FadeIn(main_use), run_time=1)
        self.wait(2)

        # How it works
        how_it_works = VGroup(
            Text("How Bitcoin Uses Key Pairs:", color=BLUE).scale(0.6),
            Text("", color=GRAY).scale(0.1),
            Text("• Private key: Proves ownership of bitcoin", color=GRAY).scale(0.5),
            Text("• Public key: Derives Bitcoin address", color=GRAY).scale(0.5),
            Text("• Signature: Proves you have private key", color=GRAY).scale(0.5),
            Text("• Verification: Anyone can verify signature", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        how_it_works.shift(DOWN * 0.3)

        self.play(FadeIn(how_it_works), run_time=1)
        self.wait(3)

        # Key insight
        insight = Text(
            "Your private key = Your bitcoin. Guard it with your life!",
            color=RED
        ).scale(0.6)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(main_use),
            FadeOut(how_it_works),
            FadeOut(insight),
            FadeOut(title),
            run_time=1
        )


class PublicKeySummary(Scene):
    """Summary of public key cryptography"""

    def construct(self):
        # Title
        title = Text("Public Key Cryptography: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Two keys: Public (share) and Private (secret)", color=BLUE).scale(0.6),
            Text("✓ Asymmetric: Different keys for different operations", color=GREEN).scale(0.6),
            Text("✓ One-way: Public key from private, not reverse", color=YELLOW).scale(0.6),
            Text("✓ Uses: Encryption, signatures, key exchange", color=ORANGE).scale(0.6),
            Text("✓ Bitcoin: Uses for digital signatures", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Elliptic Curves - the math behind Bitcoin keys",
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
