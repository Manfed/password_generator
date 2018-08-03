import { BasicResponse } from '../../commons/basic_response';

export class RCResponse extends BasicResponse {
  password: string;

  constructor(entropy: number, isSafe: boolean, password?: string) {
    super(entropy, isSafe);
    this.password = password;
  }
}
