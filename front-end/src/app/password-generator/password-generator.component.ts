import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, FormControl} from '@angular/forms';
import { RCService } from './random_characters/rc.service';
import { RCModel } from './random_characters/model/rcmodel';
import { RCResponse } from './random_characters/model/rcresponse';
import { CommonsService } from './commons/commons.service';
import { RWResponse } from './random_words/model/rwresponse';
import { RWRequest } from './random_words/model/rwrequest';
import { RWService } from './random_words/rw.service';
import { RandomCharactersCookieService } from './cookies/characters/random-characters-cookie.service';
import { RandomWordsCookieService } from './cookies/words/random-words-cookie.service';
import { SongsCookieService } from './cookies/songs/songs-cookie.service';
import { RWFSResponse } from './random_words_from_songs/model/rwfsresponse';
import { SongsService } from './random_words_from_songs/songs.service';
import { RWFSRequest } from './random_words_from_songs/model/rwfsrequest';

@Component({
  selector: 'password-generator',
  templateUrl: './password-generator.component.html',
  styleUrls: ['./password-generator.component.css']
})

export class PasswordGeneratorComponent implements OnInit {

  @Input() apiLocation: string;

  loading: boolean;

  /**
   * Password built from random characters from user-defined characters
   */

  rc_form: FormGroup;
  rc_character_groups: FormArray;
  rc_show_generation_results: boolean;
  rc_password_alert_type: string;
  rc_password: RCResponse;

  /**
   * Password created from random words with user-defined character mappings.
   */

  rw_form: FormGroup;
  rw_character_mappings: FormArray;
  rw_show_generation_results: boolean;
  rw_password_alert_type: string;
  rw_password: RWResponse;

  /**
   * Password created from words from song lyrics with character mappings.
   */

  rwfs_form: FormGroup;
  rwfs_character_mappings: FormArray;
  rwfs_show_generation_results: boolean;
  rwfs_password_alert_type: string;
  rwfs_password: RWFSResponse;

  constructor(private formBuilder: FormBuilder,
              private rcService: RCService,
              private rwService: RWService,
              private songsService: SongsService,
              private rcCookieService: RandomCharactersCookieService,
              private rwCookieService: RandomWordsCookieService,
              private rwfsCookieService: SongsCookieService) {
  }

