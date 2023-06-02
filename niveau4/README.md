# Niveau 4 - Défi de CTF

Bienvenue au niveau 4 du défi de CTF de la CIA ! Dans ce défi, vous devrez combiner des compétences en exploitation web 
et en reverse engineering pour réussir. Êtes-vous prêt ?

## Instructions

1. Clonez ce dépôt GitHub contenant les fichiers du niveau 4.

2. Exécutez le fichier Python `web_re_challenge.py` pour lancer le défi.

3. Analysez le code source du défi pour comprendre la vulnérabilité de l'application web.

4. Exploitez la vulnérabilité pour accéder au fichier binaire.

5. Utilisez des outils de reverse engineering tels que gdb ou radare2 pour comprendre le fonctionnement du binaire.

6. Trouvez la condition qui doit être satisfaite pour afficher le drapeau.

7. Une fois que vous avez trouvé la solution, soumettez-la dans le format `01253{solution}`.

8. Si votre solution est correcte, vous obtiendrez le drapeau et remporterez le défi !

## Énoncé du Défi

Dans ce défi, vous devez exploiter une vulnérabilité dans une application web pour accéder à un fichier binaire. 
Ce fichier binaire, lorsqu'il est exécuté, affiche le drapeau sous certaines conditions.

## Indices

1. Indice web : Recherchez des vulnérabilités courantes dans les applications web, telles que les injections de commandes 
ou les injections SQL.

2. Indice de reverse engineering : Utilisez des outils de reverse engineering pour analyser le fonctionnement 
interne du binaire.

3. Indice du drapeau : Recherchez les conditions ou les opérations qui doivent être remplies pour afficher le drapeau.

## Solution

La solution consiste à identifier la vulnérabilité de l'application web et à effectuer une injection de commandes 
pour accéder au fichier binaire. Une fois le fichier binaire obtenu, utilisez un outil de reverse engineering 
pour l'analyser et comprendre le code. Vous remarquerez qu'une condition spécifique doit être remplie 
pour afficher le drapeau.

La condition consiste à fournir une entrée spécifique qui satisfera la vérification dans le code du binaire. 
Une fois que vous avez trouvé la valeur qui remplit la condition, vous pouvez l'utiliser pour afficher le drapeau.

Soumettez la solution dans le format `01253{solution}` pour obtenir le drapeau et remporter le défi.

Félicitations ! Vous avez réussi le niveau 4 du défi. Vous êtes un véritable expert en sécurité informatique !

---

**Notez que le drapeau est sensible à la casse. Assurez-vous d'utiliser la casse appropriée lors de la saisie de la solution.**
