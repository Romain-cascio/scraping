import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def nbOffers(driver):
    try:
        # Trouver l'élément contenant le nombre total d'offres d'emploi
        job_count_element = driver.find_element(By.CSS_SELECTOR, '[data-testid="jobs-search-results-count"]')

        # Extraire le texte de l'élément
        job_count_text = job_count_element.text

        # Convertir le texte en entier
        job_count = int(job_count_text)

        return job_count

    except Exception as e:
        print("An error occurred in NB_OFFER:", str(e))
        return 0 

def Click(driver, xpath):
    try:
        # Trouver l'élément à cliquer en utilisant XPath
        element = driver.find_element(By.XPATH, xpath)

        # Cliquez sur l'élément
        element.click()

    except Exception as e:
        print("An error occurred in CLICK:", str(e))
        return 0  

def GetText(driver, xpath):
    try:
        # Trouver l'élément contenant le texte de l'offre d'emploi en utilisant XPath
        job_text_element = driver.find_element(By.XPATH, xpath)

        # Récupérer le texte de l'offre d'emploi
        job_text = job_text_element.text

        # Enregistrer le texte dans un fichier texte
        with open('job_text.txt', 'a', encoding='utf-8') as file:
            file.write(job_text + '\n\n')  # Ajouter un saut de ligne après chaque offre

        print("Texte de l'offre d'emploi enregistré avec succès dans le fichier 'job_text.txt'")

    except Exception as e:
        print(f"Error HTML PARSING: {e}")

# Initialisez le navigateur WebDriver
driver = webdriver.Chrome()  # Ou tout autre navigateur de votre choix

# Chargez l'URL de la page
url = "https://www.welcometothejungle.com/fr/jobs?page=1&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI"
driver.get(url)
driver.implicitly_wait(10)
nb_offers = nbOffers(driver)
print("Nombre d'offres:", nb_offers)

xpath_popup = '//*[@id="axeptio_btn_acceptAll"]'
Click(driver, xpath_popup)
time.sleep(2)
# Utilisez une boucle pour cliquer sur chaque élément de la liste et récupérer le texte
i = 1
while True:
    # Utilisez la fonction Click pour cliquer sur l'élément spécifié par XPath
    xpath = f'//*[@id="pages_jobs"]/div[2]/div/ul/li[{i}]/div/div/a'
    driver.implicitly_wait(10)
    Click(driver, xpath)

    # Utilisez la fonction GetText pour récupérer le texte de l'offre d'emploi
    xpath_texte_offre_emploi = '//*[@id="the-position-section"]/div/div[2]/div[1]/div/div[1]/div/p[1]'
    GetText(driver, xpath_texte_offre_emploi)

    # Pause pour laisser le temps de visualiser le résultat
    time.sleep(3)

    # Retournez à la liste des offres d'emploi
    driver.back()

    # Vérifiez si nous avons atteint la fin de la liste d'offres
    if i == nb_offers:
        # Cliquez sur le lien vers la page suivante
        xpath_next_page = '//*[@id="pages_jobs"]/div[2]/div/div[2]/nav/ul/li[2]/a'
        Click(driver, xpath_next_page)
        # Réinitialisez l'indice pour parcourir les offres de la nouvelle page
        i = 1
    else:
        # Incrémentez l'indice pour passer à la prochaine offre sur la même page
        i += 1