import os  # Módulo para acessar variáveis de ambiente
from dotenv import load_dotenv  # Carrega variáveis de ambiente a partir de um arquivo .env
import logging  # Módulo de logging para registrar eventos da aplicação

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Define a URI do banco de dados a partir da variável de ambiente
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    # Desativa a sinalização de modificações do SQLAlchemy para reduzir o uso de memória
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Chave secreta para proteger sessões e cookies
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Chave secreta para assinar e verificar tokens JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Nível de logging padrão da aplicação
    LOG_LEVEL = logging.INFO

    @staticmethod
    def init_app(app):
        logger = logging.getLogger(__name__)
        logger.info("Configurações carregadas com sucesso.")
