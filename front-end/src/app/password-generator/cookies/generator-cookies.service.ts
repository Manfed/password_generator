import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie';

@Injectable({
  providedIn: 'root'
})
export class GeneratorCookiesService {

  constructor(private cookieService: CookieService) { }

  setCookie(cookieName: string, value: any) {
    this.cookieService.putObject(cookieName, value);
  }

  getCookieValue(cookieName: string, defaultValue: any) {
    const cookieValue = this.cookieService.getObject(cookieName);
    if (cookieValue) {
      return cookieValue;
    } else {
      return defaultValue;
    }
  }
}
