FROM python:3.11-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libgbm-dev \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    libu2f-udev \
    xvfb \
    gnupg

# Ajouter la clé et le dépôt de Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Installer Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Vérifier la version de Chrome installée
RUN google-chrome --version

# Télécharger et configurer ChromeDriver avec une version spécifique
ENV CHROME_DRIVER_VERSION=114.0.5735.90
RUN wget -q "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip

# Copier le fichier requirements.txt et installer les bibliothèques Python
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
