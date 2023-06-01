
from scapy.all import Ether, IP, TCP, HTTP, HTTPRequest, Raw, wrpcap

# le flag
flag = "01253{Bien_joue_lagent_vous_etes_pret_pour_le_niveau_suivant}"

# Define a list to hold the packets
packets = []

# creation de 5 fauses requettes
for i in range(5):
    # Create the IP layer of the packet
    ip = IP(src="192.168.1." + str(i+1), dst="192.168.1.100")
    
    # creer le niveau TCP
    tcp = TCP(sport=1024+i, dport=80)

    if i == 4:
        http = HTTP() / HTTPRequest(
            Method="GET",
            Path="/",
            Headers={'User-Agent': 'Mozilla/5.0 (compatible; ' + flag + ')'}
        )
    else:
        
        http = HTTP() / HTTPRequest(
            Method="GET",
            Path="/",
            Headers={'User-Agent': 'Mozilla/5.0'}
        )

    # ajouter le paquet a la liste
    packets.append(Ether() / ip / tcp / http)

# ecrire le traffic dans un fichier pcap
wrpcap('network_traffic.pcap', packets)
