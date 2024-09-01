from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()

def setup_database(app):
    logger = logging.getLogger(__name__)
    try:
        db.init_app(app)
        Migrate(app, db)
        logger.info("Banco de dados inicializado com sucesso.")
    except Exception as e:
        logger.error("Erro ao inicializar o banco de dados: %s", e)
        raise
