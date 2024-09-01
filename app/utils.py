from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import logging

logger = logging.getLogger(__name__)

def generate_token(user):
    try:
        token = create_access_token(identity={'id': user.id, 'username': user.username})
        logger.info("Token gerado para o usuário: %s", user.username)
        return token
    except Exception as e:
        logger.error("Erro ao gerar o token para o usuário %s: %s", user.username, e)
        raise
