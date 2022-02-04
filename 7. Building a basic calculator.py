# Getting input from the user

num1 = input('Enter a number: ')
num2 = input('Enter a second number: ')

result = int(num1) + int(num2)  # Only works with integers. Throws an error for decimals

result2 = float(num1) + float(num2)  # Parse the input into a float

print(result)
print(result2)
