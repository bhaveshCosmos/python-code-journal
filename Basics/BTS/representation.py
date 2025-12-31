'''
repr(): Returns an unambiguous, developer-focused string representation of an object, mainly for debugging. Internally calls __repr__() and aims to be precise, sometimes recreatable.

str(): Returns a readable, user-friendly string form of an object for display. Calls __str__() and falls back to __repr__() if not defined.

print(): Outputs objects to stdout after converting them using str(). It is an output utility, not a representation method.
'''
str1 = "Python"
repr(str1)
str(str1)
print(str1)