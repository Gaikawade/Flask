# Factorial of a number using in-built function
# 5! = 5 * 4 * 3 * 2 * 1

import math

n = int(input("Enter the number: "))
result = math.factorial(n)
print(f"Factorial of {n} using in-built method is {result}")

# Factorial using Resursion method

def factorial_of_N(n):
  if n == 0:
    return 1
  else:
    return n * factorial_of_N(n-1)

print(f"Factorial of {n} using Recursion is {factorial_of_N(n)}")

# Factorial using Loop

result = 1
for i in range(n, 0, -1):    # (Initilization, condition, decrement)
  result *= i

print(f"Factorial of {n} using Loop is {result}")