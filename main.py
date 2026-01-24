import nmap3
from pprint import pprint

ip = "192.168.33.46"

if __name__ == '__main__':
    print('Hello, world!')
    # nmap = nmap3.Nmap()
    nmap = nmap3.NmapScanTechniques()
    # pprint(nmap.nmap_version()["compiled_with"])
    # results = nmap.scan_top_ports("google.com")
    results = nmap.nmap_tcp_scan(ip, args="-sV -sC -p-")

    ports=results[ip]["ports"]

    for port in ports:
        print(port["portid"])