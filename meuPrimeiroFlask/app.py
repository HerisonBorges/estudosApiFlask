from flask import Flask, jsonify, request
from produto.ProdutoController import produtoAPI

USUARIOS_DB = [{"id": 1,"nome": "João Silva","email": "joaosilva@gmail.com"},
                {"id": 2,"nome": "Maria Oliveira","email": "maria@gmail.com"}
        ]

app = Flask(__name__) # Criação da aplicação Flask
app.register_blueprint(produtoAPI) # Registro do Blueprint na aplicação principal

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





@app.route('/usuarios', methods=['GET']) # Rota que responde apenas GET
def listarUsuarios(): # Função que retorna uma lista de usuários
    return jsonify(USUARIOS_DB) # Retorna a lista de usuários em formato JSON

@app.route('/usuarios/<int:usuario_id>', methods=['GET']) # Rota que responde apenas GET com parametro
def obterUsuario(usuario_id): # Função que retorna um usuário específico
    for usuario in USUARIOS_DB: # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            return jsonify(usuario) # Retorna o usuário em formato JSON
    return jsonify({"mensagem": "Usuário não encontrado"}), 404 # Retorna mensagem de erro se o usuário não for encontrado


    
@app.route('/usuarios', methods=['POST']) 
def criarUsuario():

    global USUARIOS_DB
    
    dados = request.get_json() 
    
    # 1. Gera um novo ID baseado na lista global USUARIOS_DB
    novoID = USUARIOS_DB[-1]['id'] + 1 

    # 2. Adiciona o ID ao novo dicionário
    dados['id'] = novoID 
    
    # 3. Adiciona o novo usuário à lista GLOBAL
    USUARIOS_DB.append(dados)

    return jsonify(dados), 201

# ROTA PUT (Atualização) - Remova as chaves e garanta os dois pontos



@app.route('/usuarios/<int:usuario_id>', methods=['PUT']) # Rota PUT para atualizar usuário
def atualizarUsuario(usuario_id):
    global USUARIOS_DB
    for indice, usuario in enumerate(USUARIOS_DB): # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            dadosAtualizados = request.get_json() # Pega os dados do request
            dadosAtualizados['id'] = usuario_id # Garante que o ID permaneça o mesmo
            USUARIOS_DB[indice] = dadosAtualizados # Atualiza o usuário na lista
            return jsonify(dadosAtualizados), 200 # Retorna o usuário atualizado
    return jsonify({"mensagem": "Usuário não encontrado para atualização"}), 404 # Retorna mensagem de erro se o usuário não for encontrado

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE']) # Rota DELETE para deletar usuário
def deletarUsuario(usuario_id): # Função que deleta um usuário específico
    global USUARIOS_DB # Variável global para acessar a lista de usuários
    for indice, usuario in enumerate(USUARIOS_DB): # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            USUARIOS_DB.pop(indice) # Remove o usuário da lista
            return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200
    return jsonify({"mensagem": "Usuário não encontrado para deleção"}), 404








if __name__ == '__main__': # verifica se o script esta sendo executado
    app.run(debug=True) # Inicia o servidor Flask em modo debug
