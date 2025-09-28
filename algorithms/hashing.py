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
    print("=== Demo: Hashing Utilities ===")
    text = "Hashing on the Blockchain"
    print("SHA-256:", hash_data(text, "sha256"))
    print("SHA3-256:", hash_data(text, "sha3_256"))
    print("Blake2b", hash_data(text, "Blake2b"))
    print("Double SHA-256:", double_sha256(text))

    obj = {"sender": "Alan", "receiver": "Bill", "amount": 10}
    print("Object hash (SHA-256):", hash_object(obj))

    print("\n=== Running Benchmark ===")
    benchmark("Blockchain Test", iterations=50_000)
