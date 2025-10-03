import { Blockchain } from "./blockchain";
import { createTransaction } from "./transaction";

const myChain = new Blockchain(3);

myChain.addTransaction(createTransaction("Alice", "Bob", 50));
myChain.addTransaction(createTransaction("Bob", "Charlie", 25));

console.log("Starting the miner...");
myChain.minePendingTransactions();

myChain.addTransaction(createTransaction("Charlie", "Dave", 10));

console.log("Mining another block...");
myChain.minePendingTransactions();

console.log(JSON.stringify(myChain, null, 2));
console.log("Is chain valid?", myChain.isChainValid());
