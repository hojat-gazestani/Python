from scapy.all import *

print("Begin captuing all packets from all interfaces. send ctrl+c to terminate and print summary")
pkts = sniff(iface="wlp3s0", filter="icmp")

wrpacp("/home/icmp_packets_wlp3s0.pcap",pkts)
