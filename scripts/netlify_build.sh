#!/bin/bash
# Netlify build script for Manim Learning Project
# This script installs dependencies, renders GIFs, and prepares the site for deployment

set -e  # Exit on error

# Color output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Manim Learning - Netlify Build${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Step 1: Install system dependencies (user space - no root required)
echo -e "${YELLOW}Step 1/5: Installing system dependencies...${NC}"

# Create local bin directory for user-space binaries
mkdir -p $HOME/.local/bin
export PATH="$HOME/.local/bin:$PATH"

# Check if FFmpeg is already available (from Netlify's build image)
echo -e "${BLUE}Checking for FFmpeg...${NC}"
if command -v ffmpeg &> /dev/null; then
    echo -e "${GREEN}  ✓ FFmpeg found: $(ffmpeg -version | head -n1)${NC}"
else
    echo -e "${YELLOW}  FFmpeg not found, installing from static build...${NC}"

    # Download FFmpeg static build (no root required)
    cd /tmp
    wget -q https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
    tar xf ffmpeg-release-amd64-static.tar.xz

    # Copy to local bin
    find . -name "ffmpeg" -type f -executable -exec cp {} $HOME/.local/bin/ \;
    find . -name "ffprobe" -type f -executable -exec cp {} $HOME/.local/bin/ \;

    # Verify installation
    if command -v ffmpeg &> /dev/null; then
        echo -e "${GREEN}  ✓ FFmpeg installed successfully${NC}"
    else
        echo -e "${RED}  ✗ FFmpeg installation failed${NC}"
        exit 1
    fi

    # Clean up
    cd -
    rm -rf /tmp/ffmpeg-*
fi

echo -e "${BLUE}Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}  ✓ Python found: $(python3 --version)${NC}"
else
    echo -e "${RED}  ✗ Python not found${NC}"
    exit 1
fi

# Check for Cairo library (required for rendering)
echo -e "${BLUE}Checking for Cairo library...${NC}"
if ldconfig -p | grep -q libcairo; then
    echo -e "${GREEN}  ✓ Cairo library found${NC}"
else
    echo -e "${YELLOW}  ! Cairo library not found in ldconfig, but may still be available${NC}"
fi

# Check for Pango library (required for text rendering)
echo -e "${BLUE}Checking for Pango library...${NC}"
if ldconfig -p | grep -q libpango; then
    echo -e "${GREEN}  ✓ Pango library found${NC}"
else
    echo -e "${YELLOW}  ! Pango library not found in ldconfig, but may still be available${NC}"
fi

# Note: LaTeX is skipped for preview builds (not required for simple text)
# Manim can use simpler text rendering without LaTeX
echo -e "${YELLOW}  Note: LaTeX disabled for preview builds (using simple text rendering)${NC}"

echo -e "${GREEN}✓ System dependencies ready${NC}"
echo ""

# Step 2: Install Python dependencies
echo -e "${YELLOW}Step 2/5: Installing Python dependencies...${NC}"

# Upgrade pip first
pip install --upgrade pip --quiet

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}  ✓ Requirements installed${NC}"
else
    echo -e "${RED}  ✗ requirements.txt not found${NC}"
    exit 1
fi

# Verify Manim installation
if python3 -c "import manim" 2>/dev/null; then
    MANIM_VERSION=$(python3 -c "import manim; print(manim.__version__)" 2>/dev/null)
    echo -e "${GREEN}  ✓ Manim v${MANIM_VERSION} installed${NC}"
else
    echo -e "${RED}  ✗ Manim installation failed${NC}"
    exit 1
fi

# Check if manim command is available, if not use python -m manim
if command -v manim &> /dev/null; then
    MANIM_CMD="manim"
    echo -e "${GREEN}  ✓ Manim command available in PATH${NC}"
else
    MANIM_CMD="python3 -m manim"
    echo -e "${YELLOW}  ! Using 'python3 -m manim' instead of 'manim' command${NC}"
fi

echo -e "${GREEN}✓ Python dependencies installed${NC}"
echo ""

