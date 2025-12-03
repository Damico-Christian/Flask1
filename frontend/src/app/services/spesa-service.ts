import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SpesaService {

  private listaSpesa = signal<string[]>([]);

  constructor() {}

  getLista() {
    return this.listaSpesa;   // restituisce un SIGNAL
  }

  aggiungiElemento(item: string) {
    this.listaSpesa.update(curr => [...curr, item]);
  }
}
