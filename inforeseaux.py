import socket
import subprocess
import sys
from datetime import datetime as dt
import psutil

#-----------------fonction que je vais re utiliser  ------------------#

# fonction qui convertit un grand nombre d'octets dans un format à l'échelle


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# retour à la ligne rapide


def void():
    print("\n")

#---------------- information réseaux -------------------#


print("\n", "="*40, "Information Réseaux", "="*40, "\n")

print("\n", "-"*30, "Informations IP", "-"*30, "\n")

#---------------- information IP -------------------#


def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


print("IP :", extract_ip())

#---------------- information Interface -------------------#

print("\n", "-"*30, "Informations Interface", "-"*30, "\n")


def interface():
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")


interface()

#---------------- information Pacquets -------------------#

print("\n", "-"*30, "Informations Pacquets Activé", "-"*30, "\n")


def pathinstalled():

    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    if 'requests' in installed_packages:
        print("paquets activé :", installed_packages, "\n")


pathinstalled()
