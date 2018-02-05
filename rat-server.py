#################################################
#Auteur: Vikrant SINGH				#
#Programme: Socket-serveur			#
#						#
#################################################


#################################################
#####################Imports#####################

import socket


#################################################


hote = ' '
port = 5050

#SOCK_STREAM pour effectuer une connexion TCP et AF_INET pour l'utilisation adresse IPV4
server_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#On configure notre serveur pour qu'il écoute sur un port
server_side.bind((hote, port))

#Nombre de connexion  simultanée
server_side.listen(5)

