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
| \n              | New line        |
| \t              | Tab             |
| \\\' or \\\"    | quotation marks |

### Getting input from users

Declared using `input()`

This prompts the user to provide input

The input can be assigned to a variable using the following syntax:

`variable = input('This is a prompt for input')`

### Lists

Declarations of lists:

`list = []`

###### List functions

| Function                    | Description                                                      |
|-----------------------------|------------------------------------------------------------------|
| .append('Parameter')        | Adds the passed element to the end of a list                     |
| .sort( )                    | Sorts list in ascending order                                    |
| .clear( )                   | Removes all elements in a list                                   |
| .pop()                      | Removes the last element in a list                               |
| .index('parameter')         | Returns the index of the parameter in the list if present        |
| .copy()                     | Creates a copy of the list with the same items                   |
| .count('parameter')         | Returns the number of times an item appears on a list            |
| .insert(index, 'parameter') | Inserts into the specified index the value passed as a parameter |
| .remove('parameter')        | Removes the parameter from the list                              |

### Tuples

Declared similarly to lists but use parenthesis instead of square brackets

`tuple = (1,2)`

They are used to store immutable values i.e. Those that can't be changed

### Functions

Used to run a set of code whenever called upon.

Declared as `def function_name(parameter):`
