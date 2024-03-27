FROM python:3.8-slim

# Installation des dépendances Python
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install selenium pandas sqlalchemy pymysql

# Téléchargement et installation de Google Chrome (version arm64)
RUN wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb && \
    dpkg -i /tmp/google-chrome.deb && \
    apt-get install -y -f && \
    rm /tmp/google-chrome.deb

# Téléchargement et installation du chromedriver (version arm64)
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/98.0.4758.102/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Copie du script Python dans le conteneur
COPY Scrap-projet-kc.py /app/

# Définition du répertoire de travail
WORKDIR /app
