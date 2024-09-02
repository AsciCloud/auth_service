import logging  # Módulo de logging para registrar eventos
from flask import Blueprint, request, jsonify  # Blueprint para rotas, request para dados das requisições, jsonify para formatar respostas JSON
from .database import db  # Importa a instância do banco de dados
from .models import User  # Importa o modelo de usuário
from .utils import generate_token  # Função utilitária para gerar tokens JWT
from flask_jwt_extended import jwt_required, get_jwt_identity  # Decorador para proteger rotas e função para obter identidade do token JWT

# Logger para registrar eventos relacionados a operações de rotas
logger = logging.getLogger(__name__)

# Cria um blueprint para organizar as rotas de autenticação
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    # Obtém os dados da requisição JSON
    data = request.get_json()
    # Verifica se o usuário já existe com o email fornecido
    if User.query.filter_by(email=data['email']).first() is not None:
        logger.warning("Tentativa de registro com email já existente: %s", data['email'])
        return jsonify({"error": "User already exists"}), 400

    try:
        # Cria um novo usuário
        user = User(username=data['username'], email=data['email'])
        # Define a senha (criptografa)
        user.set_password(data['password'])
        # Adiciona e confirma a transação no banco de dados
        db.session.add(user)
        db.session.commit()

        logger.info("Novo usuário registrado com sucesso: %s", user.username)
        # Gera um token JWT para o usuário registrado
        token = generate_token(user)
        return jsonify({"token": token}), 201
    except Exception as e:
        logger.error("Erro ao registrar o usuário: %s", e)
        return jsonify({"error": "Registration failed"}), 500

@auth.route('/login', methods=['POST'])
def login():
    # Obtém os dados da requisição JSON
    data = request.get_json()
    # Busca o usuário pelo email
    user = User.query.filter_by(email=data['email']).first()
    # Verifica se o usuário existe e se a senha está correta
    if user is None or not user.check_password(data['password']):
        logger.warning("Falha na tentativa de login para o email: %s", data['email'])
        return jsonify({"error": "Invalid credentials"}), 401

    try:
        logger.info("Usuário logado com sucesso: %s", user.username)
        # Gera um token JWT para o usuário autenticado
        token = generate_token(user)
        return jsonify({"token": token}), 200
    except Exception as e:
        logger.error("Erro ao gerar token de login: %s", e)
        return jsonify({"error": "Login failed"}), 500

@auth.route('/protected', methods=['GET'])
@jwt_required()  # Exige que o usuário esteja autenticado via JWT para acessar essa rota
def protected():
    # Obtém a identidade do usuário a partir do token JWT
    current_user = get_jwt_identity()
    logger.info("Acesso à rota protegida pelo usuário: %s", current_user['username'])
    return jsonify(logged_in_as=current_user), 200
