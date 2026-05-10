bank_balance = 100
savings_goal = 500
weekly_savings = 75

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings

    if bank_balance >= savings_goal:
        print("Goal met! My current balance is " + str(bank_balance))
    elif bank_balance >= savings_goal * 0.75:
        bank_balance = bank_balance - 10
        print("So close! After treating myself, my balance is up to " + str(bank_balance))
    elif bank_balance > savings_goal / 2:
        print("Almost there! This week my balance is up to " + str(bank_balance))
    else:
        print("This week my balance increased to " + str(bank_balance))