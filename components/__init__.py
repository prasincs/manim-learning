"""
Reusable components for Manim blockchain & cryptography visualizations

Import commonly used components:
    from components import Stack, HashMachine, MerkleTree

Following Tufte's principles:
- Maximize data-ink ratio
- Integrate text and graphics
- Use small multiples for comparison
- Show the data
"""

from components.stack import StackElement, Stack, AnimatedStack
from components.hash import HashMachine, DataBox, HashVisualization, AvalancheEffect
from components.tree import HashNode, MerkleTree, MerkleProofVisualization, BinaryTreeGeneric

__all__ = [
    # Stack components
    'StackElement',
    'Stack',
    'AnimatedStack',

    # Hash components
    'HashMachine',
    'DataBox',
    'HashVisualization',
    'AvalancheEffect',

    # Tree components
    'HashNode',
    'MerkleTree',
    'MerkleProofVisualization',
    'BinaryTreeGeneric',
]

__version__ = '0.1.0'
