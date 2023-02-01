######################################################################################################
# Title: Brute force                                                                                 #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7                                                                  #
# If you use the code give me the credit please                                                      #
######################################################################################################

import socket
import sys
import subprocess
import time
import tqdm
from tqdm import tqdm

def get_service_name(port, proto):
    try:
        proto_str = ''
        if proto == socket.SOCK_STREAM:
            proto_str = 'tcp'
        elif proto == socket.SOCK_DGRAM:
            proto_str = 'udp'
        service = socket.getservbyport(port, proto_str)
        return service
    except OSError as e:
        return None

def is_port_open(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        return False

def get_host_name(host):
    try:
        host_name = socket.gethostbyaddr(host)[0]
        return host_name
    except socket.error as e:
        return host

def check_os(host):
    try:
        os = subprocess.check_output("nmap -O " + host, shell=True)
        return os
    except subprocess.CalledProcessError as e:
        return e.output

host = input("Enter the host to scan: ")
protocol = input("Enter the protocol (TCP/UDP): ")

if protocol.upper() == "TCP":
    proto = socket.SOCK_STREAM
elif protocol.upper() == "UDP":
    proto = socket.SOCK_DGRAM
else:
    print("Invalid protocol entered.")
    sys.exit()

host_name = get_host_name(host)
os = check_os(host)
print("\nHostname:", host_name)
print("Operating System:", os)

print("Scanning ports...")
for port in tqdm(range(1, 65535)):
    if is_port_open(host, port):
        service = get_service_name(port, proto)
        if service:
            print(f"Port {port} is open and running {service}.")
        else:
            print(f"Port {port} is open but the service could not be identified.")
    else:
        pass
