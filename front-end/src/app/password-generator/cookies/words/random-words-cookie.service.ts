import { Injectable } from '@angular/core';
import {GeneratorCookiesService} from "../generator-cookies.service";
import {CommonsService} from "../../commons/commons.service";
import {RWRequest} from "../../random_words/model/rwrequest";
import {FormArray, FormBuilder, FormControl, FormGroup} from "@angular/forms";
import {Mapping} from "../../commons/mapping";

@Injectable()
export class RandomWordsCookieService {

  private readonly COOKIE_NAME = 'rw_character_groups';

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
    rwCase: 'random'
  } as RWRequest;

  constructor(private cookieService: GeneratorCookiesService, private formBuilder: FormBuilder) { }

  public setCookie(data: FormGroup) {
    const passwordLength = data.get('password_length') as FormControl;
    const caseMode = data.get('rwCase') as FormControl;
    const mappings = data.get('character_mappings') as FormArray;
    this.cookieService.setCookie(this.COOKIE_NAME, new RWRequest(
      mappings.getRawValue().map(mapping => {
        return new Mapping(mapping.character, mapping.mapping, mapping.chance);
      }),
      passwordLength.value,
      caseMode.value
    ));
  }

  public getCookie(): FormGroup {
    const cookieValue = this.cookieService.getCookieValue(this.COOKIE_NAME, this.DEFAULT_COOKIE_VALUE) as RWRequest;
    return this.formBuilder.group({
      password_length: cookieValue.passwordLength,
      character_mappings: this.formBuilder.array(
        cookieValue.mappings.map(mapping => this.formBuilder.group({
          character: mapping.mappedCharacter,
          mapping: mapping.mappings,
          chance: mapping.mappingChance
        }))
      ),
      rwCase: cookieValue.rwCase
    });
  }
}
