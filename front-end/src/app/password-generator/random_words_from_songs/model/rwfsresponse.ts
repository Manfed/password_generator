import { RWResponse } from '../../random_words/model/rwresponse';

export class RWFSResponse extends RWResponse {
  lyrics: string;
  song_name: string;

  constructor(passwordWords: string[], entropy: number,
              used_words: string[], colors: string[],
              password: string, lyrics: string, song_name: string, isSafe: boolean) {
    super(passwordWords, entropy, used_words, colors, password, isSafe);
    this.lyrics = lyrics;
    this.song_name = song_name;
  }
}
