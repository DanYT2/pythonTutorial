<h1 style="text-align: center">Notes</h1>
<hr>

### Print Statements

Written as `print(' ')` with what to be printed to the console written between the quotation marks

### Variables

Python is loosely typed hence data types are not declared

Declared as `variableName = Value`

### Working with Strings

| Escape sequence | Function        |
|-----------------|-----------------|
| `\n `           | New line        |
| `\t  `          | Tab             |
| `\' or \" `     | quotation marks |

### Getting input from users

Declared using `input()`

This prompts the user to provide input

The input can be assigned to a variable using the following syntax:

`variable = input('This is a prompt for input')`

### Lists

Declarations of lists:

`list = []`

###### List functions

| Function                      | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| `.append('Parameter')`        | Adds the passed element to the end of a list                     |
| `.sort( ) `                   | Sorts list in ascending order                                    |
| `.clear( ) `                  | Removes all elements in a list                                   |
| `.pop()  `                    | Removes the last element in a list                               |
| `.index('parameter')`         | Returns the index of the parameter in the list if present        |
| `.copy()`                     | Creates a copy of the list with the same items                   |
| `.count('parameter')`         | Returns the number of times an item appears on a list            |
| `.insert(index, 'parameter')` | Inserts into the specified index the value passed as a parameter |
| `.remove('parameter')`        | Removes the parameter from the list                              |

### Tuples

Declared similarly to lists but use parenthesis instead of square brackets

`tuple = (1,2)`

They are used to store immutable values i.e. Those that can't be changed

### Functions

Used to run a set of code whenever called upon.

Declared as `def function_name(parameter):`

##### Comparison operators

| Comparison | Function                 |
|------------|--------------------------|
| `>`        | Greater than             |
| `<`        | Less than                |
| `>=`       | Greater than or equal to |
| `<=`       | Less than or equal to    |
| `!=`       | Not equal to             |
| `==`       | Equal to                 |

### Dictionaries

Used to store a set of data in the form of key value pairs. Each key MUST be unique.

Declaration

`dictionary = {'key': 'Value'}`

They can be accessed in the following ways:

`dictionary["Key"]` or `dictionary.get('Key')`

### While loop

Loops through the structure whenever the condition remains true

Declaration:

    while comparison:
        Lines of code

### File Handling

Declaration: `variable = open('Path to file', 'Access mode')`

| Access mode | Description                                                            |
|-------------|------------------------------------------------------------------------|
| r           | readable                                                               |
| a           | Append data to the end of a file. Creates a new one if it doesnt exist |
| w           | Opens a file for writing. Creates a new one if it doesnt exist         |
| x           | Creates a new file. Returns an error if it already exists              |
| r+          | Read and write permissions are granted                                 |

#### Reading files

    f = open('demofile.txt', 'r')
    f.readable()            # Checks if file can be read
    f.writable()            # Checks if the fiel is writable
    print (f.read())        # Reads the entire file
    print (f.readline())    # Reads the first line of the file
    print (f.read(3))       # Reads the first x characters in a file
    f.close()               # Closes the file once through