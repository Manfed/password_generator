import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { RWRequest } from './model/rwrequest';
import { RWResponse } from './model/rwresponse';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable()
export class RWService {

  constructor(private http: HttpClient) { }

  getRandomWordsPassword(url: string, data: RWRequest) {
    return this.http.post<RWResponse>(url.concat('/random/words'), data, httpOptions)
      .pipe(
        catchError(this.handleErrorObservable)
      );
  }

  private handleErrorObservable (error: Response | any) {
    console.error(error.message || error);
    return throwError(error.message || error);
  }
}
