"""
Tree visualization components (Merkle trees, syntax trees, etc.)
"""
from manim import *
import hashlib


class HashNode(VGroup):
    """A node in a hash tree (e.g., Merkle tree)"""

    def __init__(
        self,
        data,
        is_leaf=False,
        color=None,
        show_full_hash=False,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Determine color
        if color is None:
            color = GREEN if is_leaf else BLUE

        # Create hash if needed
        if is_leaf and not show_full_hash:
            # For leaves, show original data
            display_text = data if len(data) <= 10 else data[:7] + "..."
        else:
            # For internal nodes, show hash
            if show_full_hash:
                display_text = data[:8] + "..."
            else:
                display_text = data[:6] + "..."

        # Create text
        self.text = Text(display_text, color=BLACK).scale(0.4)

        # Create circle node
        self.circle = Circle(
            radius=0.5,
            color=WHITE,
            fill_color=color,
            fill_opacity=0.8
        )

        # Position text in center
        self.text.move_to(self.circle.get_center())

        # Store original data
        self.data = data
        self.is_leaf = is_leaf

        self.add(self.circle, self.text)


class MerkleTree(VGroup):
    """A Merkle tree visualization"""

    def __init__(self, leaf_data, vertical_spacing=1.5, horizontal_spacing=1.2, **kwargs):
        super().__init__(**kwargs)

        self.leaf_data = leaf_data
        self.levels = []
        self.edges = []

        # Build tree bottom-up
        current_level = []

        # Create leaf nodes
        for data in leaf_data:
            hash_value = hashlib.sha256(data.encode()).hexdigest()
            node = HashNode(hash_value, is_leaf=True, color=GREEN)
            current_level.append(node)

        self.levels.append(current_level)

        # Build parent levels
        while len(current_level) > 1:
            parent_level = []

            # Process pairs
            for i in range(0, len(current_level), 2):
                # Get left child
                left = current_level[i]

                # Get right child (or duplicate left if odd)
                if i + 1 < len(current_level):
                    right = current_level[i + 1]
                else:
                    right = left

                # Compute parent hash
                combined = left.data + right.data
                parent_hash = hashlib.sha256(combined.encode()).hexdigest()

                # Create parent node
                parent = HashNode(parent_hash, is_leaf=False, color=BLUE)
                parent_level.append(parent)

                # Store edge connections
                self.edges.append((parent, left))
                if right != left:
                    self.edges.append((parent, right))

            self.levels.append(parent_level)
            current_level = parent_level

        # Position nodes
        self._position_nodes(vertical_spacing, horizontal_spacing)

        # Create edge lines
        self._create_edges()

        # Add all to group
        for level in self.levels:
            self.add(*level)
        self.add(*[edge for edge, _ in self.edge_lines])

    def _position_nodes(self, v_spacing, h_spacing):
        """Position all nodes in the tree"""
        num_levels = len(self.levels)

        for level_idx, level in enumerate(self.levels):
            y_pos = -level_idx * v_spacing

            # Calculate total width needed
            num_nodes = len(level)
            total_width = (num_nodes - 1) * h_spacing

            # Center the level
            start_x = -total_width / 2

            for node_idx, node in enumerate(level):
                x_pos = start_x + node_idx * h_spacing
                node.move_to(np.array([x_pos, y_pos, 0]))

    def _create_edges(self):
        """Create lines connecting nodes"""
        self.edge_lines = []

        for parent, child in self.edges:
            line = Line(
                parent.get_bottom(),
                child.get_top(),
                color=GRAY,
                stroke_width=2
            )
            self.edge_lines.append((line, (parent, child)))

    def get_root(self):
        """Get the root node"""
        return self.levels[-1][0]

    def get_leaves(self):
        """Get all leaf nodes"""
        return self.levels[0]

    def get_proof_path(self, leaf_index):
        """Get the proof path for a specific leaf"""
        path = []
        current_index = leaf_index

        for level_idx in range(len(self.levels) - 1):
            current_level = self.levels[level_idx]

            # Sibling index
            if current_index % 2 == 0:
                sibling_index = current_index + 1
            else:
                sibling_index = current_index - 1

            # Check if sibling exists
            if sibling_index < len(current_level):
                sibling = current_level[sibling_index]
                path.append(sibling)

            # Move to parent level
            current_index = current_index // 2

        return path


class MerkleProofVisualization(VGroup):
    """Visualization of a Merkle proof"""

    def __init__(self, tree, leaf_index, **kwargs):
        super().__init__(**kwargs)

        self.tree = tree
        self.leaf_index = leaf_index
        self.proof_path = tree.get_proof_path(leaf_index)

        # Highlight the proof path
        self.highlighted_nodes = [tree.get_leaves()[leaf_index]]
        self.highlighted_nodes.extend(self.proof_path)

        # Create highlights
        self.highlights = []
        for node in self.highlighted_nodes:
            highlight = node.circle.copy()
            highlight.set_stroke(YELLOW, width=4)
            highlight.set_fill(opacity=0)
            self.highlights.append(highlight)

        self.add(*self.highlights)


# Example usage scenes
class MerkleTreeExample(Scene):
    def construct(self):
        # Title
        title = Text("Merkle Tree Example").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Create tree with 4 transactions
        transactions = ["Tx1", "Tx2", "Tx3", "Tx4"]
        tree = MerkleTree(transactions)
        tree.scale(0.8)

        # Animate building tree level by level
        for level_idx, level in enumerate(tree.levels):
            # Show nodes
            self.play(*[FadeIn(node) for node in level])
            self.wait(0.5)

            # Show edges to next level (if not last level)
            if level_idx < len(tree.levels) - 1:
                relevant_edges = [
                    edge for edge, (parent, child) in tree.edge_lines
                    if child in level
                ]
                if relevant_edges:
                    self.play(*[Create(edge) for edge in relevant_edges])
                self.wait(0.5)

        self.wait(2)

        # Highlight root
        root = tree.get_root()
        root_label = Text("Merkle Root", color=YELLOW).scale(0.5)
        root_label.next_to(root, RIGHT, buff=0.5)
        self.play(
            root.circle.animate.set_stroke(YELLOW, width=4),
            Write(root_label)
        )
        self.wait(2)

        self.play(FadeOut(tree), FadeOut(title), FadeOut(root_label))


class MerkleProofExample(Scene):
    def construct(self):
        # Title
        title = Text("Merkle Proof Example").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Create tree
        transactions = ["Tx1", "Tx2", "Tx3", "Tx4"]
        tree = MerkleTree(transactions)
        tree.scale(0.7).shift(UP * 0.5)

        # Show tree
        self.play(FadeIn(tree))
        self.wait(1)

        # Prove Tx2 is in the tree (index 1)
        proof_viz = MerkleProofVisualization(tree, leaf_index=1)

        # Explain
        explanation = Text(
            "Proving Tx2 is in the tree",
            color=YELLOW
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(1)

        # Highlight proof path
        self.play(Create(proof_viz))
        self.wait(2)

        # Show proof steps
        proof_path = tree.get_proof_path(1)
        proof_text = VGroup()

        proof_label = Text("Proof Path:", color=GREEN).scale(0.4)
        proof_text.add(proof_label)

        for i, node in enumerate(proof_path):
            step = Text(
                f"{i+1}. {node.data[:8]}...",
                color=WHITE
            ).scale(0.3)
            proof_text.add(step)

        proof_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        proof_text.to_corner(DR)

        self.play(Write(proof_text))
        self.wait(3)

        self.play(FadeOut(tree), FadeOut(proof_viz), FadeOut(title), FadeOut(explanation), FadeOut(proof_text))


class BinaryTreeGeneric(VGroup):
    """Generic binary tree (not specifically for hashing)"""

    def __init__(self, data_dict, root_key, vertical_spacing=1.5, **kwargs):
        """
        data_dict: dict mapping node_key -> (value, left_child_key, right_child_key)
        root_key: key of root node
        """
        super().__init__(**kwargs)

        self.data_dict = data_dict
        self.root_key = root_key
        self.nodes = {}
        self.edges = []

        # Build tree recursively
        self._build_tree(root_key, position=ORIGIN, h_offset=2.0, v_spacing=vertical_spacing)

        # Add all to group
        self.add(*self.nodes.values())
        self.add(*self.edges)

    def _build_tree(self, key, position, h_offset, v_spacing, depth=0):
        """Recursively build tree"""
        if key is None or key not in self.data_dict:
            return None

        value, left_key, right_key = self.data_dict[key]

        # Create node
        node = self._create_node(value, position)
        self.nodes[key] = node

        # Create children
        if left_key:
            left_pos = position + np.array([-h_offset, -v_spacing, 0])
            left_node = self._build_tree(
                left_key,
                left_pos,
                h_offset / 2,
                v_spacing,
                depth + 1
            )
            if left_node:
                edge = Line(node.get_bottom(), left_node.get_top(), color=GRAY)
                self.edges.append(edge)

        if right_key:
            right_pos = position + np.array([h_offset, -v_spacing, 0])
            right_node = self._build_tree(
                right_key,
                right_pos,
                h_offset / 2,
                v_spacing,
                depth + 1
            )
            if right_node:
                edge = Line(node.get_bottom(), right_node.get_top(), color=GRAY)
                self.edges.append(edge)

        return node

    def _create_node(self, value, position):
        """Create a tree node"""
        text = Text(str(value), color=BLACK).scale(0.5)
        circle = Circle(radius=0.4, color=WHITE, fill_color=BLUE, fill_opacity=0.8)
        circle.move_to(position)
        text.move_to(circle.get_center())
        return VGroup(circle, text)
