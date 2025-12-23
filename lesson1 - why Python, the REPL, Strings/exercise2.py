print()

dc_location = input("Enter data center location: ")
print()

print("Upper case:")
print(dc_location.upper())
print()

print("Strip off whitespace:")
print(f"Before: {repr(dc_location)}")

print(f"After: {repr(dc_location.strip())}")
print()

print("Method chaining:")
print(f"{repr(dc_location.upper().strip())}")
print()
print()

