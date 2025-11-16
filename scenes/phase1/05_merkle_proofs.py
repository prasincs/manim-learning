"""
Module 1.5: Merkle Trees Part 2
Topics: Merkle proofs and verification
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
# Add repository root to path for components module
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components import HashNode, MerkleTree, MerkleProofVisualization

# Configure background
config.background_color = "#1e1e1e"


class MerkleProofIntroduction(Scene):
    """Introduction to Merkle proofs"""

    def construct(self):
        # Title
        title = Text("Merkle Proofs", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Proving a Transaction is in a Block", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # The challenge
        challenge = VGroup(
            Text("The Challenge:", color=YELLOW).scale(0.7),
            Text("• Block contains 2000 transactions", color=GRAY).scale(0.5),
            Text("• You only care about one transaction", color=GRAY).scale(0.5),
            Text("• Don't want to download all 2000 transactions", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        challenge.shift(UP * 0.5)

        for line in challenge:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(0.8)

        self.wait(1)

        # The solution
        solution = VGroup(
            Text("The Solution: Merkle Proof", color=GREEN).scale(0.7),
            Text("• Download only log₂(n) hashes", color=GRAY).scale(0.5),
            Text("• For 2000 transactions: ~11 hashes", color=GRAY).scale(0.5),
            Text("• Verify inclusion cryptographically", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        solution.shift(DOWN * 1.2)

        self.play(FadeIn(solution), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(challenge),
            FadeOut(solution),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class ProofPathConcept(Scene):
    """Explain the concept of a proof path"""

    def construct(self):
        # Title
        title = Text("The Proof Path", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create simple tree
        transactions = ["Tx A", "Tx B", "Tx C", "Tx D"]
        tree = MerkleTree(transactions, vertical_spacing=1.3, horizontal_spacing=1.5)
        tree.scale(0.7).shift(DOWN * 0.3)

        # Show full tree
        self.play(FadeIn(tree), run_time=1)
        self.wait(1)

        # Highlight transaction B (index 1)
        target_tx = tree.get_leaves()[1]
        target_highlight = target_tx.circle.copy()
        target_highlight.set_stroke(YELLOW, width=5)
        target_highlight.set_fill(opacity=0)

        target_label = Text("Want to prove this tx", color=YELLOW).scale(0.4)
        target_label.next_to(target_tx, DOWN, buff=0.3)

        self.play(Create(target_highlight), Write(target_label), run_time=1)
        self.wait(2)

        # Show proof path (siblings needed)
        proof_path = tree.get_proof_path(1)

        proof_highlights = []
        for node in proof_path:
            highlight = node.circle.copy()
            highlight.set_stroke(GREEN, width=4)
            highlight.set_fill(opacity=0)
            proof_highlights.append(highlight)

        proof_label = Text("Proof path (sibling hashes)", color=GREEN).scale(0.5)
        proof_label.to_edge(DOWN, buff=0.3)

        self.play(
            *[Create(h) for h in proof_highlights],
            Write(proof_label),
            run_time=1
        )
        self.wait(3)

        # Clear
        self.play(
            FadeOut(tree),
            FadeOut(target_highlight),
            FadeOut(target_label),
            *[FadeOut(h) for h in proof_highlights],
            FadeOut(proof_label),
            FadeOut(title),
            run_time=1
        )


class ProofVerification(Scene):
    """Show how to verify a Merkle proof"""

    def construct(self):
        # Title
        title = Text("Verifying a Merkle Proof", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Setup
        subtitle = Text("Given: Transaction, Merkle Root, and Proof Path", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Step-by-step verification
        steps = VGroup(
            Text("Step 1: Hash the transaction", color=BLUE).scale(0.6),
            Text("Step 2: Combine with sibling hash", color=GREEN).scale(0.6),
            Text("Step 3: Hash the combination", color=YELLOW).scale(0.6),
            Text("Step 4: Repeat up the tree", color=ORANGE).scale(0.6),
            Text("Step 5: Compare final hash to Merkle root", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.move_to(ORIGIN)

        for step in steps:
            self.play(FadeIn(step), run_time=0.8)
            self.wait(1.2)

        self.wait(2)

        # Result
        self.play(FadeOut(steps), run_time=0.5)

        result = VGroup(
            Text("If computed root == given root:", color=WHITE).scale(0.7),
            Text("✓ Transaction is in the block", color=GREEN).scale(0.6)
        ).arrange(DOWN, buff=0.3)
        result.shift(UP * 0.5)

        invalid = VGroup(
            Text("If computed root ≠ given root:", color=WHITE).scale(0.7),
            Text("✗ Transaction is NOT in the block", color=RED).scale(0.6)
        ).arrange(DOWN, buff=0.3)
        invalid.shift(DOWN * 1)

        self.play(FadeIn(result), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(invalid), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(result),
            FadeOut(invalid),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class ProofExample(Scene):
    """Detailed example of Merkle proof"""

    def construct(self):
        # Title
        title = Text("Merkle Proof Example", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create tree
        transactions = ["Tx A", "Tx B", "Tx C", "Tx D"]
        tree = MerkleTree(transactions, vertical_spacing=1.2, horizontal_spacing=1.3)
        tree.scale(0.65).shift(LEFT * 3 + DOWN * 0.2)

        self.play(FadeIn(tree), run_time=1)
        self.wait(1)

        # Prove Tx C (index 2)
        target_leaf = tree.get_leaves()[2]
        target_highlight = target_leaf.circle.copy()
        target_highlight.set_stroke(YELLOW, width=5)

        target_label = Text("Prove: Tx C", color=YELLOW).scale(0.5)
        target_label.next_to(target_leaf, LEFT, buff=0.3)

        self.play(Create(target_highlight), Write(target_label), run_time=1)
        self.wait(1)

        # Show proof path
        proof_viz = MerkleProofVisualization(tree, leaf_index=2)
        self.play(Create(proof_viz), run_time=1)
        self.wait(1)

        # List proof components on the right
        proof_list = VGroup(
            Text("Merkle Proof:", color=GREEN).scale(0.6),
            Text("1. Hash(Tx C)", color=GRAY).scale(0.45),
            Text("2. Hash(Tx D) ←", color=GREEN).scale(0.45),
            Text("3. Hash(AB) ←", color=GREEN).scale(0.45),
            Text("", color=GRAY).scale(0.45),
            Text("Merkle Root:", color=BLUE).scale(0.6),
            Text("Hash(ABCD)", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        proof_list.shift(RIGHT * 3.5)

        self.play(Write(proof_list), run_time=1)
        self.wait(3)

        # Verification steps
        verify = Text("Verification: Hash(Hash(C+D) + Hash(AB)) == Root?", color=YELLOW).scale(0.45)
        verify.to_edge(DOWN, buff=0.3)
        self.play(Write(verify), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(tree),
            FadeOut(target_highlight),
            FadeOut(target_label),
            FadeOut(proof_viz),
            FadeOut(proof_list),
            FadeOut(verify),
            FadeOut(title),
            run_time=1
        )


class ProofEfficiency(Scene):
    """Show efficiency of Merkle proofs"""

    def construct(self):
        # Title
        title = Text("Proof Efficiency", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Comparison table
        header = VGroup(
            Text("Transactions", color=BLUE).scale(0.5),
            Text("Tree Height", color=GREEN).scale(0.5),
            Text("Proof Size", color=YELLOW).scale(0.5)
        ).arrange(RIGHT, buff=1.5)
        header.shift(UP * 2)

        self.play(Write(header), run_time=1)
        self.wait(1)

        # Data rows
        rows = [
            ("4", "2", "2 hashes"),
            ("8", "3", "3 hashes"),
            ("16", "4", "4 hashes"),
            ("1,024", "10", "10 hashes"),
            ("2,000", "~11", "~11 hashes"),
            ("1,000,000", "~20", "~20 hashes")
        ]

        table_rows = VGroup()
        for tx, height, proof in rows:
            row = VGroup(
                Text(tx, color=WHITE).scale(0.45),
                Text(height, color=WHITE).scale(0.45),
                Text(proof, color=WHITE).scale(0.45)
            ).arrange(RIGHT, buff=1.5)
            table_rows.add(row)

        table_rows.arrange(DOWN, buff=0.3)
        table_rows.next_to(header, DOWN, buff=0.5)

        for row in table_rows:
            self.play(FadeIn(row), run_time=0.6)
            self.wait(0.5)

        self.wait(2)

        # Key insight
        insight = Text(
            "Proof size grows logarithmically, not linearly!",
            color=GREEN
        ).scale(0.6)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(header),
            FadeOut(table_rows),
            FadeOut(insight),
            FadeOut(title),
            run_time=1
        )


class SPVWallets(Scene):
    """Explain SPV wallets using Merkle proofs"""

    def construct(self):
        # Title
        title = Text("SPV Wallets", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Simplified Payment Verification", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)

        # Full node vs SPV
        full_node = VGroup(
            Text("Full Node:", color=BLUE).scale(0.6),
            Text("• Downloads all transactions", color=GRAY).scale(0.5),
            Text("• Validates everything", color=GRAY).scale(0.5),
            Text("• ~500 GB storage", color=GRAY).scale(0.5),
            Text("• Resource intensive", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        full_node.shift(LEFT * 3)

        spv = VGroup(
            Text("SPV Wallet:", color=GREEN).scale(0.6),
            Text("• Downloads block headers only", color=GRAY).scale(0.5),
            Text("• Uses Merkle proofs", color=GRAY).scale(0.5),
            Text("• ~100 MB storage", color=GRAY).scale(0.5),
            Text("• Mobile-friendly", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        spv.shift(RIGHT * 3)

        self.play(FadeIn(full_node), run_time=1)
        self.wait(1.5)
        self.play(FadeIn(spv), run_time=1)
        self.wait(2)

        # Process
        process = VGroup(
            Text("SPV Process:", color=YELLOW).scale(0.6),
            Text("1. Download all block headers (~80 bytes each)", color=GRAY).scale(0.45),
            Text("2. To verify transaction: request Merkle proof", color=GRAY).scale(0.45),
            Text("3. Verify proof against header's Merkle root", color=GRAY).scale(0.45),
            Text("4. Trust: more confirmations = more secure", color=GRAY).scale(0.45)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        process.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(process), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(full_node),
            FadeOut(spv),
            FadeOut(process),
            FadeOut(subtitle),
            FadeOut(title),
            run_time=1
        )


class MerkleProofSummary(Scene):
    """Summary of Merkle proofs"""

    def construct(self):
        # Title
        title = Text("Merkle Proofs: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Prove transaction inclusion efficiently", color=BLUE).scale(0.6),
            Text("✓ Proof size: O(log n) hashes", color=GREEN).scale(0.6),
            Text("✓ No need to download entire block", color=YELLOW).scale(0.6),
            Text("✓ Cryptographically secure verification", color=ORANGE).scale(0.6),
            Text("✓ Enables lightweight SPV wallets", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next topic
        next_topic = Text(
            "Next: Public Key Cryptography - asymmetric encryption",
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
