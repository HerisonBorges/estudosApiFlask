from flask import Flask, Blueprint, jsonify, request
from usuario.UsuarioService import *

usuarioAPI = Blueprint('UsuarioController', __name__, url_prefix='/usuarios')

@usuarioAPI.route('/', methods=['GET']) # Rota que responde apenas GET
def listarUsuarios(): # Função que retorna uma lista de usuários
    return listarTodosUsuarios() # Chama a função do serviço para listar todos os usuários

@usuarioAPI.route('/<int:usuario_id>', methods=['GET']) # Rota que responde apenas GET com parametro
def obterUsuario(usuario_id): # Função que retorna um usuário específico
    return obterUsuarioPorId(usuario_id) # Chama a função do serviço para obter o usuário por ID

@usuarioAPI.route('/', methods=['POST'])
def criandoUsuario(): # A função de rota do Flask
    dados = request.get_json()
    usuario = servico_criar_usuario(dados) # <<< CHAMA O SERVICE
    return jsonify(usuario), 201


@usuarioAPI.route('/<int:usuario_id>', methods=['PUT'])
def atualizarUsuario(usuario_id):
    dados = request.get_json() 
    usuarioAtualizado = servico_atualizar_usuario(usuario_id, dados)
    if usuarioAtualizado:
        return jsonify(usuarioAtualizado), 200
    else:
        return jsonify({"mensagem": "Usuário não encontrado para atualização"}), 404
    
    
@usuarioAPI.route('/<int:usuario_id>', methods=['DELETE'])
def deletarUsuarioRota(usuario_id):
    return deletarUsuario(usuario_id)