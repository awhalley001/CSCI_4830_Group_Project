import { TestBed } from '@angular/core/testing';

import { YardControllerService } from './yard-controller.service';

describe('YardControllerService', () => {
  let service: YardControllerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(YardControllerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
