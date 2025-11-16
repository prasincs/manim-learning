#!/bin/bash
# Simple test script to diagnose rendering issues
# Run this to test if a single scene can render

set -e

echo "========================================="
echo "Manim Render Test Script"
echo "========================================="
echo ""

# Test 1: Check Python and Manim
echo "Test 1: Checking Manim installation..."
python3 -c "import manim; print(f'Manim version: {manim.__version__}')"
echo "✓ Manim imported successfully"
echo ""

# Test 2: Check FFmpeg
echo "Test 2: Checking FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    ffmpeg -version | head -n1
    echo "✓ FFmpeg available"
else
    echo "✗ FFmpeg not found"
    exit 1
fi
echo ""

# Test 3: Test basic Manim text rendering
echo "Test 3: Testing basic Text rendering..."
python3 << 'EOF'
from manim import Text
try:
    t = Text("Hello World")
    print(f"✓ Text object created: {type(t)}")
except Exception as e:
    print(f"✗ Failed to create Text: {e}")
    exit(1)
EOF
echo ""

# Test 4: Render a minimal scene
echo "Test 4: Rendering a minimal test scene..."
mkdir -p /tmp/manim_test

cat > /tmp/manim_test/test.py << 'EOF'
from manim import *

class MinimalTest(Scene):
    def construct(self):
        text = Text("Test", color=WHITE)
        self.add(text)
        self.wait(1)
EOF

cd /tmp/manim_test
echo "Attempting to render MinimalTest scene..."
manim -ql --format=gif test.py MinimalTest

if [ $? -eq 0 ]; then
    echo "✓ Render completed"
    echo ""
    echo "Looking for output file..."
    find . -name "*.gif" -type f
    echo ""
    echo "Directory structure:"
    ls -lR media/ 2>/dev/null || echo "No media directory"
else
    echo "✗ Render failed"
    exit 1
fi

echo ""
echo "========================================="
echo "All tests passed!"
echo "========================================="
