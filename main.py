import nmap3
from pprint import pprint

if __name__ == '__main__':
    print('Hello, world!')
    # nmap = nmap3.Nmap()
    nmap = nmap3.NmapScanTechniques()
    pprint(nmap.nmap_version()["compiled_with"])
    # results = nmap.scan_top_ports("google.com")
    results = nmap.scan_top_ports("127.0.0.1")
    # pprint(results["127.0.0.1"]["ports"])

    ports=results["127.0.0.1"]["ports"]

    for port in ports:
        print(port["portid"])