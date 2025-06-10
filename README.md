# simple-blockchain
Mini Task 1: Build &amp; Explain a Simple Blockchain

### Blockchain Basics
A blockchain is a **decentralized, distributed digital ledger** that records transactions in an immutable chain of cryptographically linked blocks. It operates without central authority, relying on consensus mechanisms to validate transactions. Each block contains a timestamp, transaction data, and a reference (hash) to the previous block, creating a tamper-evident structure. This design ensures transparency, security, and trustless verification across peer-to-peer networks[1][2].

**Real-Life Use Cases**:
- **Supply Chain Management**: Enables end-to-end tracking of goods (e.g., Walmart's food traceability system)[1].
- **Digital Identity**: Provides secure, self-sovereign identities (e.g., Estonia’s e-Residency program)[1].

---

### Block Anatomy



**Merkle Root Example**:  
For transactions TX1, TX2, TX3, TX4:
1. Hash TX1 & TX2 → Hash A
2. Hash TX3 & TX4 → Hash B
3. Hash A & B → Merkle Root  
If TX3 is altered, Hash B and the Merkle Root change, instantly revealing tampering[1][3].

---

### Consensus Conceptualization

| Mechanism          | Key Features                                                                 | Energy Use |
|--------------------|-----------------------------------------------------------------------------|------------|
| **Proof of Work**  | Miners solve cryptographic puzzles by finding a valid nonce. Requires massive computational power to repeatedly hash data until meeting target criteria. High energy consumption stems from competitive mining[1][3]. | High       |
| **Proof of Stake** | Validators are chosen based on their staked cryptocurrency. Eliminates energy-intensive mining by using deterministic selection (higher stake = higher chance). More eco-friendly than PoW[3]. | Low        |
| **Delegated PoS**  | Token holders vote for delegates (e.g., 21-101 nodes) to validate blocks. Voting power depends on stake size. Delegates take turns producing blocks and can be voted out for poor performance[3]. | Minimal    |

**Key Differences**:
- PoW: Security through computation
- PoS: Security through financial stake
- DPoS: Democratic governance via voting
