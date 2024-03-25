import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://www.kebab-frites.com/meilleur-kebab/paris-d54.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Sélectionner tous les éléments d'article contenant les informations des restaurants
articles = soup.select('article')

# Initialiser des listes pour stocker les noms, adresses, arrondissements, notes et nombres d'avis
noms = []
rues = []
arrondissements = []
notes = []
nombres_avis = []

# Parcourir chaque article pour récupérer les informations
for article in articles[:20]:  # Sélectionner les 20 premiers restaurants
    # Récupérer le nom du restaurant et nettoyer en enlevant le numéro d'apparition
    nom_elem = article.select_one('h3')
    nom = re.sub(r'#\d+ - ', '', nom_elem.text.strip()) if nom_elem else "Nom indisponible"
    
    # Récupérer l'adresse du restaurant et nettoyer
    adresse_elem = article.select_one('p')
    if adresse_elem:
        # Extraire l'adresse (rue) et le numéro de l'arrondissement (le code postal entier, 75xxx)
        adresse_text = adresse_elem.text.strip()
        match = re.search(r'^(.*?)(\d{5} Paris \d{2})$', adresse_text)
        if match:
            rue = match.group(1).strip()
            arrondissement = match.group(2)
        else:
            rue = "Adresse indisponible"
            arrondissement = "Arrondissement indisponible"
    else:
        rue = "Adresse indisponible"
        arrondissement = "Arrondissement indisponible"
    
    # Récupérer la note du restaurant (représentée par le nombre d'étoiles)
    note_class = article.select_one('.stars').get('class')[-1]  # Dernière classe dans 'stars'
    note = int(note_class[1]) if note_class.startswith('s') else 0  # Extraire le nombre d'étoiles
    
    # Récupérer le nombre d'avis du restaurant
    avis_elem = article.select_one('.avis')
    avis_text = avis_elem.text.strip() if avis_elem else "0 avis"
    avis = int(avis_text.split()[0])
    
    # Ajouter les informations aux listes respectives
    noms.append(nom)
    rues.append(rue)
    arrondissements.append(arrondissement)
    notes.append(note)
    nombres_avis.append(avis)

# Créer un DataFrame avec les informations recueillies
data = {
    'Nom': noms,
    'Rue': rues,
    'Arrondissement': arrondissements,
    'Note': notes,
    'Nombre d\'avis': nombres_avis
}

df = pd.DataFrame(data)

# Afficher le DataFrame
print(df)
