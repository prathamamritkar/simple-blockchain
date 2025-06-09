import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.sha256_hash()

    def sha256_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Modify your Block class to include a mineBlock(difficulty) function
    def mineBlock(self, difficulty):
        # Set difficulty (e.g., hash must start with "0000")
        target = '0' * difficulty
        start_time = time.time()
        attempts = 0
        # In mineBlock(), repeatedly increment the nonce until the hash meets the difficulty condition
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.sha256_hash()
            attempts += 1
        end_time = time.time()
        print(f"Block mined: {self.hash}")
        # Print how many nonce attempts were needed
        print(f"Nonce attempts: {attempts}")
        # Measure time taken using a timer
        print(f"Time taken: {end_time - start_time:.2f} sec")

block = Block(0, time.time(), "Mining Block", "0")
block.mineBlock(difficulty=4)

