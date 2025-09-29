from hashing import hash_data
import time 

class Block:
    def __init__(self, data, prev_hash="0" * 64):
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.prev_hash}"
        return hash_data(block_string, algo="sha256")

    def __repr__(self):
        return (f"Block(Hash: {self.hash[:12]}...,)"
                f"Prev: {self.prev_hash[:12]}...,"
                f"Data: {self.data}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block")

    def add_block(self, data):
        pass

    def is_valid(self):
        pass

    def __repr__(self):
        pass

if __name__ == "__main__":
    pass