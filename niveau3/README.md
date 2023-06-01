# Niveau 3 - Défi de CTF

Bienvenue au niveau 3 du défi de CTF de la CIA ! Dans ce défi, vous devrez analyser du trafic réseau capturé pour découvrir des informations sensibles. 
Êtes-vous prêt ?

## Instructions

1. Utilisez un logiciel d'analyse de trafic réseau, tel que Wireshark, pour ouvrir le fichier `network_traffic.pcap` inclus.

2. Analysez le trafic réseau capturé pour trouver les informations sensibles.

3. Les indices fournis ci-dessous vous aideront à trouver la solution.

4. Une fois que vous avez trouvé la solution, soumettez-la dans le format `01253{solution}`.

5. Si votre solution est correcte, vous obtiendrez le drapeau et passerez au niveau suivant !

## Énoncé du Défi

Dans ce défi, vous devez analyser un fichier de capture de trafic réseau (`network_traffic.pcap`) pour trouver des informations sensibles. 
Le trafic réseau comprend plusieurs requêtes HTTP, mais l'une d'entre elles contient le drapeau.

## Indices

1. Utilisez un logiciel d'analyse de trafic réseau pour visualiser les requêtes HTTP capturées.

2. Recherchez les requêtes HTTP avec des en-têtes ou des données inhabituelles.

3. Gardez un œil sur les en-têtes HTTP, les données brutes et les champs User-Agent.

## Solution

Après avoir analysé le fichier de capture de trafic réseau, vous remarquerez une requête HTTP avec un en-tête User-Agent inhabituel. 
Cette requête contient le drapeau suivant : `01253{Bien_joue_lagent_vous_etes_pret_pour_le_niveau_suivant}`.

Félicitations ! Vous avez réussi le niveau 3 du défi. Préparez-vous pour le niveau suivant !

---

Notez que le drapeau est sensible à la casse. Assurez-vous d'utiliser la casse appropriée lors de la saisie de la solution.
Notez que vous devez remplacer les espaces dans la solution avec la bare de soulignement

Amusez-vous bien et bonne chance !
