import os
import platform
import sys
import nmap3


def pick_tcp_scan_type() -> str:
    """
    Выбираем тип TCP-сканирования в зависимости от системы:
    - Windows -> -sT
    - Linux root -> -sS
    - Linux not root -> -sT
    """
    system = platform.system()
    if system == "Windows":
        return "-sT"
    if system == "Linux":
        return "-sS" if os.geteuid() == 0 else "-sT"
    return "-sT"


def format_service(port_entry: dict) -> tuple[str, str]:
    """
    Возвращает (service_name, version_string)
    """
    svc = port_entry.get("service") or {}
    name = svc.get("name") or "unknown"

    # nmap3 кладёт версии в product/version/extrainfo (если -sV дал результат) 
    # иначе- просто пусто ("")
    product = svc.get("product") or ""
    version = svc.get("version") or ""
    extrainfo = svc.get("extrainfo") or ""

    parts = [p for p in [product, version, extrainfo] if p]
    ver = " ".join(parts).strip()

    return name, (ver if ver else "unknown")


def nmap_it(target_ip: str) -> int:
    """
    Сканирует удалённый хост
    """
    print(f"Scanning ip: {target_ip}")

    # не добавляем -sS/-sT, потому что nmap_tcp_scan сам добавит TCP scan.
    args = "--reason -T3"

    nmap = nmap3.NmapScanTechniques()

    try:
        results = nmap.nmap_tcp_scan(target_ip, args=args)
    except Exception as e:
        print(f"Scan failed: {e}")
        return 2

    host = results.get(target_ip)
    if not host:
        print("No host data in results (maybe host down or key differs).")
        return 3

    ports = host.get("ports", [])

    # Фильтруем только open
    open_ports = [p for p in ports if p.get("state") == "open"]

    if not open_ports:
        print("No open TCP ports found.")
        return 0

    print("\nPORT\tSTATE\tSERVICE\tVERSION")
    for p in open_ports:
        portid = p.get("portid", "?")
        state = p.get("state", "?")
        service_name, version_str = format_service(p)
        print(f"{portid}/tcp\t{state}\t{service_name}\t{version_str}")

    return 0


if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.33.64"

    if platform.system() == "Linux" and os.geteuid() != 0:
        print("Note: running without root; for best results run: sudo -E python py_nmap.py <ip>\n")

    raise SystemExit(nmap_it(target_ip))
