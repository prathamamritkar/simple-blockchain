<!-- Mini Task 1: Build &amp; Explain a Simple Blockchain-->
# Simple Blockchain

---

### 1. Blockchain Basics

<!-- Define blockchain in your own words (100–150 words) -->
**Definition**:
A blockchain is a **decentralized, distributed digital ledger** that records transactions in an immutable chain of cryptographically linked blocks. It operates without central authority, relying on consensus mechanisms to validate transactions. Each block contains a timestamp, transaction data, and a reference (hash) to the previous block, creating a tamper-evident structure. This design ensures transparency, security, and trustless verification across peer-to-peer networks.

<!-- List 2 real-life use cases (e.g., supply chain, digital identity) -->
**Real-Life Use Cases**:
- **Supply Chain Management**: Enables end-to-end tracking of goods like Walmart's food traceability system.
- **Digital Identity**: Provides secure, self-sovereign identities like Estonia’s e-Residency program.

---

### 2. Block Anatomy

<!-- Draw a block showing: data, previous hash, timestamp, nonce, and Merkle root -->
| Block #1            |                                                                     |
|---------------------|---------------------------------------------------------------------|
| **data**           | Pratham's Block
| **previous hash**  | 0000000000000000000000000000000000000000000000000000000000000000 |
| **timestamp**      | 1749341000.0 |
| **nonce**          | 72608 |
| **Merkle root**    | e4d464a0632cdcef533e22daa3f225ba7ef09078c01828b2b25bf73f519c236c |

<!-- Briefly explain with an example how the Merkle root helps verify data integrity -->
**Merkle Root Example**:  
For transactions TX1, TX2, TX3, TX4:
1. Hash TX1 & TX2 → Hash A
2. Hash TX3 & TX4 → Hash B
3. Hash A & B → Merkle Root  
If TX3 is altered, Hash B and the Merkle Root change, instantly revealing tampering.

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
