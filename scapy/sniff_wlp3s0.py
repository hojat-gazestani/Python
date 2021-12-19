from scapy.all import *
from pprint import pprint

print("Begin capturing all packets from all interface. send ctrl+c to terminate and print summary")
pkts = sniff(iface="wlp3s0", filter="icmp")

pprint(pkts.summary())
