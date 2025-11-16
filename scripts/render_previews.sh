#!/bin/bash
# Script to render preview GIFs for Phase 1 modules
# Usage: ./scripts/render_previews.sh [module_number or 'all']
# Example: ./scripts/render_previews.sh 01
#          ./scripts/render_previews.sh all

set -e

PHASE1_DIR="scenes/phase1"
PREVIEW_DIR="previews/phase1"

# Create preview directory if it doesn't exist
mkdir -p "$PREVIEW_DIR"

# Color output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to render a single module's preview
render_module() {
    local module_file=$1
    local module_name=$2
    local scene_name=$3
    local output_name=$4

    echo -e "${BLUE}Rendering: ${module_name} - ${scene_name}${NC}"

    # Render as GIF with low quality for fast preview
    manim -ql --format=gif \
        --output_file="${output_name}" \
        "${PHASE1_DIR}/${module_file}" \
        "${scene_name}" \
        --media_dir="${PREVIEW_DIR}/.."

    # Move to preview directory
    find media/videos -name "${output_name}" -type f -exec mv {} "${PREVIEW_DIR}/" \;

    echo -e "${GREEN}✓ Created: ${PREVIEW_DIR}/${output_name}${NC}"
}

# Define all modules and their key scenes for preview
declare -A MODULES=(
    ["01"]="01_hash_intro.py|HashIntroduction|01_hash_intro.gif"
    ["02"]="02_sha256.py|SHA256Overview|02_sha256.gif"
    ["03"]="03_ripemd160.py|Hash160Visualization|03_ripemd160.gif"
    ["04"]="04_merkle_trees_intro.py|BuildingMerkleTree|04_merkle_tree.gif"
    ["05"]="05_merkle_proofs.py|ProofExample|05_merkle_proof.gif"
    ["06"]="06_public_key_intro.py|PublicKeyIntro|06_public_key.gif"
    ["07"]="07_elliptic_curves_intro.py|EllipticCurveVisualization|07_elliptic_curve.gif"
    ["08"]="08_elliptic_curves_math.py|ScalarMultiplicationVisualization|08_ec_math.gif"
    ["09"]="09_ecdsa_signing.py|ECDSASigningVisualization|09_ecdsa_sign.gif"
    ["10"]="10_ecdsa_verification.py|ECDSAVerificationVisualization|10_ecdsa_verify.gif"
    ["11"]="11_schnorr_intro.py|SchnorrVsECDSA|11_schnorr.gif"
    ["12"]="12_schnorr_aggregation.py|MuSigProtocol|12_schnorr_agg.gif"
    ["13"]="13_signatures_practice.py|NonceReuseDemo|13_sig_practice.gif"
    ["14"]="14_encoding.py|Base58CheckProcess|14_encoding.gif"
)

# Parse command line argument
MODULE=${1:-all}

if [ "$MODULE" == "all" ]; then
    echo "Rendering previews for all Phase 1 modules..."
    for key in "${!MODULES[@]}"; do
        IFS='|' read -r file scene output <<< "${MODULES[$key]}"
        render_module "$file" "Module $key" "$scene" "$output"
    done
else
    # Render single module
    if [[ -n "${MODULES[$MODULE]}" ]]; then
        IFS='|' read -r file scene output <<< "${MODULES[$MODULE]}"
        render_module "$file" "Module $MODULE" "$scene" "$output"
    else
        echo "Error: Invalid module number. Use 01-14 or 'all'"
        exit 1
    fi
fi

echo ""
echo -e "${GREEN}Preview rendering complete!${NC}"
echo "Previews saved to: ${PREVIEW_DIR}/"
echo ""
echo "To view previews, open the files in ${PREVIEW_DIR}/ or check PREVIEWS.md"
