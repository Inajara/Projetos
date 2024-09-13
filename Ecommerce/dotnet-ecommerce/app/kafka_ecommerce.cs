using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Confluent.Kafka;
using System.Threading.Tasks;
using System.Net.Http;
using Newtonsoft.Json;

namespace dotnet_ecommerce.app
{
    public class kafka_ecommerce
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
}