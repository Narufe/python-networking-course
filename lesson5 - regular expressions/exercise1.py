import re
from rich import print

filename = "show_version.txt"
with open(filename) as f:
  data = f.read()

model_num = re.search(r"^\w*\s(\w*-\d.)", data, re.M)
#suggested solution: "^cisco ([-\w]*) .*bytes of memory\.$" 


serial_num = re.search(r"[A-Z]{3}\d+[A-Z]{2}$", data, re.M)
#suggested solution: "^Processor board ID (\w+)$" 

print("=" * 30)
print(f"Model Number:   {model_num.group(1)}")
print(f"Serial Number: {serial_num.group(0)}")
print("=" * 30)

