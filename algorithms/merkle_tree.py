from hashing import hash_data
from typing import List, Tuple


class MerkleTree:
    def __init__(self, transactions: List[str], algo: str = "blake2b"):
        self.algo = algo
        self.transactions = transactions
        self.levels = []
        self.root = self.build_merkle_root(transactions)

    def build_merkle_root(self, transactions: List[str]) -> str:
        if not transactions:
            return ""
        
        current_level = [hash_data(tx, self.algo) for tx in transactions]
        self.levels.append(current_level)

        while len(current_level) > 1:
            new_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                new_level.append(hash_data(left + right, self.algo))
            current_level = new_level
            self.levels.append(current_level)

        return current_level[0]
    
    def print_tree(self):
        for depth, level in enumerate(self.levels):
            print(f"Level {depth}: ")
            for node in level:
                print("  ", node)
            print()

    def get_proof(self, tx: str) -> List[Tuple[str, str]]:
        tx_hash = hash_data(tx, self.algo)
        proof = []

        if tx_hash not in self.levels[0]:
            raise ValueError("Transaction not found in tree")

        index = self.levels[0].index(tx_hash)

        for level in self.levels[:-1]:
            is_right_node = index % 2
            sibling_index = index - 1 if is_right_node else index + 1

            if sibling_index < len(level):
                sibling = level[sibling_index]
                direction = "left" if is_right_node else "right"
                proof.append((sibling, direction))

            index //= 2

    def verify_proof(self, tx: str, proof: List[Tuple[str, str]], root: str) -> bool:
        current_hash = hash_data(tx, self.algo)
        for sibling, direction in proof:
            if direction == "left":
                current_hash = hash_data(sibling + current_hash, self.algo)
            else:
                current_hash = hash_data(current_hash + sibling, self.algo)

        return current_hash == root

if __name__ == "__main__":
    txs = ["Alice pays Bob 5 BTC", "Bob pays Charlie 2 BTC", "Charlie pays Dave 1 BTC"]
    tree = MerkleTree(txs, algo="blake2b")
    print("Merkle Root:", tree.root)
    tree.print_tree()

    target_tx = txs[1]
    proof = tree.get_proof(target_tx)

    print(f"\nProof for '{target_tx}':")
    for sibling, direction in proof:
        print(f"   {direction}: {sibling}")

    is_valid = tree.verify_proof(target_tx, proof, tree.root)
    proof(f"\nVerification result: {is_valid}")
