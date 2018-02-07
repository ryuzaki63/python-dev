#!/usr/bin/env python
# -*- coding: utf-8 -*-


#################################################
#Auteur: Vikrant SINGH                          #
#Programme: ARP Poisoning                       #
#                                               #
#################################################


#################################################
#####################Imports#####################
from Tkinter import *
from scapy.all import *
import sys
import os
#################################################

def affichage_saisie():
   print("Interface: %s\nIP Victime: %s\nIP Routeur: %s" % (e1.get(), e2.get(), e3.get() ))


fenetre = Tk()
Label(fenetre, text="Interface").grid(row=0)
Label(fenetre, text="IP Victime").grid(row=1)
Label(fenetre, text="IP Routeur").grid(row=2)

e1 = Entry(fenetre)
e2 = Entry(fenetre)
e3 = Entry(fenetre)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(fenetre, text='Quit', command=fenetre.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(fenetre, text='Show', command=affichage_saisie).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
