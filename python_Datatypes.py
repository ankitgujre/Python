'''
Python data types are actually classes, and the defined variables are their instances 
or objects.
Since Python is dynamically typed, the data type of a variable is determined at runtime
based on the assigned value.
'''
# Types of Data Types in Python

# 1. Python Numeric Data Types

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))

# 2. Python String Data Type

'''
Python string is a sequence of one or more Unicode characters, enclosed in single, 
double or triple quotation marks (also called inverted commas). Python strings are immutable 
which means when you perform an operation on strings, you always produce a new string object 
of the same type, rather than mutating an existing string.
'''

str1 = 'this is single quotes string'
print(str1)
str2 = "this is double quotes string"
print(str2)
str3 = '''This is triple qoutes string'''
print(str3)
str3 = """This is also triple quotes"""
print(type(str1))

# 3. Python Sequence Data Types

'''
Sequence is a collection data type. It is an ordered collection of items. Items in the 
sequence have a positional index starting with 0. It is conceptually similar to an array in 
C or C++. There are following three sequence data types defined in Python.

List Data Type
Tuple Data Type
Range Data Type
'''
# (a) Python List Data Type

'''
Python Lists are the most versatile compound data types. A Python list contains items 
separated by commas and enclosed within square brackets ([]).
'''

li1 = [2023, "Python", 3.11, 5+6j, 1.23E-4]
print(li1, type(li1))

nlis = [['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]  # nested list
print(nlis, type(nlis))

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# slicing syntax sequence[start : stop : step]


#-----------------(b) Python Tuple Data Type--------------------

'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 
3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

tup = (2023, "Python", 3.11, 5+6j, 1.23E-4)
print(tup, type(tup))

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples