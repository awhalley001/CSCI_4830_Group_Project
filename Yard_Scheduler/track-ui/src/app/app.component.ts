import { Component } from '@angular/core';
import {TabDirective} from "ngx-bootstrap/tabs";
import {Router} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Hump Yard Scheduler';

  constructor(private readonly router: Router) {
  }

  tabSelected($event: TabDirective) {
    console.log('tab directive', $event);
    this.router.navigateByUrl($event.id as string);
  }
}
