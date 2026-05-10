# Exercise 4.D - Bonus Number Guesser

numbers = list(range(1, 21))
numbers.sort(reverse=True)

secret_number = numbers[7]

guesses = []
guess_count = 0

print("Guess the secret number!")
print("The number is between 1 and 20.")

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isnumeric():
        print("Please enter a number.")
        continue

    guess = int(user_input)
    guesses.append(guess)
    guess_count = guess_count + 1

    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print("Correct!")
        break

print("Number of guesses: " + str(guess_count))
print("Your guesses were: " + str(guesses))

if guess_count < 5:
    print("You're awesome!")