print('Hello world!')

message = 'Hello world!'
print(message)

# It prints twice because there are two print statements:
# one prints the string directly, and the other prints the variable.

dollars = 3
cents = 0.50

print(dollars + cents)

# The result shows 3.5 instead of 3.50 because Python drops trailing zeros.

cents = cents + 0.25
print(dollars + cents)

d_str = '3 dollars'
c_str = '50 cents'

print(d_str + ' ' + c_str)