# Exercise 2.D Lab 1
# Lambdas and multiplier functions

doubler = lambda n: n * 2

print("Doubler tests:")
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

print()

tripler = lambda n: n * 3

print("Tripler tests:")
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))

print()

def multiplier(factor):
    return lambda n: n * factor


quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print("Multiplier function tests:")
print(f"4 times 5 = {quadrupler(5)}")
print(f"5 times 5 = {quintupler(5)}")
print(f"6 times 5 = {sextupler(5)}")
print(f"7 times 5 = {septupler(5)}")
print(f"8 times 5 = {octupler(5)}")
print(f"9 times 5 = {nonupler(5)}")
print(f"10 times 5 = {decupler(5)}")
