# 🧱 Week 1 – Blockchain Fundamentals  
**Part of the Month 1: Blockchain & Ethereum Foundations Roadmap**

---

## 🎯 Goal  
Understand the fundamental building blocks of blockchain systems — how data is linked, validated, and secured — and implement a simplified blockchain prototype in TypeScript.

---

## 📘 Topics Covered  

### 🔹 Blockchain Architecture  
- Structure of a block (header, transactions, Merkle root, previous hash)  
- The concept of an immutable chain through cryptographic linkage  
- The role of the Merkle Tree for efficient transaction verification  

### 🔹 Consensus Mechanisms  
- **Proof of Work (PoW)**: computational effort to secure consensus  
- **Proof of Stake (PoS)**: validation through economic stake  
- Comparison of energy efficiency, security, and decentralization tradeoffs  

### 🔹 Account Types  
- **Externally Owned Accounts (EOA):** controlled by private keys  
- **Contract Accounts:** controlled by deployed smart contract code  

---

## 🧠 Algorithms & Data Structures Studied  

| Topic | Concept | Implementation |
|-------|----------|----------------|
| Hashing | SHA-256, Keccak-256 | Used to secure and link blocks |
| Merkle Trees | Binary hash tree | Provides integrity verification for transactions |
| Linked Lists | Sequential node linkage | Forms the basic blockchain structure |

---

## 🧩 Mini Project – *Toy Blockchain in TypeScript*  

### Overview  
A simplified blockchain implementation demonstrating how transactions are grouped into blocks, validated through proof-of-work, and chained using cryptographic hashes.

### 🔧 Features  
- Blocks linked via SHA-256 hashes  
- Simple transaction objects (`from`, `to`, `amount`)  
- Proof-of-Work mining (adjustable difficulty)  
- Merkle Tree integration for transaction verification  
- Chain validation function to ensure immutability  

---