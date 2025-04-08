import re
from rich import print

filename = "aruba_cx_show_ipv6_intf.txt"

with open(filename) as f:
  ipv6_data = f.read()

m = re.search(r"^Interface (\S+) is (\S+)", ipv6_data)
if m:
  int_name = m.group(1)
  int_status = m.group(2)

m = re.search(r"^Admin state is (\S+)", ipv6_data, re.M)
if m:
  admin_state = m.group(1)

m = re.search(r"^IPv6 address:\s*(\S+)", ipv6_data, re.M)
if m:
  ipv6_addr = m.group(1)


print(40 * "=")

print(f"{int_name=}")
print(f"{int_status=}")
print(f"{admin_state=}")
print(f"{ipv6_addr=}")
print(40 * "=")
