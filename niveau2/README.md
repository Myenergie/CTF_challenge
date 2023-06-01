## Niveau 2: Analyse du trafic réseau

Dans ce défi, vous devrez analyser le trafic réseau pour trouver le drapeau caché. Le drapeau est au format 01253{}.

Pour commencer le défi, lancez le conteneur Docker en utilisant la commande suivante:

docker build -t niveau2 .
docker run -v ${PWD}:/app niveau2

Après avoir exécuté ces commandes, vous trouverez un fichier PCAP nommé network_traffic.pcap dans le répertoire courant. 
Vous aurez besoin d'un outil comme Wireshark pour analyser ce fichier.

Indice: Le drapeau pourrait être caché dans l'un des en-têtes HTTP.

docker build -t niveau2 
docker run -v ${PWD}:/app niveau2

Solution:
Ouvrez le fichier network_traffic.pcap dans Wireshark ou un autre analyseur de paquets réseau. 
Si vous regardez les requêtes HTTP, vous devriez voir un en-tête User-Agent qui semble inhabituel. 
Cet en-tête contient le drapeau caché.

