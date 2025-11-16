# Visualization Guidelines for Manim Animations

Guidelines for creating clear, effective educational visualizations following Edward Tufte's principles and Manim best practices.

## Core Principles (Edward Tufte)

### 1. **Show the Data**
- Don't hide information behind unnecessary decorations
- Make the data the star, not the animation effects
- Every element should serve the educational purpose

### 2. **Maximize Data-Ink Ratio**
- Minimize "chartjunk" - remove non-essential visual elements
- Every pixel should have a purpose
- Default to simplicity, add complexity only when needed

### 3. **Integrate Text and Graphics**
- Labels should be near what they're labeling
- Use annotations inline with visuals
- Don't separate explanations from demonstrations

### 4. **Small Multiples**
- Show variations side-by-side for comparison
- Use consistent scales and layouts
- Enable pattern recognition through repetition

### 5. **Document Evidence**
- Show sources and calculations
- Make the logic transparent
- Build trust through thoroughness

## Manim-Specific Best Practices

### Version Requirements
```python
# Ensure you're using Manim Community Edition v0.18.0+
# Check version: manim --version
# Install: pip install manim

from manim import *  # v0.18.0+
```

### Color Palette (Accessible & Clear)

```python
# Use these predefined, accessible colors
COLORS = {
    "background": "#1e1e1e",      # Dark background (easier on eyes)
    "primary": "#61AFEF",          # Blue (data, main concepts)
    "secondary": "#98C379",        # Green (success, outputs)
    "accent": "#E5C07B",           # Yellow (highlights, warnings)
    "danger": "#E06C75",           # Red (errors, attacks)
    "neutral": "#ABB2BF",          # Gray (secondary info)
    "text": "#FFFFFF",             # White (primary text)
}

# Tufte's rule: Use color sparingly and with purpose
# Good: 2-3 colors per scene
# Bad: Rainbow explosions
```

### Typography

```python
# Use consistent, readable fonts
DEFAULT_FONT = "CMU Serif"  # Computer Modern (like LaTeX)
CODE_FONT = "Fira Code"     # Monospace for code/hashes

# Font sizes (scaled appropriately)
TITLE_SCALE = 1.2
HEADING_SCALE = 0.9
BODY_SCALE = 0.7
CAPTION_SCALE = 0.5
CODE_SCALE = 0.6

# Example usage
def create_title(text):
    return Text(text, font=DEFAULT_FONT).scale(TITLE_SCALE)

def create_code(text):
    return Text(text, font=CODE_FONT, color=COLORS["neutral"]).scale(CODE_SCALE)
```

### Layout Principles

```python
# Standard layout constants
TITLE_POSITION = UP * 3.5
MAIN_AREA = ORIGIN
CAPTION_POSITION = DOWN * 3.5
SIDEBAR_LEFT = LEFT * 5
SIDEBAR_RIGHT = RIGHT * 5

# Margins and spacing
MARGIN = 0.5
SMALL_BUFF = 0.2
MEDIUM_BUFF = 0.5
LARGE_BUFF = 1.0

# Example: Consistent positioning
title = create_title("Hash Functions")
title.to_edge(UP, buff=MARGIN)
```

### Animation Timing (Critical for YouTube)

```python
# Tufte: "Respect the viewer's time and intelligence"

# Standard timings (in seconds)
QUICK_FADE = 0.3      # Quick transitions
NORMAL_FADE = 0.5     # Standard fade in/out
SLOW_FADE = 1.0       # Emphasis

QUICK_ANIM = 0.5      # Quick movements
NORMAL_ANIM = 1.0     # Standard animations
SLOW_ANIM = 2.0       # Complex transformations

PAUSE_SHORT = 0.5     # Brief pause
PAUSE_NORMAL = 1.0    # Standard pause
PAUSE_LONG = 2.0      # Let complex ideas sink in

# Usage
self.play(FadeIn(object), run_time=NORMAL_FADE)
self.wait(PAUSE_NORMAL)
```

### Scene Template (One-Shot Ready)

