FROM python:3.9-slim

# Installation des dépendances Python
RUN pip install selenium pandas sqlalchemy pymysql

RUN apt-get update --fix-missing && apt-get install -y wget gnupg2 unzip ca-certificates procps xdg-utils --fix-missing \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Téléchargement et ajout de la clé de signature de Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Ajout du dépôt de Google Chrome Stable pour architecture amd64
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Mise à jour des paquets et installation de Google Chrome Stable
RUN apt-get update && apt-get install -y wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Téléchargement et installation de Google Chrome Stable
RUN wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/google-chrome.deb \
    && apt-get install -f -y \
    && rm -rf /tmp/google-chrome.deb

# Installation du chromedriver
RUN wget -q --continue -P /chromedriver "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/linux64/chromedriver-linux64.zip" \
    && unzip /chromedriver/chromedriver* -d /usr/local/bin/ \
    && rm -rf /chromedriver

# Copie du script Python dans le conteneur
COPY Scrap-projet-kc.py /app/

# Définition du répertoire de travail
WORKDIR /app
