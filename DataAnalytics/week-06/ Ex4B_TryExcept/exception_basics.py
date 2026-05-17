# Exercise 4.B Lab 1
# Working with exceptions

# ValueError example
try:
    number = int("banana")
except ValueError:
    print("ValueError: Oops, that value cannot be converted to an integer.")
else:
    print(number)
finally:
    print("Let's try another one...")


print()


# NameError example
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to use an undefined object.")
else:
    print(m)
finally:
    print("Let's try another one...")


print()


# TypeError example
try:
    result = "5" + 10
except TypeError:
    print("TypeError: Oops, you tried to combine incompatible data types.")
else:
    print(result)
finally:
    print("Let's try another one...")


print()


# SyntaxError example
try:
    eval("x === 5")
except SyntaxError:
    print("SyntaxError: Oops, the Python syntax is invalid.")
else:
    print("No syntax error.")
finally:
    print("Let's try another one...")


print()


# Another ValueError example
try:
    age = int(input("Enter your age as a whole number: "))
except ValueError:
    print("ValueError: Please enter digits only, like 25.")
else:
    print(f"You entered age: {age}")
finally:
    print("Let's try another one...")
