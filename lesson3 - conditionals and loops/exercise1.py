ip_address = "192.168.254."

print()

# Prompt user to enter a subnet prefix
subnet_prefix = int(input("Enter a subnet prefix length between 25-30: "))

# Subnet bits
subnet_bits = subnet_prefix - 24

# Number of subnets
num_of_subnets = 2 ** subnet_bits

# Host bits
host_bits = 32 - subnet_prefix

# Subnet size: each subnet starts at a multiple of this 
# increment starting from zero
subnet_increment = 2 ** host_bits

# Number of hosts (after taking out subnet network address 
# and broadcoast addres)
number_of_hosts = subnet_increment - 2

print("\nSubnets:")
print(f" Number of subnets: {num_of_subnets}")

# Print subnet addreses by iterating with a counter and adding 
# the increment

count = 0
subnet = 0
while count < num_of_subnets:
  print(f" Subnet Number: {ip_address}{subnet}")
  subnet += subnet_increment
  count += 1 

# Number of hosts in each subnet
print(f"\na. Number of hosts in each subnet: {number_of_hosts}")

# Total number of subnets 
print(f"\nb. Total number of subnets: {num_of_subnets}")

# First and last host address in just the first subnet
print(f"\nc. First host address in first subnet: {ip_address}1")
print(f"\nc. Last host address in first subnet: {ip_address}{subnet_increment-1}")

print()



