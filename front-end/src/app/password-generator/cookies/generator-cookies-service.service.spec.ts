import { TestBed, inject } from '@angular/core/testing';

import { GeneratorCookiesService } from './generator-cookies.service';

describe('GeneratorCookiesServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GeneratorCookiesService]
    });
  });

  it('should be created', inject([GeneratorCookiesService], (service: GeneratorCookiesService) => {
    expect(service).toBeTruthy();
  }));
});
