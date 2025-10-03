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

}