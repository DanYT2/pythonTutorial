# Used to monitor certain errors to prevent entire code from halting when it occurs
try:
    number = float(input('Enter a number: '))
    print(number)
except ValueError:  # Catches the specified error
    print('Invalid Input')
except ZeroDivisionError:
    print('Divided by zero')
else:
    print('If no error occurs, this runs')
finally:  # Runs regardless of error
    print('Code has been executed')
