# Projet de Web Scraping avec Docker
Ce projet vise à créer un environnement Docker pour exécuter un script de web scraping en Python utilisant Selenium. Le script est conçu pour extraire des données à partir de pages web spécifiques et les stocker dans une base de données MySQL.

## Prérequis
Assurez-vous d'avoir Docker installé sur votre système. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer à partir du site officiel de Docker : https://www.docker.com/get-started

## Configuration du conteneur Docker
### Dockerfile
Le fichier Dockerfile contient les instructions pour construire l'image Docker. Il installe toutes les dépendances nécessaires, telles que Python, Selenium, Pandas, SQLAlchemy, PyMySQL, Google Chrome et Chromedriver.

### docker-compose.yml
Le fichier docker-compose.yml définit les services nécessaires pour exécuter l'application. Il crée un service pour la base de données MySQL et un autre pour exécuter le script de web scraping.

```yaml
version: '3'

services:
  database:
    image: mysql
    ports:
      - "3307:3307"
    volumes:
      - ./database:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
    restart: always

  web_scraping:
    build: .
    depends_on:
      - database
```

### Exécution du script
#### Pour exécuter le script de web scraping, suivez les étapes suivantes :

Clonez ce référentiel sur votre machine locale.
Assurez-vous d'être dans le répertoire contenant les fichiers Docker (Dockerfile, docker-compose.yml) et le script Python (Scrap-projet-kc.py).

**Exécutez la commande suivante pour construire l'image Docker et démarrer les conteneurs :**
`docker-compose up --build`
Une fois les conteneurs démarrés, le script de web scraping sera automatiquement exécuté.

### Personnalisation du script
Si vous souhaitez personnaliser le script de web scraping pour extraire des données à partir de différentes sources ou pour stocker les données différemment, vous pouvez modifier le fichier Scrap-projet-kc.py. Assurez-vous de mettre à jour le script en conséquence et de reconstruire l'image Docker si nécessaire.