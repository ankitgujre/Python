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