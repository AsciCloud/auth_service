# Usar uma imagem leve do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de requisitos e instalá-los
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o contêiner vai utilizar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "main.py"]
