sales_data = [
    ("Marcus Webb", "East", 4250.00),
    ("Priya Sharma", "West", 5875.50),
    ("DeShawn Carter", "East", 3100.75),
    ("LaTonya Rivers", "South", 6420.00),
    ("Bob Nguyen", "West", 4980.25),
]

total_sales = 0

for name, region, sales in sales_data:
    total_sales = total_sales + sales
    print(name + " (" + region + "): $" + str(round(sales, 2)))

    if sales > 5000:
        print("^ Top performer!")

print("Overall total sales: $" + str(round(total_sales, 2)))