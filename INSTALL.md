# Installation Guide

Quick guide to set up your environment for creating Manim animations.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/prasincs/manim-learning.git
cd manim-learning
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `manim` (v0.18.0+) - The animation library
- `numpy` - Mathematical operations
- `pillow` - Image processing

### 3. Verify Installation

Test that Manim is installed correctly:

```bash
manim --version
```

You should see something like: `Manim Community v0.18.0`

### 4. Test Render

Try rendering the example module:

```bash
manim -pql EXAMPLE_MODULE.py HashFunctionIntro
```

This should:
1. Render a low-quality preview
2. Open the video automatically
3. Create output in `media/videos/`

## Optional: Voiceover Support

If you want to add voiceovers to your animations:

```bash
pip install manim-voiceover[azure]
```

See the [Manim Voiceover docs](https://voiceover.manim.community/) for setup.

## System-Specific Notes

### macOS

If you encounter issues, you may need to install additional dependencies:

```bash
brew install cairo ffmpeg pango pkg-config scipy
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

### Windows

Use WSL (Windows Subsystem for Linux) or install dependencies via chocolatey:

```bash
choco install python ffmpeg
```

## Troubleshooting

### "manim: command not found"

Make sure Python's bin directory is in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Add this to your `~/.bashrc` or `~/.zshrc` to make it permanent.

### Import errors

If you get import errors for components:

```bash
# Make sure you're in the project directory
cd /path/to/manim-learning

# Python should find the components package
python3 -c "from components import HashMachine; print('OK')"
```

### Rendering is slow

- Use `-ql` (low quality) for development
- Close other applications
- Upgrade your hardware (GPU helps)

### FFmpeg errors

Manim requires FFmpeg for video rendering. Install it:

- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`
- Windows: Download from [ffmpeg.org](https://ffmpeg.org/)

## Development Setup

For active development, consider installing in editable mode:

```bash
# Install in development mode
pip install -e .

# Install development tools
pip install black flake8 pytest
```

## IDE Setup

### VS Code

Recommended extensions:
- Python (Microsoft)
- Pylance
- Black Formatter
- GitLens

Settings (`.vscode/settings.json`):
```json
{
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "editor.formatOnSave": true
}
```

### PyCharm

1. Open the project folder
2. Configure Python interpreter (File → Settings → Project → Python Interpreter)
3. Select the virtual environment or system Python with manim installed

## Virtual Environment (Recommended)

To avoid conflicts with system packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt

# When done, deactivate
deactivate
```

## Next Steps

After installation:

1. ✅ Read [GET_STARTED.md](GET_STARTED.md) for project overview
2. ✅ Check [ROADMAP.md](ROADMAP.md) for module list
3. ✅ Review [CLAUDE.md](CLAUDE.md) for visualization guidelines
4. ✅ Try the [QUICK_START.md](QUICK_START.md) workflow

## Getting Help

- **Manim Community Docs**: https://docs.manim.community/
- **Manim Discord**: https://www.manim.community/discord/
- **Issue Tracker**: https://github.com/ManimCommunity/manim/issues

---

Happy animating! 🎬
