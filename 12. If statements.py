# Simple declaration
is_male = True
is_tall = False

if is_male and is_tall:
    print('You are Male and you are tall')
elif is_male and not is_tall:
    print('You are male, but you are short')
else:
    print('You are female')


# If statement and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 3, 3))
