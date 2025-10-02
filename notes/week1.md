# Week 1 – Blockchain Fundamentals

## 🔑 Hashing

* **Definition**: A hash function takes input data and produces a fixed-size output (digest).
* **SHA-256**:

  * Used in Bitcoin.
  * Produces a 256-bit (64 hex character) hash.
  * Deterministic: same input → same output.
  * Pre-image resistant (hard to reverse).
* **Keccak-256**:

  * Used in Ethereum.
  * Different algorithm family but same cryptographic properties.
* **Key insight**: Hashing secures transactions and links blocks together.

---

## 🌳 Merkle Trees

* **Purpose**: Efficiently prove that a transaction is included in a block.
* **How it works**:

  * Hash each transaction → leaf nodes.
  * Pairwise hash nodes until a single root remains = **Merkle Root**.
  * Root is stored in the block header.
* **Merkle Proofs**:

  * Path of sibling hashes used to verify inclusion of a transaction without downloading the full block.
* **Key insight**: This allows **light clients** (SPV nodes) to validate transactions securely.

---

## 🟩 Genesis Block

* The **first block** in a blockchain.
* Has no previous block (prev hash = `0…0`).
* Hardcoded into the blockchain protocol.
* Establishes the starting point of the chain.

---

## 🔗 Linked List Analogy

* Blockchain = **linked list of blocks**.
* Each block points to the previous block via its **hash**.
* If any block is altered:

  * Its hash changes → breaks the link to the next block.
* **Key insight**: This immutability property is enforced cryptographically.

---

## 💡 Proof of Work (PoW)

* **Goal**: Make it computationally expensive to add new blocks, preventing tampering.
* **Mechanism**:

  * Find a nonce such that `hash(block_header) < target`.
  * Target is adjusted by **difficulty**.
* **Tampering Demo**:

  * If a block is changed (e.g., "5 BTC → 500 BTC"), its hash changes → invalid chain.
  * Attacker must re-mine the tampered block **and all following blocks**.
  * With enough difficulty, this becomes **computationally infeasible**.
* **Key insight**: PoW makes the blockchain secure against retroactive tampering.

---

✅ **Summary of Week 1 Concepts**

* **Hashing** secures data and links blocks.
* **Merkle Trees** allow efficient transaction verification.
* **Genesis Block** is the immutable starting point.
* **Blockchain = Linked List** with cryptographic hashes.
* **Proof of Work** prevents tampering by making attacks costly.
