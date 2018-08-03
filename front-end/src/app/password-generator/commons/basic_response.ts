export class BasicResponse {
  entropy: number;
  isSafe: boolean;

  constructor(entropy: number, isSafe: boolean) {
    this.entropy = entropy;
    this.isSafe = isSafe;
  }
}
