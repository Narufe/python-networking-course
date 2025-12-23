ip_addr = "192.168.254."

subnet_prefix = int(input("Enter the subnet prefix length between 25 to 30: "))

#subnet size
host_bits = 32 - subnet_prefix

#subnet size: each subnet starts at a multiple of this 
#increment starting from zero
subnet_increment = 2 ** host_bits

#number of hosts (after taking out subnet network address 
#and broadcoast addres)
number_of_hosts = subnet_increment - 2

print(f"1. The number of hosts in the subnet: {number_of_hosts} \n")

print(f"2. The network number of the first two subnets: ")
print(f"{ip_addr}0")
print(f"{ip_addr}{subnet_increment} \n")

print(f"3. The first and last host addresses in the first subnet")
#first host in first subnet
print(f"{ip_addr}1")
#last host in first subnet
print(f"{ip_addr}{number_of_hosts}")
