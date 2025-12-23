file_name = "show_ip_int_brief.txt"

file = open(file_name)

lines = file.readlines()

for line in lines:
  if "10.220" in line:
    line = line.split()  
    intf_name = line[0]
    ip_addr = line[1]

print(f"Interface name: {intf_name}")
print(f"Ip address: {ip_addr}")
