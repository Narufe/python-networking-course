line = "Processor board ID FAL127990LA"
if "Processor board ID" in line:
  print(True)  

words = line.split()

print(words[3])

