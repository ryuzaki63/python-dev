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

hote= "127.0.0.1"
port= 5050

client_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_side.connect((hote,port))
print ("connexion OK ")
