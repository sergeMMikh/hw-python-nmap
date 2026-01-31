from pprint import pprint
import nmap3

# network = "192.168.1.0/24"

def scan_net(network: str) -> list:


    nmap = nmap3.NmapHostDiscovery()
    results = nmap.nmap_no_portscan(network)

    alive_hosts = []

    for key, value in results.items():
        # пропускаем служебные секции
        if key in ("runtime", "stats", "task_results"):
            continue

        state_block = value.get("state")
        if not isinstance(state_block, dict):
            continue

        # print(state_block)
        # print(state_block.get("state"))

        if state_block.get("state") == "up":
            alive_hosts.append(key)
            # print(key, value)

    # print(alive_hosts)

    return alive_hosts