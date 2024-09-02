from app import create_app  # Importa a função que cria e configura a aplicação
import logging  # Módulo de logging para registrar eventos

# Cria a instância da aplicação Flask
app = create_app()
# Cria um logger para registrar eventos ao iniciar a aplicação
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Iniciando o serviço Flask na porta 5000...")
    # Inicia o servidor Flask na porta 5000
    app.run(host='0.0.0.0', port=5000)
