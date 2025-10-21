from flask import Flask, jsonify, request


PRODUTOS_DB =  [ # Lista de produtos
        {"id": 1, "nome": "Produto A", "preco": 10.0},
        {"id": 2, "nome": "Produto B", "preco": 20.0},
        {"id": 3, "nome": "Produto C", "preco": 30.0}
    ]

USUARIOS_DB = [{"id": 1,"nome": "João Silva","email": "joaosilva@gmail.com"},
                {"id": 2,"nome": "Maria Oliveira","email": "maria@gmail.com"}
        ]

app = Flask(__name__) # Criação da aplicação Flask
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

@app.route('/produtos', methods=['GET']) # Rota que responde apenas GET
def listarProdutos(): # Função que retorna uma lista de produtos
    return jsonify(PRODUTOS_DB) # Retorna a lista de produtos em formato JSON

@app.route('/produtos/<int:produto_id>', methods=['GET']) # Rota que responde apenas GET com parametro
def obterProduto(produto_id): # Função que retorna um produto específico

    for produto in PRODUTOS_DB: # Percorre a lista de produtos
        if produto['id'] == produto_id: # Verifica se o ID do produto corresponde ao ID fornecido
            return jsonify(produto) # Retorna o produto em formato JSON
    return jsonify({"mensagem": "Produto não encontrado"}), 404 # Retorna mensagem de erro se o produto não for encontrado

@app.route('/usuarios', methods=['GET']) # Rota que responde apenas GET
def listarUsuarios(): # Função que retorna uma lista de usuários
    return jsonify(USUARIOS_DB) # Retorna a lista de usuários em formato JSON

@app.route('/usuarios/<int:usuario_id>', methods=['GET']) # Rota que responde apenas GET com parametro
def obterUsuario(usuario_id): # Função que retorna um usuário específico
    for usuario in USUARIOS_DB: # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            return jsonify(usuario) # Retorna o usuário em formato JSON
    return jsonify({"mensagem": "Usuário não encontrado"}), 404 # Retorna mensagem de erro se o usuário não for encontrado

@app.route('/produtos', methods=['POST']) 
def criarProduto():

    global PRODUTOS_DB

    novoProduto = request.get_json() 

    # 1. Gera um novo ID baseado na lista global PRODUTOS_DB
    novoID = PRODUTOS_DB[-1]['id'] + 1 

    # 2. Adiciona o ID ao novo dicionário
    novoProduto['id'] = novoID 

    # 3. Adiciona o novo produto à lista GLOBAL
    PRODUTOS_DB.append(novoProduto) 

    return jsonify(novoProduto), 201

    
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
@app.route('/produtos/<int:produto_id>', methods=['PUT']) 
def atualizarProduto(produto_id): # Remova as chaves
    
    global PRODUTOS_DB
    
    # 1. Percorre a lista para achar o índice
    for indice, produto in enumerate(PRODUTOS_DB):
        if produto['id'] == produto_id:
            
            # 2. Recebe os novos dados do JSON
            dadosAtualizados = request.get_json() # Usando 'dadosAtualizados'
            
            # 3. Garante que o ID do objeto atualizado é o ID correto
            dadosAtualizados['id'] = produto_id 
            
            # 4. Substitui o item antigo pelo novo no índice encontrado
            PRODUTOS_DB[indice] = dadosAtualizados
            
            # 5. Retorna o objeto atualizado com status 200
            return jsonify(dadosAtualizados), 200 # <<< Retorna 200 (OK)
    
    # Se o loop terminar e o produto não for encontrado
    return jsonify({"mensagem": "Produto não encontrado para atualização"}), 404




if __name__ == '__main__': # verifica se o script esta sendo executado
    app.run(debug=True) # Inicia o servidor Flask em modo debug
