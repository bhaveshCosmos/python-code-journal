# *args allows a function to accept a variable number of positional arguments, which are received as a tuple in Python.

def add(*args, sum=0):
    print(type(args))
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4,5,6))

# **kwargs allows a function to accept a variable number of keyword arguments, which are received as a dictionary in Python.

def fun(**kwargs):
    print(type(kwargs))
    for i, j in kwargs.items():
        print(f"{i}: {j}")
    return sum
fun(Name = "Bhavesh",age = 19, major = "CSE")