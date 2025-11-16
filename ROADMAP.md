# Blockchain & Cryptography Learning Roadmap

A comprehensive guide for creating educational Manim visualizations covering blockchain and cryptography fundamentals.

## Table of Contents
- [Overview](#overview)
- [YouTube Video Pipeline](#youtube-video-pipeline)
- [Learning Modules](#learning-modules)
- [Module Status Tracker](#module-status-tracker)

---

## Overview

This roadmap breaks down blockchain and cryptography education into small, digestible chunks. Each module should be:
- **5-10 minutes of video content**
- **Self-contained** (can be understood independently)
- **Visual-first** (leverage Manim's animation capabilities)
- **Beginner-friendly** (build up from fundamentals)

---

## YouTube Video Pipeline

### Workflow for Each Video

1. **Research & Script** (1-2 hours)
   - Research the topic
   - Write a script with voiceover text
   - Identify key visual concepts

2. **Code Animation** (2-4 hours)
   - Create Manim scene class
   - Build visual primitives
   - Add voiceover integration
   - Test and iterate

3. **Render** (10-30 minutes)
   - High quality render: `manim -pqh <file>.py <Scene>`
   - Review output

4. **Post-Production** (30 minutes)
   - Add intro/outro (optional)
   - Final review
   - Export to YouTube format

5. **Publish** (15 minutes)
   - Upload to YouTube
   - Write description with key concepts
   - Add to playlist
   - Share on social media

### Tools & Setup
- **Manim Community**: Animation engine
- **Azure TTS**: Voiceover (already configured)
- **Git**: Version control for animations
- **Docker**: (TODO) Portable environment

---

## Learning Modules

### Phase 1: Cryptography Fundamentals (14 modules)

#### 1.1 Hash Functions Basics
**File**: `01_hash_intro.py`
**Topics**: What is a hash? Properties (deterministic, one-way, collision-resistant)
**Visuals**:
- Show data going through a "hash machine"
- Demonstrate avalanche effect (small input change → big hash change)
- Compare hash sizes

#### 1.2 SHA-256 Deep Dive
**File**: `02_sha256.py`
**Topics**: SHA-256 algorithm internals
**Visuals**:
- Block diagram of SHA-256 rounds
- Compression function animation
- Message scheduling

#### 1.3 RIPEMD-160
**File**: `03_ripemd160.py`
**Topics**: RIPEMD-160 and its use in Bitcoin addresses
**Visuals**:
- Hash160 = RIPEMD160(SHA256(data))
- Address generation flow

#### 1.4 Merkle Trees Part 1
**File**: `04_merkle_trees_intro.py`
**Topics**: Tree structure, building a Merkle tree
**Visuals**:
- Animate building tree from transactions
- Show root hash computation

#### 1.5 Merkle Trees Part 2
**File**: `05_merkle_proofs.py`
**Topics**: Merkle proofs and verification
**Visuals**:
- Prove a transaction is in a block
- Highlight proof path in tree
- Verify proof step-by-step

#### 1.6 Public Key Cryptography Intro
**File**: `06_public_key_intro.py`
**Topics**: Asymmetric encryption concept, key pairs
**Visuals**:
- Alice & Bob scenario
- Lock and key metaphor
- Public vs private key usage

#### 1.7 Elliptic Curves Basics
**File**: `07_elliptic_curves_intro.py`
**Topics**: What is an elliptic curve? Point addition
**Visuals**:
- Plot y² = x³ + 7 (secp256k1)
- Animate point addition geometrically
- Show point doubling

#### 1.8 Elliptic Curves Math
**File**: `08_elliptic_curves_math.py`
**Topics**: Scalar multiplication, generator point
**Visuals**:
- Animate k * G for different k values
- Show discrete log problem
- Connect to private/public keys

#### 1.9 ECDSA Signing
**File**: `09_ecdsa_signing.py`
**Topics**: How ECDSA signatures are created
**Visuals**:
- Signing algorithm steps
- Nonce importance
- r and s values

#### 1.10 ECDSA Verification
**File**: `10_ecdsa_verification.py`
**Topics**: How to verify an ECDSA signature
**Visuals**:
- Verification algorithm
- Why it works mathematically
- Invalid signature detection

#### 1.11 Schnorr Signatures Intro
**File**: `11_schnorr_intro.py`
**Topics**: Schnorr vs ECDSA, advantages
**Visuals**:
- Compare signature sizes
- Linearity property
- Why Schnorr is simpler

#### 1.12 Schnorr Math & Aggregation
**File**: `12_schnorr_aggregation.py`
**Topics**: Signature aggregation, MuSig
**Visuals**:
- Combine multiple signatures
- Multi-signature scenarios
- Key aggregation

#### 1.13 Digital Signatures in Practice
**File**: `13_signatures_practice.py`
**Topics**: Common pitfalls, nonce reuse attack
**Visuals**:
- Show nonce reuse vulnerability
- Demonstrate private key extraction
- Best practices

#### 1.14 Base58 & Bech32 Encoding
**File**: `14_encoding.py`
**Topics**: Bitcoin address formats
**Visuals**:
- Base58Check encoding process
- Bech32 encoding (SegWit addresses)
- QR code-friendly properties

---

### Phase 2: Bitcoin Fundamentals (16 modules)

#### 2.1 Bitcoin Transaction Structure ✅
**File**: `simpletransactionintro.py` (already exists)
**Status**: DONE
**Topics**: Version, inputs, outputs, locktime

#### 2.2 UTXOs Explained
**File**: `15_utxo_model.py`
**Topics**: UTXO vs account model
**Visuals**:
- Show UTXO set
- Transaction consuming and creating UTXOs
- UTXO lifecycle

#### 2.3 Transaction Inputs Deep Dive
**File**: `16_tx_inputs.py`
**Topics**: Previous output reference, scriptSig, sequence
**Visuals**:
- Break down input structure
- Show connection to previous output
- Witness data

#### 2.4 Transaction Outputs Deep Dive
**File**: `17_tx_outputs.py`
**Topics**: Value, scriptPubKey, output types
**Visuals**:
- Different output types
- Locking conditions
- OP_RETURN outputs

#### 2.5 Bitcoin Script Intro
**File**: `18_script_intro.py`
**Topics**: Stack-based language, basic opcodes
**Visuals**:
- Stack visualization
- Execute simple script
- OP_DUP, OP_HASH160, etc.

#### 2.6 P2PKH Transactions
**File**: `19_p2pkh.py`
**Topics**: Pay-to-Public-Key-Hash
**Visuals**:
- scriptPubKey structure
- scriptSig structure
- Full validation flow

#### 2.7 P2SH Transactions
**File**: `20_p2sh.py`
**Topics**: Pay-to-Script-Hash
**Visuals**:
- Why P2SH?
- RedeemScript concept
- Validation process

#### 2.8 MultiSig Transactions
**File**: `21_multisig.py`
**Topics**: M-of-N multisig, OP_CHECKMULTISIG
**Visuals**:
- 2-of-3 multisig example
- Signing process
- Use cases

#### 2.9 SegWit Part 1
**File**: `22_segwit_intro.py`
**Topics**: Transaction malleability problem, witness data
**Visuals**:
- Show malleability issue
- Witness vs non-witness data
- Block weight vs size

#### 2.10 SegWit Part 2
**File**: `23_segwit_addresses.py`
**Topics**: P2WPKH and P2WSH
**Visuals**:
- Native SegWit outputs
- Nested SegWit (P2SH-wrapped)
- Address formats

#### 2.11 Taproot Intro
**File**: `24_taproot_intro.py`
**Topics**: Taproot upgrade, benefits
**Visuals**:
- MAST (Merkelized Abstract Syntax Tree)
- Key path vs script path
- Privacy improvements

#### 2.12 Taproot Scripts
**File**: `25_taproot_scripts.py`
**Topics**: TapScript, Schnorr in Taproot
**Visuals**:
- Script tree structure
- Control block
- Spending paths

#### 2.13 Transaction Fees
**File**: `26_transaction_fees.py`
**Topics**: Fee calculation, fee markets, RBF
**Visuals**:
- Input sum - Output sum = Fee
- Fee rate (sat/vByte)
- Mempool visualization

#### 2.14 Timelocks
**File**: `27_timelock.py`
**Topics**: nLockTime, nSequence, CLTV, CSV
**Visuals**:
- Absolute vs relative timelocks
- Use cases (escrow, payment channels)
- How they work

#### 2.15 Covenants Intro ✅
**File**: `covenants.py` (already exists)
**Status**: DONE
**Topics**: OP_CHECKSIGFROMSTACK, CAT

#### 2.16 Advanced Covenants
**File**: `28_advanced_covenants.py`
**Topics**: Vault patterns, recursive covenants
**Visuals**:
- Vault spending conditions
- Recursive covenant concept
- Future opcodes (OP_CTV, etc.)

---

### Phase 3: Blockchain Fundamentals (12 modules)

#### 3.1 Block Structure
**File**: `29_block_structure.py`
**Topics**: Block header, transaction list
**Visuals**:
- Break down header fields
- Merkle root connection
- Block size limits

#### 3.2 Blockchain Data Structure
**File**: `30_blockchain_structure.py`
**Topics**: Linked list of blocks
**Visuals**:
- Chain of block hashes
- Previous block hash pointer
- Why immutability works

#### 3.3 Proof of Work Intro
**File**: `31_pow_intro.py`
**Topics**: Mining concept, difficulty target
**Visuals**:
- Hash puzzle
- Nonce searching
- Finding valid block

#### 3.4 Mining Deep Dive
**File**: `32_mining.py`
**Topics**: Mining hardware, hashrate, pools
**Visuals**:
- CPU → GPU → ASIC evolution
- Pool mining vs solo
- Block rewards

#### 3.5 Difficulty Adjustment
**File**: `33_difficulty_adjustment.py`
**Topics**: Retargeting algorithm, 2016 blocks
**Visuals**:
- Target calculation
- Adapt to hashrate changes
- 10-minute block time goal

#### 3.6 Coinbase Transaction
**File**: `34_coinbase_tx.py`
**Topics**: First transaction in block, block reward
**Visuals**:
- Coinbase structure
- Block subsidy + fees
- Halving schedule

#### 3.7 Chain Reorganization
**File**: `35_reorg.py`
**Topics**: Competing chains, longest chain rule
**Visuals**:
- Fork visualization
- Reorg scenario
- Confirmation depth

#### 3.8 51% Attack
**File**: `36_51_attack.py`
**Topics**: Majority hashrate attack
**Visuals**:
- Double-spend scenario
- Private chain building
- Why it's expensive

#### 3.9 SPV and Light Clients
**File**: `37_spv.py`
**Topics**: Simplified Payment Verification
**Visuals**:
- Full node vs SPV node
- Merkle proof verification
- Trust assumptions

#### 3.10 Network Propagation
**File**: `38_network_propagation.py`
**Topics**: P2P network, gossip protocol
**Visuals**:
- Node connections
- Transaction/block propagation
- Network topology

#### 3.11 Consensus Rules
**File**: `39_consensus.py`
**Topics**: Block validation rules
**Visuals**:
- List key consensus rules
- Why everyone must agree
- Soft fork vs hard fork

#### 3.12 Forks (Soft vs Hard)
**File**: `40_forks.py`
**Topics**: Protocol upgrades
**Visuals**:
- Soft fork compatibility
- Hard fork split
- Historical examples (SegWit, BCH)

---

### Phase 4: Layer 2 & Advanced (10 modules)

#### 4.1 Payment Channels Intro
**File**: `41_payment_channels.py`
**Topics**: Bidirectional channels, commitment transactions
**Visuals**:
- Opening channel
- Updating balance
- Closing channel

#### 4.2 Lightning Network Basics
**File**: `42_lightning_intro.py`
**Topics**: Network of channels, routing
**Visuals**:
- Multi-hop payments
- Path finding
- Network topology

#### 4.3 HTLCs
**File**: `43_htlc.py`
**Topics**: Hash Time-Locked Contracts
**Visuals**:
- Preimage and hash
- Timeout mechanism
- Atomic routing

#### 4.4 Lightning Invoices
**File**: `44_lightning_invoices.py`
**Topics**: BOLT11 invoices
**Visuals**:
- Invoice structure
- Payment flow
- Proof of payment

#### 4.5 Channel Factories
**File**: `45_channel_factories.py`
**Topics**: Multi-party channels
**Visuals**:
- Factory construction
- Sub-channels
- Scalability benefits

#### 4.6 Submarine Swaps
**File**: `46_submarine_swaps.py`
**Topics**: On-chain ↔ off-chain atomic swaps
**Visuals**:
- Swap flow
- No custodian needed
- Use cases

#### 4.7 Atomic Swaps
**File**: `47_atomic_swaps.py`
**Topics**: Cross-chain swaps
**Visuals**:
- HTLC on both chains
- Trustless exchange
- Bitcoin ↔ Litecoin example

#### 4.8 CoinJoin
**File**: `48_coinjoin.py`
**Topics**: Privacy through mixing
**Visuals**:
- Multiple inputs/outputs
- Breaking transaction graph
- Anonymity set

#### 4.9 Confidential Transactions
**File**: `49_confidential_tx.py`
**Topics**: Pedersen commitments, hiding amounts
**Visuals**:
- Commitment scheme
- Homomorphic property
- Range proofs

#### 4.10 Sidechains & Drivechains
**File**: `50_sidechains.py`
**Topics**: Pegged sidechains
**Visuals**:
- 2-way peg
- SPV proofs
- Use cases

---

### Phase 5: Advanced Cryptography (8 modules)

#### 5.1 Zero-Knowledge Proofs Intro
**File**: `51_zkp_intro.py`
**Topics**: Prove knowledge without revealing
**Visuals**:
- Where's Waldo analogy
- Prover and verifier
- Cave example

#### 5.2 zk-SNARKs Basics
**File**: `52_zksnarks.py`
**Topics**: Succinct non-interactive proofs
**Visuals**:
- Trusted setup
- Proof size
- Verification time

#### 5.3 Bulletproofs
**File**: `53_bulletproofs.py`
**Topics**: Range proofs without trusted setup
**Visuals**:
- Inner product argument
- Logarithmic size
- Use in Monero

#### 5.4 Ring Signatures
**File**: `54_ring_signatures.py`
**Topics**: Sign on behalf of group
**Visuals**:
- Anonymity set
- Monero usage
- Linkability

#### 5.5 Threshold Signatures
**File**: `55_threshold_sigs.py`
**Topics**: t-of-n signatures
**Visuals**:
- Shamir's Secret Sharing
- FROST protocol
- Use cases

#### 5.6 Adaptor Signatures
**File**: `56_adaptor_sigs.py`
**Topics**: Scriptless scripts
**Visuals**:
- Two-stage revelation
- Atomic swaps without scripts
- Point-time locked contracts

#### 5.7 MPC Intro
**File**: `57_mpc_intro.py`
**Topics**: Multi-Party Computation
**Visuals**:
- Compute on private data
- Key generation (TSS)
- Wallet applications

#### 5.8 Homomorphic Encryption
**File**: `58_homomorphic.py`
**Topics**: Compute on encrypted data
**Visuals**:
- Additive homomorphism
- Multiplicative homomorphism
- Fully homomorphic (FHE)

---

### Phase 6: Alternative Consensus & Chains (6 modules)

#### 6.1 Proof of Stake Intro
**File**: `59_pos_intro.py`
**Topics**: Stake-based consensus
**Visuals**:
- Validator selection
- Slashing
- Nothing-at-stake problem

#### 6.2 Ethereum Basics
**File**: `60_ethereum_intro.py`
**Topics**: Account model, gas
**Visuals**:
- EOA vs contract accounts
- State tree
- Gas mechanism

#### 6.3 Smart Contracts
**File**: `61_smart_contracts.py`
**Topics**: Solidity, EVM
**Visuals**:
- Simple contract example
- Contract deployment
- Function calls

#### 6.4 Ethereum 2.0
**File**: `62_eth2.py`
**Topics**: Beacon chain, sharding
**Visuals**:
- PoW → PoS transition
- Validators
- Sharding concept

#### 6.5 Rollups
**File**: `63_rollups.py`
**Topics**: Optimistic vs ZK rollups
**Visuals**:
- Layer 2 scaling
- Data availability
- Fraud proofs vs validity proofs

#### 6.6 Other Consensus Mechanisms
**File**: `64_other_consensus.py`
**Topics**: PBFT, Tendermint, Avalanche
**Visuals**:
- BFT consensus
- Voting mechanisms
- Trade-offs

---

## Module Status Tracker

### Completed ✅
- [ ] 2.1 Bitcoin Transaction Structure (`simpletransactionintro.py`)
- [ ] 2.15 Covenants Intro (`covenants.py`)

### In Progress 🚧
- [ ] None

### Planned 📋
- [ ] Phase 1: Cryptography Fundamentals (14 modules)
- [ ] Phase 2: Bitcoin Fundamentals (14 remaining)
- [ ] Phase 3: Blockchain Fundamentals (12 modules)
- [ ] Phase 4: Layer 2 & Advanced (10 modules)
- [ ] Phase 5: Advanced Cryptography (8 modules)
- [ ] Phase 6: Alternative Consensus (6 modules)

**Total**: 64 modules (2 done, 62 remaining)

---

## Prioritization Strategy

For maximum learning value with limited credits, prioritize in this order:

### High Priority (Core Fundamentals)
1. **Phase 1**: Modules 1.1-1.14 (Cryptography basics)
2. **Phase 2**: Modules 2.2-2.8 (Bitcoin transactions & scripts)
3. **Phase 3**: Modules 3.1-3.6 (Blockchain basics)

### Medium Priority (Advanced Bitcoin)
4. **Phase 2**: Modules 2.9-2.14, 2.16 (SegWit, Taproot, advanced features)
5. **Phase 3**: Modules 3.7-3.12 (Security & consensus)

### Lower Priority (Specialized Topics)
6. **Phase 4**: Layer 2 solutions
7. **Phase 5**: Advanced cryptography
8. **Phase 6**: Alternative blockchains

---

## Tips for Efficient Production

1. **Batch similar topics**: Record all hash function videos together
2. **Reuse visual components**: Create a library of common animations (stacks, trees, etc.)
3. **Start with low-quality renders** for testing (`-ql` flag)
4. **Template scripts**: Create templates for common patterns
5. **Use voiceover library**: Pre-record common phrases
6. **Modular scenes**: Build scenes from reusable components

---

## Next Steps

1. Set up project structure:
   ```bash
   mkdir -p scenes/{phase1,phase2,phase3,phase4,phase5,phase6}
   mkdir -p scripts
   mkdir -p outputs
   ```

2. Create reusable components library:
   - `components/stack.py` - Stack visualization
   - `components/tree.py` - Tree structures
   - `components/hash.py` - Hash function animations
   - `components/signature.py` - Signature visualizations

3. Pick first module and start coding!

---

## Resources

- [Manim Community Docs](https://docs.manim.community/)
- [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook)
- [Bitcoin Optech](https://bitcoinops.org/)
- [Learn Me a Bitcoin](https://learnmeabitcoin.com/)
- [Chaincode Seminars](https://chaincode.com/seminars/)
