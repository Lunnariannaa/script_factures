import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(r"C:\script_factures\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    site_url = "https://example.com"
    username = "votre_email@example.com"
    password = "votre_mot_de_passe"

    driver.get(site_url)
    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()

    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Mes Factures").click()

    factures = driver.find_elements(By.LINK_TEXT, "Télécharger PDF")
    for facture in factures:
        facture.click()
        time.sleep(1)
finally:
    driver.quit()
