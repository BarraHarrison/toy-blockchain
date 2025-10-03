import { Block } from "./block";
import { Transaction } from "./transaction";

export class Blockchain {
    public chain: Block[];
    public difficulty: number;
    public pendingTransactions: Transaction[];

    constructor(difficulty: number = 3) {
        this.chain = [this.createGenesisBlock()];
        this.difficulty = difficulty;
        this.pendingTransactions = [];
    }

    private createGenesisBlock(): Block {
        return new Block([], "0");
    }

    getLatestBlock(): Block {
        return this.chain[this.chain.length - 1];
    }

    addTransaction(transaction: Transaction): void {
        this.pendingTransactions.push(transaction);
    }

    minePendingTransactions(): void {
        const block = new Block(this.pendingTransactions, this.getLatestBlock().hash);
        block.mineBlock(this.difficulty);
        this.chain.push(block);
        this.pendingTransactions = [];
    }

    isChainValid(): boolean {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const prevBlock = this.chain[i - 1];

            if (currentBlock.hash !== currentBlock.calculateHash()) return false;
            if (currentBlock.previousHash !== prevBlock.hash) return false;
        }
        return true;
    }

}