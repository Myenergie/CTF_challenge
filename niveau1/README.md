# Niveau 1 - Recrutement de la CIA

## Description du Challenge

Bienvenue à la première étape du processus de recrutement de la CIA. Votre mission est de révéler un message caché dans une image. 

## Configuration

1. Installer les dépendances nécessaires avec la commande suivante: 
    ```
    pip install -r requirements.txt
	
	pour docker
    ```
2. Lancer le script Python en utilisant la commande suivante:
    ```
    python niveau1.py
    ```
3. Suivez les instructions affichées à l'écran.

## Indications

* La CIA a caché le message en utilisant une technique de stéganographie.
* Un peu de recherche sur la stéganographie vous conduira à la méthode LSB.
* Le message caché est chiffré, le chiffre de César est couramment utilisé par la CIA.

## Solution

La solution à ce niveau implique l'utilisation de la stéganographie. En particulier, la méthode LSB (Least Significant Bit) est utilisée pour cacher le message dans l'image. Le message est également chiffré avec un chiffrement de César avec un décalage de 3.

1. Exécutez le script Python et suivez les instructions.
2. Ouvrez l'image et utilisez un outil de stéganographie pour extraire le message caché. 
3. Le message que vous récupérerez sera chiffré. Utilisez un déchiffreur de César pour le déchiffrer et obtenir le flag.



Le flag est sous la forme `01253{message_déchiffré}`.

Notes: Veuillez remplacer les espaces dans la reponse par la bare de soulignement si necessaire.

Félicitations! Vous avez réussi la première étape du processus de recrutement de la CIA.
