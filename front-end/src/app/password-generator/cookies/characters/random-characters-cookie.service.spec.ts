import { TestBed, inject } from '@angular/core/testing';

import { RandomCharactersCookieService } from './random-characters-cookie.service';

describe('RandomCharactersCookieService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RandomCharactersCookieService]
    });
  });

  it('should be created', inject([RandomCharactersCookieService], (service: RandomCharactersCookieService) => {
    expect(service).toBeTruthy();
  }));
});
