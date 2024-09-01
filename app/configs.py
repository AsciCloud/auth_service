import os
from dotenv import load_dotenv
import logging

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Configuração do logging
    LOG_LEVEL = logging.INFO

    @staticmethod
    def init_app(app):
        logger = logging.getLogger(__name__)
        logger.info("Configurações carregadas com sucesso.")
