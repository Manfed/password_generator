export class Mapping {
  mappedCharacter: string;
  mappings: string;
  mappingChance: number;

  constructor(mappedCharacter: string, mappings: string, mappingChance: number) {
    this.mappedCharacter = mappedCharacter;
    this.mappings = mappings;
    this.mappingChance = mappingChance;
  }
}
