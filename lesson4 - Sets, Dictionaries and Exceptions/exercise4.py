from rich import print

filename = "arubacx_show_vlan.txt"

with open(filename) as f:
  data = f.read()

vlans_dict = {}

for line in data.splitlines():
  # Skip the header
  if "--" in line or "Name" in line:
    continue
  
  vlan_id, *fields, type, interfaces = line.split()
  intf_groups = interfaces.split(",")

  # Construct a list of interfaces associated with a given VLAN
  intf_list = []
  for intf in intf_groups:
    # Check for ranges
    if "-" in intf:
      intf_start, intf_end = intf.split("-")
      
      # Dropping last character will give base interface
      base_intf = intf_start[0:-1]

      # Extract last number and convert to integer
      start = int(intf_start[-1])
      end = int(intf_end[-1])

      # Loop trough range of interfaces
      for interface_index in range(start, end + 1):
        # Reconstruct the interface string
        # Add it to the list of interfaces
        intf_list.append(base_intf + str(interface_index))

    # If the item is not a range, append it to the list  
    else:
      intf_list.append(intf)



  #  Add Vlan Id and its interfaces list to the dictionary
  vlans_dict[int(vlan_id)] = intf_list

print(vlans_dict)


