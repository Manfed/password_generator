import { Mapping } from '../../commons/mapping';

export class RWRequest {
  mappings: Mapping[];
  passwordLength: number;
  rwCase: string;

  constructor(mappings: Mapping[], passwordLength: number, rwCase: string) {
    this.mappings = mappings;
    this.passwordLength = passwordLength;
    this.rwCase = rwCase;
  }
}
