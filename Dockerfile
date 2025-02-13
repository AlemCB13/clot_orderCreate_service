# Usar una imagen base de Python
FROM python:3.12

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá Flask
EXPOSE 5000

# Definir el comando de inicio
CMD ["python", "src/app.py"]
