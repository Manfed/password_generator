import { RWRequest } from '../../random_words/model/rwrequest';
import { Mapping } from '../../commons/mapping';

export class RWFSRequest extends RWRequest {
  artist: string;

  constructor(mappings: Mapping[], passwordLength: number, rwCase: string, artist: string) {
    super(mappings, passwordLength, rwCase);
    this.artist = artist;
  }
}
