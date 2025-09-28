import hashlib
import json
import time

def hash_data(data: str, algo: str = "sha256") -> str:
    try:
        h = hashlib.new(algo)
    except ValueError:
        raise ValueError(f"Unsupported algorithm: {algo}")
    h.update(data.encode("utf-8"))
    return h.hexdigest()

def hash_object(obj, algo: str = "sha256") -> str:
    serialized = json.dumps(obj, sort_keys=True)
    return hash_data(serialized, algo)

def double_sha256(data: str) -> str:
    return hashlib.sha256(
        hashlib.sha256(data.encode("utf-8")).digest()
    ).hexdigest()

def benchmark():
    pass


if __name__ == "__main__":
    pass
