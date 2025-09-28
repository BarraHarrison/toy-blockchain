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

def benchmark(data="hello world", iterations=100_000, algos=None):
    if algos is None:
        algos = ["sha256", "sha3_256", "blake2b"]

    print(f"Benchmarking {iterations} iterations on inpu: '{data}'\n")
    for algo in algos:
        start = time.time()
        for _ in range(iterations):
            hash_data(data, algo)
        elapsed = time.time() - start
        print(f"{algo}: {elapsed:.2f} seconds")


if __name__ == "__main__":
    pass
