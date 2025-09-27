import hashlib 
import time 

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index 
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain():
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True


if __name__ == "__main__":
    bc = Blockchain()
    bc.add_block("Adam pays Bill 10 BTC")
    bc.add_block("Bill pays Charles 6 BTC")

    for block in bc.chain:
        print(vars(block))

    print("Blockchain valid: ", bc.is_valid())