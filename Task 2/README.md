<!-- Choose one platform from each category:
- Public Blockchain: (e.g., Ethereum, Bitcoin, Solana)
- Private Blockchain: (e.g., Hyperledger Fabric, R3 Corda in private mode)
- Consortium Blockchain: (e.g., R3 Corda, Quorum, IBM Food Trust) -->
# Blockchain Types and Examples


## 1. Comparison Table

<!-- Create a comparison table or markdown sheet with the following columns for each platform:
- Blockchain Name
- Type (Public/Private/Consortium)
- Consensus Mechanism Used
- Permission Model (Open/Permissioned)
- Speed / Throughput (TPS if available)
- Smart Contract Support (Y/N + Language)
- Token Support (Native or not)
- Typical Use Case
- Notable Technical Feature (e.g., privacy, pluggable consensus) -->
| Blockchain Name | Type | Consensus Mechanism Used | Permission Model | Speed / Throughput (TPS) | Smart Contract Support (Language) | Token Support | Typical Use Case | Notable Technical Feature |
|-----------------|------|--------------------------|------------------|--------------------|------------------------|---------------|------------------|---------------------------|
| Solana | Public | PoH, PoS | Open | >65000 | Y (Rust, C, C++) | Native | dApps, DeFi, NFTs | High TPS, low latency |
| R3 in Private Mode | Private | Pluggable (Raft, PBFT) | Permissioned | >1000 | Y (Kotlin, Java) | Not native | CorDapps, B2B, FinTech, ERP | Privacy, P2P transactions |
| IBM Food Trust | Consortium | PBFT | Permissioned | >1000 | Y ( Go, Java, Node.js) | Not native | Supply chain, food traceability | Privacy, modularity |

---

## 2. Short Report

<!-- 2. Write a Short Report (150–200 words):
- Compare and contrast the technical capabilities of each.
- Which platform would you choose for:
- A decentralized app?
- A supply chain network among known partners?
- An inter-bank financial application?
- Justify your choice based on technical points. -->
Solana, R3 Corda, and IBM Food Trust differ in design and technical capabilities. Solana, a public blockchain, combines Proof of History (PoH) with Proof of Stake (PoS) to achieve unparalleled throughput (~65,000 TPS) and sub-second latency, ideal for decentralized applications (dApps) requiring speed and scalability. Its open, permissionless model supports Rust/C/C++ smart contracts and native SOL tokens, making it a powerhouse for DeFi, NFTs, and open ecosystems. R3 Corda in Private Mode operates as a permissioned ledger optimized for enterprises, prioritizing privacy and direct P2P transactions. Its pluggable consensus (Raft for crash tolerance, PBFT for Byzantine fault tolerance) and Kotlin/Java-based CorDapps suit regulated financial workflows but lack native tokens. IBM Food Trust, a consortium blockchain built on Hyperledger Fabric, uses PBFT consensus and modular chaincode (Go/Java/Node.js) to ensure data integrity and privacy for supply chains, enabling traceability among trusted partners.
- **Decentralized app (dApp):** Solana as its public, high-TPS architecture and low fees support large-scale dApps, while PoH ensures deterministic transaction ordering without bottlenecks.
- **Supply chain network among known partners:** IBM Food Trust as its permissioned, modular design allows controlled data sharing and auditability among known entities, critical for traceability and compliance.
- **Inter-bank financial application:** R3 Corda as its private P2P transactions, pluggable BFT consensus, and lack of public tokenization align with banking privacy needs and regulatory requirements.
