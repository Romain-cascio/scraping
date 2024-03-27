import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
import pandas as pd

def insert_dataframe_to_mysql(df, table_name, database_url):
    engine = create_engine(database_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def scroll_page(driver):
    try:
        # Obtenir la position actuelle de la fenêtre du navigateur
        current_position = driver.execute_script("return window.pageYOffset;")
        
        # Ajouter 500 pixels à la position actuelle pour faire défiler la page vers le bas
        new_position = current_position + 700
        
        # Faire défiler la page vers le bas de 500 pixels
        driver.execute_script(f"window.scrollTo(0, {new_position});")

    except Exception as e:
        print("Une erreur s'est produite lors du défilement de la page:", str(e))

def Click_in_Shadow_DOM(driver):
    try:
        element = driver.execute_script("""return document.querySelector('.needsclick').shadowRoot.querySelector("button#axeptio_btn_acceptAll")""")
        element.click()


    except Exception as e:
        print("An error occurred:", str(e))
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
    
def GetText_esport(driver):
    try:
        # Trouver la balise div avec la classe "swiper-wrapper"
        div_element = driver.find_element(By.XPATH, '//div[@class="swiper-wrapper"]')

        # Trouver tous les éléments <h3> à l'intérieur de la balise div
        h3_elements = div_element.find_elements(By.TAG_NAME, 'h3')

        # Initialiser une liste pour stocker les textes des éléments <h3>
        h3_texts = []

        # Parcourir tous les éléments <h3> et récupérer leur texte
        for h3_element in h3_elements:
            # Récupérer le texte de l'élément <h3>
            h3_text = h3_element.text.strip()
            if h3_text:
                # Ajouter le texte à la liste des textes <h3>
                h3_texts.append(h3_text)

        # Retourner la liste de textes <h3>
        return h3_texts

    except Exception as e:
        print(f"Erreur lors de l'extraction du texte des éléments <h3> : {e}")
        return []  # En cas d'erreur, retourner une liste vide

def GetText_h2_prices(driver):
    try:
        # Trouver tous les éléments <h2> à l'intérieur de la div avec l'ID "shopify-section-template--21223087636821__main"
        h2_elements = driver.find_elements(By.XPATH, '//*[@class="product__title"]//h2')

        # Trouver tous les prix des produits à partir des balises <a> avec la classe "product__price"
        price_elements = driver.find_elements(By.XPATH, '//*[@class="product__price"]//span[@class="product__price-value"]')

        # Initialiser deux listes pour stocker les textes des éléments <h2> et les prix des produits
        h2_texts = []
        prices = []

        # Parcourir tous les éléments <h2> et récupérer leur texte
        for h2_element in h2_elements:
            # Récupérer le texte de l'élément <h2>
            h2_text = h2_element.text.strip()
            if h2_text:
                # Ajouter le texte à la liste des textes <h2>
                h2_texts.append(h2_text)

        # Parcourir tous les éléments de prix des produits et récupérer leur texte
        for price_element in price_elements:
            # Récupérer le texte du prix du produit
            price_text = price_element.text.strip()
            if price_text:
                # Ajouter le prix à la liste des prix des produits
                prices.append(price_text)

        # Retourner les listes de textes <h2> et les prix des produits
        return h2_texts, prices

    except Exception as e:
        print(f"Erreur lors de l'extraction du texte des éléments <h2> et des prix des produits : {e}")
        return [], []  # En cas d'erreur, retourner des listes vides
    
def GetText_partenaires(driver):
    try:
        # Trouver tous les éléments <h2> à l'intérieur de la classe "section__content"
        h2_elements = driver.find_elements(By.XPATH, '//*[@class="section__content"]//h2')

        # Initialiser une liste pour stocker les textes des éléments <h2>
        h2_texts = []

        # Parcourir tous les éléments <h2> et récupérer leur texte
        for h2_element in h2_elements:
            # Récupérer le texte de l'élément <h2>
            h2_text = h2_element.text.strip()
            if h2_text:
                # Ajouter le texte à la liste des textes <h2>
                h2_texts.append(h2_text)

        # Retourner la liste de textes <h2>
        return h2_texts

    except Exception as e:
        print(f"Erreur lors de l'extraction du texte des éléments <h2> : {e}")
        return []  # En cas d'erreur, retourner une liste vide
    
def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Ouvrir l'URL
    url = "https://www.karminecorp.fr/"
    driver.get(url)
    time.sleep(4)
    Click_in_Shadow_DOM(driver)
     
    driver.implicitly_wait(10)
    xpath_boutique = '//*[@id="shopify-section-sections--21223088128341__header"]/u-header/nav/ul/li[6]/a'
    xpath_essential = '//*[@id="shopify-section-template--21381985010005__2f02d09a-9073-4fe4-b384-34e7761cf6ef"]/div/div/div/div[2]/a[1]'
    xpath_prokit = '//*[@id="shopify-section-template--21381985010005__2f02d09a-9073-4fe4-b384-34e7761cf6ef"]/div/div/div/div[1]/a[2]'
    xpath_partenaires = '//*[@id="shopify-section-sections--21223088128341__header"]/u-header/nav/ul/li[5]/a'
    xpath_esport = '//*[@id="shopify-section-sections--21223088128341__header"]/u-header/nav/ul/li[3]/a'

    Click(driver, xpath_boutique)
    time.sleep(1)
    Click(driver, xpath_boutique)
    time.sleep(1)
    Click(driver, xpath_essential)
    time.sleep(1)
    h2_texts, span_texts = GetText_h2_prices(driver)
    time.sleep(1)
    driver.back()
    time.sleep(1)
    Click(driver, xpath_prokit)
    time.sleep(1)
    h2_texts_pro, span_texts_pro = GetText_h2_prices(driver)
    time.sleep(1)
    Click(driver, xpath_partenaires)
    time.sleep(1)
    h2_partenaires = GetText_partenaires(driver)
    time.sleep(1)
    Click(driver, xpath_esport)
    time.sleep(1)
    Click(driver, xpath_esport)
    time.sleep(1)
    esports = GetText_esport(driver)


    h2_texts.extend(h2_texts_pro)
    span_texts.extend(span_texts_pro)
    
    data_produits = {
    'Nom_produit': h2_texts,
    'Prix': span_texts
    }

    data_partenaires = {
        'Nom partenaires': h2_partenaires
    }

    data_esports = {
        'Nom des jeux': esports
    }

    df = pd.DataFrame(data_produits)
    df_partenaires = pd.DataFrame(data_partenaires)
    df_esports = pd.DataFrame(data_esports)

    database_url = 'mysql+pymysql://root:root@database:3307/scrap'
    insert_dataframe_to_mysql(df, 'produits', database_url)
    insert_dataframe_to_mysql(df_partenaires, 'partenaires', database_url)
    insert_dataframe_to_mysql(df_esports, 'esports', database_url)

    print(df_partenaires)
    print(df_esports)
    print(df)

    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()