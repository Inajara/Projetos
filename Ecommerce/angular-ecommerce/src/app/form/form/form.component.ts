import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-form',
  standalone: true,
  imports: [],
  templateUrl: './form.component.html',
  styleUrl: './form.component.css'
})
export class FormComponent {
  // Modelo para os dados da compra
  compra = {
    nomeCliente: '',
    produtoComprado: '',
    valor: 0,
    // outros campos relevantes
  };

  constructor(private http: HttpClient) { }

  enviarCompra() {
    // Enviar os dados da compra para o backend
    this.http.post<any>('http://localhost:3000/compras', this.compra)
      .subscribe(
        response => {
          console.log('Compra enviada com sucesso para o backend', response);
        },
        error => {
          console.error('Erro ao enviar compra para o backend', error);
        }
      );
  }
}
