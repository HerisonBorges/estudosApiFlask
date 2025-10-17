from flask import Flask, jsonify, request # Importa funções do Flask
from flask_sqlalchemy import SQLAlchemy # Importa SQLAlchemy para ORM
from sqlalchemy.dialects.postgresql import UUID # para gerar iDS aleatórios
import uuid # Biblioteca para gerar UUIDs

app = Flask(__name__) # Cria a aplicação Flask e armazena na variável app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:159357.Ab@localhost:5432/inventario_db' # Configura a URI do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desativa o rastreamento de modificações do SQLAlchemy
db = SQLAlchemy(app) # Inicializa o SQLAlchemy com a aplicação Flask

#criando a classe Produto que representa a tabela produtos no banco de dados
class Produto(db.Model):
   # A sua linha corrigida no app.py deve ser:
    __tablename__ = 'produtos' # Nome da tabela no banco de dados
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable = False) # Coluna ID do tipo UUID
    nome = db.Column(db.String(100), nullable=False) # Coluna nome do produto
    descricao = db.Column(db.String(255)) # Coluna descrição do produto
    preco = db.Column(db.Float, nullable=False) # Coluna preço do produto
    quantidade = db.Column(db.Integer, nullable=False) # Coluna quantidade do produto

    def to_dict(self): # Método para converter o objeto em dicionário
        return {
            'id': str(self.id),
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'quantidade': self.quantidade
        }
    
def criandoTabelas(): # Função para criar as tabelas no banco de dados
    with app.app_context(): # Garante que o contexto da aplicação está ativo
        db.create_all() # Cria todas as tabelas definidas nos modelos
        print("Tabelas criadas com sucesso!") 

if __name__ == '__main__': # Verifica se o script está sendo executado diretamente
        criandoTabelas() # Chama a função para criar as tabelas
        print("Aplicação iniciada!")


#--- 1 -- Rota para criar um novo produto
@app.route('/produtos', methods=['POST']) # INFORMA AO FLASK QUE SE O HTTP FOR POST NA ROTA /PRODUTOS, ELE DEVE CHAMAR A FUNÇÃO ABAIXO
def criarProduto():
    dados = request.get_json() # Obtém os dados JSON da requisição

    if ('nome' not in dados or 
        'preco' not in dados or 
        'quantidade' not in dados): # Verifica se os campos obrigatórios estão presentes

       
        return jsonify({'erro': 'Campos obrigatórios faltando'}), 400 
    novoProduto = Produto( # Cria Objeto: Cria uma instância (objeto) da sua classe de modelo Produto. Este objeto existe apenas na memória do Python por enquanto.
        nome=dados['nome'], # Mapeamento: Pega o valor da chave 'nome' do dicionário dados (o JSON que o cliente enviou) e atribui ao atributo nome do novo objeto.
        descricao=dados.get('descricao', ''), # Mapeamento: Pega o valor do 'preco' do dicionário e atribui ao objeto.
        preco=dados['preco'], # Preço do produto
        quantidade=dados['quantidade'] # Mapeamento: Pega o valor da 'quantidade' do dicionário e atribui ao objeto.
    ) 