# Step 3: Create output directory
echo -e "${YELLOW}Step 3/5: Setting up output directories...${NC}"
mkdir -p public/previews/phase1
mkdir -p public/previews/phase2
mkdir -p media
echo -e "${GREEN}✓ Output directories created${NC}"
echo ""

# Step 4: Render preview GIFs
echo -e "${YELLOW}Step 4/5: Rendering preview GIFs...${NC}"

# Set PYTHONPATH to include the repository root so components module can be found
export PYTHONPATH="$(pwd):${PYTHONPATH}"
echo -e "${BLUE}PYTHONPATH set to: $(pwd)${NC}"
echo ""

# First, test if Manim can render at all with a simple test
echo -e "${BLUE}Running Manim smoke test...${NC}"
TEST_RESULT=$(python3 -c "
import sys
from manim import *

try:
    # Test 1: Basic text rendering
    t = Text('Hello')
    print('✓ Manim text rendering works')

    # Test 2: Import components module
    from components import HashMachine, DataBox
    print('✓ Components module imports successfully')

    print('SUCCESS: All smoke tests passed')
except ImportError as e:
    print(f'ERROR: Import failed - {str(e)}')
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f'ERROR: {str(e)}')
    import traceback
    traceback.print_exc()
" 2>&1)

echo "$TEST_RESULT"
if echo "$TEST_RESULT" | grep -q "SUCCESS"; then
    echo -e "${GREEN}  ✓ Manim smoke test passed${NC}"
elif echo "$TEST_RESULT" | grep -q "ERROR"; then
    echo -e "${RED}  ✗ Manim cannot render - check error above${NC}"
    echo -e "${YELLOW}  Continuing anyway to see specific scene errors...${NC}"
fi
echo ""

echo -e "${BLUE}Rendering scenes (this may take 10-20 minutes)...${NC}"
echo ""

PHASE1_DIR="scenes/phase1"
PREVIEW_DIR="public/previews/phase1"

# Function to render a single module's preview
render_module() {
    local module_file=$1
    local scene_name=$2
    local output_name=$3
    local module_num=$4

    echo -e "${BLUE}  [$module_num/14] Rendering: ${scene_name}${NC}"

    # Render as GIF with low quality for fast preview
    # Capture both stdout and stderr to a temp file for debugging
    RENDER_LOG="/tmp/render_${module_num}.log"

    if $MANIM_CMD -ql --format=gif \
        --output_file="${output_name}" \
        "${PHASE1_DIR}/${module_file}" \
        "${scene_name}" > "$RENDER_LOG" 2>&1; then

        # Rendering succeeded
        if find media -name "${output_name}" -type f -exec cp {} "${PREVIEW_DIR}/" \; 2>/dev/null; then
            echo -e "${GREEN}    ✓ Created: ${output_name}${NC}"
            rm -f "$RENDER_LOG"
            return 0
        else
            echo -e "${RED}    ✗ Render succeeded but GIF not found: ${output_name}${NC}"
            echo -e "${YELLOW}    Last 10 lines of output:${NC}"
            tail -10 "$RENDER_LOG" | sed 's/^/      /'
            rm -f "$RENDER_LOG"
            return 1
        fi
    else
        # Rendering failed
        echo -e "${RED}    ✗ Failed to render: ${scene_name}${NC}"
        echo -e "${YELLOW}    Error output (last 15 lines):${NC}"
        tail -15 "$RENDER_LOG" | sed 's/^/      /'
        rm -f "$RENDER_LOG"
        return 1
    fi
}

