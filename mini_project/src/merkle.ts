import { sha256 } from "./hash";
import { Transaction } from "./transaction";

export function calculateMerkleRoot(transactions: Transaction[]): string {
    if (transactions.length === 0) return sha256("");

    let hashes = transactions.map((tx) => sha256(JSON.stringify(tx)));

    while (hashes.length > 1) {
        const temp: string[] = [];
        for (let i = 0; i < hashes.length; i += 2) {
            const left = hashes[i];
            const right = hashes[i + 1] || left;
            temp.push(sha256(left + right));
        }
        hashes = temp;
    }

    return hashes[0];
}