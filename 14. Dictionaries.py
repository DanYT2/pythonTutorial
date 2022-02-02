# Stores information in key value pairs
# Declaration

# Keys need to be unique
monthConversion = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

# Accessing values in a dictionary
print(monthConversion['Dec'])
print(monthConversion.get('Aug', 'Key not found'))
