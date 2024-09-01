from app import create_app
import logging

app = create_app()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Iniciando o serviço Flask na porta 5000...")
    app.run(host='0.0.0.0', port=5000)
