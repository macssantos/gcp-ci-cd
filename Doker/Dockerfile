# Use a imagem base Python
FROM python:3.8

# Copie todos os arquivos Python do diretório local para o diretório de trabalho no contêiner
COPY *.py /gcp-ci-cd/

# Defina o diretório de trabalho como /app
WORKDIR /gcp-ci-cd

# Execute todos os scripts Python no diretório de trabalho
CMD ["bash", "-c", "for script in *.py; do python $script; done"]