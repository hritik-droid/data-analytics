# Exercise 3.B Lab 1
# Enhanced Restaurant class

class Restaurant:
    """A class that represents a restaurant and tracks customers served and ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5, 5 being excellent? "))
                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)
                    print(f"Your rating was {rating}. The average rating for this restaurant is {average:.2f}.")
                    break
                else:
                    print("Please enter an integer from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a whole number from 1 to 5.")


restaurant_1 = Restaurant("Taco Town", "Mexican food")
restaurant_2 = Restaurant("Pasta Palace", "Italian food")
restaurant_3 = Restaurant("Curry Corner", "Indian food")

restaurant_1.describe_rest()
restaurant_1.rest_open()
restaurant_1.print_num_served()

print()

restaurant_2.describe_rest()
restaurant_2.rest_open()
restaurant_2.print_num_served()

print()

restaurant_3.describe_rest()
restaurant_3.rest_open()
restaurant_3.print_num_served()

# To test add_num_served() and customer_rating(), uncomment these lines:
# restaurant_1.add_num_served()
# restaurant_1.print_num_served()
# restaurant_1.customer_rating()
