import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl} from '@angular/forms';
import { RCService } from './random_characters/rc.service';
import { RCModel } from './random_characters/model/rcmodel';
import { RCResponse } from './random_characters/model/rcresponse';

@Component({
  selector: 'password-generator',
  templateUrl: './password-generator.component.html',
  styleUrls: ['./password-generator.component.css']
})
export class PasswordGeneratorComponent implements OnInit {
  @Input() apiLocation: string;

  formBuilder: FormBuilder;
  rc_form: FormGroup;
  rc_character_groups: FormArray;
  rc_password: RCResponse;

  constructor(formBuilder: FormBuilder, private rcService: RCService) {
    this.formBuilder = formBuilder;
  }

  ngOnInit() {
    this.rc_form = this.formBuilder.group({
      password_length: '',
      character_groups: this.formBuilder.array([ this.createRCCharacterGroups() ])
    });
    this.rc_character_groups = this.rc_form.get('character_groups') as FormArray;
  }

  createRCCharacterGroups(): FormGroup {
    return this.formBuilder.group({
      value: ''
    });
  }

  addRCCharacterGroup(): void {
    this.rc_character_groups.push(this.createRCCharacterGroups());
  }

  removeRCCharacterGroup(index: number): void {
    if (this.rc_character_groups.length  > 1) {
      this.rc_character_groups.removeAt(index);
    } else {
      console.warn('At least one character group required');
    }
  }

  onRCSubmit() {
    if (this.rc_form.valid) {
      const formControl = this.rc_form.get('password_length') as FormControl;
      const data = new RCModel(
        this.rc_character_groups.getRawValue(),
        formControl.value
      );
      this.rcService.getRandomCharactersPassword(this.apiLocation, data).subscribe(rcResult => this.rc_password = rcResult);
    }
  }
}
