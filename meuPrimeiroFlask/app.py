from flask import Flask, jsonify, request
from produto.ProdutoController import produtoAPI
from usuario.UsuarioController import usuarioAPI

app = Flask(__name__) # Criação da aplicação Flask
app.register_blueprint(produtoAPI) # Registro do Blueprint na aplicação principal
app.register_blueprint(usuarioAPI) # Registro do Blueprint na aplicação principal

@app.route('/', methods=['GET']) # rota que responde apenas GET
def helloWord(): # Função que retorna uma mensagem
    return "Olá, Flask!"

@app.route('/status', methods=['GET']) # Rota que responde apenas GET
def status(): # Função que retorna o status da aplicação

    respostaJson = { # Dicionário com a resposta JSON
        "apiNome": "Minha API Flask",
        "status" : "Online",
        "versao": "1.0.0",
        "timestamp": "2024-06-01T12:00:00Z"
    }
    return jsonify(respostaJson) # Retorna a resposta em formato JSON

if __name__ == '__main__': # verifica se o script esta sendo executado
    app.run(debug=True) # Inicia o servidor Flask em modo debug
