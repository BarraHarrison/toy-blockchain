import hashlib
import _sha3

def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

try:
    def keccak256_hash():
        pass
except ImportError:
    def keccak256_hash():
        pass

