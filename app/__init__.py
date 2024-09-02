from flask import Flask  # Importa a classe Flask, que é a base da aplicação
from flask_jwt_extended import JWTManager  # Gerenciador de JWT para autenticação
from .configs import Config  # Configurações da aplicação, incluindo chaves secretas e URI do banco de dados
from .database import setup_database  # Função que configura e inicializa o banco de dados
from .routes import auth  # Importa o blueprint que define as rotas de autenticação
from .logging_config import setup_logging  # Configuração de logging para monitoramento e depuração
import logging


def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__)
    # Carrega as configurações da aplicação a partir do objeto Config
    app.config.from_object(Config)

    # Configura o sistema de logging
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Configuração de logging concluída")

    # Configura e inicializa o banco de dados
    setup_database(app)
    logger.info("Configuração do banco de dados concluída")

    # Configura o gerenciador de JWT para autenticação
    JWTManager(app)
    logger.info("Configuração do JWT concluída")

    # Registra o blueprint de autenticação com a aplicação
    app.register_blueprint(auth, url_prefix='/auth')
    logger.info("Blueprint de autenticação registrado")

    return app  # Retorna a instância da aplicação configurada