```python
from manim import *

# Configuration for consistent quality
config.background_color = "#1e1e1e"
config.max_files_cached = 100

class BaseEducationalScene(Scene):
    """
    Base class for all educational scenes.
    Incorporates Tufte principles and consistent styling.
    """

    def setup(self):
        # Standard colors
        self.colors = {
            "primary": BLUE,
            "secondary": GREEN,
            "accent": YELLOW,
            "danger": RED,
            "neutral": GRAY,
        }

        # Typography settings
        self.title_scale = 1.2
        self.heading_scale = 0.9
        self.body_scale = 0.7
        self.caption_scale = 0.5

        # Timing
        self.quick = 0.5
        self.normal = 1.0
        self.slow = 2.0

    def create_title(self, text, color=WHITE):
        """Create a title following Tufte principles"""
        title = Text(text, color=color).scale(self.title_scale)
        title.to_edge(UP, buff=0.5)
        return title

    def create_heading(self, text, color=None):
        """Create a section heading"""
        color = color or self.colors["primary"]
        return Text(text, color=color).scale(self.heading_scale)

    def create_body(self, text, color=WHITE):
        """Create body text"""
        return Text(text, color=color).scale(self.body_scale)

    def create_caption(self, text):
        """Create caption text"""
        caption = Text(text, color=GRAY).scale(self.caption_scale)
        caption.to_edge(DOWN, buff=0.3)
        return caption

    def create_labeled_box(self, content, label, box_color=BLUE):
        """
        Create a box with integrated label (Tufte principle: integrate text and graphics)
        """
        # Create content
        if isinstance(content, str):
            content_obj = Text(content, color=WHITE).scale(0.6)
        else:
            content_obj = content

        # Create box
        box = SurroundingRectangle(
            content_obj,
            color=WHITE,
            fill_color=box_color,
            fill_opacity=0.3,
            buff=0.3
        )

        # Create label (positioned at top-left of box)
        label_text = Text(label, color=WHITE).scale(0.5)
        label_text.next_to(box.get_corner(UL), DR, buff=0.1)

        return VGroup(box, content_obj, label_text)

    def create_comparison(self, left_content, right_content, left_label, right_label):
        """
        Create side-by-side comparison (Tufte: small multiples)
        """
        # Left side
        left_group = self.create_labeled_box(left_content, left_label, BLUE)
        left_group.shift(LEFT * 3)

        # Right side
        right_group = self.create_labeled_box(right_content, right_label, GREEN)
        right_group.shift(RIGHT * 3)

        return VGroup(left_group, right_group)

    def show_clean(self, *mobjects, run_time=1.0):
        """
        Clean entrance (Tufte: maximize data-ink ratio)
        Simple fade in, no unnecessary flourishes
        """
        self.play(*[FadeIn(mob, run_time=run_time) for mob in mobjects])

    def hide_clean(self, *mobjects, run_time=0.5):
        """Clean exit"""
        self.play(*[FadeOut(mob, run_time=run_time) for mob in mobjects])


# Example usage
class HashFunctionDemo(BaseEducationalScene):
    def construct(self):
        # Title
        title = self.create_title("Hash Functions")
        self.show_clean(title)
        self.wait(self.normal)

        # Show hash visualization
        input_box = self.create_labeled_box("Hello, World!", "Input", BLUE)
        input_box.shift(LEFT * 3)

        output_box = self.create_labeled_box("2ef7b...", "Hash Output", GREEN)
        output_box.shift(RIGHT * 3)

        arrow = Arrow(
            input_box.get_right(),
            output_box.get_left(),
            color=YELLOW,
            buff=0.3
        )

        self.show_clean(input_box, output_box, arrow)
        self.wait(self.slow)

        # Caption (integrated with visual)
        caption = self.create_caption("Same input always produces same output")
        self.show_clean(caption)
        self.wait(self.slow)

        # Clean exit
        self.hide_clean(title, input_box, output_box, arrow, caption)
```

## Specific Guidelines for Blockchain Visualizations

### 1. Hash Functions

```python
# Good: Simple, clear representation
def show_hash(self, input_data, hash_algo="SHA-256"):
    """
    Tufte principle: Show the data
    - Display input clearly
    - Show the transformation
    - Display output prominently
    """
    # Input
    input_text = Text(input_data, color=BLUE).scale(0.7)
    input_box = SurroundingRectangle(input_text, color=BLUE, buff=0.2)
    input_group = VGroup(input_box, input_text)

    # Hash algorithm label
    algo_label = Text(hash_algo, color=YELLOW).scale(0.6)

    # Output
    hash_value = hashlib.sha256(input_data.encode()).hexdigest()
    output_text = Text(hash_value[:16] + "...", color=GREEN, font="Fira Code").scale(0.5)
    output_box = SurroundingRectangle(output_text, color=GREEN, buff=0.2)
    output_group = VGroup(output_box, output_text)

    # Layout
    input_group.shift(LEFT * 3)
    output_group.shift(RIGHT * 3)
    algo_label.move_to(ORIGIN + UP * 0.3)

    # Arrow with algorithm label
    arrow = Arrow(input_group.get_right(), output_group.get_left(), buff=0.2)

    return VGroup(input_group, algo_label, arrow, output_group)
```

