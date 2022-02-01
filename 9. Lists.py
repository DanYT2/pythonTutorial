# Used to store information

friends = ['Andrew', 'Kevin', 'Caren', 'Tim', 4.5, True, 'Oscar', 'Limes']
# Accessing individual elements in a list

print(friends)
print(friends[0])  # Accessing a specific elements in a list
print(friends[-1])  # Negative indexes the list from the back of the list
print(friends[2:])  # Access the element at index 2 and all other elements
print(friends[1:4])  # All elements from 1 upto, but not including, 4

# Modifying elements in a list
friends[1] = 'Michael'

# List functions
luckyNumbers = [4, 6, 8, 12, 67, 89]
people = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim', 'Karen']

print(people)
# people.extend(luckyNumbers)  # Takes the list and appends another list at the end of it
print(people)
people.append('Cyprian')  # Adds the passed item to the end of the list
people.insert(1, 'Ron')  # Inserts a value at the specified index with the other items being pushed to the right
people.remove('Jim')  # Removes an item from the list
# people.clear()  # Removes all the elements from a list
people.pop()  # Removes the last element from a list
people.index('Kevin')  # Displays the index of the passed parameter if present. If absent, it returns an error
people.count('Karen')  # Displays the number of times the passed value is present in the list
people.sort()  # Arranges in ascending order
luckyNumbers.reverse()  # Changes the order of a list
people2 = people.copy()  # Returns a copy of the list and assigns it a variable name

print(people)
