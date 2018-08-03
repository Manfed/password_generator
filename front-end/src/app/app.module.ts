import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { PasswordGeneratorComponent } from './password-generator/password-generator.component';
import { RCService } from './password-generator/random_characters/rc.service';
import { CommonsService } from './password-generator/commons/commons.service';
import { RWService } from './password-generator/random_words/rw.service';
import { CookieModule } from 'ngx-cookie';
import { RandomCharactersCookieService } from './password-generator/cookies/characters/random-characters-cookie.service';
import { SongsCookieService } from './password-generator/cookies/songs/songs-cookie.service';
import { RandomWordsCookieService } from './password-generator/cookies/words/random-words-cookie.service';
import { GeneratorCookiesService } from './password-generator/cookies/generator-cookies.service';
import { PasswordStrengthMeterModule } from 'angular-password-strength-meter';
import { ToastrModule } from 'ngx-toastr';
import { SongsService } from './password-generator/random_words_from_songs/songs.service';
import { LoadingModule } from 'ngx-loading';

@NgModule({
  declarations: [
    AppComponent,
    PasswordGeneratorComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    PasswordStrengthMeterModule,
    LoadingModule.forRoot({
      fullScreenBackdrop: true
    }),
    NgbModule.forRoot(),
    CookieModule.forRoot(),
    ToastrModule.forRoot()
  ],
  providers: [
    RCService,
    RWService,
    SongsService,
    CommonsService,
    GeneratorCookiesService,
    RandomCharactersCookieService,
    RandomWordsCookieService,
    SongsCookieService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
