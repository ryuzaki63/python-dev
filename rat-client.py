#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
#Auteur: Vikrant SINGH                          #
#Programme: Socket-client                       #
#                                               #
#################################################


#################################################
#####################Imports#####################

import socket


#################################################

def commande_recus():
	commande = client_toserver.recv(2048)
	commande = commande.decode()
	print (commande)


def envoi_confirm():
	client_toserver.send ("Victime: d'accord sire !")


hote= "127.0.0.1"
port= 5050

client_toserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_toserver.connect((hote,port))
print ("connexion OK ")

message= " "

while message != 'stop':
	commande_recus()
	envoi_confirm()
