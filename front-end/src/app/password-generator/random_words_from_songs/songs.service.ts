import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { RWFSRequest } from './model/rwfsrequest';
import { RWFSResponse } from './model/rwfsresponse';
import { catchError } from 'rxjs/internal/operators';
import { throwError } from 'rxjs/index';
import { ToastrService } from 'ngx-toastr';
import { Subscription } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable()
export class SongsService {

  constructor(private http: HttpClient, private toastr: ToastrService) { }

  getSongWordsPassword(url: string, data: RWFSRequest) {
    return this.http.post<RWFSResponse>(url.concat('/random/song'), data, httpOptions)
      .pipe(
        catchError(this.handleError.bind(this))
      );
  }

  private handleError (error: Response | any) {
    console.error(error.error || error);
    this.toastr.error(
      'Error during password creation. Check logs for more information',
      'Password creation failed'
    );
    return throwError(error.message || error);
  }
}
