# A list is a mutable, ordered collection of elements enclosed in square brackets and separated by commas

# CRUD
# Create
nums = [10, 20, 30,40, 50]
nested_list = [[1,2], [3,4], [5,"Hello"]]
print(nested_list)

string = "PYTHON"
print(list(string)) # Creating a list using iterable

even_range = range(2,13,2)
print(list(even_range))

# Read
my_list = [[1,3,4], "Hello", "World", 99, 100]
print(my_list[3])
print(my_list[0:2])
print(my_list[::-1])
print(my_list[0][2])
# Slicing returns a copy of the sequence and does not change the original.

# Update
laptops = ["Dell", "HP", "Lenovo", "Asus", "Acer", "MacBook Air"]

laptops[4] = "MacBook Pro"
laptops.append("Samsung")
laptops.insert(2,"Microsoft Surface")
mobiles = ["iPhone", "Samsung", "OnePlus", "Xiaomi"]
laptops.extend(mobiles)

print(laptops)

# Delete 
laptops.remove("Asus")
laptops.pop(2) # Default -1
print(laptops.pop(2))

del laptops[1:3]
print(laptops)

laptops.clear()
print(laptops)

# Packing - Unpacking
# Packing Unpacking
packed_list = [1,2,3,3,4,5]
a,b,*c,d =  packed_list
print(a,b,c,d)