"""
Module 1.4: Merkle Trees Part 1
Topics: Tree structure, building a Merkle tree
Duration: 5-10 minutes
"""

from manim import *
import hashlib
import sys
sys.path.append('/home/user/manim-learning')
from components import HashNode, MerkleTree

# Configure background
config.background_color = "#1e1e1e"


class MerkleTreeIntroduction(Scene):
    """Introduction to Merkle Trees"""

    def construct(self):
        # Title
        title = Text("Merkle Trees", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Subtitle
        subtitle = Text("Efficient Data Structure for Verifying Large Datasets", color=GRAY).scale(0.6)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2)

        # Key facts
        facts = VGroup(
            Text("• Binary tree of hashes", color=BLUE).scale(0.6),
            Text("• Leaves contain data hashes", color=GREEN).scale(0.6),
            Text("• Parents hash their children", color=YELLOW).scale(0.6),
            Text("• Root summarizes entire tree", color=ORANGE).scale(0.6),
            Text("• Used in Bitcoin blocks", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        facts.move_to(ORIGIN)

        for fact in facts:
            self.play(FadeIn(fact), run_time=0.8)
            self.wait(1)

        self.wait(2)

        # Clear
        self.play(FadeOut(facts), FadeOut(subtitle), FadeOut(title), run_time=1)


class MerkleTreeProblem(Scene):
    """Explain the problem Merkle trees solve"""

    def construct(self):
        # Title
        title = Text("The Problem", color=RED).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Scenario
        scenario = Text(
            "Bitcoin block contains thousands of transactions",
            color=GRAY
        ).scale(0.6)
        scenario.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(scenario), run_time=1)
        self.wait(2)

        # Problems
        problems = VGroup(
            Text("Without Merkle Trees:", color=YELLOW).scale(0.7),
            Text("❌ Must download all transactions to verify one", color=RED).scale(0.5),
            Text("❌ Wastes bandwidth and storage", color=RED).scale(0.5),
            Text("❌ Slow for light clients (SPV nodes)", color=RED).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        problems.shift(UP * 0.5)

        for problem in problems:
            self.play(FadeIn(problem), run_time=0.8)
            self.wait(1)

        self.wait(1)

        # Solution
        solution = VGroup(
            Text("With Merkle Trees:", color=GREEN).scale(0.7),
            Text("✓ Verify any transaction with small proof", color=GREEN).scale(0.5),
            Text("✓ Proof size: O(log n) hashes", color=GREEN).scale(0.5),
            Text("✓ Efficient for SPV wallets", color=GREEN).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        solution.shift(DOWN * 1.2)

        self.play(FadeIn(solution), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(problems),
            FadeOut(solution),
            FadeOut(scenario),
            FadeOut(title),
            run_time=1
        )


class BuildingMerkleTree(Scene):
    """Demonstrate building a Merkle tree"""

    def construct(self):
        # Title
        title = Text("Building a Merkle Tree", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Create tree with 4 transactions
        transactions = ["Tx A", "Tx B", "Tx C", "Tx D"]
        tree = MerkleTree(transactions, vertical_spacing=1.3, horizontal_spacing=1.5)
        tree.scale(0.7).shift(DOWN * 0.3)

        # Step 1: Show transactions (leaves)
        step1 = Text("Step 1: Hash each transaction", color=GREEN).scale(0.6)
        step1.next_to(title, DOWN, buff=0.3)
        self.play(Write(step1), run_time=0.8)
        self.wait(1)

        leaves = tree.levels[0]
        for leaf in leaves:
            self.play(FadeIn(leaf), run_time=0.5)
            self.wait(0.3)

        self.wait(1)
        self.play(FadeOut(step1), run_time=0.5)

        # Step 2: Show level 1 (pairs)
        step2 = Text("Step 2: Hash pairs of children", color=YELLOW).scale(0.6)
        step2.next_to(title, DOWN, buff=0.3)
        self.play(Write(step2), run_time=0.8)
        self.wait(1)

        # Show edges to level 1
        level1_edges = [
            edge for edge, (parent, child) in tree.edge_lines
            if child in leaves
        ]
        self.play(*[Create(edge) for edge in level1_edges], run_time=1)
        self.wait(0.5)

        # Show level 1 nodes
        level1_nodes = tree.levels[1]
        for node in level1_nodes:
            self.play(FadeIn(node), run_time=0.5)
            self.wait(0.3)

        self.wait(1)
        self.play(FadeOut(step2), run_time=0.5)

        # Step 3: Show root
        step3 = Text("Step 3: Compute root hash", color=ORANGE).scale(0.6)
        step3.next_to(title, DOWN, buff=0.3)
        self.play(Write(step3), run_time=0.8)
        self.wait(1)

        # Show edges to root
        level2_edges = [
            edge for edge, (parent, child) in tree.edge_lines
            if child in level1_nodes
        ]
        self.play(*[Create(edge) for edge in level2_edges], run_time=1)
        self.wait(0.5)

        # Show root
        root = tree.get_root()
        self.play(FadeIn(root), run_time=1)
        self.wait(1)

        # Highlight root
        root_highlight = root.circle.copy()
        root_highlight.set_stroke(YELLOW, width=4)
        root_highlight.set_fill(opacity=0)

        root_label = Text("Merkle Root", color=YELLOW).scale(0.5)
        root_label.next_to(root, RIGHT, buff=0.5)

        self.play(Create(root_highlight), Write(root_label), run_time=1)
        self.wait(2)

        # Clear
        self.play(
            FadeOut(tree),
            FadeOut(root_highlight),
            FadeOut(root_label),
            FadeOut(step3),
            FadeOut(title),
            run_time=1
        )


class MerkleRootExplanation(Scene):
    """Explain the Merkle root"""

    def construct(self):
        # Title
        title = Text("The Merkle Root", color=YELLOW).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Explanation
        explanation = VGroup(
            Text("The root hash represents ALL transactions", color=WHITE).scale(0.6),
            Text("• Changing any transaction changes the root", color=GRAY).scale(0.5),
            Text("• Stored in Bitcoin block header", color=GRAY).scale(0.5),
            Text("• Only 32 bytes to represent thousands of transactions", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.move_to(ORIGIN + UP * 0.5)

        for line in explanation:
            self.play(FadeIn(line), run_time=0.8)
            self.wait(1)

        self.wait(1)

        # Visual example
        before = Text("Before: Root = abc123...", color=GREEN).scale(0.6)
        change = Text("Change one transaction →", color=YELLOW).scale(0.6)
        after = Text("After: Root = xyz789...", color=RED).scale(0.6)

        demo = VGroup(before, change, after).arrange(DOWN, buff=0.4)
        demo.shift(DOWN * 1.5)

        self.play(FadeIn(demo), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(explanation),
            FadeOut(demo),
            FadeOut(title),
            run_time=1
        )


class MerkleTreeProperties(Scene):
    """Key properties of Merkle trees"""

    def construct(self):
        # Title
        title = Text("Merkle Tree Properties", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Properties
        properties = VGroup(
            VGroup(
                Text("1. Tamper-Evident", color=BLUE).scale(0.7),
                Text("Any change propagates to root", color=GRAY).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),

            VGroup(
                Text("2. Efficient Verification", color=GREEN).scale(0.7),
                Text("Verify inclusion with O(log n) hashes", color=GRAY).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),

            VGroup(
                Text("3. Compact Representation", color=YELLOW).scale(0.7),
                Text("Single hash represents entire dataset", color=GRAY).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),

            VGroup(
                Text("4. Deterministic", color=ORANGE).scale(0.7),
                Text("Same data always produces same root", color=GRAY).scale(0.5)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        properties.move_to(ORIGIN)

        # Show properties
        for prop in properties:
            self.play(FadeIn(prop), run_time=1)
            self.wait(1.5)

        self.wait(2)

        # Clear
        self.play(FadeOut(properties), FadeOut(title), run_time=1)


class BitcoinUsage(Scene):
    """How Bitcoin uses Merkle trees"""

    def construct(self):
        # Title
        title = Text("Merkle Trees in Bitcoin", color=WHITE).scale(1.0)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Block structure
        block_structure = VGroup(
            Text("Bitcoin Block Header (80 bytes):", color=BLUE).scale(0.6),
            Text("• Version", color=GRAY).scale(0.5),
            Text("• Previous Block Hash", color=GRAY).scale(0.5),
            Text("• Merkle Root ← All transactions", color=YELLOW).scale(0.5),
            Text("• Timestamp", color=GRAY).scale(0.5),
            Text("• Difficulty Target", color=GRAY).scale(0.5),
            Text("• Nonce", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        block_structure.shift(UP * 0.5)

        for line in block_structure:
            self.play(FadeIn(line), run_time=0.6)
            self.wait(0.5)

        self.wait(1)

        # SPV explanation
        spv = VGroup(
            Text("SPV (Simplified Payment Verification):", color=GREEN).scale(0.6),
            Text("• Light clients download only block headers", color=GRAY).scale(0.5),
            Text("• Verify transactions using Merkle proofs", color=GRAY).scale(0.5),
            Text("• No need to download entire blockchain", color=GRAY).scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        spv.shift(DOWN * 1.5)

        self.play(FadeIn(spv), run_time=1)
        self.wait(3)

        # Clear
        self.play(
            FadeOut(block_structure),
            FadeOut(spv),
            FadeOut(title),
            run_time=1
        )


class MerkleTreeSummary(Scene):
    """Summary of Merkle trees"""

    def construct(self):
        # Title
        title = Text("Merkle Trees: Summary", color=WHITE).scale(1.2)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        # Key points
        summary = VGroup(
            Text("✓ Binary hash tree structure", color=BLUE).scale(0.6),
            Text("✓ Root hash represents all data", color=GREEN).scale(0.6),
            Text("✓ Efficient verification (logarithmic)", color=YELLOW).scale(0.6),
            Text("✓ Tamper-evident (changes propagate up)", color=ORANGE).scale(0.6),
            Text("✓ Enables SPV wallets in Bitcoin", color=PURPLE).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        summary.move_to(ORIGIN)

        for point in summary:
            self.play(FadeIn(point), run_time=0.8)
            self.wait(0.8)

        self.wait(2)

        # Next
        next_topic = Text(
            "Next: Merkle Proofs - proving a transaction is in a block",
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
