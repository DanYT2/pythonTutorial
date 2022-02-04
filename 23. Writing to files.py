# employee_file = open('employees.txt', 'w')  # Overwrites the entire file. Deletes current data and adds what is passed
employee_file = open('employees.txt', 'a')  # Adds data to the end of the file
new_file = open('employee1.txt', 'w')

employee_file.write('\nToby - Human Resources')
employee_file.write('\nKelly - Customer Service')  # Appends value to the end of a file
new_file.write('\nThis is a new file that i have created')
employee_file.close()
new_file.close()
