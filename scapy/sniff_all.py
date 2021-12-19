from scapy.all import *
from pprint import pprint

print("Begin capturing all packets from all interfaces, send ctrl+c to terminate and print summary")
pkts = sniff()

pprint(pkts.summary())
