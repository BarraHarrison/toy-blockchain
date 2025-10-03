import { sha256 } from "./hash";
import { Transaction } from "./transaction";
import { calculateMerkleRoot } from "./merkle";
import { PassThrough } from "stream";

export class Block {
    public timestamp: number;
    public transactions: Transaction[];
    public previousHash: string;
    public hash: string;
    public nonce: number;
    public merkleRoot: string;

    constructor(transactions: Transaction[], previousHash: string = "") {
        this.timestamp = Date.now();
        this.transactions = transactions;
        this.previousHash = previousHash;
        this.nonce = 0;
        this.merkleRoot = calculateMerkleRoot(transactions);
        this.hash = this.calculateHash();
    }

    calculateHash(): string {
        return sha256(
            this.previousHash + this.timestamp + this.nonce + this.merkleRoot
        );
    }

    mineBlock(difficulty: number): void {
        const target = "0".repeat(difficulty);
        while (!this.hash.startsWith(target)) {
            this.nonce++;
            this.hash = this.calculateHash();
        }
        console.log(`⛏️  Block mined: ${this.hash}`)
    }
}