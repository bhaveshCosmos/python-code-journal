list1 = [1,2,3]
list2 = list1
# list2 = list1, no new list is created. Python copies the reference, so both list1 and list2 point to the same memory address
print(list1 == list2) # True
# Check whether values are Equal
print(list1 is list2) # True
# Check whether memory addresses are equal
list1[0] = 99
# list1[0] = 99, the change appears in list2 because both references point to the same mutable object.
print(list1) # [99, 2, 3]
print(list2) # [99, 2, 3]


l1 = [1,2,3]
l2 = l1
l1 = [1,2,3] # l1 = [1,2,3] creates a new list object in memory, even though the contents look identical.
print(l1 == l2) # True
print(l1 is l2) # False
l1[0] = 55
# l1[0] = 55, l2 remains unchanged because it refers to a different list object.
print(l1) # [55, 2, 3]
print(l2) # [1, 2, 3]

'''
Internally, Python uses reference counting and garbage collection to manage memory. 
Since both names reference the same list object, the reference count increases. 
The object is only deallocated when all references to it are removed, 
ensuring memory safety while allowing efficient object sharing.
'''