# Challenge de Recrutement - CIA

Ce projet est un défi de recrutement basé sur la cybersécurité et le cryptage. 
Les participants doivent résoudre plusieurs niveaux de défis pour prouver leurs compétences en matière de cryptographie, 
de stéganographie, de forensique réseau, de sécurité des applications Web et de reverse engineering.

## Niveau 1 : "L'Académie" (Cryptographie et Stéganographie de base)

Le défi commence avec un message encodé dans un chiffre de César. 
Les joueurs doivent décoder le message en utilisant une clé de décalage spécifique pour retrouver le message original. 
Le message décodé révèle l'emplacement d'un fichier image. À l'intérieur du fichier image, 
en utilisant des techniques de stéganographie basées sur le bit de poids faible (LSB), 
se trouve un autre message caché. Les joueurs doivent extraire ce message en utilisant 
des outils appropriés pour révéler le drapeau et passer au niveau suivant.

## Niveau 2 : "L'Agent de Terrain" (Forensique Réseau)

Dans ce défi, les joueurs se voient présenté un fichier de capture de trafic réseau (.pcap). 
Ils doivent analyser ce fichier à l'aide d'outils tels que Wireshark pour examiner le trafic réseau et 
identifier des informations sensibles. Les joueurs doivent rechercher des adresses IP, des protocoles spécifiques 
et des schémas de communication suspects pour trouver des indices cachés. Ces indices les guideront 
vers la découverte d'un fichier secret qui contient le drapeau. La résolution de ce défi démontrera les compétences 
en forensique réseau des joueurs.

## Niveau 3 : "L'Analyste Cyber" (Sécurité des Applications Web)

Dans ce défi, les joueurs se voient présenté une application web simulée qui imite un site interne sécurisé de la CIA. 
Les joueurs doivent analyser le code source de l'application, identifier les vulnérabilités de sécurité et 
les exploiter pour obtenir un accès non autorisé ou révéler des informations sensibles. 
Ils peuvent rencontrer des vulnérabilités telles que les injections SQL, les attaques de type Cross-Site Scripting (XSS) 
ou les attaques de type Server Side Request Forgery (SSRF). En exploitant ces vulnérabilités, 
les joueurs pourront obtenir le drapeau et passer au niveau suivant.

## Niveau 4 : "L'Agent Secret" (Web Exploitation et Reverse Engineering)

Dans ce dernier niveau, les joueurs doivent démontrer leurs compétences en web exploitation et 
en reverse engineering. Ils devront exploiter une vulnérabilité dans une application web 
pour obtenir l'accès à un fichier binaire. Le fichier binaire est un programme exécutable 
qui nécessite d'être analysé en utilisant des outils de reverse engineering tels que gdb (GNU Debugger) ou radare2. 
Les joueurs devront comprendre le fonctionnement du binaire et trouver une condition spécifique pour révéler le drapeau. 
Ce niveau combine les compétences de l'exploitation web et du reverse engineering pour un défi plus complexe.

---

**Notez que les drapeaux dans chaque niveau suivent le format `01253{drapeau}`. Assurez-vous de respecter le

 format lors de la soumission de vos réponses.**

Amusez-vous bien et bonne chance !