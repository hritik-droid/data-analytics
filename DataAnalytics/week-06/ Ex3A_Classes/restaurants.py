# Exercise 3.A Lab 1
# Working with classes

class Restaurant:
    """A simple class that represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant_1 = Restaurant("Taco Town", "Mexican food")
restaurant_2 = Restaurant("Pasta Palace", "Italian food")
restaurant_3 = Restaurant("Curry Corner", "Indian food")

restaurant_1.describe_rest()
restaurant_1.rest_open()

print()

restaurant_2.describe_rest()
restaurant_2.rest_open()

print()

restaurant_3.describe_rest()
restaurant_3.rest_open()
