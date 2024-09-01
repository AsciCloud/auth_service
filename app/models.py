from .database import db
from flask_bcrypt import generate_password_hash, check_password_hash
import logging

logger = logging.getLogger(__name__)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        try:
            self.password_hash = generate_password_hash(password).decode('utf8')
            logger.info("Senha criptografada para o usuário: %s", self.username)
        except Exception as e:
            logger.error("Erro ao criptografar a senha para o usuário %s: %s", self.username, e)
            raise

    def check_password(self, password):
        try:
            result = check_password_hash(self.password_hash, password)
            logger.info("Verificação de senha realizada para o usuário: %s", self.username)
            return result
        except Exception as e:
            logger.error("Erro ao verificar a senha para o usuário %s: %s", self.username, e)
            return False

    def __repr__(self):
        return f'<User {self.username}>'
