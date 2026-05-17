# Exercise 4.A Lab 1
# Practicing file reading

# Open the file in read mode.
f = open("about_me.txt", "r")

# Read the first 50 characters.
first_50 = f.read(50)

# Read the next four lines and save them in a list.
next_four_lines = []
for i in range(1, 5):
    next_four_lines.append(f.readline())

# Read the next 100 characters, rounded up to complete lines.
next_100 = f.readlines(100)

# Print the results.
print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")

# Close the file after reading.
f.close()
