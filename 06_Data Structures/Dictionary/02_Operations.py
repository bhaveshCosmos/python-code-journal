student = {
    "101": {"name": "Rahul", "age": 19, "course": "BTech"},
    "102": {"name": "Anita", "age": 20, "course": "BSc"},
    "103": {"name": "Rohit", "age": 18, "course": "BA"}
}


print("101" in student)
print("104" not in student)
print(len(student))

for i in student:
    print(i, student[i]["name"])

# Methods
print(student.keys())
print(student.values())
print(student.items())

dict1 = {"a": 1, "b": 2}
dict2 = {"x": 10, "b": 20}

dict1 |= dict2
print(dict1)
