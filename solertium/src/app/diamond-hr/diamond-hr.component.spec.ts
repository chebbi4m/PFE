import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiamondHrComponent } from './diamond-hr.component';

describe('DiamondHrComponent', () => {
  let component: DiamondHrComponent;
  let fixture: ComponentFixture<DiamondHrComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DiamondHrComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DiamondHrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
