def reverse(str):
  result = ""
  for i in str:
    result = i + result
  return result

string = input("Enter a string: ")
print(f'Actual String is {string!r}')
print(f'Reveresed String is {reverse(string)!r}')