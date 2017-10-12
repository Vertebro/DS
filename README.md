#############DS_GitUD#######################

Si vous lisez ce texte vous avez réussi à 
cloner le projet DS_GitUDP.

############################################
#		Description		   #
############################################


Ce projet comprend les fichiers suivants :
* README.md
* clientUDP.py


Le fichier README.md contient les instructions


**Le programme python clientUDP.py permet de gagner
une place de ciné après modification du code pour 
échanger les trames selon le protocole suivant :**

Question:
* clientUDP ---["cinema"]----serveurUDP(192.168.0.202:5005)

Réponse:
* clientUDP ---[b0,b1,b2,b3]----serveurUDP(192.168.0.202:5005)

Format de la trame de réponse:
* Le numéro de carte client est un entier sur 32bits.
* Ce numéro est renvoyé suite à la demande string "cinema".
* Ce numéro est renvoyé sur 4 octet, octet de poids faible en premier


Si vous décriptez ce code dans le programme client, vous pouvez gagner
cette carte de ciné!!!!


############################################
#		Instructions		   #
############################################
0. Cloner le projet distant (déjà fait si vous lisez ce texte) (2pts)
1. Synchroniser ce projet avec votre compte GitHub (2pts)
2. Modifier le programme clientUDP.py selon le protocole définit (7pts)
3. Commenter proprement le programme (3pts)
4. Tester votre programme.
5. Indiquer le numéro de la carte de ciné : 4158522552 (2pts)
6. Sauvegarder vos changement en local (2pts)
7. Partager votre travail sur votre serveur GitHub (2pts)
