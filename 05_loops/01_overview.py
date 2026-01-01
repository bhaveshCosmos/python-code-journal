# the range() function in Python returns a range object that is a lazy sequence, meaning it does not store all the numbers in memory at once.
# This range object only stores the start, stop, and step values, and generates each number on-demand when accessed, such as during iteration.
print((range(1,11,2))) # range(1, 11, 2)
print(list(range(1,11,2))) # [1, 3, 5, 7, 9]