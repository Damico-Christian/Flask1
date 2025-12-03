import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SpesaService } from './services/spesa-service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],        // <- necessario per *ngFor
  templateUrl: './app.html'
})
export class App implements OnInit {

  lista = signal<any[]>([]);
  nuovoElemento = signal('');

  constructor(private spesa: SpesaService) {}

  ngOnInit() {
    this.caricaLista();
  }

  caricaLista() {
    this.lista.set(this.spesa.getLista()());
  }

  aggiungi() {
    const val = this.nuovoElemento().trim();
    if (!val) return;

    this.spesa.aggiungiElemento(val);
    this.nuovoElemento.set('');
    this.caricaLista();
  }
}
