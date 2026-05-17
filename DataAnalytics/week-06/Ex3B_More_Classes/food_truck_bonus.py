# Exercise 3.B Lab 3 Optional
# FoodTruck child class

class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


class FoodTruck(Restaurant):
    """A child class that represents a food truck."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = "N"
        self.truck_location = ""
        self.location_history = []

    def accepts_private_bookings(self):
        answer = input("Does this food truck accept private bookings? Y/N ")
        self.private_bookings = answer.upper()

        if self.private_bookings == "Y":
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck currently does not accept private bookings.")

    def relocate_truck(self):
        self.truck_location = input("Enter the truck's current location, street address and city: ")
        self.location_history.append(self.truck_location)
        print(f"Truck is currently located at {self.truck_location}")

    def print_location_history(self):
        print("Location History:")
        for location in self.location_history:
            print(location)


truck_1 = FoodTruck("Rolling Tacos", "Mexican food")
truck_1.describe_rest()
truck_1.rest_open()

# To test input methods, uncomment these lines:
# truck_1.accepts_private_bookings()
# truck_1.relocate_truck()
# truck_1.print_location_history()

# I chose to keep duplicate locations in the history.
# This could be useful because the same location on different days may still matter for tracking business activity.
