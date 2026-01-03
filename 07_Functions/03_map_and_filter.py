# Map
def square(x,y):
    return (x+y)**2

x_list = [1,2,3,4,5]
y_list = [11,22,33,44]
squared_list = map(square, x_list, y_list)

print(list(squared_list))

# Filter
def even(x):
    return x%2 == 0

num_list = [1,2,3,4,5,6,7,8]

filtered_list = filter(even,num_list)
print(list(filtered_list))
