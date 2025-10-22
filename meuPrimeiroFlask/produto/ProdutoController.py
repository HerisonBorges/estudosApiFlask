from flask import Flask, Blueprint, jsonify, request
from produto.ProdutoService import *

produtoAPI = Blueprint('ProdutoController', __name__, url_prefix='/produtos')

@produtoAPI.route('/', methods=['GET']) # Rota que responde apenas GET
def listarProdutos(): # Função que retorna uma lista de produtos
    return listarTodosProdutos() # Chama a função do serviço para listar todos os produtos

@produtoAPI.route('/<int:produto_id>', methods=['GET']) # Rota que responde apenas GET com parametro
def obterProduto(produto_id): # Função que retorna um produto específico
    return obterProdutoPorId(produto_id) # Chama a função do serviço para obter o produto por ID

@produtoAPI.route('/', methods=['POST']) 
def criarProduto():
    return criar() # Chama a função do serviço para criar um novo produto

@produtoAPI.route('/<int:produto_id>', methods=['PUT']) 
def atualizarProduto(produto_id): # Remova as chaves
    return atualizar(produto_id) # Chama a função do serviço para atualizar o produto

@produtoAPI.route('/<int:produto_id>', methods=['DELETE']) # Rota DELETE para deletar produto
def deletarProduto(produto_id):
    return deletar(produto_id) # Chama a função do serviço para deletar o produto