foods = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

for index, food in enumerate(foods, start=1):
    if index == 1:
        print(str(index) + ". " + food + " <- top pick!")
    else:
        print(str(index) + ". " + food)

print("Reverse order:")

for index, food in enumerate(reversed(foods), start=1):
    print(str(index) + ". " + food)