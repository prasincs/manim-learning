# Preview GIFs for Phase 1 Modules

This document explains how to generate and view preview GIFs for the Phase 1 cryptography modules.

## Setup

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Rendering Previews

### Render All Previews

To generate preview GIFs for all Phase 1 modules:

```bash
chmod +x scripts/render_previews.sh
./scripts/render_previews.sh all
```

This will create GIF previews in the `previews/phase1/` directory.

### Render Single Module

To generate a preview for a specific module (e.g., module 01):

```bash
./scripts/render_previews.sh 01
```

### Manual Rendering

You can also render individual scenes manually:

```bash
# Low quality GIF (fast, for previews)
manim -ql --format=gif scenes/phase1/01_hash_intro.py HashIntroduction

# Medium quality GIF
manim -qm --format=gif scenes/phase1/01_hash_intro.py HashIntroduction

# High quality MP4 (for production)
manim -qh scenes/phase1/01_hash_intro.py HashIntroduction
```

## Preview Gallery

Below is what each module demonstrates. After rendering, GIFs will appear here:

### 1.1 Hash Functions Basics
**File**: `01_hash_intro.gif`
**Scene**: `HashIntroduction`
**Shows**: Basic hash function concept, input → hash machine → output

**Topics Covered:**
- What is a hash function?
- Deterministic property
- One-way property
- Collision resistance
- Avalanche effect

---

### 1.2 SHA-256 Deep Dive
**File**: `02_sha256.gif`
**Scene**: `SHA256Overview`
**Shows**: SHA-256 process overview with 4 main steps

**Topics Covered:**
- Message padding
- Initial hash values
- Compression function (64 rounds)
- Final hash production

---

### 1.3 RIPEMD-160
**File**: `03_ripemd160.gif`
**Scene**: `Hash160Visualization`
**Shows**: Hash160 = RIPEMD160(SHA256(data)) process

**Topics Covered:**
- RIPEMD-160 algorithm
- Hash160 two-step process
- Bitcoin address generation

---

### 1.4 Merkle Trees Part 1
**File**: `04_merkle_tree.gif`
**Scene**: `BuildingMerkleTree`
**Shows**: Animated construction of Merkle tree from 4 transactions

**Topics Covered:**
- Tree structure
- Building bottom-up
- Root hash computation
- Tamper-evident property

---

### 1.5 Merkle Trees Part 2
**File**: `05_merkle_proof.gif`
**Scene**: `ProofExample`
**Shows**: Merkle proof verification for a specific transaction

**Topics Covered:**
- Proof path concept
- Verification algorithm
- SPV wallets
- Logarithmic efficiency

---

### 1.6 Public Key Cryptography Intro
**File**: `06_public_key.gif`
**Scene**: `PublicKeyIntro`
**Shows**: Asymmetric encryption concept

**Topics Covered:**
- Key pairs
- Lock and key metaphor
- Alice & Bob scenario
- Public vs private usage

---

### 1.7 Elliptic Curves Basics
**File**: `07_elliptic_curve.gif`
**Scene**: `EllipticCurveVisualization`
**Shows**: Elliptic curve y² = x³ + 7 with point addition

**Topics Covered:**
- Curve equation
- Point addition geometry
- Point doubling
- Curve properties

---

### 1.8 Elliptic Curves Math
**File**: `08_ec_math.gif`
**Scene**: `ScalarMultiplicationVisualization`
**Shows**: Scalar multiplication k * G

**Topics Covered:**
- Scalar multiplication
- Generator point
- Discrete log problem
- Public key = private key * G

---

### 1.9 ECDSA Signing
**File**: `09_ecdsa_sign.gif`
**Scene**: `ECDSASigningVisualization`
**Shows**: ECDSA signing process flow

**Topics Covered:**
- Signing algorithm
- Nonce importance
- r and s values
- Deterministic nonces (RFC 6979)

---

### 1.10 ECDSA Verification
**File**: `10_ecdsa_verify.gif`
**Scene**: `ECDSAVerificationVisualization`
**Shows**: ECDSA verification process

**Topics Covered:**
- Verification algorithm
- Mathematical proof
- Invalid signature detection
- Security properties

---

### 1.11 Schnorr Signatures Intro
**File**: `11_schnorr.gif`
**Scene**: `SchnorrVsECDSA`
**Shows**: Comparison between Schnorr and ECDSA

**Topics Covered:**
- Schnorr advantages
- Simpler algorithm
- Linearity property
- Signature size comparison

---

### 1.12 Schnorr Math & Aggregation
**File**: `12_schnorr_agg.gif`
**Scene**: `MuSigProtocol`
**Shows**: MuSig protocol for signature aggregation

**Topics Covered:**
- Signature aggregation
- Key aggregation
- Multi-signature scenarios
- Batch verification

---

### 1.13 Digital Signatures in Practice
**File**: `13_sig_practice.gif`
**Scene**: `NonceReuseDemo`
**Shows**: Nonce reuse attack demonstration

**Topics Covered:**
- Common pitfalls
- Nonce reuse vulnerability
- PlayStation 3 incident
- Best practices

---

### 1.14 Base58 & Bech32 Encoding
**File**: `14_encoding.gif`
**Scene**: `Base58CheckProcess`
**Shows**: Base58Check encoding step-by-step

**Topics Covered:**
- Base58 alphabet
- Checksum addition
- Bech32 format
- QR code friendliness

---

## File Sizes

Preview GIFs are rendered at low quality (`-ql` flag) to keep file sizes reasonable for git:

- Expected size per GIF: ~500KB - 2MB
- Total for all 14 previews: ~10-20MB

## Checking Previews into Git

After rendering, you can commit the preview GIFs:

```bash
git add previews/phase1/*.gif
git commit -m "Add preview GIFs for Phase 1 modules"
git push
```

## Viewing Previews

### On GitHub
When pushed to GitHub, the GIFs will display inline in this markdown file.

### Locally
Open the GIF files in any image viewer or web browser.

### In VS Code
Install the "GIF Preview" extension to view GIFs directly in the editor.

## Rendering Tips

1. **Low quality for previews**: Use `-ql` for fast, small GIFs
2. **Medium quality for sharing**: Use `-qm` for better quality
3. **High quality for production**: Use `-qh` for final videos (MP4, not GIF)

4. **Render specific scenes**:
   ```bash
   # List all scenes in a file
   manim scenes/phase1/01_hash_intro.py -l

   # Render specific scene
   manim -ql --format=gif scenes/phase1/01_hash_intro.py AvalancheEffectDemo
   ```

5. **Speed up rendering**:
   - Use `-ql` (low quality) during development
   - Render on a machine with a good GPU
   - Close other applications to free up resources

## Troubleshooting

### "manim: command not found"
Install manim: `pip install -r requirements.txt`

### GIF file too large
Use lower quality flag or shorter scene

### Rendering is slow
- Use `-ql` instead of `-qm` or `-qh`
- Reduce scene complexity
- Render fewer frames

### Preview looks different from expected
Check that you're using the latest code from the repository

## Alternative: Static Thumbnails

If GIFs are too large, you can create static thumbnails instead:

```bash
# Render as PNG (single frame)
manim -ql --format=png -n 0,1 scenes/phase1/01_hash_intro.py HashIntroduction
```

This creates a single frame that can serve as a thumbnail.

---

**Note**: Previews are for documentation and quick reference. For production videos, always use high-quality MP4 rendering with proper audio.
