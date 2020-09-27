import { catchError } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';
import { PasswordOptions } from '../models/password-options.model'

@Injectable({
  providedIn: 'root'
})
export class PasswordGeneratorService {

  constructor(private http: HttpClient) { }

  public generate(data: PasswordOptions): Observable<string> {
    let url = `${environment.apiUrl}/`;
    let params = this.getParams(data);

    return this.http
      .get<string>(url, { params: params })
      .pipe(
        catchError(this.handleError)
      )
  }

  private getParams(data: object): HttpParams {
    let params: HttpParams = new HttpParams()
    Object.entries(data).forEach(
      (v) => params = params.append(v[0], v[1])
    )

    return params;
  }

  private handleError(error: HttpErrorResponse) {
    return throwError(error.error)
  };
}
