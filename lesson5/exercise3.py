import re
from rich import print

filename = "arista_show_ip_arp.txt"

f = open(filename)

ip_mac_tuples = re.findall(r"([\d{1,3}\.]+).*([0-9a-fA-F\.]{14})\s+Vlan1", f.read())

print(40 * "=")
print(dict(ip_mac_tuples))
print(40 * "=")


