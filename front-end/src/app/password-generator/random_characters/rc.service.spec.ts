import { TestBed, inject } from '@angular/core/testing';

import { RCServiceService } from './rc.service';

describe('RCServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RCServiceService]
    });
  });

  it('should be created', inject([RCServiceService], (service: RCServiceService) => {
    expect(service).toBeTruthy();
  }));
});
