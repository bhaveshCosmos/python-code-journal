set_A = {1,2,3,4}
set_B = {1,2,3,4,3,4,7,8,9}

# Union
print(set_A | set_B) # Only with Sets
print(set_A.union([11,22,33])) # # With other iterables

# Intersection 
print(set_A & set_B)
print(set_B.intersection([7,8,10]))

# Difference
print(set_A - set_B)
print(set_B.difference([7,8,10]))

# Symmetric Difference
print(set_A ^ set_B)
print(set_B.symmetric_difference([7,8,10]))

# Subset
print(set_A.issubset(set_B))

# Frozenset
normal_set = {1,2,3,4}
frozen_set = frozenset(normal_set)
normal_set.add(5)
# frozen_set.add(5) # AttributeError: 'frozenset' object has no attribute 'add'
print(normal_set)
print(frozen_set)