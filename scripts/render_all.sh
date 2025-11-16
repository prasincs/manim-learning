#!/bin/bash
# Render all Phase 1 scenes
# This script is used by Docker builds where LaTeX is available

set -e

PHASE1_DIR="scenes/phase1"
PREVIEW_DIR="public/previews/phase1"

echo "========================================="
echo "Rendering All Phase 1 Scenes"
echo "========================================="
echo ""

# Define all scenes to render
declare -A SCENES=(
    ["01_hash_intro.py"]="HashIntroduction"
    ["02_sha256.py"]="SHA256Overview"
    ["03_ripemd160.py"]="Hash160Visualization"
    ["04_merkle_trees_intro.py"]="BuildingMerkleTree"
    ["05_merkle_proofs.py"]="ProofExample"
    ["06_public_key_intro.py"]="PublicKeyIntroduction"
    ["07_elliptic_curves_intro.py"]="EllipticCurveIntroduction"
    ["08_elliptic_curves_math.py"]="VisualizingScalarMultiplication"
    ["09_ecdsa_signing.py"]="SigningVisualization"
    ["10_ecdsa_verification.py"]="VerificationVisualization"
    ["11_schnorr_intro.py"]="ECDSAvsSchnorr"
    ["12_schnorr_aggregation.py"]="MuSigProtocol"
    ["13_signatures_practice.py"]="NonceReuseDeepDive"
    ["14_encoding.py"]="Base58CheckEncoding"
)

# Output file names
declare -A OUTPUTS=(
    ["01_hash_intro.py"]="01_hash_intro.gif"
    ["02_sha256.py"]="02_sha256.gif"
    ["03_ripemd160.py"]="03_ripemd160.gif"
    ["04_merkle_trees_intro.py"]="04_merkle_tree.gif"
    ["05_merkle_proofs.py"]="05_merkle_proof.gif"
    ["06_public_key_intro.py"]="06_public_key.gif"
    ["07_elliptic_curves_intro.py"]="07_elliptic_curve.gif"
    ["08_elliptic_curves_math.py"]="08_ec_math.gif"
    ["09_ecdsa_signing.py"]="09_ecdsa_sign.gif"
    ["10_ecdsa_verification.py"]="10_ecdsa_verify.gif"
    ["11_schnorr_intro.py"]="11_schnorr.gif"
    ["12_schnorr_aggregation.py"]="12_schnorr_agg.gif"
    ["13_signatures_practice.py"]="13_sig_practice.gif"
    ["14_encoding.py"]="14_encoding.gif"
)

RENDERED=0
FAILED=0
COUNT=1

# Render each scene
for file in $(echo "${!SCENES[@]}" | tr ' ' '\n' | sort); do
    scene="${SCENES[$file]}"
    output="${OUTPUTS[$file]}"

    echo "[$COUNT/14] Rendering: $scene"

    if manim -ql --format=gif \
        --output_file="$output" \
        "${PHASE1_DIR}/${file}" \
        "${scene}" 2>&1 | grep -i "file ready at"; then

        # Find and copy the generated GIF
        if find media -name "$output" -type f -exec cp {} "${PREVIEW_DIR}/" \; 2>/dev/null; then
            echo "  ✓ Created: $output"
            ((RENDERED++))
        else
            echo "  ✗ Failed to find: $output"
            ((FAILED++))
        fi
    else
        echo "  ✗ Render failed: $scene"
        ((FAILED++))
    fi

    ((COUNT++))
    echo ""
done

echo "========================================="
echo "Rendering Summary"
echo "========================================="
echo "Rendered: $RENDERED"
echo "Failed: $FAILED"
echo ""

if [ $FAILED -gt 0 ]; then
    echo "⚠ Some scenes failed to render"
    exit 1
fi

echo "✓ All scenes rendered successfully!"
