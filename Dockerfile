# 1. Usamos la versión Alpine de Python
FROM python:3.11-alpine

# 2. Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos todo el contenido de nuestro proyecto actual al contenedor ignorando el .dockerignore
COPY . .

# 4. Ejecutamos el archivo principal directamente desde la carpeta src
CMD ["python", "src/main.py"]
