import crypto from "crypto";

export function sha256(data: string): string {
    return crypto.createHash("sha256").update(data).digest("hex");
}

export function doubleSha256(data: string): string {
    return sha256(sha256(data));
}
