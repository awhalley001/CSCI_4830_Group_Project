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
   return this.httpClient.post('http://ec2-54-91-175-209.compute-1.amazonaws.com:8000/uploadFile', formParams);
 }
}
