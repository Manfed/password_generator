import { Injectable } from '@angular/core';
import { GeneratorCookiesService } from '../generator-cookies.service';
import { RCModel } from '../../random_characters/model/rcmodel';
import { FormArray, FormBuilder, FormControl, FormGroup } from '@angular/forms';

@Injectable()
export class RandomCharactersCookieService {

  private readonly COOKIE_NAME = 'rc_character_groups';

  private readonly DEFAULT_GROUPS = [
    'ABCDEFGHIJKLMNOPRSTUWVQXXYZ',
    'abcdefghijklmnoprstuwvqxxyz',
    '0123456789',
    '!@#$%^&*()_+-=[]{}'
  ];

  private readonly DEFAULT_LENGTH = 20;

  private readonly DEFAULT_COOKIE_VALUE = new RCModel(this.DEFAULT_GROUPS, this.DEFAULT_LENGTH);

  constructor(private cookieService: GeneratorCookiesService, private formBuilder: FormBuilder) { }

  public setCookie(data: FormGroup) {
    const passwordLength = data.get('password_length') as FormControl;
    const groups = data.get('character_groups') as FormArray;
    this.cookieService.setCookie(this.COOKIE_NAME, new RCModel(
      groups.getRawValue().map(formGroup => formGroup.value),
      passwordLength.value
    ));
  }

  public getCookie(): FormGroup {
    const cookieValue = this.cookieService.getCookieValue(this.COOKIE_NAME, this.DEFAULT_COOKIE_VALUE) as RCModel;
    return this.formBuilder.group({
      password_length: cookieValue.length,
      character_groups: this.formBuilder.array(
        cookieValue.groups.map(group => this.formBuilder.group({
          value: group
        }))
      )
    });
  }
}
