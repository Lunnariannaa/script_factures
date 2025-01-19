import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def collect_factures():
    print("=== Collecte de factures ===")
    
    # Récupération des variables d'environnement
    site_url = os.getenv("SITE_URL")  # URL du site
    username = os.getenv("USERNAME")  # Nom d'utilisateur
    password = os.getenv("PASSWORD")  # Mot de passe

    if not site_url or not username or not password:
        print("Erreur : Les variables d'environnement SITE_URL, USERNAME ou PASSWORD sont manquantes.")
        return

    # Configuration de Selenium pour Railway (headless mode obligatoire)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Mode sans interface graphique
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Résolution fixe

    # Initialisation du navigateur
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=options)

    try:
        # Étape 1 : Ouvrir le site
        print(f"Connexion au site : {site_url}")
        driver.get(site_url)

        # Étape 2 : Remplir les champs de connexion
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

        # Étape 3 : Cliquer sur le bouton de connexion
        driver.find_element(By.ID, "login-button").click()  # Modifier selon l'ID réel du bouton
        print("Connexion en cours...")

        # Étape 4 : Vérifier si la connexion a réussi
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))  # Modifier selon la classe d'un élément de la page
        print("Connexion réussie !")

        # Étape 5 : Naviguer vers la page des factures
        driver.find_element(By.LINK_TEXT, "Factures").click()  # Modifier selon le lien ou le bouton
        print("Navigation vers la page des factures...")

        # Étape 6 : Récupérer les liens de téléchargement des factures
        factures = driver.find_elements(By.CLASS_NAME, "facture-link")  # Modifier selon la classe réelle des liens
        for facture in factures:
            facture_url = facture.get_attribute("href")
            print(f"Téléchargement de la facture depuis : {facture_url}")
            # Tu peux utiliser `driver.get(facture_url)` ou une autre méthode pour télécharger

        print("Téléchargement des factures terminé !")

    except Exception as e:
        print("Une erreur est survenue :", e)

    finally:
        # Étape 7 : Fermer le navigateur
        driver.quit()
        print("Script terminé.")

# Lancer le script
if __name__ == "__main__":
    collect_factures()