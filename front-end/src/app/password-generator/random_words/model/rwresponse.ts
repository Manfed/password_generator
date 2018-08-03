import { RCResponse } from '../../random_characters/model/rcresponse';

export class RWResponse extends RCResponse {
  passwordWords: string[];
  entropy: number;
  used_words: string[];
  colors: string[];
  password: string;

  constructor(passwordWords: string[], entropy: number, used_words: string[], colors: string[], password: string, isSafe: boolean) {
    super(entropy, isSafe);
    this.passwordWords = passwordWords;
    this.used_words = used_words;
    this.colors = colors;
    this.password = password;
  }
}
