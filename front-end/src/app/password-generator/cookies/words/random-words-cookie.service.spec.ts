import { TestBed, inject } from '@angular/core/testing';

import { RandomWordsCookieService } from './random-words-cookie.service';

describe('RandomWordsCookieService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RandomWordsCookieService]
    });
  });

  it('should be created', inject([RandomWordsCookieService], (service: RandomWordsCookieService) => {
    expect(service).toBeTruthy();
  }));
});
