import logging
from datetime import datetime
import subprocess
import sys
import signal

# Suppress Scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

try:
    from scapy.all import *
except ImportError:
    print("Scapy package for Python is not installed on your system.")
    sys.exit()

# Print a message to the user
print("\n! Make sure to run this program as ROOT !\n")

# Function to handle graceful exit
def signal_handler(sig, frame):
    print("\n[*] Exiting the sniffer...")
    sniffer_log.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Ask the user for input
net_iface = input("* Enter the interface on which to run the sniffer (e.g. 'enp0s8'): ")