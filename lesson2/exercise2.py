file_name = "show_version.txt"

#open file
f = open(file_name)

#read entire file
data = f.read() # data here is a string

#print data type of the variable
print(f"\nData Type: {type(data)}")

#print first line
print("\nPrinting the first line: \n")
print("#" * 80)
print(data.splitlines()[0])
print("#" * 80)

#close the file
f.close()
print()



#same task using context manager
with(open(file_name) as f):
  data = f.readlines() #data list has each line as list item
 
print(f"\nData Type: {type(data)}")
print("\nPrinting the first line: \n")
print("#" * 80)
print(data[0].strip()) #strips the list item from 
print("#" * 80)
print()


