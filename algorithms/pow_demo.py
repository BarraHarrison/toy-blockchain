import time
from hashing import hash_data

class Block:
    def __init__(self, index: int, data: str, prev_hash: str = "0"*64, difficulty: int = 3):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
        return hash_data(block_string, algo="sha256")

    def mine(self):
        target_prefix = "0" * self.difficulty
        self.nonce = 0
        self.hash = self.compute_hash()
        start = time.time()
        while not self.hash.startswith(target_prefix):
            self.nonce += 1
            self.hash = self.compute_hash()
        elapsed = time.time() - start
        return elapsed

    def __repr__(self):
        return (f"Block#{self.index} Hash:{self.hash[:12]}... Prev:{self.prev_hash[:12]}..."
                f"Nonce:{self.nonce} Data:{self.data!r}")


class Blockchain:
    def __init__(self):
        pass

    def create_genesis_block(self):
        pass

    def add_block(self):
        pass

    def is_valid(self):
        pass

    def print_chain(self):
        pass

    def re_mine_from(self):
        pass




if __name__ == "__main__":
    pass