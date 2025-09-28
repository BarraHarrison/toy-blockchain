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

    def verify_proof():
        pass

if __name__ == "__main__":
    txs = ["Alice pays Bob 5 BTC", "Bob pays Charlie 2 BTC", "Charlie pays Dave 1 BTC"]
    tree = MerkleTree(txs, algo="blake2b")
    print("Merkle Root:", tree.root)
    print("\n=== Full Tree ===")
    tree.print_tree()
