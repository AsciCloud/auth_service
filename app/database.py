from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy para ORM e gerenciamento de banco de dados
from flask_migrate import Migrate  # Flask-Migrate para gerenciar migrações de banco de dados
import logging  # Módulo de logging para registrar eventos

# Instância do SQLAlchemy, usada para interagir com o banco de dados
db = SQLAlchemy()

def setup_database(app):
    logger = logging.getLogger(__name__)
    try:
        # Inicializa a aplicação com o banco de dados
        db.init_app(app)
        # Configura o Migrate para lidar com migrações de banco de dados
        Migrate(app, db)
        logger.info("Banco de dados inicializado com sucesso.")
    except Exception as e:
        logger.error("Erro ao inicializar o banco de dados: %s", e)
        raise  # Repassa a exceção para cima
