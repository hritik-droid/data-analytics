import math

tourists = 38
van_capacity = 15
van_cost = 250

vans_needed = math.ceil(tourists / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / tourists

print("Number of tourists: " + str(tourists))
print("Vans needed: " + str(vans_needed))
print("Total van cost: $" + format(total_cost, ".2f"))
print("Cost per person: $" + format(cost_per_person, ".2f"))

# There may be leftover money because the cost per person is rounded up/down
# and vans must be rented as full vans, not partial vans.