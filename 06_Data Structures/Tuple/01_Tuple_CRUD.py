# A tuple is an ordered, immutable collection of elements enclosed in parentheses and separated by commas in Python.

# Create & Read
empty_tuple = ()
tup_1 = (1,2,3)
tup_2 = 1,2,3
tup_3 = (1,)
tuple_from_list = tuple([1,2,3,"Python"])
tuple_from_iter = tuple(range(1,11))
tuple_from_string = tuple("JAVA")

print(tup_1)
print(tup_2)
print(tup_3)
print(tuple_from_iter)
print(tuple_from_list)
print(tuple_from_string)

# Packing Unpacking
packed_tuple = 1,2,3,3,4,5
a,b,*c,d =  packed_tuple
print(a,b,c,d)

# Update
# Immutability applies to the tuple container, not to the mutable elements inside it.
tup_lis = (1,2,3,[4,5])
tup_lis[3].append(99)
print(tup_lis)

new_tup = (1,2,3)
new_tup+=(99,88)
print(new_tup)

# Delete
del tup_1
