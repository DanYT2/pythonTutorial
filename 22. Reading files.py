# Read the employees in a file

employee_file = open('employees.txt', 'r')

print(employee_file.readable())  # Checks if the file is readable. Boolean
print(employee_file.read())  # Reads the entire document
print(employee_file.readline())  # Reads a single line in the file
print(employee_file.readlines()[1])  # Creates an array made of each line of the file

for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # Closes the document once done
