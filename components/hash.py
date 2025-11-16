"""
Hash function visualization components
"""
from manim import *
import hashlib


class HashMachine(VGroup):
    """Visual representation of a hash function"""

    def __init__(
        self,
        label="SHA-256",
        input_color=BLUE,
        output_color=GREEN,
        machine_color=GRAY,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Machine body
        self.machine = RoundedRectangle(
            width=3,
            height=2,
            corner_radius=0.2,
            color=machine_color,
            fill_opacity=0.8
        )

        # Label
        self.label = Text(label, color=WHITE).scale(0.7)
        self.label.move_to(self.machine.get_center())

        # Input port
        self.input_port = Circle(radius=0.2, color=input_color, fill_opacity=1)
        self.input_port.move_to(self.machine.get_left() + RIGHT * 0.2)

        # Output port
        self.output_port = Circle(radius=0.2, color=output_color, fill_opacity=1)
        self.output_port.move_to(self.machine.get_right() + LEFT * 0.2)

        # Add all parts
        self.add(self.machine, self.label, self.input_port, self.output_port)

    def get_input_pos(self):
        """Get position for input connection"""
        return self.input_port.get_left()

    def get_output_pos(self):
        """Get position for output connection"""
        return self.output_port.get_right()


class DataBox(VGroup):
    """A box containing data (input or output)"""

    def __init__(self, data, color=BLUE, max_width=2.5, **kwargs):
        super().__init__(**kwargs)

        # Truncate if too long
        display_data = data if len(data) <= 16 else data[:13] + "..."

        # Text
        self.text = Text(display_data, color=WHITE).scale(0.5)

        # Box
        self.box = SurroundingRectangle(
            self.text,
            color=WHITE,
            fill_color=color,
            buff=0.2,
            fill_opacity=0.9
        )

        # Ensure max width
        if self.box.width > max_width:
            scale_factor = max_width / self.box.width
            self.text.scale(scale_factor)
            self.box = SurroundingRectangle(
                self.text,
                color=WHITE,
                fill_color=color,
                buff=0.2,
                fill_opacity=0.9
            )

        self.add(self.box, self.text)

    def get_connection_point(self, direction):
        """Get point for arrow connection"""
        if direction == "left":
            return self.box.get_left()
        elif direction == "right":
            return self.box.get_right()
        elif direction == "top":
            return self.box.get_top()
        else:  # bottom
            return self.box.get_bottom()


class HashVisualization(VGroup):
    """Complete hash visualization with input -> machine -> output"""

    def __init__(
        self,
        input_data="Input",
        hash_function="SHA-256",
        compute_hash=True,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Input box
        self.input_box = DataBox(input_data, color=BLUE)

        # Hash machine
        self.machine = HashMachine(label=hash_function)

        # Output box (compute actual hash if requested)
        if compute_hash and hash_function == "SHA-256":
            hash_output = hashlib.sha256(input_data.encode()).hexdigest()[:16] + "..."
        else:
            hash_output = "Hash Output"

        self.output_box = DataBox(hash_output, color=GREEN)

        # Position elements
        self.input_box.next_to(self.machine, LEFT, buff=1)
        self.output_box.next_to(self.machine, RIGHT, buff=1)

        # Arrows
        self.input_arrow = Arrow(
            self.input_box.get_connection_point("right"),
            self.machine.get_input_pos(),
            buff=0.1,
            color=YELLOW
        )

        self.output_arrow = Arrow(
            self.machine.get_output_pos(),
            self.output_box.get_connection_point("left"),
            buff=0.1,
            color=YELLOW
        )

        # Add all elements
        self.add(
            self.input_box,
            self.machine,
            self.output_box,
            self.input_arrow,
            self.output_arrow
        )


class AvalancheEffect(VGroup):
    """Demonstrate avalanche effect - small change in input = big change in output"""

    def __init__(self, input1="Hello", input2="hello", **kwargs):
        super().__init__(**kwargs)

        # Compute hashes
        hash1 = hashlib.sha256(input1.encode()).hexdigest()
        hash2 = hashlib.sha256(input2.encode()).hexdigest()

        # Create two hash visualizations
        self.viz1 = HashVisualization(input_data=input1, hash_function="SHA-256")
        self.viz2 = HashVisualization(input_data=input2, hash_function="SHA-256")

        # Position vertically
        self.viz1.to_edge(UP, buff=0.5)
        self.viz2.to_edge(DOWN, buff=0.5)

        # Highlight differences
        self.diff_label = Text("One character difference", color=RED).scale(0.6)
        self.diff_label.move_to(ORIGIN + LEFT * 3)

        self.hash_diff_label = Text("Completely different hashes!", color=YELLOW).scale(0.6)
        self.hash_diff_label.move_to(ORIGIN + RIGHT * 3)

        self.add(self.viz1, self.viz2, self.diff_label, self.hash_diff_label)


# Example usage scene
class HashExample(Scene):
    def construct(self):
        # Title
        title = Text("Hash Function Visualization").to_edge(UP)
        self.play(Write(title))

        # Simple hash visualization
        hash_viz = HashVisualization(input_data="Hello, Bitcoin!", compute_hash=True)

        # Animate creation
        self.play(FadeIn(hash_viz.input_box))
        self.wait(0.5)

        self.play(
            Create(hash_viz.input_arrow),
            FadeIn(hash_viz.machine)
        )
        self.wait(0.5)

        self.play(
            Create(hash_viz.output_arrow),
            FadeIn(hash_viz.output_box)
        )
        self.wait(2)

        # Clear
        self.play(FadeOut(hash_viz))

        # Show avalanche effect
        avalanche = AvalancheEffect(input1="Bitcoin", input2="bitcoin")
        self.play(FadeIn(avalanche))
        self.wait(3)

        # Cleanup
        self.play(FadeOut(avalanche), FadeOut(title))


class HashComparison(Scene):
    """Compare multiple hash functions"""

    def construct(self):
        title = Text("Hash Function Comparison").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Create multiple hash visualizations
        input_data = "Bitcoin"

        # SHA-256
        sha256_hash = hashlib.sha256(input_data.encode()).hexdigest()
        sha256_label = Text("SHA-256:", color=BLUE).scale(0.6)
        sha256_output = Text(sha256_hash[:32] + "...", color=WHITE).scale(0.4)

        # SHA-1 (for comparison, though insecure)
        sha1_hash = hashlib.sha1(input_data.encode()).hexdigest()
        sha1_label = Text("SHA-1:", color=YELLOW).scale(0.6)
        sha1_output = Text(sha1_hash, color=WHITE).scale(0.4)

        # MD5 (for comparison, though insecure)
        md5_hash = hashlib.md5(input_data.encode()).hexdigest()
        md5_label = Text("MD5:", color=RED).scale(0.6)
        md5_output = Text(md5_hash, color=WHITE).scale(0.4)

        # Arrange vertically
        sha256_group = VGroup(sha256_label, sha256_output).arrange(RIGHT, buff=0.3)
        sha1_group = VGroup(sha1_label, sha1_output).arrange(RIGHT, buff=0.3)
        md5_group = VGroup(md5_label, md5_output).arrange(RIGHT, buff=0.3)

        all_hashes = VGroup(sha256_group, sha1_group, md5_group).arrange(DOWN, buff=0.5)

        # Input
        input_box = DataBox(f'Input: "{input_data}"', color=BLUE)
        input_box.next_to(all_hashes, UP, buff=1)

        self.play(FadeIn(input_box))
        self.wait(1)

        self.play(Write(all_hashes))
        self.wait(3)

        # Add security notes
        note = Text(
            "Note: SHA-256 is secure, SHA-1 and MD5 are broken!",
            color=RED
        ).scale(0.5).to_edge(DOWN)

        self.play(Write(note))
        self.wait(2)
