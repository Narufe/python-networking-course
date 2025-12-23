file_name = "show_arp.txt"

with open(file_name) as f:
  show_arp = f.readlines()

print()

print(f"a. Data type of 'show_arp' variable:  {type(show_arp)}")

print(f"\nb. Length of list: {len(show_arp)}")

header = show_arp[0]
print(f"\nc. Header line: {show_arp[0]}")

print(f"d. First line of tabular data: {show_arp[1]}")
print(f"   Last line of tabular data: {show_arp[-1]}")

fields = header.split()
print(f"e. Fields of the header: {fields}")

print(f"\nf. Data type of 'fields':  {type(fields)}")

print(f"\ng. Length of 'fields' list: {len(fields)}")

print(f"\nh. First field and last field:")
print(f"   {fields[0]}")
print(f"   {fields[-1]}")

print("\nFixing the the Age (min) in the header")
fields.pop(3)
print(fields)

print("\nFixing the the Hardware Addr in the header")
fields[3] = fields[3] + "_" + fields[4]
fields.pop(4)
print(fields)
print()
