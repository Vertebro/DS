# -*- coding: utf-8 -*-

import socket


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)

sock.connect(("192.168.0.202", 5005)) # Buffer de connexion du socket 
sock.send("cinema") # Fonction qui envoie des données au serveur


trameReponse, addr = sock.recvfrom(1024) # On reçoit la réponse du serveur qui est stockée dans la variable "trameReponse", ainsi que l'adresse et le port


print "Réception de la trame de réponse", trameReponse.encode("hex") # Affiche la trame reçue en hexadécimal

trame = bytearray(trameReponse) # Transforme la trame en tableau binaire d'octets

code = trame[0] # Première partie de la trame qui contient le premier octet (poids faible donc pas de décalage)
code += trame[1] << 8 # Seconde partie avec un décalage de de 8 bits vers la gauche pour récupérer les octets avec leurs poids respectifs
code += trame[2] << 16 # Troisième partie avec un décalage de 16 bits vers la gauche
code += trame[3] << 24 # Quatrième partie avec un décalage de 24 bits vers la gauche

# Le += sert à ajouter à la variable, dans ce cas précis on superpose 

print code # Affiche le nombre décodé

