import hashlib
from typing import List

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

class MerkleTree:
    def __init__(self, transactions: List[str]):
        self.transactions = transactions
        self.root = self.build_merkle_root(transactions)

    def build_merkle_root(self, tx_list: List[str]) -> str:
        if not tx_list:
            return ""

        level = [sha256(tx) for tx in tx_list]

        while len(level) > 1:
            if len(level) % 2 != 0:
                level.append(level[-1])
            level = [sha256(level[i] + level[i+1]) for i in range(0, len(level), 2)]

        return level

if __name__ == "__main__":
    txs = ["tx1", "tx2", "tx3", "tx4"]
    tree = MerkleTree(txs)
    print("Transactions: ", txs)
    print("Merkle Root: ", tree.root)