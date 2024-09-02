from flask_jwt_extended import create_access_token  # Função para criar tokens JWT
import logging  # Módulo de logging para registrar eventos

# Logger para registrar eventos relacionados a utilitários
logger = logging.getLogger(__name__)

def generate_token(user):
    try:
        # Cria um token JWT que contém a identidade do usuário
        token = create_access_token(identity={'id': user.id, 'username': user.username})
        logger.info("Token gerado para o usuário: %s", user.username)
        return token
    except Exception as e:
        logger.error("Erro ao gerar o token para o usuário %s: %s", user.username, e)
        raise  # Repassa a exceção para cima
