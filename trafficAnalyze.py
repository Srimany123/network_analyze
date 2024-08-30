from scapy.all import rdpcap

packets = rdpcap('network_traffic.pcap')
for pkt in packets:
    print(pkt.summary())
