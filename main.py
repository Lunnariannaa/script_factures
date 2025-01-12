from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Configuration du navigateur
driver = webdriver.Chrome()

# URL et identifiants du site
site_url = "https://example.com"
username = "votre_email@example.com"
password = "votre_mot_de_passe"

# Connexion au site
driver.get(site_url)
time.sleep(2)

# Remplir les champs d'identifiant et de mot de passe
driver.find_element(By.ID, "login_field").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "commit").click()

# Naviguer vers la section des factures
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Mes Factures").click()

# Télécharger les fichiers
factures = driver.find_elements(By.LINK_TEXT, "Télécharger PDF")
for facture in factures:
    facture.click()
    time.sleep(1)

driver.quit()
