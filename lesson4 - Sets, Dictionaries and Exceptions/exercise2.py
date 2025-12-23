from rich import print

filename = "show_ip_int_brief.txt"

with open(filename) as f:
  data = f.read()

interfaces = {}

for line in data.splitlines():
  
  # Skip header line
  if "Interface" in line:
    continue

  inter_name, IP, *fields, status, protcol = line.split()

  interfaces[inter_name] = {
    "ip_addr": IP, 
    "line_status": status, 
    "line_protocol": protcol}

print(interfaces)
