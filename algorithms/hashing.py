import hashlib
import sha3

def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

try:
    def keccak256_hash(data: str) -> str:
        k = sha3.keccak_256()
        k.update(data.encode('utf-8'))

        return k.hexdigest()

except ImportError:
    def keccak256_hash(data: str) -> str:
        raise ImportError("Install pysha3 for keccak256: pip install pysha3")


if __name__ == "__main__":
    message = "Hello Blockchain"
    print("Message:", message)
    print("SHA-256 :", sha256_hash(message))
    print("Keccak-256 :", keccak256_hash(message))
