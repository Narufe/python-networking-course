import re
from rich import print

filename = "show_lldp.txt"
with open(filename) as f:
  lldp_entries = f.read()

entry_pattern = "Chassis id:.*?(?=\n\n|$)"
match_list = re.findall(entry_pattern, lldp_entries, re.DOTALL)


port_id_pattern = r"Port id: (?P<remote_port>[\w/]+)"
local_port_id_pattern = r"Local Port id: (?P<local_port>[\w/]+)"
system_name_pattern = r"System Name: (?P<remote_system_name>[\w\.]+)"

print()

for entry in match_list:
  print(40 * "=")

  match = re.search(local_port_id_pattern, entry)
  if match:
    local_port = match.group("local_port")
    print(f"{local_port=}")

  match = re.search(system_name_pattern, entry)
  if match:
    remote_system_name = match.group("remote_system_name")
    print(f"{remote_system_name=}")

  match = re.search(port_id_pattern, entry)
  if match:
    remote_port = match.group("remote_port")
    print(f"{remote_port=}")

  print(40 * "=")
  print()
  

print()
