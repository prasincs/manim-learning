# Quick Start Guide

## Getting Started with Your First Module

### 1. Choose a Module
Start with **Phase 1, Module 1.1 (Hash Functions Basics)** - it's foundational and relatively simple.

### 2. Development Workflow

```bash
# Create the file
touch scenes/phase1/01_hash_intro.py

# Develop with low quality (fast iteration)
manim -pql scenes/phase1/01_hash_intro.py HashIntro

# Final render in high quality
manim -pqh scenes/phase1/01_hash_intro.py HashIntro

# Output will be in media/videos/
```

### 3. Module Template

Use this template for each new module:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class ModuleName(VoiceoverScene):
    def construct(self):
        # Set up voiceover
        self.set_speech_service(
            AzureService(voice="en-US-JennyNeural", style="newscast")
        )

        # Title screen
        title = Text("Module Title Here")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        with self.voiceover(
            """Your voiceover script here."""
        ):
            # Your animations here
            pass

        self.wait(2)
```

### 4. Script Writing Tips

**Good voiceover script structure:**
1. **Hook** (5-10 seconds): "Ever wondered how Bitcoin ensures..."
2. **Explanation** (2-3 minutes): Core concept with visuals
3. **Example** (1-2 minutes): Concrete demonstration
4. **Summary** (30 seconds): Key takeaways

**Keep it conversational:**
- ✅ "Let's see what happens when we change one bit..."
- ❌ "The alteration of a single bit results in..."

### 5. Animation Best Practices

```python
# Create objects first
circle = Circle()
text = Text("Hello")

# Then animate them
self.play(Create(circle))
self.play(Write(text))

# Use appropriate timing
self.wait(1)  # Give viewers time to absorb

# Clean up before next section
self.play(FadeOut(circle), FadeOut(text))
```

### 6. Common Manim Patterns

**Stack visualization:**
```python
stack = VGroup()
for item in ["item1", "item2", "item3"]:
    text = Text(item)
    box = SurroundingRectangle(text)
    element = VGroup(text, box)
    stack.add(element)

stack.arrange(DOWN, buff=0.1)
```

**Tree visualization:**
```python
# Use graphs for trees
from manim import Graph

vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
tree = Graph(vertices, edges, layout="tree", root_vertex=1)
```

**Hash function metaphor:**
```python
# Input box
input_box = Rectangle(width=2, height=1, color=BLUE)
input_text = Text("Input Data").scale(0.5).move_to(input_box)

# Hash machine
machine = Rectangle(width=3, height=2, color=GRAY)
machine_label = Text("Hash Function").scale(0.6).move_to(machine)

# Output box
output_box = Rectangle(width=4, height=1, color=GREEN)
output_text = Text("Hash Output").scale(0.5).move_to(output_box)

# Arrows
arrow1 = Arrow(input_box.get_right(), machine.get_left())
arrow2 = Arrow(machine.get_right(), output_box.get_left())
```

### 7. Testing Checklist

Before rendering final version:

- [ ] Voiceover timing matches animations
- [ ] Text is readable (not too small)
- [ ] Colors have good contrast
- [ ] Animations aren't too fast or slow
- [ ] Key concepts are highlighted/emphasized
- [ ] Clean transitions between sections
- [ ] No objects left on screen accidentally
- [ ] Total runtime is 5-10 minutes

### 8. Render Quality Settings

```bash
# Development (fast, low quality)
manim -ql file.py Scene      # 480p 15fps

# Preview (medium quality)
manim -qm file.py Scene      # 720p 30fps

# YouTube (high quality)
manim -qh file.py Scene      # 1080p 60fps

# 4K (if needed)
manim -qk file.py Scene      # 2160p 60fps
```

### 9. Organize Your Outputs

```bash
# After rendering, organize files
mkdir -p outputs/phase1
cp media/videos/phase1/01_hash_intro/1080p60/HashIntro.mp4 outputs/phase1/

# Update ROADMAP.md with completion status
```

### 10. Git Workflow

```bash
# After completing a module
git add scenes/phase1/01_hash_intro.py
git add outputs/phase1/HashIntro.mp4
git commit -m "Add Phase 1 Module 1.1: Hash Functions Basics"
git push -u origin claude/blockchain-crypto-learning-014jVej5QU6dHfaTYgiHR7Xq
```

## Recommended First 5 Modules

To maximize learning value, start with these:

1. **1.1 Hash Functions Basics** - Foundation for everything
2. **1.6 Public Key Crypto Intro** - Core concept
3. **2.2 UTXOs Explained** - Bitcoin's key innovation
4. **1.4 Merkle Trees Part 1** - Used everywhere
5. **3.1 Block Structure** - Understand blocks

These 5 modules will give you a solid foundation and reusable components for future videos.

## Time Estimates

**Per module average:**
- Research & scripting: 1-2 hours
- Coding animations: 2-4 hours
- Testing & iteration: 1 hour
- Final render: 30 minutes
- **Total: 4.5-7.5 hours per module**

**For 10 modules:** ~50-75 hours of work
**For 30 modules:** ~150-225 hours of work

## Next Steps

1. Run setup script: `bash setup_project.sh`
2. Pick your first module from the recommended list
3. Write the script in `scripts/01_hash_intro.txt`
4. Code the animation in `scenes/phase1/01_hash_intro.py`
5. Iterate until happy
6. Render and publish!

Good luck! 🚀
