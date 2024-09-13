Para desenvolver um sistema que envie informações de compras de um ecommerce para o WhatsApp do vendedor, utilizando Angular no frontend, Kafka como mensageiro e diferentes backends (Python, Node.js, .NET Core), vamos dividir o sistema em três partes principais: o frontend Angular, o backend que consome mensagens do Kafka e o serviço que envia mensagens para o WhatsApp.

### Arquitetura do Sistema

1. **Frontend Angular:**
   - Interface onde os dados da compra são inseridos e enviados para o backend.
   - Responsável por coletar informações de compra (como nome do cliente, produto comprado, etc.) e enviar essas informações para o backend.

2. **Backend Kafka Consumer:**
   - Responsável por consumir mensagens do tópico do Kafka que contêm informações sobre compras.
   - Pode ser implementado em Python, Node.js ou .NET Core, dependendo da preferência e do ambiente do desenvolvedor.

3. **Serviço de Envio para WhatsApp:**
   - Recebe as informações de compra do Kafka e envia uma mensagem formatada para o WhatsApp do vendedor.

### Implementação Passo a Passo

#### 1. Frontend Angular

Crie um formulário no Angular para capturar as informações da compra e enviá-las para o backend. Para simplificar, vamos assumir que o frontend envia um JSON com os detalhes da compra para o backend através de uma requisição HTTP POST.

Exemplo de código Angular (`ecommerce-form.component.ts`):

```typescript
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-ecommerce-form',
  templateUrl: './ecommerce-form.component.html',
  styleUrls: ['./ecommerce-form.component.css']
})
export class EcommerceFormComponent {

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
```

Exemplo de template HTML (`ecommerce-form.component.html`):

```html
<form (ngSubmit)="enviarCompra()">
  <label>Nome do Cliente:</label>
  <input type="text" [(ngModel)]="compra.nomeCliente" name="nomeCliente" required>
  <br><br>
  
  <label>Produto Comprado:</label>
  <input type="text" [(ngModel)]="compra.produtoComprado" name="produtoComprado" required>
  <br><br>
  
  <label>Valor:</label>
  <input type="number" [(ngModel)]="compra.valor" name="valor" required>
  <br><br>
  
  <button type="submit">Enviar Compra</button>
</form>
```

#### 2. Backend Kafka Consumer

Implemente um serviço backend que consome mensagens do tópico do Kafka e envia as informações relevantes para o serviço de envio para WhatsApp. Aqui estão exemplos de implementações para Python, Node.js e .NET Core:

- **Python (utilizando Kafka-Python):**

  ```python
  from kafka import KafkaConsumer
  import requests

  consumer = KafkaConsumer('compras_topic', bootstrap_servers=['localhost:9092'])

  for message in consumer:
      compra = message.value.decode('utf-8')
      # Lógica para enviar a compra para o serviço de WhatsApp
      requests.post('http://localhost:5000/whatsapp', data=compra)
  ```

- **Node.js (utilizando kafka-node):**

  ```javascript
  const kafka = require('kafka-node');
  const request = require('request');

  const consumer = new kafka.ConsumerGroup({
      kafkaHost: 'localhost:9092',
      groupId: 'compras-consumer-group',
      topics: ['compras_topic']
  });

  consumer.on('message', function(message) {
      const compra = JSON.parse(message.value);
      // Lógica para enviar a compra para o serviço de WhatsApp
      request.post('http://localhost:3000/whatsapp', { json: compra }, function(error, response, body) {
          if (error) {
              console.error('Erro ao enviar para WhatsApp:', error);
          } else {
              console.log('Compra enviada para WhatsApp:', body);
          }
      });
  });
  ```

- **.NET Core (utilizando Confluent.Kafka):**

  ```csharp
  using System;
  using Confluent.Kafka;
  using System.Threading.Tasks;
  using System.Net.Http;
  using Newtonsoft.Json;

  class Program
  {
      static async Task Main(string[] args)
      {
          var config = new ConsumerConfig
          {
              BootstrapServers = "localhost:9092",
              GroupId = "compras-consumer-group",
              AutoOffsetReset = AutoOffsetReset.Earliest
          };

          using (var consumer = new ConsumerBuilder<Ignore, string>(config).Build())
          {
              consumer.Subscribe("compras_topic");

              while (true)
              {
                  var consumeResult = consumer.Consume();
                  var compra = JsonConvert.DeserializeObject(consumeResult.Message.Value);

                  // Lógica para enviar a compra para o serviço de WhatsApp
                  using (var client = new HttpClient())
                  {
                      var response = await client.PostAsJsonAsync("http://localhost:5000/whatsapp", compra);
                      response.EnsureSuccessStatusCode();
                      var responseBody = await response.Content.ReadAsStringAsync();
                      Console.WriteLine($"Compra enviada para WhatsApp: {responseBody}");
                  }
              }
          }
      }
  }
  ```

#### 3. Serviço de Envio para WhatsApp

Implemente um serviço backend que receba as informações da compra e envie uma mensagem formatada para o WhatsApp do vendedor. Aqui um exemplo genérico usando Flask para Python:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def enviar_whatsapp():
    compra = request.json
    # Lógica para formatar e enviar mensagem para o WhatsApp do vendedor
    mensagem = f'Nova compra!\nCliente: {compra["nomeCliente"]}\nProduto: {compra["produtoComprado"]}\nValor: R${compra["valor"]}'
    # Código para enviar a mensagem para o WhatsApp

    return jsonify({'message': 'Mensagem enviada para WhatsApp do vendedor'})

if __name__ == '__main__':
    app.run(port=5000)
```

### Configuração e Execução

- **Configuração do Kafka:**
  - Instale e configure o Kafka localmente ou em um servidor.
  - Crie um tópico `compras_topic` para armazenar as mensagens de compra.

- **Configuração do Angular:**
  - Instale o Angular CLI e configure seu projeto.
  - Implemente o componente `EcommerceFormComponent` para enviar dados de compra para o backend.

- **Configuração do Backend (Python/Node.js/.NET Core):**
  - Instale as dependências necessárias para Kafka e implemente o consumidor de mensagens.
  - Implemente o serviço que recebe mensagens do Kafka e envia para o WhatsApp.

- **Configuração do Serviço de Envio para WhatsApp:**
  - Implemente um serviço que receba dados da compra e envie uma mensagem formatada para o WhatsApp do vendedor.

- **Execução:**
  - Execute cada parte do sistema (frontend Angular, Kafka Consumer backend, WhatsApp Service backend).
  - Teste o sistema enviando dados de compra pelo frontend e verifique se a mensagem é entregue corretamente no WhatsApp do vendedor.

Este sistema é um exemplo básico e pode ser expandido com funcionalidades adicionais, como validações de dados, autenticação, e tratamento de erros mais robusto. Certifique-se de adaptar o código conforme suas necessidades específicas e considerar aspectos de segurança, como a proteção de chaves de API e dados sensíveis.