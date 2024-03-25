import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import unquote
#from tqdm.notebook import tqdm # pour afficher des barres de chargement
from tqdm import tqdm
import numpy as np # pour calculer des médianes

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')

soup

print(soup.prettify())
soup.find('p')
soup.find_all('p')
soup.find('p').get_text()
soup.find('p').get_text().strip()
soup.find_all('p')[0].get_text()

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content)
soup.find_all('p')
print(soup.prettify())
soup.find_all('p', {"class":"outer-text"})[0].get_text().strip()
soup.find_all('p', {"class":"outer-text", "id":"second"})[0].get_text().strip()

# un id étant unique en HTML, on peut y accéder directement sans mentionner le tag
soup.find(id="first")

wikipedia_DS_url = "https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es"
wiki_raw = requests.get(wikipedia_DS_url)
soup = BeautifulSoup(wiki_raw.content)
str(soup)[:1000]

main_soup = soup.find("main")  # pas besoin de find_all car il n'y a qu'un main
str(main_soup)[:1000]

links = main_soup.find_all("a")

links = main_soup.find_all("a", href=True, title=True)
links[:10]

#utilisons la méthode startswith
'Bonjour'.startswith("a")

#meme méthode en utilisant une fonctions lambda
links = main_soup.find_all("a", href=lambda link: link and link.startswith("/wiki/"), title=True)

print(links[:5])

liens = []
for l in links:
    liens.append(l['href'])

liens[:5]

decoded_urls = [unquote(url) for url in liens]

for i,url in enumerate(decoded_urls):
    print(url)
    if i==4: break

# Dans un tag, on peut accéder aux attributs avec le slicing habituel
links[0]['href']

list_of_article_links = [ link["href"] for link in links ]
list_of_article_links = [unquote(url) for url in list_of_article_links]; list_of_article_links[:10]

# on va récupérer le contenu du premier lien
#example_url = list_of_article_links[0]
#requests.get(example_url).content

prefix = "https://fr.wikipedia.org"
prefix + list_of_article_links[0] # concaténation rapide

first_article_content = requests.get(prefix + list_of_article_links[0]).content
first_article_content[:1000]

# Essayons de rendre nos noms de variables le plus clair possible
list_article_links_complete = [prefix + extension for extension in list_of_article_links]
list_article_links_complete[:10]

print(pd.DataFrame(list_article_links_complete, columns=['liens']))

### Notre analyse

articles_number_notes = []

for article_link in tqdm(list_article_links_complete[:50]): # intégrer tdqm permet d'afficher une barre de progression de la boucle

    # constitution de notre soup de façon classique
    first_article_content = requests.get(article_link).content
    first_article_soup = BeautifulSoup(first_article_content, 'html.parser')

    # Certains articles n'auront ni notes ni références, ils donneront une erreur
    # Ces erreurs seront gérés par la commande except
    try:

        # On parcourt l'arbre pour trouver les éléments dans la liste référence
        notes_et_references = (first_article_soup
                               .find('main')
                               .find("ol", {"class": "references"})
                               .find_all("li")
                              )
        # on stocke dans une liste le nombre de références
        number_of_notes = len(notes_et_references)
        articles_number_notes.append(number_of_notes)

    except AttributeError:
        print("No note or reference in article", article_link)
        articles_number_notes.append(0)   # Il n'y a pas de notes donc on ajoute 0 à la liste.

print("\nMedian number of notes per article is", np.median(articles_number_notes))
print("Mean number of notes per article is", np.mean(articles_number_notes))
print("Stdev of number of notes per article is", np.std(articles_number_notes))