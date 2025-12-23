list_ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5"]

# Add individual address using append()
list_ip_addresses.append("10.0.0.6")

# Add a list of new address using extend()
list_ip_addresses.extend(["10.0.0.7", "10.0.0.8"])

# Add a list of new addresses using concatenation
list_ip_addresses += ["10.0.0.9", "10.0.0.10"]

# Printing
print(f"\nList of IP addreses: {list_ip_addresses}\n")

print(f"First IP address: {list_ip_addresses[0]}")
print(f"Last IP address: {list_ip_addresses[-1]}")
print()

#Remove first and last addresses
list_ip_addresses.pop(0)
list_ip_addresses.pop()

print("After removing first and last IP addreses: ")
print(list_ip_addresses)
print()

# Change the new first address
list_ip_addresses[0] = "2.2.2.2"
print("After updating the new first IP address: ")
print(list_ip_addresses)
print()
