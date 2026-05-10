a = 12
b = 5
c = 20

smallest = a
largest = a

if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

if b > largest:
    largest = b
if c > largest:
    largest = c

print("The smallest number is " + str(smallest))
print("The largest number is " + str(largest))