import { Injectable } from '@angular/core';
import { GeneratorCookiesService } from '../generator-cookies.service';
import { RWFSRequest } from '../../random_words_from_songs/model/rwfsrequest';
import { FormArray, FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { Mapping } from '../../commons/mapping';

@Injectable()
export class SongsCookieService {

  constructor(private cookieService: GeneratorCookiesService, private formBuilder: FormBuilder) { }

  private readonly COOKIE_NAME = 'rwfs_character_groups';

  private readonly DEFAULT_COOKIE_VALUE = {
    mappings: [
      {
        mappedCharacter: 's',
        mappings: '5T',
        mappingChance: 50
      }, {
        mappedCharacter: 'a',
        mappings: '@4',
        mappingChance: 50
      }, {
        mappedCharacter: 'b',
        mappings: '8D',
        mappingChance: 50
      }, {
        mappedCharacter: 't',
        mappings: '5sS',
        mappingChance: 50
      }
    ],
    passwordLength: 10,
    rwCase: 'random',
    artist: 'Myslovitz'
  } as RWFSRequest;

  public setCookie(data: FormGroup) {
    const passwordLength = data.get('password_length') as FormControl;
    const artist = data.get('artist') as FormControl;
    const caseMode = data.get('rwfsCase') as FormControl;
    const mappings = data.get('character_mappings') as FormArray;
    this.cookieService.setCookie(this.COOKIE_NAME, new RWFSRequest(
      mappings.getRawValue().map(mapping => {
        return new Mapping(mapping.character, mapping.mapping, mapping.chance);
      }),
      passwordLength.value,
      caseMode.value,
      artist.value
    ));
  }

  public getCookie(): FormGroup {
    const cookieValue = this.cookieService.getCookieValue(this.COOKIE_NAME, this.DEFAULT_COOKIE_VALUE) as RWFSRequest;
    return this.formBuilder.group({
      password_length: cookieValue.passwordLength,
      character_mappings: this.formBuilder.array(
        cookieValue.mappings.map(mapping => this.formBuilder.group({
          character: mapping.mappedCharacter,
          mapping: mapping.mappings,
          chance: mapping.mappingChance
        }))
      ),
      rwfsCase: cookieValue.rwCase,
      artist: cookieValue.artist
    });
  }
}
