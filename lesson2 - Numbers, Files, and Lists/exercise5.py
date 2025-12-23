# Assign a string of from command show ip int br 
intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"

# Split the variable into fields based on white spaces and assign to a list variable
intf_fields = intf.split()

print(intf_fields)

# Assign the different list items to different variables
intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[4]
intf_protocol = intf_fields[5]

# Print the variables
print(f"Interface name: {intf_name}")
print(f"Ip address: {intf_ip_addr}")
print(f"Interface status: {intf_status}")
print(f"Protocol status: {intf_protocol}")

# Check the line status and print it
line_status = intf_fields[4] == "up"
print(line_status)

# Check the protocol status and print it
line_protocol = intf_fields[5] == "up"
print(line_protocol)



