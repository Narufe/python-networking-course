filename = "junos_show_arp.txt"

with open(filename) as f:
  for line in f:
    # Skip header and trailer lines
    if "MAC Address" in line or "Total entries"in line:
      continue

    mac_addr, ip_addr, *fields = line.split()

    alt_mac_addr = mac_addr.replace(":", "-")
    print(alt_mac_addr, ip_addr)
