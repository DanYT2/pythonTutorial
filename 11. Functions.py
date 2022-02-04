# A collection of code that performs a specific task
# Declaring a function
def say_hi():
    print('Hello user')


# Calling on a function
print('Top')
say_hi()
print('Bottom')


# Passing parameters
def sayHello(name: str, age: int):
    print('Hello ' + name + '. You are ' + str(age) + ' years old')


sayHello('Dan', 45)


# Return statement
def cube(num):
    return pow(num, 3)


print(cube(3))
