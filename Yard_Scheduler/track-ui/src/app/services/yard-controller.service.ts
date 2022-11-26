import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {catchError} from "rxjs";
import {Track} from "../models/track";

@Injectable({
  providedIn: 'root'
})
export class YardControllerService {

  private readonly URL: string = '/yard_capacity/list_tracks_api/';
  constructor(private readonly http:  HttpClient) { }

  get() {
    return this.http.get(this.URL);
  }
}
