import logging  # Módulo de logging do Python
import logging.config  # Módulo para configuração avançada de logging
import os  # Módulo para interagir com o sistema operacional
from logging.handlers import RotatingFileHandler  # Manipulador de arquivos de log com rotação

# Diretório onde os logs serão armazenados
log_directory = 'logs'
# Verifica se o diretório de logs existe; se não, cria-o
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuração de logging com rotação de logs
LOGGING_CONFIG = {
    'version': 1,  # Versão do formato de configuração
    'disable_existing_loggers': False,  # Não desativa os loggers existentes
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'  # Formato padrão dos logs
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',  # Nível de log para o console
            'class': 'logging.StreamHandler',  # Tipo de handler (saída para o console)
            'formatter': 'standard',  # Formatação a ser usada
        },
        'file': {
            'level': 'INFO',  # Nível de log para o arquivo principal
            'class': 'logging.handlers.RotatingFileHandler',  # Handler de arquivo com rotação
            'formatter': 'standard',  # Formatação a ser usada
            'filename': os.path.join(log_directory, 'auth_service.log'),  # Nome do arquivo de log
            'maxBytes': 10485760,  # Tamanho máximo do arquivo de log antes de rotacionar (10MB)
            'backupCount': 3,  # Número de backups a manter
            'mode': 'a',  # Modo de abertura do arquivo (append)
        },
        'error_file': {
            'level': 'ERROR',  # Nível de log para o arquivo de erros
            'class': 'logging.handlers.RotatingFileHandler',  # Handler de arquivo com rotação
            'formatter': 'standard',  # Formatação a ser usada
            'filename': os.path.join(log_directory, 'error.log'),  # Nome do arquivo de log de erros
            'maxBytes': 10485760,  # Tamanho máximo do arquivo de log antes de rotacionar (10MB)
            'backupCount': 3,  # Número de backups a manter
            'mode': 'a',  # Modo de abertura do arquivo (append)
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file', 'error_file'],  # Handlers a serem usados por este logger
            'level': 'DEBUG',  # Nível mínimo de log para registrar
            'propagate': True  # Propaga os logs para loggers ancestrais
        },
    }
}

def setup_logging():
    # Aplica a configuração de logging
    logging.config.dictConfig(LOGGING_CONFIG)
