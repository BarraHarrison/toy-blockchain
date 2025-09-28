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

def hash_object():
    pass

def double_sha256():
    pass

def benchmark():
    pass


if __name__ == "__main__":
    pass
