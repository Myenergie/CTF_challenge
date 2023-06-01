# Challenge de Recrutement - CIA

Ce projet est un défi de recrutement basé sur la cybersécurité et le cryptage. 
Les participants doivent résoudre plusieurs niveaux de défis pour prouver 
leurs compétences en matière de cryptographie, de stéganographie, 
de forensique réseau et de sécurité des applications Web.

## Niveau 1 : "L'Académie" (Cryptographie et Stéganographie de base)

Le défi commence avec un message encodé dans un chiffre de César. 
Les joueurs doivent décoder le message pour découvrir un fichier image. 
À l'intérieur du fichier image, en utilisant des techniques de stéganographie, 
se trouve un autre message caché. Ce message peut être extrait en utilisant des techniques 
de stéganographie basées sur le bit de poids faible (least significant bit), 
guidant ainsi le joueur vers le prochain défi.

## Niveau 2 : "L'Agent de Terrain" (Forensique Réseau)

Dans ce défi, les joueurs reçoivent un fichier .pcap (fichier de capture de paquets), 
qui est un fichier de données contenant une capture instantanée du trafic réseau. 
Les joueurs doivent analyser le trafic réseau à l'aide d'outils tels que Wireshark. 
Ils doivent extraire des informations importantes telles que les adresses IP, 
identifier un trafic réseau anormal et trouver un fichier caché transmis via FTP ou HTTP.

Dans le fichier caché, il y a une énigme qui, une fois résolue, indique un protocole spécifique et un numéro de port. 
Les joueurs doivent revenir au fichier .pcap et filtrer ce protocole spécifique et ce port pour trouver un message caché qui les mènera au niveau suivant.

## Niveau 3 : "L'Analyste Cyber" (Sécurité des Applications Web)

Pour le dernier niveau, les joueurs se voient présenter une application Web vulnérable 
qui imite un site interne sécurisé de la CIA. Ils doivent exploiter les vulnérabilités 
de l'application Web (comme les injections SQL, les attaques de type Cross-Site Scripting (XSS) 
ou les attaques de type Server Side Request Forgery (SSRF)) pour obtenir un accès non autorisé 
ou révéler des informations cachées.

Le drapeau (flag) est divisé en plusieurs parties et caché dans toute l'application ; 
une fois les recrues rassemblent toutes les parties et assemblent le drapeau, elles ont réussi le défi de recrutement.
