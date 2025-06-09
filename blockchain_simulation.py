import hashlib
import time

# Implement a simple hash generator using SHA-256
def sha256_hash(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

# Create a Block class with: index, timestamp, data, previousHash, hash, and nonce
class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = sha256_hash(f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}")

# Link 3 blocks by chaining their previousHash
blockchain = [Block(0, time.time(), "Genesis Block", "0")]
for i in range(1, 3):
    previous_block = blockchain[-1]
    new_block = Block(
        index=i,
        timestamp=time.time(),
        data=f"Block {i} Data",
        previousHash=previous_block.hash
    )
    blockchain.append(new_block)

# Display all blocks with their hashes
for block in blockchain:
    print(f"""Index: {block.index}
Data: {block.data}
Previous Hash: {block.previousHash}
Hash: {block.hash}\n""")

# Change the data of Block 1 and recalculate its hash.
blockchain[1].data = "Tampered Data"
blockchain[1].hash = sha256_hash(f"{blockchain[1].index}{blockchain[1].timestamp}{blockchain[1].data}{blockchain[1].previousHash}{blockchain[1].nonce}")

# Observe how all following blocks become invalid unless hashes are recomputed.
print("\nAfter tampering Block 1:")
for block in blockchain:
    print(f"""Index: {block.index}
Data: {block.data}
Previous Hash: {block.previousHash}
Hash: {block.hash}\n""")
