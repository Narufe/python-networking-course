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
  intf_set = set()
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
        intf_set.add(base_intf + str(interface_index))

    # If the item is not a range, append it to the list  
    else:
      intf_set.add(intf)

  #  Add Vlan Id and its interfaces list to the dictionary
  vlans_dict[int(vlan_id)] = intf_set

print("-" * 80)

print(f"a. Vlans common to Vlan 1, 2 and 3: {vlans_dict[1] & vlans_dict[2] & vlans_dict[3]}")

all_vlans_intf = set()
for key in vlans_dict:
  all_vlans_intf = vlans_dict[key] | all_vlans_intf
print(f"b. All Vlans Interfaces: {all_vlans_intf}")

print(f"c. Interfaces associated with Vlan 12 + 13: {vlans_dict[12] | vlans_dict[13]}")

print("-" * 80)
  
