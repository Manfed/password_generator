import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { PasswordGeneratorComponent } from './password-generator/password-generator.component';
import { RCService } from './password-generator/random_characters/rc.service';

@NgModule({
  declarations: [
    AppComponent,
    PasswordGeneratorComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule.forRoot()
  ],
  providers: [
    RCService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
