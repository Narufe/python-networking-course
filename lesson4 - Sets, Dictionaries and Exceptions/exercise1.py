from rich import print

filename = "show_ip_int_brief.txt"

valid_interfaces = {}

with open(filename) as f:
  for line in f:
    if "Interface" not in line or "IP-Address" not in line:
      if "unassigned" not in line:
        interface = line.split()
        interface_name = interface[0]
        IP_address = interface[1]
        
        # Populate the dictionary
        valid_interfaces[interface_name] = IP_address

print(valid_interfaces)
