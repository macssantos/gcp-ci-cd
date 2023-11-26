# Imagem base para o Python
FROM python:3.9

# Criando diretório de trabalho
WORKDIR /GCP

# Copiando os arquivos de código para o diretório de trabalho
COPY biblioteca.py .
#COPY script2.py .

# Executando o primeiro arquivo de código
CMD ["python", "script1.py"]# Imagem base para o Python
FROM python:3.9

# Criando diretório de trabalho
WORKDIR /GCP

# Copiando os arquivos de código para o diretório de trabalho
COPY biblioteca.py .
COPY script2.py .

# Executando o primeiro arquivo de código
CMD ["python", "script1.py"]