### 2. Merkle Trees

```python
# Good: Hierarchical clarity
def create_merkle_tree(self, transactions, show_full_hash=False):
    """
    Tufte principles:
    - Clear hierarchy (vertical layout)
    - Minimal decoration
    - Integrated labels
    """
    # Use consistent colors
    LEAF_COLOR = self.colors["secondary"]  # Green for leaves
    NODE_COLOR = self.colors["primary"]    # Blue for internal nodes
    ROOT_COLOR = self.colors["accent"]     # Yellow for root

    # Keep node size consistent
    # Use simple circles, not complex shapes
    # Label integration: put hash inside circle, full value on hover/click
    pass
```

### 3. Blockchain Structure

```python
# Good: Linear, clear chain
def create_blockchain(self, blocks):
    """
    Tufte principles:
    - Small multiples (identical block structure)
    - Clear connections (arrows)
    - Minimal decoration
    """
    BLOCK_WIDTH = 2.0
    BLOCK_HEIGHT = 1.5
    SPACING = 0.5

    chain = VGroup()

    for i, block_data in enumerate(blocks):
        # Create block (simple rectangle, not 3D cube)
        block = Rectangle(
            width=BLOCK_WIDTH,
            height=BLOCK_HEIGHT,
            color=WHITE,
            fill_color=self.colors["primary"],
            fill_opacity=0.3
        )

        # Add essential info only
        # - Block number
        # - Hash (abbreviated)
        # - Previous hash (abbreviated)
        block_num = Text(f"Block {i}", color=WHITE).scale(0.5)
        block_num.move_to(block.get_top() + DOWN * 0.3)

        block_group = VGroup(block, block_num)
        block_group.shift(RIGHT * i * (BLOCK_WIDTH + SPACING))

        chain.add(block_group)

    return chain
```

### 4. Stack Visualizations (Bitcoin Script)

```python
# Good: Vertical stack, clear operations
def create_stack_operation(self, operation, before_stack, after_stack):
    """
    Tufte principles:
    - Show before and after (small multiples)
    - Highlight the change
    - Integrate operation description
    """
    # Before state
    before = self.create_stack(before_stack)
    before.shift(LEFT * 3)
    before_label = Text("Before", color=GRAY).scale(0.5)
    before_label.next_to(before, UP)

    # After state
    after = self.create_stack(after_stack)
    after.shift(RIGHT * 3)
    after_label = Text("After", color=GRAY).scale(0.5)
    after_label.next_to(after, UP)

    # Operation (centered)
    op_text = Text(operation, color=self.colors["accent"]).scale(0.7)
    op_text.move_to(ORIGIN + UP * 0.5)
    op_arrow = Arrow(LEFT, RIGHT, color=YELLOW)
    op_arrow.move_to(ORIGIN)

    return VGroup(before, before_label, after, after_label, op_text, op_arrow)

def create_stack(self, elements):
    """Simple vertical stack"""
    stack = VGroup()
    for i, elem in enumerate(elements):
        elem_text = Text(elem, color=BLACK).scale(0.6)
        elem_box = SurroundingRectangle(
            elem_text,
            color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.8,
            buff=0.15
        )
        elem_group = VGroup(elem_box, elem_text)
        elem_group.shift(UP * i * 0.8)  # Vertical spacing
        stack.add(elem_group)

    return stack
```

## Anti-Patterns (What NOT to Do)

### ❌ Bad: Too Much Animation

```python
# DON'T: Excessive spinning, rotating, bouncing
self.play(
    Rotate(text, angle=TAU * 3),  # Why spin 3 times?
    run_time=5
)
```

### ✅ Good: Purposeful Animation

```python
# DO: Simple, clear transformations
self.play(FadeIn(text), run_time=0.5)
```

### ❌ Bad: Chartjunk

```python
# DON'T: Unnecessary 3D, shadows, gradients, glows
fancy_box = RoundedRectangle(...).set_sheen(-0.3, UL)  # Sheen not needed
fancy_box.set_gloss(0.5)  # Gloss distracts
```

### ✅ Good: Clean and Clear

```python
# DO: Simple, flat, focused
clean_box = Rectangle(color=WHITE, fill_color=BLUE, fill_opacity=0.3)
```

