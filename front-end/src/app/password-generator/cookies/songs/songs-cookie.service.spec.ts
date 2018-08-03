import { TestBed, inject } from '@angular/core/testing';

import { SongsCookieService } from './songs-cookie.service';

describe('SongsCookieService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SongsCookieService]
    });
  });

  it('should be created', inject([SongsCookieService], (service: SongsCookieService) => {
    expect(service).toBeTruthy();
  }));
});
