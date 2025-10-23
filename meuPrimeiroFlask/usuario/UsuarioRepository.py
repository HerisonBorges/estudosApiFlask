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
    global USUARIOS_DB
    novoID = USUARIOS_DB[-1]['id'] + 1
    novoUsuario['id'] = novoID
    USUARIOS_DB.append(novoUsuario)

    return USUARIOS_DB[-1]

def salvandoAlteracao(usuarioParaAtualizar):
    global USUARIOS_DB   
    id_para_atualizar = usuarioParaAtualizar['id'] 
    for indice, usuario_existente in enumerate(USUARIOS_DB):
        if usuario_existente['id'] == id_para_atualizar:
            USUARIOS_DB[indice] = usuarioParaAtualizar
            return usuarioParaAtualizar
            
    return None

def removerUsuario(usuario_id):
    global USUARIOS_DB
    for indice, usuario in enumerate(USUARIOS_DB): # Percorre a lista de usuários
        if usuario['id'] == usuario_id: # Verifica se o ID do usuário corresponde ao ID fornecido
            USUARIOS_DB.pop(indice) # Remove o usuário da lista
            return True
    return False