### ❌ Bad: Disconnected Text

```python
# DON'T: Separate explanation from visual
explanation = Text("This is a hash").to_edge(DOWN)
hash_visual = HashBox().to_edge(UP)
# Viewer has to look up and down
```

### ✅ Good: Integrated Labels

```python
# DO: Put text near what it describes
hash_visual = HashBox()
explanation = Text("This is a hash").next_to(hash_visual, UP, buff=0.2)
# Everything in one glance
```

## Performance Optimization

```python
# For faster rendering and iteration

# 1. Use static images for complex unchanging elements
# Instead of rendering the same complex logo every frame,
# use SVG or PNG

# 2. Cache expensive calculations
@cache
def compute_merkle_root(transactions):
    # This only runs once per unique input
    pass

# 3. Use low quality for development
# Command: manim -ql file.py Scene

# 4. Limit FPS for quick iteration
# config.frame_rate = 15  # Development
# config.frame_rate = 60  # Final render
```

## Accessibility Considerations

```python
# 1. Color contrast
# Ensure text is readable on all backgrounds
# Use: https://webaim.org/resources/contrastchecker/

# 2. Don't rely solely on color
# Use shapes, positions, labels too
# Good: "Red box (error)" not just red box

# 3. Font sizes
# Minimum: 0.5 scale for captions
# Preferred: 0.7 scale for body text

# 4. Animation speed
# Not too fast (viewers need time to read)
# Not too slow (respect viewer's time)
# Rule: If voiceover is present, sync to speech pace
```

## Voiceover Integration

```python
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class VoiceoverEducation(VoiceoverScene, BaseEducationalScene):
    def construct(self):
        # Set up voice
        self.set_speech_service(
            AzureService(
                voice="en-US-JennyNeural",
                style="newscast"  # Clear, professional
            )
        )

        with self.voiceover(
            text="Let's explore how hash functions work."
        ) as tracker:
            # Animations sync to voiceover duration
            # tracker.duration gives you the audio length
            hash_demo = self.show_hash("Hello", "SHA-256")
            self.play(FadeIn(hash_demo), run_time=tracker.duration * 0.8)

        # Rule: Animation should complete slightly before speech
        # Gives viewer time to absorb
```

## Testing Checklist

Before finalizing any animation:

- [ ] Does every element serve a purpose? (Data-ink ratio)
- [ ] Is text readable at 1080p? (Typography)
- [ ] Are colors accessible? (Contrast >= 4.5:1)
- [ ] Is the animation speed appropriate? (Not too fast/slow)
- [ ] Are labels integrated with graphics? (Not separate)
- [ ] Is the visual hierarchy clear? (Important things stand out)
- [ ] Would Tufte approve? (Minimal decoration, maximal information)
- [ ] Can someone understand it without audio? (Visual clarity)
- [ ] Does it respect the viewer's time? (No unnecessary waits)
- [ ] Is it accurate? (Verify technical details)

## Quick Reference: Scene Structure

```python
"""
Standard structure for one-shot visualization
"""

from manim import *

class MyEducationalScene(Scene):
    def construct(self):
        # 1. Setup (titles, constants)
        title = Text("Topic Name").to_edge(UP)

        # 2. Introduce (simple fade in)
        self.play(FadeIn(title))
        self.wait(1)

        # 3. Build concept (step by step)
        concept = self.build_visualization()
        self.play(Create(concept))
        self.wait(2)

        # 4. Demonstrate (show it in action)
        self.demonstrate(concept)
        self.wait(1)

        # 5. Emphasize key point
        key_point = self.highlight_key_point(concept)
        self.play(FadeIn(key_point))
        self.wait(2)

        # 6. Clean exit
        self.play(FadeOut(VGroup(title, concept, key_point)))

    def build_visualization(self):
        # Return VGroup of all visual elements
        pass

    def demonstrate(self, visual):
        # Show the concept in action
        pass

    def highlight_key_point(self, visual):
        # Return the key takeaway
        pass
```

## Resources

- **Tufte, Edward R.** *The Visual Display of Quantitative Information*
- **Manim Community Docs**: https://docs.manim.community/
- **Manim Physics**: https://github.com/Matheart/manim-physics (for physical simulations)
- **Color Contrast Checker**: https://webaim.org/resources/contrastchecker/
- **3Blue1Brown** (Grant Sanderson): Creator of Manim, excellent reference for style

---

**Remember**: The goal is education, not entertainment. Clarity trumps fanciness every time.
