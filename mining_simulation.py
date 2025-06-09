import hashlib
import time

def sha256_hash(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

class Block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = sha256_hash(f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}")

  # Modify your Block class to include a mineBlock(difficulty) function
    def mineBlock(self, difficulty):
      target = '0' * difficulty
      start_time = time.time()
      attempts = 0
      # In mineBlock(), repeatedly increment the nonce until the hash meets the difficulty condition
      while not self.hash.startswith(target):
          self.nonce += 1
          self.hash = self.calculate_hash()
          attempts += 1
      end_time = time.time()
      print(f"Block mined: {self.hash}")
      print(f"Nonce attempts: {attempts}")
      print(f"Time taken: {end_time - start_time:.2f} seconds")

# Set difficulty (e.g., hash must start with "0000")
block = Block(0, time.time(), "Mining Block", "0")
block.mineBlock(difficulty=4)

