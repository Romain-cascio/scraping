FROM python:3.8-slim

# Installation des dépendances Python
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install selenium pandas sqlalchemy pymysql

# Téléchargement et installation de Chromium pour Linux
RUN apt-get update && apt-get install -y chromium

# Téléchargement et installation du chromedriver pour Linux
RUN wget -q -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/98.0.4758.102/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver_linux64.zip

# Copie du script Python dans le conteneur
COPY Scrap-projet-kc.py /app/

# Définition du répertoire de travail
WORKDIR /app
