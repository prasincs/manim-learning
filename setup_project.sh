#!/bin/bash

# Setup script for blockchain & cryptography learning project

echo "Setting up project structure..."

# Create directory structure
mkdir -p scenes/{phase1,phase2,phase3,phase4,phase5,phase6}
mkdir -p scripts/{phase1,phase2,phase3,phase4,phase5,phase6}
mkdir -p outputs/{phase1,phase2,phase3,phase4,phase5,phase6}
mkdir -p components
mkdir -p assets

echo "✓ Created directory structure"

# Move existing files to appropriate locations
if [ -f "simpletransactionintro.py" ]; then
    mv simpletransactionintro.py scenes/phase2/
    echo "✓ Moved simpletransactionintro.py to scenes/phase2/"
fi

if [ -f "covenants.py" ]; then
    mv covenants.py scenes/phase2/
    echo "✓ Moved covenants.py to scenes/phase2/"
fi

# Create .gitignore additions
cat >> .gitignore << 'EOF'

# Manim outputs
media/
__pycache__/
*.pyc

# Voiceover cache
media/voiceover/

# OS files
.DS_Store
Thumbs.db

# IDEs
.vscode/
.idea/
*.swp
*.swo
EOF

echo "✓ Updated .gitignore"

# Create a components __init__.py
touch components/__init__.py

echo "✓ Created components package"

echo ""
echo "Project setup complete!"
echo ""
echo "Directory structure:"
echo "├── scenes/          # Manim animation files"
echo "│   ├── phase1/     # Cryptography fundamentals"
echo "│   ├── phase2/     # Bitcoin fundamentals"
echo "│   ├── phase3/     # Blockchain fundamentals"
echo "│   ├── phase4/     # Layer 2 & advanced"
echo "│   ├── phase5/     # Advanced cryptography"
echo "│   └── phase6/     # Alternative consensus"
echo "├── scripts/         # Voiceover scripts"
echo "├── outputs/         # Final rendered videos"
echo "├── components/      # Reusable animation components"
echo "└── assets/          # Images, logos, etc."
echo ""
echo "Next steps:"
echo "1. Review ROADMAP.md for full module list"
echo "2. Check QUICK_START.md for development workflow"
echo "3. Start with Phase 1, Module 1.1!"
