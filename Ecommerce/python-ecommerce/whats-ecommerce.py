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
