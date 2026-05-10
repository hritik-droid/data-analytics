# Description: This script tests various numeric conversion techniques
# Author: Hritik

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Convert values
a_float = float(a)  # works, converts to 101.1
a_int = int(float(a))  # works after converting to float first

b_int = int(b)  # works, converts to 55
b_float = float(b)  # works, converts to 55.0

# c_int = int(c)  # ERROR: contains letters
# c_float = float(c)  # ERROR: contains letters

# Extract numeric part from c using slicing
c_num = c[:3]  # "402"
c_int = int(c_num)

# d_int = int(d)  # ERROR: contains text

# Extract number from d
d_num = d[-2]  # gets '5'
d_int = int(d_num)

# Strip spaces from a and d
print("a stripped:", a.strip())
print("d stripped:", d.strip())

# Print values and types
print(a_float, type(a_float))
print(a_int, type(a_int))

print(b_int, type(b_int))
print(b_float, type(b_float))

print(c_int, type(c_int))
print(d_int, type(d_int))