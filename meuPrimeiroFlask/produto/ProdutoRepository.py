from flask import Flask, jsonify, request

PRODUTOS_DB =  [ # Lista de produtos
        {"id": 1, "nome": "Produto A", "preco": 10.0},
        {"id": 2, "nome": "Produto B", "preco": 20.0},
        {"id": 3, "nome": "Produto C", "preco": 30.0}
    ]

def todosProdutos(): # Função que retorna uma lista de produtos
    return PRODUTOS_DB # Retorna a lista de produtos como lista de objetos


def porId(produto_id): # Função que retorna um produto específico
    for produto in PRODUTOS_DB: # Percorre a lista de produtos
        if produto['id'] == produto_id: # Verifica se o ID do produto corresponde ao ID fornecido
            return produto # Retorna o produto como objeto
    return None # Retorna None se o produto não for encontrado


def adicionarProduto(produto): # Função para adicionar um novo produto
    global PRODUTOS_DB
    # 1. Gera um novo ID baseado na lista global PRODUTOS_DB
    novoID = PRODUTOS_DB[-1]['id'] + 1 
    # 2. Adiciona o ID ao novo dicionário
    produto['id'] = novoID 
    # 3. Adiciona o novo produto à lista GLOBAL
    PRODUTOS_DB.append(produto) # Adiciona o novo produto à lista global
    return PRODUTOS_DB[-1] # Retorna o produto adicionado

def salvarAlteração(produtoParaAtualizar): # Remova as chaves
    global PRODUTOS_DB  
    # 1. Percorre a lista para achar o índice
    for indice, produto in enumerate(PRODUTOS_DB):
        if produto['id'] == produtoParaAtualizar['id']: # Verifica se o ID do produto corresponde ao ID fornecido
            PRODUTOS_DB[indice] = produtoParaAtualizar # Substitui o item antigo pelo novo no índice encontrado
            return produtoParaAtualizar, 200 # retorna o objeto atualizado
    return None # Retorna None se o produto não for encontrado


def removerProduto(produto_id): # Função para deletar um produto
    global PRODUTOS_DB # 'Variável global para acessar a lista de produtos
    for indice, produto in enumerate(PRODUTOS_DB): # Percorre a lista de produtos
        if produto['id'] == produto_id: #' Verifica se o ID do produto corresponde ao ID fornecido
            PRODUTOS_DB.pop(indice) # Remove o produto da lista
            return True 
    return False