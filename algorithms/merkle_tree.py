from hashing import hash_data
from typing import List


class MerkleTree:
    def __init__(self, transactions: List[str], algo: str = "sha256"):
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

if __name__ == "__main__":
    txs = ["Alice pays Bob 5 BTC", "Bob pays Charlie 2 BTC", "Charlie pays Dave 1 BTC"]
    tree = MerkleTree(txs, algo="sha256")
    print("Merkle Root:", tree.root)
    print("\n=== Full Tree ===")
    tree.print_tree()
