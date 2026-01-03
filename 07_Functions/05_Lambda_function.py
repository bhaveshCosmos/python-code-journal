diff = lambda x,y: x-y
print(diff(10,5))

cube = lambda x: x**3
print(cube(10))

cel_tempt = [0, 10, 20, 30]
fe_temp = map(lambda x: (x*(9/5))+32, cel_tempt)
print(list(fe_temp))

students = [("Rahul", 85), ("Anita", 92), ("Rohit", 78), ("Neha", 88)]
sorted_list = sorted(students, key = lambda x : x[1], reverse=True)
print(sorted_list)