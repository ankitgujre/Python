'''
Python variables are the reserved memory locations used to store values with in a Python Program. This means that when you create a variable you reserve some space in the memory.

Based on the data type of a variable, memory space is allocated to it. Therefore, by assigning different data types to Python variables, you can store integers, decimals or characters in these variables.

'''
month = "May"
print(id(month)) # Python's built-in id() function returns the address where the object is stored.
'''
del month  # You can delete a single object or multiple objects by using the del statement.
print(month)'''

# Getting Type of a Variable

'''
You can get the data type of a Python variable using the python built-in function type() 
as follows.
'''

x = "Ankit"
y =  10
z =  10.10

print(type(x))
print(type(y))
print(type(z))

# Casting Python Variables

'''You can specify the data type of a variable with the help of casting as follows:'''

a = str(111)
b = int(14)
c = float(3.14)

print(a)
print(b)
print(c)

print(type(a))

# Case-Sensitivity of Python Variables

'''Python variables are case sensitive which means Age and age are two different variables:'''

age = 20
Age = 30

print( "age =", age )
print( "Age =", Age )

# Python Variables - Multiple Assignment

a=b=c = 10

print(a,b,c) # 10 10 10

a,b,c = 10,20,30

print(a,b,c)

a=b=10
print(id(a))
print(id(b))