print('Giraffe\nAcademy')
phrase = 'Phrase variable.'
print(phrase)

# Concatenation
print(phrase + ' is Cool')

# String functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())  # Checks if it is all in upper case
print(phrase.upper().isupper())  # Converts into upper then checks if all characters are uppercase
print(len(phrase))  # Length of a string variable
print(phrase[0])  # Index of a string variable
print(phrase.index('a'))  # Locates the index of the first occurrence of the passed parameter
print(phrase.replace('Phrase', 'Elephant'))
