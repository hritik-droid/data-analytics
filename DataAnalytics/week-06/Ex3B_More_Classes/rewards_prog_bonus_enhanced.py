# Exercise 3.B Lab 2 Optional
# Enhanced Rewards Program class

cust_list = []


class RewardsProgram:
    """A class that stores customer rewards program information and tracks restaurant visits."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    def calculate_rewards(self, food_bill):
        return int(food_bill)

    def visit_rest(self):
        restaurant = input("Name of restaurant: ")

        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)

        food_bill = float(input("What was the total food bill for this visit? "))
        points = self.calculate_rewards(food_bill)
        self.rewards_points += points

        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned: {self.rewards_points}")
        print(f"Thank you for visiting {restaurant}!")


customer_1 = RewardsProgram("Hritik Zope", "555-111-2222", "hritik@example.com")
customer_1.profile()
customer_1.thank_you()
customer_1.add_to_cust_list()

print()
print("Customer List:")
print(cust_list)

# To test visit_rest(), uncomment this line:
# customer_1.visit_rest()
