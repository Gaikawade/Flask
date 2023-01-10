# Program to find Armstrong Number

for i in range(1001):
    num = i
    result = 0
    no_of_digits = len(str(i))  # We cant find length of numbers, so we are using str function to find length
    while i != 0:
        digit = i % 10
        result += digit**no_of_digits
        i = i // 10  # Division to get the number by removing units digit
    if num == result:
        print(num)
