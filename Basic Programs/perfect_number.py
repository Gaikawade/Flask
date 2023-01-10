#  PERFECT NUMBER
#  It is a positive integer that is equal to the sum of its positive divisors excluding the number itself

num = int(input("Enter a number: "))
result = 0
for i in range(1, num):
  if (num % i ) == 0:
    result += i

if result == num:
  print(f"{num} is a perfect number")
else:
  print(f"{num} is not a perfect number")