filename = "show_ip_int_brief.txt"

ip_lst = []
intr_lst = []
with open(filename) as f:
  # lines = f.readlines()
  for line in f:
    if "10." in line:
      line = line.split()
      ip_lst.append(line[1])
      intr_lst.append(line[0])

print(f"\nIP Addreses list: {ip_lst}")      
print(f"\nInterfaces list: {intr_lst}")      



