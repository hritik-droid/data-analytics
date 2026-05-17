import random

products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
    'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
    'Surge Protector'
]

product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

survey_products = random.sample(products, 3)
print(f"Products selected for usability survey: {survey_products}")

random.shuffle(products)
print(f"Randomized product presentation order: {products}")

transaction_count = random.randint(50, 300)
print(f"Simulated daily transaction count: {transaction_count}")
