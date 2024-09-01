import logging
import logging.config
import os
from logging.handlers import RotatingFileHandler

# Diretório onde os logs serão armazenados
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuração de logging com rotação de logs
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(log_directory, 'auth_service.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 3,       # Mantém até 3 arquivos de log antigos
            'mode': 'a',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(log_directory, 'error.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 3,       # Mantém até 3 arquivos de log antigos
            'mode': 'a',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file', 'error_file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
