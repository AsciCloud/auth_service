import logging
from flask import Blueprint, request, jsonify
from .database import db
from .models import User
from .utils import generate_token
from flask_jwt_extended import jwt_required, get_jwt_identity

# Configurar o logger
logger = logging.getLogger(__name__)

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first() is not None:
        logger.warning("Tentativa de registro com email já existente: %s", data['email'])
        return jsonify({"error": "User already exists"}), 400

    try:
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        logger.info("Novo usuário registrado com sucesso: %s", user.username)
        token = generate_token(user)
        return jsonify({"token": token}), 201
    except Exception as e:
        logger.error("Erro ao registrar o usuário: %s", e)
        return jsonify({"error": "Registration failed"}), 500

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user is None or not user.check_password(data['password']):
        logger.warning("Falha na tentativa de login para o email: %s", data['email'])
        return jsonify({"error": "Invalid credentials"}), 401

    try:
        logger.info("Usuário logado com sucesso: %s", user.username)
        token = generate_token(user)
        return jsonify({"token": token}), 200
    except Exception as e:
        logger.error("Erro ao gerar token de login: %s", e)
        return jsonify({"error": "Login failed"}), 500

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    logger.info("Acesso à rota protegida pelo usuário: %s", current_user['username'])
    return jsonify(logged_in_as=current_user), 200
