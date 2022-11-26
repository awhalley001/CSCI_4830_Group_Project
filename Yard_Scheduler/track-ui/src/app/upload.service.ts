import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from "rxjs";

@Injectable({
 providedIn: 'root'
})
export class UploadService {

 constructor(
   private httpClient: HttpClient,
 ) { }

 public uploadFile(file: File): Observable<any> {
   let formParams = new FormData();
   formParams.append('file', file)
   console.log(file);
   return this.httpClient.post('http://localhost:4200/uploadFile', formParams);
 }
}
