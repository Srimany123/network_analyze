from scapy.all import rdpcap
import pandas as pd

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    features = []

    for pkt in packets:
        feature = {}
        if 'IP' in pkt:
            feature['src_ip'] = pkt['IP'].src
            feature['dst_ip'] = pkt['IP'].dst
            feature['protocol'] = pkt['IP'].proto
            feature['length'] = len(pkt)
            features.append(feature)
    return pd.DataFrame(features)

features_df = extract_features('network_traffic.pcap')
print(features_df.head())
