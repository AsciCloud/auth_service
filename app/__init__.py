from flask import Flask
from flask_jwt_extended import JWTManager
from .configs import Config
from .database import setup_database
from .routes import auth
from .logging_config import setup_logging
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Configuração de logging concluída")

    setup_database(app)
    logger.info("Configuração do banco de dados concluída")

    JWTManager(app)
    logger.info("Configuração do JWT concluída")

    app.register_blueprint(auth, url_prefix='/auth')
    logger.info("Blueprint de autenticação registrado")

    return app