# Define all modules and their key scenes for preview
# Format: "file.py|SceneName|output.gif"
MODULES=(
    "01_hash_intro.py|HashIntroduction|01_hash_intro.gif|01"
    "02_sha256.py|SHA256Overview|02_sha256.gif|02"
    "03_ripemd160.py|Hash160Visualization|03_ripemd160.gif|03"
    "04_merkle_trees_intro.py|BuildingMerkleTree|04_merkle_tree.gif|04"
    "05_merkle_proofs.py|ProofExample|05_merkle_proof.gif|05"
    "06_public_key_intro.py|PublicKeyIntro|06_public_key.gif|06"
    "07_elliptic_curves_intro.py|EllipticCurveVisualization|07_elliptic_curve.gif|07"
    "08_elliptic_curves_math.py|ScalarMultiplicationVisualization|08_ec_math.gif|08"
    "09_ecdsa_signing.py|ECDSASigningVisualization|09_ecdsa_sign.gif|09"
    "10_ecdsa_verification.py|ECDSAVerificationVisualization|10_ecdsa_verify.gif|10"
    "11_schnorr_intro.py|SchnorrVsECDSA|11_schnorr.gif|11"
    "12_schnorr_aggregation.py|MuSigProtocol|12_schnorr_agg.gif|12"
    "13_signatures_practice.py|NonceReuseDemo|13_sig_practice.gif|13"
    "14_encoding.py|Base58CheckProcess|14_encoding.gif|14"
)

# Check if phase1 scenes exist, if not skip rendering
if [ ! -d "$PHASE1_DIR" ]; then
    echo -e "${RED}✗ Warning: $PHASE1_DIR not found. Skipping preview rendering.${NC}"
    echo -e "${YELLOW}  Current directory: $(pwd)${NC}"
    echo -e "${YELLOW}  Directory listing:${NC}"
    ls -la scenes/ 2>/dev/null || echo "  No scenes directory found"
else
    echo -e "${GREEN}✓ Found ${PHASE1_DIR} directory${NC}"
    FILE_COUNT=$(ls -1 "${PHASE1_DIR}"/*.py 2>/dev/null | wc -l)
    echo -e "${BLUE}  Found ${FILE_COUNT} Python files in ${PHASE1_DIR}${NC}"
    echo ""

    # Render all modules
    RENDERED=0
    FAILED=0
    SKIPPED=0

    for module_info in "${MODULES[@]}"; do
        IFS='|' read -r file scene output num <<< "$module_info"

        # Check if the file exists before trying to render
        if [ -f "${PHASE1_DIR}/${file}" ]; then
            render_module "$file" "$scene" "$output" "$num"
            if [ $? -eq 0 ]; then
                ((RENDERED++))
            else
                ((FAILED++))
            fi
        else
            echo -e "${YELLOW}  [$num/14] Skipping: ${file} (not found)${NC}"
            ((SKIPPED++))
        fi
    done

    echo ""
    echo -e "${BLUE}Rendering Summary:${NC}"
    echo -e "  ${GREEN}Rendered: ${RENDERED}${NC}"
    echo -e "  ${RED}Failed: ${FAILED}${NC}"
    echo -e "  ${YELLOW}Skipped: ${SKIPPED}${NC}"
fi

echo ""
echo -e "${GREEN}✓ Preview rendering complete${NC}"
echo ""

# Step 5: Generate index.html
echo -e "${YELLOW}Step 5/5: Generating gallery page...${NC}"

# Copy static assets if they exist
if [ -f "public_template/index.html" ]; then
    cp public_template/index.html public/
else
    # Will be created by a separate script
    echo "Note: index.html will be created separately"
fi

# Copy CSS/JS if they exist
if [ -d "public_template/css" ]; then
    cp -r public_template/css public/
fi

if [ -d "public_template/js" ]; then
    cp -r public_template/js public/
fi

echo -e "${GREEN}✓ Gallery page generated${NC}"
echo ""

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Build Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "Output directory: ${BLUE}public/${NC}"
echo -e "Preview GIFs: ${BLUE}public/previews/phase1/${NC}"
echo ""

# List generated files
GIF_COUNT=$(find public/previews/phase1 -name "*.gif" 2>/dev/null | wc -l)
echo -e "Generated ${GREEN}${GIF_COUNT}${NC} preview GIFs"

# Show total size
TOTAL_SIZE=$(du -sh public 2>/dev/null | cut -f1)
echo -e "Total build size: ${GREEN}${TOTAL_SIZE}${NC}"
echo ""

echo -e "${GREEN}Ready for deployment!${NC}"
