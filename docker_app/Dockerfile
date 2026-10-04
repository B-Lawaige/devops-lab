FROM python:3.10-slim

WORKDIR /app

# On copie d'abord le requirements.txt pour profiter du cache Docker
COPY requirements.txt .

# Installation des dépendances à partir du fichier
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 80

CMD ["python", "app.py"]