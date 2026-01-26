from pprint import pprint
from scan_net import scan_net
from py_nmap import nmap_it

network = "192.168.1.0/24"

if __name__ == '__main__':
    res = scan_net(network)
    pprint(res)
    for host in res:
        nmap_it(str(host))
else:
    print('Nope, not executed.')