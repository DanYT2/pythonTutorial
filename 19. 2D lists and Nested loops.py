# Multidimensional list
number_grid = [
    [1, 2, 3, 4, 5],
    [2, 3, 0, 23, 43],
    [56, 68, 86, 32, 90],
    [0]
]

# Accessing elements in a multidimensional list
print(number_grid[2][4])

# Nested for loop
for row in number_grid:
    for column in row:
        print(column)
