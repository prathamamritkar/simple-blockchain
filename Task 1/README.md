<!-- Mini Task 1: Build & Explain a Simple Blockchain-->
# Simple Blockchain

### 1. Blockchain Basics

<!-- Define blockchain in your own words (100–150 words) -->
**Definition**:
A blockchain is a **decentralized, distributed digital ledger** that records transactions in an immutable chain of cryptographically linked blocks, relying on consensus mechanisms to validate transactions. Each block contains a data, previous hash, timestamp, nonce, Merkle root; creating a tamper-evident structure design ensuring transparency, security, and trustless verification across peer-to-peer networks.  Each Merkle root is simply the SHA-256 hash of that transaction data; in case of multiple transactions, each transaction is hashed, then pairs of those hashes is hashed, and so on, until one root hash remains.

<!-- List 2 real-life use cases (e.g., supply chain, digital identity) -->
**Real-Life Use Cases**:
- **Supply Chain**: Enables end-to-end tracking of goods like Walmart's food traceability system.
- **Digital Identity**: Provides secure, self-sovereign identities like Estonia’s e-Residency program.

---

### 2. Block Anatomy

<!-- Draw a block showing: data, previous hash, timestamp, nonce, and Merkle root -->
| Block               | #1                                                                  |
|---------------------|---------------------------------------------------------------------|
| **data**           | Pratham's Block |
| **previous hash**  | 0000000000000000000000000000000000000000000000000000000000000000 |
| **timestamp**      | 1749341000.0 |
| **nonce**          | 72608 |
| **Merkle root**    | e4d464a0632cdcef533e22daa3f225ba7ef09078c01828b2b25bf73f519c236c |

<!-- Briefly explain with an example how the Merkle root helps verify data integrity -->
  
**Merkle Root Example**:
```
Merkle Root (HashA + HashB)
│
|-- HashA (TX1 + TX2)
│    |-- TX1: [Hash of TX1]
|    |-- TX2: [Hash of TX2]
│
|-- HashB (TX3 + TX4)
    |-- TX3: [Hash of TX3]
    |-- TX4: [Hash of TX4]
```
- For transactions TX1, TX2, TX3, TX4; if TX4 is changed, subsequently HashB changes, and subsequently Merkle Root changes, instantly revealing tampering.

---

### 3. Consensus Conceptualization

<!-- Explain in brief (4–5 sentences each): -->
<!-- What is Proof of Work and why does it require energy? -->
**Proof of Work**
- Miners solve cryptographic puzzles by finding a valid nonce.
- Requires massive computational power to repeatedly hash data until meeting target criteria.
- High energy consumption stems from competitive mining.
- Energy required is high.
- **PoW: Security through computation**  


<!-- What is Proof of Stake and how does it differ? -->
**Proof of Stake**
- Validators are chosen based on their staked cryptocurrency.
- Eliminates energy-intensive mining by using deterministic selection (higher stake = higher chance).
- More eco-friendly than PoW
- Energy required is low.
- **PoS: Security through financial stake**  

<!-- What is Delegated Proof of Stake and how are validators selected? -->
**Delegated PoS**
- Token holders vote for delegates (e.g., 21-101 nodes) to validate blocks.
- Voting power depends on stake size.
- Delegates take turns producing blocks and can be voted out for poor performance.
- Energy required is minimal.
- **DPoS: Democratic governance via voting**  
