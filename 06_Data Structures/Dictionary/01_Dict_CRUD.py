# A dictionary is a mutable, Ordered [(from Python 3.7 onwards); earlier versions treated dictionaries as unordered]collection of key–value pairs enclosed in curly braces {}, where each key is unique and used to access its corresponding value in Python.

# Dictionary keys must be immutable (hashable) types, such as int, float, str, or tuple

# Internal Working
# hash(key) % size_of_hash_table
print(hash("name")%8)
print(hash("age")%8)
print(hash("major")%8)
# Python handles hash collisions using open addressing with probing, where colliding keys are placed in the next available slot based on a probe sequence while ensuring fast lookup and minimal clustering.

# Create
student = {
    "name" : "Bhavesh Upadhyay",
    "age" : 19,
    "major" : "Computer Science",
}
fruits = dict(Apple = "Red", Mango = "Yellow", Kiwi = "Brown") # dict(key = value)
laptops = dict([("Dell", 55000), ("Lenovo", 58000), ("Asus", 62000), ("MacBook Air", 95000),  ("Samsung", 68000), ("Microsoft Surface", 120000)])

# Read
print(student["name"])
print(fruits)
print(laptops.get("Lenovo", "Not Found"))
print(laptops.get("Dell", "Not Found"))

# Update
laptops["Lenovo"] = 79999
laptops.update([("HP",99999)])
print(laptops)

# Delete
del laptops["MacBook Air"]
laptops.pop("HP", "N/A")
laptops.popitem()
print(laptops)

laptops.clear()
print(laptops)

