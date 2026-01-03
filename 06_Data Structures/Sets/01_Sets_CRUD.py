# A set is an unordered, mutable collection of unique elements enclosed in curly braces {}

# Create
my_set = {1,2,3,4}
print(type(my_set))

arr = [1,1,2,3,4,4,4,5,6]
new_set = set(arr)

# Read
print(new_set)

for i in my_set:
    print(i)

# Update
new_set.add(7)
new_set.update([11,22,33,33])
print(new_set)

# Delete
# new_set.remove(99) # Error if not found
new_set.remove(1)
new_set.discard(23) # Return None if not found
new_set.pop()
print(new_set)