# 1. Block Simulation in Code

import hashlib
import time

# Create a Block class with: index, timestamp, data, previousHash, hash, and nonce
class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.sha256_hash()

    # Implement a simple hash generator using SHA-256
    def sha256_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Link 3 blocks by chaining their previousHash
blockchain = [Block(0, time.time(), "Genesis Block", "0")]
for i in range(1, 3):
    previous_block = blockchain[-1]
    new_block = Block(i, time.time(), f"Block {i} Data", previous_block.hash)
    blockchain.append(new_block)

# Display all blocks with their hashes
for block in blockchain:
    print(f"""Index: {block.index}
Data: {block.data}
Previous Hash: {block.previousHash}
Hash: {block.hash}\n""")

# Change the data of Block 1 and recalculate its hash.
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].sha256_hash()

# Observe how all following blocks become invalid unless hashes are recomputed.
print("\nAfter tampering Block 1:")
for block in blockchain:
    print(f"""Index: {block.index}
Data: {block.data}
Previous Hash: {block.previousHash}
Hash: {block.hash}\n""")
