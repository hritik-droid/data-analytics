# Exercise 2.A - Tips Calculation

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate total
total_due = food_cost + tax + tip

# Display results
# str() is used to convert numbers into strings so they can be combined with text in print()

# Original output
# print("The total due is " + str(total_due))

# Improved output
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))