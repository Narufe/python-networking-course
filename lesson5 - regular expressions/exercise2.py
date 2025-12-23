import re
from rich import print

filename = "show_ip_bgp_neighbors.txt"

with open(filename) as f:
  data = f.read()

neighbor_ip = re.search(r"^BGP neighbor is ([\d\.]+)", data)
remote_AS = re.search(r"remote AS (\d+)", data)
bgp_ver = re.search(r"BGP version (\d)", data, re.M)
rmt_rt_ID = re.search(r"remote router ID ([\d\.]+)", data, re.M)
bgp_state = re.search(r"BGP state = (\w+)", data, re.M)

print(40 * "=")
print(f"BGP neighbor is {neighbor_ip.group(1)}")
print(f"remote AS {remote_AS.group(1)}")
print(f"BGP version {bgp_ver.group(1)}")
print(f"remote router ID {rmt_rt_ID.group(1)}")
print(f"BGP state = {bgp_state.group(1)}")
print(40 * "=")
