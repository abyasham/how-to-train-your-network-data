import glob
import os
#import pyshark

# Set the path to the directory containing the pcap files
path = "C:/Users/wistara/Documents/dataset/BMS-20230316T101542Z-001/BMS/alerts/event/"

# Set the path to the directory where the csv files will be saved
output_path = "C:/Users/wistara/Documents/dataset/BMS-20230316T101542Z-001/BMS/alerts/event/"

# Use glob to recursively search for all pcap files in the directory and its subdirectories
pcap_files = glob.glob(os.path.join(path, "**/*.pcap*"), recursive=True)
#for dirpath, dirnames, filenames in os.walk(path):
# Loop through the pcap files
for pcap_file in pcap_files:
    output_csv = pcap_file + '.csv'
    os.system(f'tshark -r {pcap_file} -T fields -E separator=, -E quote=d -E occurrence=f -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -E header=y -E separator=/t > {output_csv}')