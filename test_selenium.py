from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Options pour Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Mode sans interface graphique
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Indiquer le chemin vers ChromeDriver
service = Service("C:/chemin/vers/chromedriver.exe")  # Change ce chemin
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com")
    print("Titre de la page :", driver.title)
finally:
    driver.quit()