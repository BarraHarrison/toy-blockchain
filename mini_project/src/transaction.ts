export interface Transaction {
    from: string;
    to: string;
    amount: number;
}

export function createTransaction(from: string, to: string, amount: number): Transaction {
    return { from, to, amount };
}