  ngOnInit() {
    // Random characters
    this.rc_form = this.rcCookieService.getCookie();
    this.rc_character_groups = this.rc_form.get('character_groups') as FormArray;

    // Random words
    this.rw_form = this.rwCookieService.getCookie();
    this.rw_character_mappings = this.rw_form.get('character_mappings') as FormArray;

    // Random words from songs
    this.rwfs_form = this.rwfsCookieService.getCookie();
    this.rwfs_character_mappings = this.rwfs_form.get('character_mappings') as FormArray;
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
      this.turnLoadingOn();
      const formControl = this.rc_form.get('password_length') as FormControl;
      const data = new RCModel(
        this.rc_character_groups.getRawValue(),
        formControl.value
      );
      this.rcService.getRandomCharactersPassword(this.apiLocation, data).subscribe(rcResult => {
        this.rc_password = rcResult;
        this.rc_show_generation_results = true;
        if (rcResult.entropy < CommonsService.MEDIUM_PASSWORD_ENTROPY) {
          this.rc_password_alert_type = 'danger';
        } else if (rcResult.entropy >= CommonsService.MEDIUM_PASSWORD_ENTROPY &&
          rcResult.entropy < CommonsService.STRONG_PASSWORD_ENTROPY) {
          this.rc_password_alert_type = 'warning';
        } else {
          this.rc_password_alert_type = 'success';
        }
        this.turnLoadingOff();
      }, err => {
        this.turnLoadingOff();
      });
      this.rcCookieService.setCookie(this.rc_form);
    }
  }

  createRWCharacterMappings(): FormGroup {
    return this.formBuilder.group({
      character: '',
      mapping: '',
      chance: 50
    });
  }

  addRWCharacterGroup(): void {
    this.rw_character_mappings.push(this.createRWCharacterMappings());
  }

  removeRWCharacterGroup(index: number): void {
    if (this.rw_character_mappings.length  > 1) {
      this.rw_character_mappings.removeAt(index);
    } else {
      console.warn('At least one character group required');
    }
  }

  onRWSubmit() {
    if (this.rw_form.valid) {
      this.turnLoadingOn();
      const formControl = this.rw_form.get('password_length') as FormControl;
      const caseMode = this.rw_form.get('rwCase') as FormControl;
      const data = new RWRequest(
        this.rw_character_mappings.getRawValue(),
        formControl.value,
        caseMode.value
      );
      this.rwService.getRandomWordsPassword(this.apiLocation, data).subscribe(rwResult => {
        this.rw_password = this.parseRWResults(rwResult);
        this.rw_show_generation_results = true;
        if (rwResult.entropy < CommonsService.MEDIUM_PASSWORD_ENTROPY) {
          this.rw_password_alert_type = 'danger';
        } else if (rwResult.entropy >= CommonsService.MEDIUM_PASSWORD_ENTROPY &&
          rwResult.entropy < CommonsService.STRONG_PASSWORD_ENTROPY) {
          this.rw_password_alert_type = 'warning';
        } else {
          this.rw_password_alert_type = 'success';
        }
        this.turnLoadingOff();
      }, err => {
        this.turnLoadingOff();
      });
      this.rwCookieService.setCookie(this.rw_form);
    }
  }

  getRandomColor() {
    let color = Math.floor(0x1000000 * Math.random());
    // When color too close to white -> move it to darker colors.
    if (color > 0xC8C8C8) {
      color -= 0x373737;
    }
    return '#' + ('000000' + color.toString()).slice(-6);
  }

  parseRWResults(rwResponse: any): RWResponse {
    const colors = [];
    for (let i = 0; i < rwResponse.used_words.length; i++) {
      colors.push(this.getRandomColor());
    }
    return new RWResponse(rwResponse.passwordWords,
                          rwResponse.entropy,
                          rwResponse.used_words,
                          colors,
                          rwResponse.passwordWords.reduce((previousValue, currentValue) => previousValue + currentValue, ''),
                          rwResponse.isSafe);
  }

  onRWFSSubmit() {
    if (this.rwfs_form.valid) {
      this.turnLoadingOn();
      const formControl = this.rwfs_form.get('password_length') as FormControl;
      const caseMode = this.rwfs_form.get('rwfsCase') as FormControl;
      const artist = this.rwfs_form.get('artist') as FormControl;
      const data = new RWFSRequest(
        this.rwfs_character_mappings.getRawValue(),
        formControl.value,
        caseMode.value,
        artist.value
      );
      this.songsService.getSongWordsPassword(this.apiLocation, data).subscribe(rwResult => {
        this.rwfs_password = this.parseRWFSResults(rwResult);
        this.rwfs_show_generation_results = true;
        if (rwResult.entropy < CommonsService.MEDIUM_PASSWORD_ENTROPY) {
          this.rwfs_password_alert_type = 'danger';
        } else if (rwResult.entropy >= CommonsService.MEDIUM_PASSWORD_ENTROPY &&
          rwResult.entropy < CommonsService.STRONG_PASSWORD_ENTROPY) {
          this.rwfs_password_alert_type = 'warning';
        } else {
          this.rwfs_password_alert_type = 'success';
        }
        this.turnLoadingOff();
      }, err => {
        this.turnLoadingOff();
      });
      this.rwfsCookieService.setCookie(this.rwfs_form);
    }
  }

  parseRWFSResults(rwResponse: any): RWFSResponse {
    const colors = [];
    for (let i = 0; i < rwResponse.used_words.length; i++) {
      colors.push(this.getRandomColor());
    }
    return new RWFSResponse(
      rwResponse.password_words,
      rwResponse.entropy,
      rwResponse.used_words,
      colors,
      rwResponse.password_words.reduce((previousValue, currentValue) => previousValue + currentValue, ''),
      rwResponse.lyrics,
      rwResponse.song_name,
      rwResponse.isSafe);
  }

  addRWFSCharacterGroup(): void {
    this.rwfs_character_mappings.push(this.createRWCharacterMappings());
  }

  removeRWFSCharacterGroup(index: number): void {
    if (this.rwfs_character_mappings.length  > 1) {
      this.rwfs_character_mappings.removeAt(index);
    } else {
      console.warn('At least one character group required');
    }
  }

  turnLoadingOn() {
    this.loading = true;
  }

  turnLoadingOff() {
    this.loading = false;
  }
}
