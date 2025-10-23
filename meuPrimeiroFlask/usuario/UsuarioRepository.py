from flask import Flask, Blueprint, jsonify, request


USUARIOS_DB = [{"id": 1,"nome": "João Silva","email": "joaosilva@gmail.com"},
                {"id": 2,"nome": "Maria Oliveira","email": "maria@gmail.com"}
        ]

def todosUsuarios(): # Função que retorna todos os usuários
    return USUARIOS_DB

def usuarioPorId(usuario_id): # Função que retorna um usuário por ID
    for usuario in USUARIOS_DB: # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            return usuario # Retorna o usuário encontrado
    return None # Retorna None se o usuário não for encontrado

def adicionarUsuario(novoUsuario): # <<< Deve receber um argumento!
    global USUARIOS_DB # 'Variável global para acessar a lista de usuários
    novoID = USUARIOS_DB[-1]['id'] + 1 # Gera um novo ID baseado na lista global USUARIOS_DB 
    novoUsuario['id'] = novoID # Adiciona o ID ao novo dicionário 
    USUARIOS_DB.append(novoUsuario) # Adiciona o novo usuário à lista GLOBAL 

    return USUARIOS_DB[-1] # Retorna o usuário adicionado  
 
def salvandoAlteracao(usuarioParaAtualizar):   # Função para salvar alterações em um usuário 
    global USUARIOS_DB   #  'Variável global para acessar a lista de usuários
    id_para_atualizar = usuarioParaAtualizar['id']  # Obtém o ID do usuário a ser atualizado 
    for indice, usuario_existente in enumerate(USUARIOS_DB): # Percorre a lista para achar o índice 
        if usuario_existente['id'] == id_para_atualizar: # Verifica se o ID do usuário corresponde ao ID fornecido
            USUARIOS_DB[indice] = usuarioParaAtualizar # Substitui o item antigo pelo novo no índice encontrado
            return usuarioParaAtualizar # retorna o objeto atualizado   
            
    return None # Retorna None se o usuário não for encontrado

def removerUsuario(usuario_id): # Função para deletar um usuário
    global USUARIOS_DB # 'Variável global para acessar a lista de usuários
    for indice, usuario in enumerate(USUARIOS_DB): # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            USUARIOS_DB.pop(indice) # Remove o usuário da lista
            return True
    return False