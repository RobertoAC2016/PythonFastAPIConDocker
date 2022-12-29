# Aqui descarga de la imagen de python q se usara para ejecutar la app
FROM python:3.9-slim-buster

# Copiar el directorio de la app local en el directorio remoto
COPY . usr/src/app

# Hay q indicar cual es el directorio de trabajo remoto
WORKDIR /usr/src/app

# Ejecutar algunos comando previos donde sean requieridos antes de ejecutar la app
RUN pip install -r requirements.txt

# ahora indicamos como ejecutar la app
ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
