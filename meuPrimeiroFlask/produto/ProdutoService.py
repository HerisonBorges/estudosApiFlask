from flask import Flask, jsonify, request
from produto.ProdutoRepository import *


def listarTodosProdutos(): # Função que retorna uma lista de produtos
    return jsonify(todosProdutos()) # Retorna o objeto retornado pela função todosProdutos em formato JSON


def obterProdutoPorId(produto_id): # Função que retorna um produto específico

    produto = porId(produto_id) # Chama a função porId do ProdutoRepository
    if produto: 
        return jsonify(produto) 
    else:
        return jsonify({"mensagem": "Produto não encontrado"}), 404
    

def criar():
    novoProduto = request.get_json() 
    produto = adicionarProduto(novoProduto) # Chama a função adicionarProduto do ProdutoRepository
    return jsonify(produto), 201 # Retorna o objeto adicionado com status 201

def atualizar(produto_id): 
    produtoParaAtualizar = request.get_json() # Pega os dados do request
    produtoParaAtualizar['id'] = produto_id # Adiciona o ID ao dicionário
    produtoAtualizado = salvarAlteração(produtoParaAtualizar) # Chama a função salvarAlteração do ProdutoRepository
    if produtoAtualizado: # Verifica se o produto foi atualizado
        return jsonify(produtoAtualizado), 200
    else:
        return jsonify({"mensagem": "Produto não encontrado para atualização"}), 404

def deletar(produto_id):
    if removerProduto(produto_id): # Chama a função deletar do ProdutoRepository
        return jsonify({"mensagem": "Produto deletado com sucesso"}), 200 # Retorna mensagem de sucesso
    else:
        return jsonify({"mensagem": "Produto não encontrado para deleção"}), 404 # Retorna mensagem de erro se o produto não for encontrado