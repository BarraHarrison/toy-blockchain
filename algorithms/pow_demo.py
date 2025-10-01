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
    def __init__(self, difficulty: int = 3):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", prev_hash="0"*64, difficulty=self.difficulty)

    def add_block(self, data: str, mine: bool = True):
        prev_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), data, prev_hash=prev_hash, difficulty=self.difficulty)
        if mine:
            elapsed = new_block.mine()
            print(f"Mined block {new_block.index} in {elapsed:.4f}s (nonce={new_block.nonce})")
        self.chain.append(new_block)

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.compute_hash():
                print(f"Invalid: Block {i} hash mismatch")
                return False
            
            if current.prev_hash != previous.hash:
                print(f"Invalid: Block {i} previous hash mismatch (expected {previous.hash[:12]}..., got {current.prev_hash[:12]}...)")
                return False

            if not current.hash.startswith("0" * current.difficulty):
                print(f"Invalid: Block {i} does not PoW difficulty")
                return False
            
            return True

    def print_chain(self):
        for b in self.chain:
            print(b)

    def re_mine_from(self, index: int):
        total_time = 0.0
        if index > 0:
            self.chain[index].prev_hash = self.chain[index-1].hash
        for i in range(index, len(self.chain)):
            block = self.chain[i]
            if i > 0:
                block.prev_hash = self.chain[i-1].hash
            block.timestamp = time.time()
            block.nonce = 0
            elapsed = block.mine()
            total_time += elapsed

        return total_time




if __name__ == "__main__":
    difficulty = 4
    print(f"Creating chain with difficulty = {difficulty}")
    bc = Blockchain(difficulty=difficulty)

    bc.chain[0].nonce = 0
    bc.chain[0].timestamp = time.time()
    t0 = bc.chain[0].mine()
    print(f"Mined genesis in {t0:.4f}s")
    bc.add_block("Adam -> Bill: 5 BTC", mine=True)
    bc.add_block("Bill -> Charles: 2 BTC", mine=True)
    bc.add_block("Charles -> David: 1 BTC", mine=True)

    