from flask import Flask, jsonify, request
from usuario.UsuarioRepository import *

def listarTodosUsuarios(): # Função que retorna uma lista de usuários
    return jsonify(USUARIOS_DB) # Retorna o objeto retornado pela função todosUsuarios em formato JSON

def obterUsuarioPorId(usuario_id): # Função that returns a specific user

    usuario = usuarioPorId(usuario_id) # Chama a função usuarioPorId do UsuarioRepository
    if usuario: 
        return jsonify(usuario) 
    else:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404
    

def servico_criar_usuario(dados_novos): # <<< NOVO NOME + RECEBE DADOS
    usuario = adicionarUsuario(dados_novos) 
    return usuario # Retorna o objeto adicionado (o Repositório cuida do ID)


def servico_atualizar_usuario(usuario_id, dados_atualizados): 
    dados_atualizados['id'] = usuario_id
    usuarioAtualizado = salvandoAlteracao(dados_atualizados) 
    return usuarioAtualizado # Retorna o objeto (ou None)
    
def deletarUsuario(usuario_id):
    sucesso = removerUsuario(usuario_id) 
    if sucesso:
        return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200
    else:
        return jsonify({"mensagem": "Usuário não encontrado para deleção"}), 404
    
    