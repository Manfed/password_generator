import { TestBed, inject } from '@angular/core/testing';

import { RWService } from './rw.service';

describe('RWService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RWService]
    });
  });

  it('should be created', inject([RWService], (service: RWService) => {
    expect(service).toBeTruthy();
  }));
});
