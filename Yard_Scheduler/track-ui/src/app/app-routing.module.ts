import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { UploadCsvComponent } from './upload-csv/upload-csv.component';
import {YardComponent} from "./yard/yard.component";

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full'},
  { path: 'home', component: UploadCsvComponent},
  { path: 'yard', component: YardComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
