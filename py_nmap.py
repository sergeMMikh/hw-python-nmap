import nmap3
import os
import platform
import sys

from pprint import pprint

system = platform.system()

ip = "192.168.33.46"


def tcp_scan_args():
    system = platform.system()
    if system == "Windows":
        return "-sT"
    if system == "Linux" and os.geteuid() == 0:
        return "-sS"
    return "-sT"

nmap = nmap3.Nmap()

args = (
    f"{tcp_scan_args()} "
    "-sV -sC -p- "
    "-O "
    "--reason "
    "--version-all "
    "-T3"
)

def nmap_it(ip: str):
    print(f'Scanning ip: {ip}')
    # nmap = nmap3.Nmap()
    nmap = nmap3.Nmap()
    results = ()
    # pprint(nmap.nmap_version()["compiled_with"])
    # results = nmap.scan_top_ports("google.com")
    # results = nmap.nmap_tcp_scan(ip, args="-sV -sC -p-")
    # results = nmap.nmap_tcp_scan(ip, args=args)
    try:
        results = nmap.nmap_command(args, ip)
    except Exception as e:
        print(e)
        return

    pprint(results)

    # ports=results[ip]["ports"]

    # for port in ports:
    #     print(port["portid"])

if __name__ == '__main__':
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.33.64"
    nmap_it(target_ip)  
else:
    print('Nope, not executed.')