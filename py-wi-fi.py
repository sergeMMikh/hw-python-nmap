import pywifi
import time
from pprint import pprint

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print(iface.name())
pprint(iface)

iface.scan()
time.sleep(2)

result = iface.scan_results()

for net in result:
    print("-" * 40)
    print("SSID:   ", net.ssid)
    print("BSSID:  ", net.bssid)
    print("Signal: ", net.signal)
    print("Auth:   ", net.auth)
    print("Cipher: ", net.cipher)

