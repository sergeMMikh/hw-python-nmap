import nmap3
from pprint import pprint


# ip = "192.168.33.46"

args = (
    # "-sS "                 # SYN scan (полуоткрытый TCP-скан, быстрый и менее шумный)
    "-sV "                 # Определение версий сервисов на открытых портах
    "-sC "                 # Запуск стандартных NSE-скриптов (default)
    "-p- "                 # Сканирование всех TCP-портов (1–65535)

    "-O "                  # Определение операционной системы (OS fingerprinting)
    "--reason "            # Показ причины, почему порт считается open/closed
    "--version-all "       # Максимально агрессивное определение версии сервисов

    "--script-timeout 10m "# Увеличенный таймаут для NSE-скриптов (до 10 минут)
    "--max-retries 3 "     # Ограничение количества повторных попыток
    "--host-timeout 6h "   # Максимальное время сканирования одного хоста

    "-T3"                  # Умеренный тайминг (баланс скорости и стабильности)
)


def nmap_it(ip: str):
    print(f'Scanning ip: {ip}')
    # nmap = nmap3.Nmap()
    nmap = nmap3.NmapScanTechniques()
    # pprint(nmap.nmap_version()["compiled_with"])
    # results = nmap.scan_top_ports("google.com")
    # results = nmap.nmap_tcp_scan(ip, args="-sV -sC -p-")
    results = nmap.nmap_tcp_scan(ip, args=args)

    ports=results[ip]["ports"]

    for port in ports:
        print(port["portid"])