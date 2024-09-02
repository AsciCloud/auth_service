from .database import db  # Importa a instância do banco de dados
from flask_bcrypt import generate_password_hash, check_password_hash  # Para criptografar e verificar senhas
import logging  # Módulo de logging para registrar eventos

# Logger para registrar eventos relacionados a operações do modelo
logger = logging.getLogger(__name__)

# Modelo de dados do usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária, identificador único do usuário
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nome de usuário único
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email único do usuário
    password_hash = db.Column(db.String(128), nullable=False)  # Hash da senha, nunca armazenamos a senha em si

    def set_password(self, password):
        try:
            # Cria um hash seguro da senha e o armazena
            self.password_hash = generate_password_hash(password).decode('utf8')
            logger.info("Senha criptografada para o usuário: %s", self.username)
        except Exception as e:
            logger.error("Erro ao criptografar a senha para o usuário %s: %s", self.username, e)
            raise

    def check_password(self, password):
        try:
            # Verifica se a senha fornecida corresponde ao hash armazenado
            result = check_password_hash(self.password_hash, password)
            logger.info("Verificação de senha realizada para o usuário: %s", self.username)
            return result
        except Exception as e:
            logger.error("Erro ao verificar a senha para o usuário %s: %s", self.username, e)
            return False

    def __repr__(self):
        # Representação do modelo, útil para debug e logs
        return f'<User {self.username}>'
