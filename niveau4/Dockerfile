
# Utilisez l'image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY web_re_challenge.py /app/

# Installer les dépendances Python
RUN pip install scapy

# Définir la commande à exécuter lorsque le conteneur démarre
CMD [ "python", "web_re_challenge.py" ]
