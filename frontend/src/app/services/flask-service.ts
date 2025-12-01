import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
@Injectable({
providedIn: 'root',
})
export class FlaskService {
constructor(private http: HttpClient) {}
getProfilo() {
return this.http.get("https://psychic-spoon-g4xqrv4vq4j7f9jw5-5000.app.github.dev/profilo");
}
}